"""Summarize observed X post records without estimating ranking or causal lift."""
import argparse
import json
import math
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

METRICS = ("views", "likes", "replies", "reposts", "quotes", "bookmarks")

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

def merge_same_snapshot(previous, current):
    """Combine complementary observations at one verified timestamp; expose conflicts."""
    missing = lambda value: value is None or (isinstance(value, str) and value in ('', 'unknown', 'not_viewed'))
    result = dict(previous)
    for key, value in current.items():
        if key != 'metrics' and not missing(value):
            result[key] = value
    conflicts = dict(previous.get('observation_conflicts') or {})
    old_metrics = previous.get('metrics') if isinstance(previous.get('metrics'), dict) else {}
    new_metrics = current.get('metrics') if isinstance(current.get('metrics'), dict) else {}
    metrics = dict(old_metrics)
    for key, value in new_metrics.items():
        if missing(value):
            continue
        field = 'metrics.'+key
        old = old_metrics.get(key)
        if field in conflicts:
            if value not in conflicts[field]:
                conflicts[field] = conflicts[field]+[value]
            metrics[key] = None
        elif not missing(old) and old != value:
            conflicts[field] = [old, value]
            metrics[key] = None
        else:
            metrics[key] = value
    result['metrics'] = metrics
    old_text, new_text = previous.get('text'), current.get('text')
    if not missing(old_text) and not missing(new_text) and old_text != new_text:
        conflicts['text'] = [old_text, new_text]
        result['body_status'] = 'partial'
    if conflicts:
        result['observation_conflicts'] = conflicts
    return result

def summarize(rows):
    selected = {}
    duplicates = []
    invalid = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            invalid.append({"row":index,"reason":"record is not an object"})
            continue
        url = canonical_url(row.get("url"))
        raw_url = row.get("url")
        if raw_url is None or (isinstance(raw_url, str) and not raw_url.strip()):
            # Keep screenshot/export evidence without inventing post identity.
            # Row IDs distinguish observations only; they never prove uniqueness.
            selected[f'unresolved:{index}'] = dict(row, url=None,
                provisional_id=f'row:{index}', identity_status='unconfirmed')
            continue
        if not url or not re.search(r"/(?:status|article)/[0-9]+$", url):
            invalid.append({"row":index,"reason":"missing or unrecognized X post/article permalink"})
            continue
        key = post_key(url)
        item = dict(row, url=url, identity_status='permalink')
        previous = selected.get(key)
        if previous is not None:
            duplicates.append({"identity":key,"row":index,"url":url})
            old_time, new_time = timestamp(previous.get("observed_at")), timestamp(item.get("observed_at"))
            if old_time is not None and (new_time is None or new_time < old_time):
                continue
            if old_time is not None and old_time == new_time:
                item = merge_same_snapshot(previous, item)
        selected[key] = item
    linked_content = {}
    for item in selected.values():
        if item['url'] is None:
            continue
        own_key = post_key(item['url']) if item['url'] is not None else None
        article = canonical_url(item.get('article_url'))
        if re.search(r'/article/[0-9]+$', article):
            linked_content[own_key] = post_key(article)
        carrier = canonical_url(item.get('carrier_post_url'))
        if own_key.startswith('article:') and re.search(r'/status/[0-9]+$', carrier):
            linked_content[post_key(carrier)] = own_key
        thread = canonical_url(item.get('thread_root_url'))
        if re.search(r'/status/[0-9]+$', thread) and own_key not in linked_content:
            linked_content[own_key] = post_key(thread)
    posts = []
    for item in selected.values():
        observed, published = timestamp(item.get("observed_at")), timestamp(item.get("published_at"))
        age = (observed-published).total_seconds()/3600 if observed and published else None
        if age is not None and age < 0:
            age = None
        raw_metrics = item.get("metrics") or {}
        if not isinstance(raw_metrics, dict):
            raw_metrics = {}
        own_key = post_key(item['url']) if item['url'] is not None else None
        posts.append(dict(item, content_identity=linked_content.get(own_key, own_key), format=item.get("format","unknown"), body_status=item.get("body_status","unknown"), media_status=item.get("media_status","not_viewed"), age_hours=age, metrics={k:parse_count(raw_metrics.get(k)) for k in METRICS}))
    return {
        "input_rows":len(rows), "unique_posts":sum(p['url'] is not None for p in posts), "duplicate_rows":len(duplicates),
        "unique_content_items":len({p['content_identity'] for p in posts if p['content_identity'] is not None}),
        "unresolved_identity_records":sum(p['url'] is None for p in posts),
        "duplicates":duplicates, "invalid_rows":invalid,
        "format_counts":dict(Counter(p["format"] for p in posts)),
        "posts":posts,
        "scope":"Latest observed row per permalink identity, plus all URL-less observations under provisional row IDs. unique_posts and unique_content_items exclude unconfirmed identities; unresolved_identity_records counts retained observations, not distinct posts. Explicit Article/carrier and Thread links retain separate metrics. Unknown relationships are not inferred. Displayed counts are not unique people or Home impressions. Differing ages, content, promotion and source prevent a causal format comparison.",
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="JSON list or object containing posts; raw count strings stay distinguishable from exact values")
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    rows = data if isinstance(data, list) else data.get("posts")
    if not isinstance(rows, list):
        parser.error("input must be a list or an object containing posts")
    print(json.dumps(summarize(rows), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
