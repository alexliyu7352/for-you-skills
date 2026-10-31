"""Query the report-derived X knowledge base; preserve evidence and coverage.

No network calls, prediction model, recommendation score, or exposure estimate.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import sys

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



def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def load(root=ROOT):
    registry = read_json(root / 'sources.json')
    units = read_json(root / 'source-units.json')['units']
    topics = []
    claims = []
    for path in sorted(root.glob('topic-*.json')):
        topic = read_json(path)
        topics.append({'file': path.name, 'topic': topic['topic'], 'ids': [c['id'] for c in topic['claims']]})
        for claim in topic['claims']:
            claims.append(dict(claim, topic=topic['topic'], topic_file=path.name))
    return registry, units, topics, claims


def expand_claim(claim, sources):
    result = copy.deepcopy(claim)
    for e in result['evidence']:
        source = sources[e['source_id']]
        e['title'] = source.get('title', e['source_id'])
        e['links'] = [source['links'][i] for i in e['link_indices']]
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


def validate(claims, sources, units):
    errors = []
    ids = [c.get('id') for c in claims]
    if len(ids) != len(set(ids)):
        errors.append('duplicate claim IDs')
    unit_ids = {u['id'] for u in units}
    required_units = {u['id'] for u in units if u['kind'] != 'anchor'}
    covered = set()
    required = {'id', 'title', 'kind', 'conclusion', 'conditions', 'practical_meaning', 'check', 'limits', 'source_units', 'evidence', 'related_unknowns'}
    for c in claims:
        ident = c.get('id', '?')
        if required - c.keys():
            errors.append(f'{ident}: missing fields {sorted(required-c.keys())}')
            continue
        if c['kind'] not in {'code', 'official', 'observation', 'editorial', 'unknown', 'myth'}:
            errors.append(f'{ident}: invalid kind')
        if not all(c[k] for k in ('title', 'conclusion', 'practical_meaning')):
            errors.append(f'{ident}: empty substantive field')
        check = c['check']
        if not isinstance(check, dict) or {'when','needed','verify','if_missing'} - check.keys():
            errors.append(f'{ident}: incomplete check')
        for k in ('conditions', 'limits', 'source_units', 'evidence', 'related_unknowns'):
            if not isinstance(c[k], list):
                errors.append(f'{ident}: {k} must be a list')
        for u in c['source_units']:
            if u not in unit_ids:
                errors.append(f'{ident}: unknown source unit {u}')
            covered.add(u)
        for q in c['related_unknowns']:
            if q not in ids:
                errors.append(f'{ident}: missing related_unknown {q}')
        if c['kind'] in {'code', 'official'} and not c['evidence']:
            errors.append(f'{ident}: factual claim lacks evidence')
        for e in c['evidence']:
            sid = e.get('source_id')
            if sid not in sources:
                errors.append(f'{ident}: unknown source {sid}')
                continue
            if not e.get('supports') or not e.get('link_indices'):
                errors.append(f'{ident}: incomplete evidence {sid}')
            for i in e.get('link_indices', []):
                if isinstance(i, bool) or not isinstance(i, int) or i < 0 or i >= len(sources[sid]['links']):
                    errors.append(f'{ident}: invalid link index {sid}/{i}')
    for u in sorted(required_units - covered):
        errors.append(f'uncovered source unit {u}')
    return errors


def output(value):
    print(json.dumps(value, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    catalog = sub.add_parser('catalog', help='List all topics; select a topic to read every rule and trigger.')
    catalog.add_argument('--topic', help='Topic file number, name fragment, or topic title.')
    catalog.add_argument('--all-rules', action='store_true', help='Include every rule and trigger; potentially large output.')
    get = sub.add_parser('get', help='Return exact claims and their resolved original links.')
    get.add_argument('ids', nargs='+')
    search = sub.add_parser('search', help='Lexical/synonym retrieval; inspect results, not an exhaustive semantic oracle.')
    search.add_argument('query')
    search.add_argument('--limit', type=int, default=8)
    source = sub.add_parser('sources', help='Show original reference groups without inventing URLs.')
    source.add_argument('ids', nargs='+')
    origin = sub.add_parser('original', help='Read the exact report units supporting a claim.')
    origin.add_argument('unit_ids', nargs='+')
    sub.add_parser('audit', help='Check schema, citations and complete source-unit coverage offline.')
    args = parser.parse_args()
    registry, units, topics, claims = load()
    sources = registry['sources']
    by_id = {c['id']:c for c in claims}
    if args.command == 'catalog':
        subset = claims
        if args.topic:
            subset = [c for c in claims if args.topic.lower() in (c['topic_file']+' '+c['topic']).lower()]
        result = {'snapshot':registry['snapshot'], 'research_through':registry['research_through'],
                  'topics':[{'file':t['file'],'topic':t['topic'],'rule_count':len(t['ids'])} for t in topics]}
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
                'related_unknowns':sorted({q for c in selected for q in c['related_unknowns']})})
    elif args.command == 'search':
        output({'retrieval':'lexical with topic synonyms; read topic catalog if relevant coverage is unclear',
                'results':[{'match_score':s,'id':c['id'],'title':c['title'],'kind':c['kind'],'topic_file':c['topic_file'],'when':c['check']['when']} for s,c in search_claims(claims,args.query,max(1,args.limit))]})
    elif args.command == 'sources':
        missing = [i for i in args.ids if i not in sources]
        if missing:
            parser.error('Unknown source IDs: '+', '.join(missing))
        output({i:sources[i] for i in args.ids})
    elif args.command == 'original':
        by_unit = {u['id']:u for u in units}
        if any(i not in by_unit for i in args.unit_ids):
            parser.error('Unknown source unit')
        lines = REPORT.read_text(encoding='utf-8').splitlines()
        output([dict(by_unit[i], text='\n'.join(lines[by_unit[i]['line_start']-1:by_unit[i]['line_end']])) for i in args.unit_ids])
    else:
        errors = validate(claims,sources,units)
        report = REPORT.read_bytes()
        if hashlib.sha256(report).hexdigest() != registry['report_sha256']:
            errors.append('Report snapshot hash differs from source registry')
        cited = {e['source_id'] for c in claims for e in c['evidence']}
        output({'claims':len(claims),'unresolved_questions':sum(c['id'].startswith('Q') for c in claims),
                'source_units':len(units),'required_units':sum(u['kind']!='anchor' for u in units),
                'covered_units':len({u for c in claims for u in c['source_units']}),
                'source_groups':len(sources),'cited_source_groups':len(cited),
                'uncited_groups':sorted(set(sources)-cited),'errors':errors,
                'scope':'Offline content/reference integrity; not source availability or current production verification.'})
        sys.exit(bool(errors))


if __name__ == '__main__':
    main()
