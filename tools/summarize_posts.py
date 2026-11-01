"""Summarize observed X post records without estimating ranking or causal lift."""
import argparse
import json
import sys
import math
import re
from collections import Counter
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

METRICS = ("views", "likes", "replies", "reposts", "quotes", "bookmarks")
ENUMS = {
    'format': ('post', 'long_post', 'thread_root', 'thread_reply', 'quote', 'repost', 'article', 'article_carrier', 'unknown'),
    'body_status': ('complete', 'partial', 'preview', 'blocked', 'unknown'),
    'media_status': ('complete', 'partial', 'not_viewed', 'unavailable', 'unknown'),
    'metric_scope': ('post', 'article_page', 'carrier_post', 'owner_analytics', 'unknown'),
}

def parse_count(raw):
    result = {"raw": raw, "value": None, "precision": "unknown"}
    if isinstance(raw, bool):
        return result
    if isinstance(raw, int) and raw >= 0:
        return dict(result, value=raw, precision="exact")
    if isinstance(raw, float) and math.isfinite(raw) and raw >= 0 and raw.is_integer():
        return dict(result, value=int(raw), precision="exact")
    if not isinstance(raw, str):
        return result
    value = raw.strip()
    if re.fullmatch(r"(?:[0-9]+|[0-9]{1,3}(?:,[0-9]{3})+)", value):
        return dict(result, value=int(value.replace(",", "")), precision="exact")
    matched = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)\s*([KkMm万亿])", value)
    if matched:
        multiplier = {"k":1000, "m":1000000, "万":10000, "亿":100000000}[matched[2].lower()]
        number = float(matched[1]) * multiplier
        if math.isfinite(number):
            return dict(result, value=number, precision="rounded")
    return result

def canonical_url(value):
    if not isinstance(value, str):
        return ""
    try:
        parsed = urlsplit(value.strip())
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ""
    if parsed.scheme not in ("http", "https") or host not in ("x.com", "www.x.com", "twitter.com", "www.twitter.com") or parsed.username or parsed.password:
        return ""
    return urlunsplit(("https", "x.com", parsed.path.rstrip("/"), "", ""))

def post_key(url):
    matched = re.search(r"/(?:status|article)/([0-9]+)$", url)
    if matched:
        kind = "article" if "/article/" in url else "status"
        return kind + ":" + matched[1]
    return url

def timestamp(value):
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if parsed.tzinfo is not None else None
    except ValueError:
        return None

def missing(value):
    return value is None or (isinstance(value, str) and value in ('', 'unknown', 'not_viewed'))

def stable_value(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)

def count_equal(first, second):
    parsed_first, parsed_second = parse_count(first), parse_count(second)
    if parsed_first['precision'] == parsed_second['precision'] == 'exact':
        return parsed_first['value'] == parsed_second['value']
    return type(first) is type(second) and first == second

def alternatives(values, metric=False):
    result = []
    for value in sorted((value for value in values if not missing(value)), key=stable_value):
        if not any(count_equal(value, old) if metric else value == old for old in result):
            result.append(value)
    return result

def merge_same_snapshot(previous, current):
    """Combine only one identity, scope and verified timestamp; expose conflicts."""
    result = dict(previous)
    for key, value in current.items():
        if key not in ('metrics', 'observation_conflicts') and not missing(value):
            result[key] = value
    # A sparse card cannot undo fuller coverage observed at this same instant.
    for field, levels in (
        ('body_status', ('unknown', 'blocked', 'preview', 'partial', 'complete')),
        ('media_status', ('unknown', 'not_viewed', 'unavailable', 'partial', 'complete')),
    ):
        observed = [value for value in (previous.get(field), current.get(field)) if value in levels]
        if observed:
            result[field] = max(observed, key=levels.index)
    if previous.get('media_notes') or current.get('media_notes'):
        result['media_notes'] = sorted(set((previous.get('media_notes') or []) + (current.get('media_notes') or [])))
    conflicts = dict(previous.get('observation_conflicts') or {})
    old_metrics = previous.get('metrics') if isinstance(previous.get('metrics'), dict) else {}
    new_metrics = current.get('metrics') if isinstance(current.get('metrics'), dict) else {}
    metrics = dict(old_metrics)
    for key, value in new_metrics.items():
        field = 'metrics.'+key
        values = alternatives(conflicts.get(field, []) + [old_metrics.get(key), value], metric=True)
        if len(values) > 1:
            conflicts[field] = values
            metrics[key] = None
        elif values:
            metrics[key] = values[0]
    result['metrics'] = metrics
    texts = alternatives(conflicts.get('text', []) + [previous.get('text'), current.get('text')])
    if len(texts) > 1:
        conflicts['text'] = texts
        result['text'] = texts[0]
    if 'text' in conflicts:
        result['body_status'] = 'partial'
    if conflicts:
        result['observation_conflicts'] = conflicts
    return result

def record_error(row):
    if not isinstance(row, dict):
        return 'record is not an object'
    for field, choices in ENUMS.items():
        value = row.get(field)
        if value is not None and (not isinstance(value, str) or value not in choices):
            return '{} must be null or one of: {}'.format(field, ', '.join(choices))
    for field in ('url', 'article_url', 'carrier_post_url', 'thread_root_url', 'text', 'observed_at', 'published_at'):
        if row.get(field) is not None and not isinstance(row[field], str):
            return field + ' must be a string or null'
    for field in ('media_notes', 'supporting_post_urls'):
        value = row.get(field)
        if value is not None and (not isinstance(value, list) or any(not isinstance(part, str) for part in value)):
            return field + ' must be a list of strings or null'
    metrics = row.get('metrics')
    if metrics is not None and not isinstance(metrics, dict):
        return 'metrics must be an object or null'
    for field, value in (metrics or {}).items():
        if value is not None and (isinstance(value, bool) or not isinstance(value, (str, int, float))):
            return 'metrics.' + str(field) + ' must be a count string, number or null'
    return None

def content_groups(identities, observations):
    """Resolve the explicit relationship graph without uniting distinct Articles."""
    graph = {identity:set() for identity in identities}
    directed = {identity:set() for identity in identities}
    roots = {}
    conflicts = []
    for source in observations:
        row = source['record']
        own = post_key(canonical_url(row.get('url')))
        if own not in identities:
            continue
        for field, kind in (('article_url', 'article'), ('carrier_post_url', 'status'), ('thread_root_url', 'status')):
            value = row.get(field)
            if missing(value):
                continue
            target_url = canonical_url(value)
            valid = re.search(r'/' + kind + r'/[0-9]+$', target_url)
            if field == 'carrier_post_url' and not own.startswith('article:'):
                valid = False
            if field == 'thread_root_url' and not own.startswith('status:'):
                valid = False
            if not valid:
                conflicts.append({'type':'invalid_link', 'identity':own, 'field':field, 'row':source['row'], 'value':value})
                continue
            target = post_key(target_url)
            if field == 'thread_root_url':
                roots.setdefault(own, set()).add(target)
            start, end = (target, own) if field == 'carrier_post_url' else (own, target)
            for identity in (start, end):
                graph.setdefault(identity, set())
                directed.setdefault(identity, set())
            if start != end:
                graph[start].add(end)
                graph[end].add(start)
                directed[start].add(end)
    for own, targets in sorted(roots.items()):
        if len(targets) > 1:
            conflicts.append({'type':'contradictory_thread_roots', 'identity':own, 'targets':sorted(targets)})

    # Iterative DFS terminates even for cyclic or very long supplied Threads.
    finished, cycles = set(), set()
    for start in sorted(graph):
        if start in finished:
            continue
        path, active = [start], {start:0}
        stack = [iter(sorted(directed[start]))]
        while stack:
            target = next(stack[-1], None)
            if target is None:
                finished.add(path[-1])
                active.pop(path.pop())
                stack.pop()
            elif target in active:
                cycles.add(tuple(sorted(path[active[target]:])))
            elif target not in finished:
                active[target] = len(path)
                path.append(target)
                stack.append(iter(sorted(directed[target])))
    conflicts.extend({'type':'cycle', 'identities':list(cycle)} for cycle in sorted(cycles))

    groups, remaining = {}, set(graph)
    while remaining:
        pending, component = [min(remaining)], set()
        while pending:
            identity = pending.pop()
            if identity in component:
                continue
            component.add(identity)
            pending.extend(graph[identity] - component)
        remaining.difference_update(component)
        articles = sorted(identity for identity in component if identity.startswith('article:'))
        if len(articles) > 1:
            conflicts.append({'type':'multiple_articles', 'identities':sorted(component), 'articles':articles})
            for identity in component:
                groups[identity] = identity if identity.startswith('article:') else None
        else:
            sinks = sorted(identity for identity in component if not directed[identity])
            representative = articles[0] if articles else min(sinks or component)
            groups.update((identity, representative) for identity in component)
    return groups, sorted(conflicts, key=stable_value)

def summarize(rows):
    if not isinstance(rows, list):
        raise ValueError('posts must be a list of observation records')
    buckets, duplicates, invalid = {}, [], []
    for index, row in enumerate(rows):
        error = record_error(row)
        if error:
            invalid.append({'row':index, 'reason':error})
            continue
        raw_url = row.get('url')
        url = canonical_url(raw_url)
        unresolved = raw_url is None or not raw_url.strip()
        if not unresolved and (not url or not re.search(r'/(?:status|article)/[0-9]+$', url)):
            invalid.append({'row':index, 'reason':'missing or unrecognized X post/article permalink'})
            continue
        item = deepcopy(row)
        # Computed conflicts come from this run, never an unvalidated input field.
        item.pop('observation_conflicts', None)
        for field in ENUMS:
            item[field] = row.get(field) if row.get(field) is not None else ('not_viewed' if field == 'media_status' else 'unknown')
        item.update(url=None if unresolved else url, identity_status='unconfirmed' if unresolved else 'permalink')
        if unresolved:
            item['provisional_id'] = 'row:{}'.format(index)
        identity = 'unresolved:{}'.format(index) if unresolved else post_key(url)
        key = (identity, item['metric_scope'])
        if key in buckets:
            duplicates.append({'identity':identity, 'metric_scope':item['metric_scope'], 'row':index, 'url':url})
        buckets.setdefault(key, []).append((item, {'row':index, 'record':deepcopy(row)}))

    selected, current_sources = [], []
    for observations in buckets.values():
        dated, undated = [], []
        for item, source in observations:
            (dated if timestamp(item.get('observed_at')) is not None else undated).append((item, source))
        if dated:
            latest = max(timestamp(item.get('observed_at')) for item, _ in dated)
            current = [(item, source) for item, source in dated if timestamp(item.get('observed_at')) == latest]
            current.sort(key=lambda pair: stable_value(pair[0]))
            merged = current[0][0]
            for item, _ in current[1:]:
                merged = merge_same_snapshot(merged, item)
            merged.update(source_observations=[source for _, source in dated],
                          selected_observation_rows=sorted(source['row'] for _, source in current),
                          selection_status='latest_confirmed_timestamp')
            selected.append(merged)
            current_sources.extend(source for _, source in current)
        # Without comparable timestamps there is no safe latest-row choice or merge.
        for item, source in undated:
            item.update(source_observations=[source], selected_observation_rows=[source['row']],
                        selection_status='unverified_timestamp')
            selected.append(item)
            current_sources.append(source)

    identities = {post_key(item['url']) for item in selected if item['url'] is not None}
    linked_content, relationship_conflicts = content_groups(identities, current_sources)
    posts = []
    for item in selected:
        observed, published = timestamp(item.get("observed_at")), timestamp(item.get("published_at"))
        age = (observed-published).total_seconds()/3600 if observed and published else None
        if age is not None and age < 0:
            age = None
        raw_metrics = item.get("metrics") or {}
        if not isinstance(raw_metrics, dict):
            raw_metrics = {}
        own_key = post_key(item['url']) if item['url'] is not None else None
        content_identity = linked_content.get(own_key)
        posts.append(dict(item, content_identity=content_identity,
                          content_identity_status='unconfirmed' if own_key is None else ('conflicted' if content_identity is None else 'resolved'),
                          age_hours=age, metrics={k:parse_count(raw_metrics.get(k)) for k in METRICS}))
    unresolved_content = sum(linked_content.get(identity) is None for identity in identities)
    unresolved_records = sum(p['url'] is None for p in posts)
    return {
        "input_rows":len(rows), "unique_posts":len(identities), "duplicate_rows":len(duplicates),
        "retained_observations":len(posts),
        "unique_content_items":len({p['content_identity'] for p in posts if p['content_identity'] is not None}),
        "unresolved_identity_records":unresolved_records,
        "unresolved_content_identities":unresolved_content,
        "content_count_complete":not (unresolved_records or unresolved_content or relationship_conflicts or invalid),
        "relationship_conflicts":relationship_conflicts,
        "duplicates":duplicates, "invalid_rows":invalid,
        "format_counts":dict(Counter(p["format"] for p in posts)),
        "posts":posts,
        "scope":"Latest confirmed timestamp per (permalink identity, metric_scope), plus independent observations without comparable timestamps and all URL-less evidence. source_observations preserves original records including older dated snapshots; selected_observation_rows identifies the current evidence. unique_posts counts confirmed identities, while retained_observations and format_counts count output observations. duplicate_rows counts additional input observations of the same identity and scope, not independent samples. unique_content_items counts resolved observed content groups, not a complete total when content_count_complete is false. Unresolved identities and conflicting Article links are excluded from that count and reported separately. Content relationships never combine metrics. Unknown relationships are not inferred. Displayed counts are not unique people or Home impressions. Differing ages, content, promotion and source prevent a causal format comparison.",
    }

def main():
    # JSON is always UTF-8, including redirected output on legacy Windows locales.
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="JSON list or object containing posts; raw count strings stay distinguishable from exact values")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        parser.error('cannot read input JSON: {}'.format(error))
    rows = data if isinstance(data, list) else data.get("posts") if isinstance(data, dict) else None
    if not isinstance(rows, list):
        parser.error("input must be a list or an object containing posts")
    print(json.dumps(summarize(rows), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
