"""Validate English evidence, original coverage, local references and distributable skills."""
import json
from pathlib import Path
import re
import sys

import build
import knowledge

ROOT = Path(__file__).resolve().parents[1]


def frontmatter_errors(text, name):
    """Validate the repository's dependency-free YAML scalar subset.

    A complete --- block contains only name and description, once each, at
    column zero. Values are single-line plain strings, JSON double-quoted
    strings, or YAML single-quoted strings (escape a quote by doubling it).
    Blank lines and whole-line comments are allowed. Plain strings cannot
    start with YAML indicators or number-like text, contain ': ' or inline
    comments, or be YAML booleans/nulls. Collections, tags, aliases, block
    scalars and other keys require a fuller YAML parser and are rejected.
    """
    prefix = f'Invalid frontmatter {name}: '
    lines = text.splitlines()
    if not lines or lines[0] != '---':
        return [prefix + 'expected an opening --- delimiter on the first line']
    try:
        end = lines.index('---', 1)
    except ValueError:
        return [prefix + 'missing closing --- delimiter']
    fields, errors = {}, []
    for line in lines[1:end]:
        if not line.strip() or line.startswith('#'):
            continue
        match = re.fullmatch(r'(name|description):[ \t]*(.*)', line)
        if not match:
            errors.append(prefix + 'supported keys are name and description at column zero; use single-line string values')
            continue
        key, raw = match.groups()
        if key in fields:
            errors.append(prefix + f'duplicate {key} field')
            continue
        fields[key] = None
        raw = raw.strip()
        value = raw
        if raw.startswith('"'):
            try:
                value = json.loads(raw)
            except ValueError:
                value = None
        elif raw.startswith("'"):
            value = raw[1:-1].replace("''", "'") if re.fullmatch(r"'(?:[^']|'')*'", raw) else None
        elif (not raw or raw[0] in '-?:,[]{}#&*!|>\"\'%@`' or
              re.match(r'(?:\d|[.+-]\d)', raw) or re.search(r':(?:\s|$)|\s#', raw) or
              raw.lower() in {'null', '~', 'true', 'false', 'yes', 'no', 'on', 'off', '.nan', '.inf', '+.inf'}):
            value = None
        if not isinstance(value, str) or not value.strip() or any(ord(c) < 32 for c in value):
            errors.append(prefix + f'{key} requires a single-line string; quote ambiguous plain values (collections and block scalars are unsupported)')
            continue
        fields[key] = value
    if fields.get('name') != name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        errors.append(prefix + f'name must be {name!r} (lowercase letters, digits and single hyphens; maximum 64 characters)')
    if not isinstance(fields.get('description'), str) or not 0 < len(fields['description']) <= 1024:
        errors.append(prefix + 'description must contain 1 to 1024 characters')
    return errors


def validate_repository(root=ROOT):
    root = Path(root)
    errors = []
    try:
        original = (root/'provenance/research-report.zh-CN.md').read_bytes()
        registry, units, topics, claims = knowledge.load(root/'knowledge', report=original)
        baseline = knowledge.read_json(root/'provenance/migration-baseline.json')
    except knowledge.KnowledgeError as exc:
        return exc.errors, {}
    except OSError as exc:
        return [f'Cannot read repository evidence: {exc}'], {}
    if not isinstance(baseline, dict) or not all(isinstance(baseline.get(k), dict) for k in ('claims', 'source_urls')):
        return ['migration-baseline.json must contain claims and source_urls objects'], {}
    if len(claims) != 578 or sum(c['id'].startswith('Q') for c in claims) != 49:
        errors.append('Unexpected original claim/unknown count')
    fields = ('id', 'kind', 'source_units', 'related_unknowns')
    current = {}
    for claim in claims:
        immutable = {k:claim[k] for k in fields}
        immutable['evidence'] = [{k:e[k] for k in ('source_id','link_indices')} for e in claim['evidence']]
        current[claim['id']] = immutable
    if current != baseline['claims']:
        errors.append('Claim identity, evidence or coverage mapping changed during migration')
    urls = {k:[x['url'] for x in v['links']] for k,v in registry['sources'].items()}
    if urls != baseline['source_urls']:
        errors.append('Original source URLs/order changed')
    for path in (root/'knowledge').glob('*.json'):
        if re.search(r'[\u3400-\u9fff]', path.read_text(encoding='utf-8')):
            errors.append(f'Untranslated knowledge prose: {path.name}')
    for name in build.NAMES:
        folder = root/'skills'/name
        entry = folder/'SKILL.md'
        if not entry.is_file():
            errors.append(f'Missing skill {name}')
            continue
        text = entry.read_text(encoding='utf-8')
        errors.extend(frontmatter_errors(text, name))
        for page in folder.rglob('*.md'):
            if page.name == 'research-report.md':
                continue
            data = page.read_text(encoding='utf-8')
            if re.search(r'[\u3400-\u9fff]', data):
                errors.append(f'Untranslated instructions {page.relative_to(root)}')
            for target in re.findall(r'\]\(([^)]+)\)', data):
                if re.match(r'\w+://|#', target):
                    continue
                if not (page.parent/target.split('#')[0]).exists():
                    errors.append(f'Broken local reference {page.relative_to(root)} -> {target}')
    errors.extend('Generated drift: '+p for p in build.check(root))
    return errors, {'claims':len(claims), 'unknowns':49, 'source_groups':len(registry['sources']),
                    'required_units':sum(u['kind']!='anchor' for u in units),
                    'covered_units':len({u for c in claims for u in c['source_units']}),
                    'unique_urls':len({url for group in urls.values() for url in group})}


if __name__ == '__main__':
    errors, counts = validate_repository()
    print(json.dumps(dict(counts, errors=errors, scope='Offline integrity, not live deployment or exposure uplift.'), indent=2))
    sys.exit(bool(errors))
