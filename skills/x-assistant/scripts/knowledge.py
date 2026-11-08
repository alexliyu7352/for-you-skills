"""Query the report-derived X knowledge base; preserve evidence and coverage.

No network calls, prediction model, recommendation score, or exposure estimate.
"""
import argparse
import copy
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE / 'references' / 'knowledge' if (BASE / 'references' / 'knowledge').is_dir() else BASE / 'knowledge'
REPORT = ROOT.parent / 'research-report.md' if (ROOT.parent / 'research-report.md').is_file() else BASE / 'provenance' / 'research-report.zh-CN.md'
SYNONYMS = [
    (("frequency", "daily", "second post", "interval", "一天", "每天", "幾條", "几条", "频率", "頻率"), ("frequency", "daily", "author diversity", "candidate", "posting")),
    (("image", "photo", "picture", "图片", "圖片", "首图", "首圖"), ("image", "first", "photo_expand", "media")),
    (("article", "long post", "thread", "長文", "长文", "文章"), ("Article", "Post", "format", "body", "4000")),
    (("bookmark", "收藏"), ("bookmark", "SimClusters")),
    (("cold start", "冷启动", "冷啟動", "200"), ("cold-start", "Home", "Beta", "eligibility")),
    (("32 likes", "32赞", "32讚"), ("32fav", "1fav", "index")),
    (("video", "10 seconds", "视频", "影片"), ("video", "10000", "VQV", "duration")),
    (("shadowban", "low reach", "限流", "曝光低"), ("visibility", "label", "Under the Hood", "audience")),
    (("weight", "score", "权重", "權重", "加分"), ("weight", "coefficient", "prediction", "ranking")),
    (("hashtag", "话题标签", "話題標籤"), ("hashtag", "MaxHashtagsPerTweet")),
    (("external link", "pinned", "外链", "外鏈", "置顶", "置頂"), ("URL", "link", "LOW_QUALITY", "pinned")),
    (("completion", "dwell", "read through", "完读", "完讀", "停留", "閱讀", "阅读"), ("CREAD", "ld", "dwell", "reading")),
]
STOP = set("a an the is are was were be been being to of for on in with how what why when where can should does do i my we you it this that and or x twitter".split()) | {"什么", "是否", "怎样", "怎么", "为何", "为什么", "多少", "可以", "能不能", "应该", "如何"}



class KnowledgeError(ValueError):
    """An invalid corpus, with diagnostics safe for API and CLI callers."""

    def __init__(self, errors):
        self.errors = errors
        super().__init__('; '.join(errors))


def _unique_json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON field ' + key)
        result[key] = value
    return result


def read_json(path, reject_duplicate_keys=False):
    try:
        return json.loads(path.read_text(encoding='utf-8'),
                          object_pairs_hook=_unique_json_object if reject_duplicate_keys else None)
    except (OSError, UnicodeError, ValueError) as exc:
        raise KnowledgeError([f'{path.name}: cannot read JSON: {exc}']) from exc


def load(root=ROOT, report=None):
    """Load only a schema- and provenance-validated corpus.

    The optional report is the exact snapshot as UTF-8 bytes or text. Repository
    and installed layouts otherwise resolve their own bundled report.
    """
    root = Path(root)
    registry = read_json(root / 'sources.json')
    unit_document = read_json(root / 'source-units.json')
    errors = []
    if not isinstance(registry, dict):
        errors.append('sources.json: root must be an object')
    else:
        for field in ('snapshot', 'comparison_snapshot'):
            _string(registry.get(field), 'sources.json.' + field, errors)
        _date(registry.get('research_through'), 'sources.json.research_through', errors)
        _sha256(registry.get('report_sha256'), 'sources.json.report_sha256', errors)
        if not isinstance(registry.get('sources'), dict):
            errors.append('sources.json.sources must be an object')
    if not isinstance(unit_document, dict):
        errors.append('source-units.json: root must be an object')
    else:
        _list(unit_document.get('units'), 'source-units.json.units', errors, nonempty=True)
    documents = []
    claims = []
    for path in sorted(root.glob('topic-*.json')):
        topic = read_json(path)
        if not isinstance(topic, dict):
            errors.append(f'{path.name}: root must be an object')
            continue
        _string(topic.get('topic'), path.name + '.topic', errors)
        if _list(topic.get('claims'), path.name + '.claims', errors, nonempty=True):
            claims.extend(topic['claims'])
        documents.append((path.name, topic))
    if not documents:
        errors.append('No valid topic-*.json documents found')
    if errors:
        raise KnowledgeError(errors)
    units = unit_document['units']
    if report is None:
        report_path = (root.parent / 'research-report.md' if root.parent.name == 'references'
                       else root.parent / 'provenance' / 'research-report.zh-CN.md')
        try:
            report = report_path.read_bytes()
        except OSError as exc:
            raise KnowledgeError([f'{report_path.name}: cannot read report: {exc}']) from exc
    errors = validate(claims, registry['sources'], units, report=report)
    if isinstance(report, str):
        report = report.encode('utf-8')
    if isinstance(report, bytes) and hashlib.sha256(report).hexdigest() != registry['report_sha256']:
        errors.append('Report snapshot hash differs from source registry')
    if errors:
        raise KnowledgeError(errors)
    topics = [{'file': name, 'topic': topic['topic'], 'ids': [c['id'] for c in topic['claims']]}
              for name, topic in documents]
    claims = [dict(c, topic=topic['topic'], topic_file=name)
              for name, topic in documents for c in topic['claims']]
    return registry, units, topics, claims


def load_updates(root=ROOT, claim_ids=None):
    """Load the independently versioned upstream review, without rewriting claims.

    The file is required by this API. Historical corpora may still use load()
    without it. Callers that already loaded the corpus can supply its claim IDs
    to avoid loading and checking the same report twice.
    """
    root = Path(root)
    document = read_json(root / 'algorithm-updates.json', reject_duplicate_keys=True)
    errors = []
    label = 'algorithm-updates.json'
    fields = {'schema_version', 'repository', 'reviewed_at', 'base_snapshot',
              'snapshot', 'commits', 'entries'}
    if not isinstance(document, dict):
        raise KnowledgeError([label + ': root must be an object'])
    if set(document) != fields:
        errors.append(label + ' must contain exactly ' + ', '.join(sorted(fields)))
    if type(document.get('schema_version')) is not int or document['schema_version'] != 1:
        errors.append(label + '.schema_version must be 1')
    if document.get('repository') != 'xai-org/x-algorithm':
        errors.append(label + '.repository must be xai-org/x-algorithm')
    _date(document.get('reviewed_at'), label + '.reviewed_at', errors)
    snapshots_valid = True
    for field in ('base_snapshot', 'snapshot'):
        snapshots_valid = _sha1(document.get(field), label + '.' + field, errors) and snapshots_valid
    if snapshots_valid and document['base_snapshot'] == document['snapshot']:
        errors.append(label + ': base_snapshot and snapshot must differ')
    commits = document.get('commits')
    commits_valid = _unique_strings(commits, label + '.commits', errors, nonempty=True)
    if commits_valid:
        for index, commit in enumerate(commits):
            commits_valid = _sha1(commit, f'{label}.commits[{index}]', errors) and commits_valid
        if snapshots_valid:
            if commits[-1] != document['snapshot']:
                errors.append(label + '.commits must end at snapshot')
            if document['base_snapshot'] in commits:
                errors.append(label + '.commits must exclude base_snapshot')
    if claim_ids is None:
        claim_ids = {c['id'] for c in load(root)[3]}
    else:
        try:
            if isinstance(claim_ids, (str, bytes)):
                raise TypeError
            claim_ids = set(claim_ids)
            if not all(isinstance(ident, str) for ident in claim_ids):
                raise TypeError
        except TypeError as exc:
            raise KnowledgeError(['claim_ids must be an iterable of claim ID strings']) from exc
    topic_ids = {match.group(1) for path in root.glob('topic-*.json')
                 for match in [re.fullmatch(r'topic-(\d{2})\.json', path.name)] if match}
    entries = document.get('entries')
    entry_fields = {'id', 'title', 'status', 'topics', 'affects', 'summary',
                    'details', 'practical_meaning', 'limits', 'evidence'}
    ids = set()
    if _list(entries, label + '.entries', errors, nonempty=True):
        for index, entry in enumerate(entries):
            location = f'{label}.entries[{index}]'
            if not isinstance(entry, dict):
                errors.append(location + ' must be an object')
                continue
            if set(entry) != entry_fields:
                errors.append(location + ' must contain exactly ' + ', '.join(sorted(entry_fields)))
            ident = entry.get('id')
            if not isinstance(ident, str) or not re.fullmatch(r'A\d{8}-\d{2,}', ident):
                errors.append(location + '.id must be an update ID such as A20261108-01')
            else:
                if ident in ids:
                    errors.append('duplicate update ID ' + ident)
                ids.add(ident)
            for field in ('title', 'summary', 'practical_meaning'):
                _string(entry.get(field), location + '.' + field, errors)
            if entry.get('status') not in ('changed', 'unchanged'):
                errors.append(location + '.status must be changed or unchanged')
            for field in ('details', 'limits'):
                _unique_strings(entry.get(field), location + '.' + field, errors, nonempty=True)
            for field, allowed, description in (('topics', topic_ids, 'topic'),
                                                 ('affects', claim_ids, 'affected claim')):
                if _unique_strings(entry.get(field), location + '.' + field, errors,
                                   nonempty=(field == 'topics')):
                    for reference in entry[field]:
                        if reference not in allowed:
                            errors.append(f'{location}: unknown {description} {reference}')
            evidence = entry.get('evidence')
            if _list(evidence, location + '.evidence', errors, nonempty=True):
                urls = set()
                for number, item in enumerate(evidence):
                    evidence_label = f'{location}.evidence[{number}]'
                    if not isinstance(item, dict):
                        errors.append(evidence_label + ' must be an object')
                        continue
                    if set(item) != {'label', 'url'}:
                        errors.append(evidence_label + ' must contain exactly label, url')
                    _string(item.get('label'), evidence_label + '.label', errors)
                    url = item.get('url')
                    if isinstance(url, str):
                        if url in urls:
                            errors.append(evidence_label + ': duplicate evidence URL')
                        urls.add(url)
                    if (not snapshots_valid or not commits_valid or
                            not _pinned_update_url(url, document)):
                        errors.append(evidence_label + '.url must be a pinned GitHub blob at base_snapshot '
                                      'or snapshot, a reviewed commit, or the exact base...snapshot comparison')
    if errors:
        raise KnowledgeError(errors)
    return document


def _sha1(value, label, errors):
    if not isinstance(value, str) or not re.fullmatch(r'[0-9a-f]{40}', value):
        errors.append(label + ' must be a full commit SHA (40 lowercase hexadecimal characters)')
        return False
    return True


def _unique_strings(value, label, errors, nonempty=False):
    if not _list(value, label, errors, nonempty=nonempty):
        return False
    if not _strings(value, label, errors):
        return False
    if len(value) != len(set(value)):
        errors.append(label + ' must not contain duplicates')
        return False
    return True


def _pinned_update_url(url, document):
    if not isinstance(url, str) or re.search(r'\s', url):
        return False
    try:
        parsed = urlsplit(url)
    except ValueError:
        return False
    prefix = '/xai-org/x-algorithm/'
    if (parsed.scheme != 'https' or parsed.netloc != 'github.com' or
            parsed.query or not parsed.path.startswith(prefix)):
        return False
    path = parsed.path[len(prefix):]
    parts = path.split('/')
    if parts[0] == 'blob' and len(parts) >= 3:
        return (parts[1] in (document['base_snapshot'], document['snapshot']) and
                all(part not in ('', '.', '..') and '%' not in part for part in parts[2:]))
    if parts[0] == 'commit' and len(parts) == 2:
        return parts[1] in [document['base_snapshot'], *document['commits']]
    return path == 'compare/' + document['base_snapshot'] + '...' + document['snapshot']


def update_coverage(document):
    """Describe reviewed public source coverage separately from report dates."""
    if document is None:
        return None
    entries = document['entries']
    return {**{field: document[field] for field in
               ('repository', 'reviewed_at', 'base_snapshot', 'snapshot')},
            'commit_count': len(document['commits']), 'update_count': len(entries),
            'changed_count': sum(e['status'] == 'changed' for e in entries),
            'unchanged_count': sum(e['status'] == 'unchanged' for e in entries),
            'affected_claim_count': len({ident for e in entries for ident in e['affects']}),
            'scope': 'Reviewed public source changes; not current production deployment verification.'}


def search_updates(entries, query, limit=8, claim_ids=()):
    """Retrieve new vocabulary and reviews attached to historical matches."""
    query_terms = terms(query)
    literal_query = query.strip().lower()
    selected = set(claim_ids)
    ranked = []
    for entry in entries:
        title = entry['title'].lower()
        body = ' '.join([entry['summary'], entry['practical_meaning'],
                         *entry['details'], *entry['limits']]).lower()
        score = sum((8 if term in title else 0) + (1 if term in body else 0)
                    for term in query_terms)
        # A new field's exact name must outrank broad synonym expansions such
        # as "weight"; otherwise the new vocabulary can disappear at limit=1.
        if query_terms and literal_query and (literal_query in title or literal_query in body):
            score += 100
        if query.lower() == entry['id'].lower():
            score += 10000
        if selected.intersection(entry['affects']):
            score += 4
        if score:
            ranked.append((score, entry))
    return sorted(ranked, key=lambda pair: (-pair[0], pair[1]['id']))[:limit]


def expand_claim(claim, sources):
    result = copy.deepcopy(claim)
    for e in result['evidence']:
        source = sources[e['source_id']]
        e['title'] = source.get('title', e['source_id'])
        e['links'] = [copy.deepcopy(source['links'][i]) for i in e['link_indices']]
    return result


def terms(query):
    q = query.lower()
    result = set(re.findall(r'[a-z_][a-z0-9_:.]*|\d+(?:\.\d+)?', q)) - STOP
    for chunk in re.findall(r'[\u3400-\u9fff]+', q):
        if chunk not in STOP:
            result.add(chunk)
        for size in (2, 3, 4):
            result.update(chunk[i:i+size] for i in range(len(chunk)-size+1) if chunk[i:i+size] not in STOP)
    for triggers, expansion in SYNONYMS:
        if any(t.lower() in q for t in triggers):
            result.update(t.lower() for t in expansion)
    return result


def search_claims(claims, query, limit=8):
    ts = terms(query)
    numbers = re.findall(r'\d+(?:\.\d+)?', query)
    ranked = []
    for c in claims:
        title = c['title'].lower()
        trigger = c['check']['when'].lower()
        body = ' '.join([c['conclusion'], *c['conditions'], *c['limits'], c['practical_meaning']]).lower()
        score = sum((8 if t in title else 0) + (4 if t in trigger else 0) + (1 if t in body else 0) for t in ts)
        for number in numbers:
            pattern = r'(?<![\d.])' + re.escape(number) + r'(?![\d.])'
            score += 16 if re.search(pattern, title) else 0
            score += 6 if re.search(pattern, body) else 0
        if query.lower() == c['id'].lower():
            score += 10000
        if score:
            ranked.append((score, c))
    return sorted(ranked, key=lambda pair: (-pair[0], pair[1]['id']))[:limit]


def _string(value, label, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f'{label} must be a nonempty string')
        return False
    return True


def _list(value, label, errors, nonempty=False):
    if not isinstance(value, list) or (nonempty and not value):
        errors.append(f'{label} must be a {"nonempty " if nonempty else ""}list')
        return False
    return True


def _strings(value, label, errors):
    if not _list(value, label, errors):
        return False
    valid = True
    for index, item in enumerate(value):
        valid = _string(item, f'{label}[{index}]', errors) and valid
    return valid


def _sha256(value, label, errors):
    if not isinstance(value, str) or not re.fullmatch(r'[0-9a-f]{64}', value):
        errors.append(f'{label} must be a SHA-256 hash (64 lowercase hexadecimal characters)')
        return False
    return True


def _date(value, label, errors):
    if isinstance(value, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        try:
            date.fromisoformat(value)
            return True
        except ValueError:
            pass
    errors.append(f'{label} must be a valid YYYY-MM-DD date')
    return False


def _links(value, label, errors):
    if not _list(value, label, errors, nonempty=True):
        return
    for index, link in enumerate(value):
        location = f'{label}[{index}]'
        if not isinstance(link, dict):
            errors.append(f'{location} must be an object')
            continue
        _string(link.get('label'), location + '.label', errors)
        url = link.get('url')
        valid = isinstance(url, str) and not re.search(r'\s', url)
        if valid:
            try:
                parsed = urlsplit(url)
                valid = parsed.scheme == 'https' and bool(parsed.hostname)
            except ValueError:
                valid = False
        if not valid:
            errors.append(f'{location}.url must be an absolute https URL')


def _sources(sources, errors):
    """Return safe link counts for reference checks, after validating shapes."""
    if not isinstance(sources, dict):
        errors.append('sources must be an object')
        return {}
    counts = {}
    for sid, source in sources.items():
        label = f'sources.{sid}'
        if not _string(sid, label + ' ID', errors):
            continue
        if not isinstance(source, dict):
            errors.append(f'{label} must be an object')
            continue
        _string(source.get('title'), label + '.title', errors)
        number = source.get('number')
        if number is not None and (type(number) is not int or number < 1):
            errors.append(f'{label}.number must be a positive integer or null for an unnumbered source')
        _links(source.get('links'), label + '.links', errors)
        if isinstance(source.get('links'), list):
            counts[sid] = len(source['links'])
    return counts


def _units(units, source_ids, report, errors):
    """Validate 1-based inclusive slices; unit hashes omit a trailing newline."""
    unit_ids, required = set(), set()
    lines = None
    if report is not None:
        try:
            if isinstance(report, bytes):
                report = report.decode('utf-8')
            if not isinstance(report, str):
                errors.append('report must be UTF-8 text or bytes')
            else:
                lines = report.splitlines()
        except UnicodeError as exc:
            errors.append(f'report must be UTF-8: {exc}')
    if not _list(units, 'source-units', errors, nonempty=True):
        return unit_ids, required
    previous_end = 0
    for index, unit in enumerate(units):
        label = f'source-units[{index}]'
        if not isinstance(unit, dict):
            errors.append(f'{label} must be an object')
            continue
        ident = unit.get('id')
        if _string(ident, label + '.id', errors):
            label = f'source unit {ident}'
            if ident in unit_ids:
                errors.append(f'duplicate source unit ID {ident}')
            unit_ids.add(ident)
            if unit.get('kind') != 'anchor':
                required.add(ident)
        kind = unit.get('kind')
        if not isinstance(kind, str) or kind not in {'anchor', 'prose', 'table', 'code', 'unknown', 'provenance'}:
            errors.append(f'{label}.kind is invalid')
        _string(unit.get('section'), label + '.section', errors)
        valid_hash = _sha256(unit.get('sha256'), label + '.sha256', errors)
        if _strings(unit.get('source_ids'), label + '.source_ids', errors):
            for sid in unit['source_ids']:
                if sid not in source_ids:
                    errors.append(f'{label}: unknown source ID {sid}')
        bounds_valid = True
        for field in ('line_start', 'line_end'):
            if type(unit.get(field)) is not int or unit[field] < 1:
                errors.append(f'{label}.{field} must be a positive integer')
                bounds_valid = False
        if not bounds_valid:
            continue
        start, end = unit['line_start'], unit['line_end']
        if end < start or (lines is not None and end > len(lines)):
            errors.append(f'{label}: invalid report line range {start}-{end}')
            continue
        if start <= previous_end:
            errors.append(f'{label}: source units must be in report order without overlapping ranges')
        previous_end = end
        if lines is not None and valid_hash:
            digest = hashlib.sha256('\n'.join(lines[start-1:end]).encode('utf-8')).hexdigest()
            if digest != unit['sha256']:
                errors.append(f'{label}: report slice hash mismatch')
    return unit_ids, required


def _correction(value, label, errors):
    if not isinstance(value, dict):
        errors.append(f'{label} must be an object')
        return
    fields = {'review_finding', 'origin', 'date', 'summary', 'sources'}
    if set(value) != fields:
        errors.append(f'{label} must contain exactly {", ".join(sorted(fields))}')
    for field in ('review_finding', 'summary'):
        _string(value.get(field), label + '.' + field, errors)
    if value.get('origin') not in ('original_report', 'english_distillation'):
        errors.append(f'{label}.origin must be original_report or english_distillation')
    _date(value.get('date'), label + '.date', errors)
    _links(value.get('sources'), label + '.sources', errors)


def validate(claims, sources, units, report=None):
    """Return schema/reference errors without iterating malformed containers.

    Pass the report text or bytes to also verify slice bounds and content hashes.
    Loading a corpus, repository validation and all CLI commands always do so.
    """
    errors = []
    source_counts = _sources(sources, errors)
    unit_ids, required_units = _units(units, source_counts, report, errors)
    if not _list(claims, 'claims', errors, nonempty=True):
        return errors
    ids = [c['id'] for c in claims if isinstance(c, dict) and isinstance(c.get('id'), str)]
    if len(ids) != len(set(ids)):
        errors.append('duplicate claim IDs')
    ids = set(ids)
    covered = set()
    for index, claim in enumerate(claims):
        label = f'claims[{index}]'
        if not isinstance(claim, dict):
            errors.append(f'{label} must be an object')
            continue
        if isinstance(claim.get('id'), str) and claim['id'].strip():
            label = claim['id']
        for field in ('id', 'title', 'conclusion', 'practical_meaning'):
            _string(claim.get(field), label + '.' + field, errors)
        kind = claim.get('kind')
        if not isinstance(kind, str) or kind not in {'code', 'official', 'observation', 'editorial', 'unknown', 'myth'}:
            errors.append(f'{label}.kind is invalid')
        check = claim.get('check')
        if not isinstance(check, dict):
            errors.append(f'{label}.check must be an object')
        else:
            for field in ('when', 'if_missing'):
                _string(check.get(field), label + '.check.' + field, errors)
            for field in ('needed', 'verify'):
                _strings(check.get(field), label + '.check.' + field, errors)
        for field in ('conditions', 'limits'):
            _strings(claim.get(field), label + '.' + field, errors)
        if _strings(claim.get('source_units'), label + '.source_units', errors):
            for unit in claim['source_units']:
                if unit not in unit_ids:
                    errors.append(f'{label}: unknown source unit {unit}')
                covered.add(unit)
        if _strings(claim.get('related_unknowns'), label + '.related_unknowns', errors):
            for related in claim['related_unknowns']:
                if related not in ids:
                    errors.append(f'{label}: missing related_unknown {related}')
        evidence = claim.get('evidence')
        if _list(evidence, label + '.evidence', errors):
            if kind in ('code', 'official') and not evidence:
                errors.append(f'{label}: factual claim lacks evidence')
            for index, item in enumerate(evidence):
                location = f'{label}.evidence[{index}]'
                if not isinstance(item, dict):
                    errors.append(f'{location} must be an object')
                    continue
                sid = item.get('source_id')
                source_valid = _string(sid, location + '.source_id', errors)
                if source_valid and sid not in source_counts:
                    errors.append(f'{location}: unknown source {sid}')
                    source_valid = False
                _string(item.get('supports'), location + '.supports', errors)
                indices = item.get('link_indices')
                if _list(indices, location + '.link_indices', errors, nonempty=True):
                    for link_index in indices:
                        if (type(link_index) is not int or link_index < 0 or
                                (source_valid and link_index >= source_counts[sid])):
                            errors.append(f'{location}: invalid link index {sid}/{link_index}')
        if 'correction' in claim:
            _correction(claim['correction'], label + '.correction', errors)
    for unit in sorted(required_units - covered):
        errors.append(f'uncovered source unit {unit}')
    return errors


def output(value):
    print(json.dumps(value, ensure_ascii=False, indent=2))


def main():
    # JSON is always UTF-8, including redirected output on legacy Windows locales.
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    catalog = sub.add_parser('catalog', help='List all topics; select a topic to read every rule and trigger.')
    catalog.add_argument('--topic', help='Topic file number, name fragment, or topic title.')
    catalog.add_argument('--all-rules', action='store_true', help='Include every rule and trigger; potentially large output.')
    get = sub.add_parser('get', help='Return exact claims and their resolved original links.')
    get.add_argument('ids', nargs='+')
    updates_parser = sub.add_parser('updates', help='List versioned upstream findings, or read selected update IDs.')
    updates_parser.add_argument('ids', nargs='*')
    search = sub.add_parser('search', help='Lexical/synonym retrieval; inspect results, not an exhaustive semantic oracle.')
    search.add_argument('query')
    search.add_argument('--limit', type=int, default=8)
    source = sub.add_parser('sources', help='Show original reference groups without inventing URLs.')
    source.add_argument('ids', nargs='+')
    origin = sub.add_parser('original', help='Read the exact report units supporting a claim.')
    origin.add_argument('unit_ids', nargs='+')
    sub.add_parser('audit', help='Check schema, citations and complete source-unit coverage offline.')
    args = parser.parse_args()
    try:
        report = REPORT.read_bytes()
        registry, units, topics, claims = load(report=report)
        updates = (load_updates(claim_ids={c['id'] for c in claims})
                   if (ROOT / 'algorithm-updates.json').is_file() else None)
    except (KnowledgeError, OSError) as exc:
        errors = exc.errors if isinstance(exc, KnowledgeError) else [f'Cannot read report: {exc}']
        if args.command == 'audit':
            output({'errors': errors, 'scope': 'Offline content/reference integrity; corpus is invalid.'})
            sys.exit(1)
        parser.error('Invalid knowledge corpus: ' + '; '.join(errors))
    sources = registry['sources']
    by_id = {c['id']:c for c in claims}
    entries = updates['entries'] if updates else []
    coverage = update_coverage(updates)
    if args.command == 'catalog':
        subset = claims
        if args.topic:
            subset = [c for c in claims if args.topic.lower() in (c['topic_file']+' '+c['topic']).lower()]
        result = {'snapshot':registry['snapshot'], 'research_through':registry['research_through'],
                  'current_coverage':coverage,
                  'topics':[{'file':t['file'],'topic':t['topic'],'rule_count':len(t['ids']),
                             'update_count':sum(t['file'][6:8] in e['topics'] for e in entries)} for t in topics]}
        if args.topic or args.all_rules:
            result['rules'] = [{'id':c['id'],'title':c['title'],'kind':c['kind'],'when':c['check']['when']} for c in subset]
        else:
            result['next_step'] = 'Read all topic scopes, then use catalog --topic NN for each applicable topic; get selected IDs for full evidence.'
        output(result)
    elif args.command == 'get':
        missing = [i for i in args.ids if i not in by_id]
        if missing:
            parser.error('Unknown claim IDs: '+', '.join(missing))
        selected = [by_id[i] for i in args.ids]
        output({'research_through':registry['research_through'],'claims':[expand_claim(c,sources) for c in selected],
                'original_snapshot':registry['snapshot'], 'current_coverage':coverage,
                'current_updates':[e for e in entries if set(args.ids).intersection(e['affects'])],
                'related_unknowns':sorted({q for c in selected for q in c['related_unknowns']})})
    elif args.command == 'updates':
        by_update_id = {e['id']:e for e in entries}
        missing = [ident for ident in args.ids if ident not in by_update_id]
        if missing:
            parser.error('Unknown update IDs: ' + ', '.join(missing))
        result = {'research_through':registry['research_through'],
                  'original_snapshot':registry['snapshot'], 'current_coverage':coverage}
        if args.ids:
            result['entries'] = [by_update_id[ident] for ident in args.ids]
        else:
            result['entries'] = [{field:e[field] for field in
                                  ('id', 'title', 'status', 'topics', 'affects', 'summary')} for e in entries]
            result['next_step'] = 'Use updates AYYYYMMDD-NN for full findings and fixed source evidence.'
        output(result)
    elif args.command == 'search':
        matches = search_claims(claims, args.query, max(1, args.limit))
        output({'retrieval':'lexical with topic synonyms; read topic catalog if relevant coverage is unclear',
                'research_through':registry['research_through'], 'current_coverage':coverage,
                'results':[{'match_score':s,'id':c['id'],'title':c['title'],'kind':c['kind'],'topic_file':c['topic_file'],'when':c['check']['when']} for s,c in matches],
                'current_updates':[dict(e, match_score=s) for s,e in search_updates(
                    entries, args.query, max(1,args.limit), claim_ids=[c['id'] for _,c in matches])]})
    elif args.command == 'sources':
        missing = [i for i in args.ids if i not in sources]
        if missing:
            parser.error('Unknown source IDs: '+', '.join(missing))
        output({i:sources[i] for i in args.ids})
    elif args.command == 'original':
        by_unit = {u['id']:u for u in units}
        if any(i not in by_unit for i in args.unit_ids):
            parser.error('Unknown source unit')
        lines = report.decode('utf-8').splitlines()
        output([dict(by_unit[i], text='\n'.join(lines[by_unit[i]['line_start']-1:by_unit[i]['line_end']])) for i in args.unit_ids])
    else:
        errors = []  # load validated schema, report snapshot and all source slices.
        cited = {e['source_id'] for c in claims for e in c['evidence']}
        output({'claims':len(claims),'unresolved_questions':sum(c['id'].startswith('Q') for c in claims),
                'research_through':registry['research_through'], 'original_snapshot':registry['snapshot'],
                'current_coverage':coverage,
                'source_units':len(units),'required_units':sum(u['kind']!='anchor' for u in units),
                'covered_units':len({u for c in claims for u in c['source_units']}),
                'source_groups':len(sources),'cited_source_groups':len(cited),
                'uncited_groups':sorted(set(sources)-cited),'errors':errors,
                'scope':'Offline content/reference integrity; not source availability or current production verification.'})
        sys.exit(bool(errors))


if __name__ == '__main__':
    main()
