"""Validate English evidence, original coverage, local references and distributable skills."""
import hashlib
import json
from pathlib import Path
import re
import sys

import build
import knowledge

ROOT = Path(__file__).resolve().parents[1]


def validate_repository(root=ROOT):
    errors = []
    registry, units, topics, claims = knowledge.load(root/'knowledge')
    errors.extend(knowledge.validate(claims, registry['sources'], units))
    if len(claims) != 578 or sum(c['id'].startswith('Q') for c in claims) != 49:
        errors.append('Unexpected original claim/unknown count')
    original = (root/'provenance/research-report.zh-CN.md').read_bytes()
    if hashlib.sha256(original).hexdigest() != registry['report_sha256']:
        errors.append('Original report hash mismatch')
    baseline = json.loads((root/'provenance/migration-baseline.json').read_text())
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
        if re.search(r'[\u3400-\u9fff]', path.read_text()):
            errors.append(f'Untranslated knowledge prose: {path.name}')
    for name in build.NAMES:
        folder = root/'skills'/name
        entry = folder/'SKILL.md'
        if not entry.is_file():
            errors.append(f'Missing skill {name}')
            continue
        text = entry.read_text()
        if not text.startswith('---\n') or f'\nname: {name}\n' not in text:
            errors.append(f'Invalid frontmatter {name}')
        description = re.search(r'^description: (.+)$', text, re.M)
        if not description or not 0 < len(description.group(1)) <= 1024:
            errors.append(f'Invalid description {name}')
        for page in folder.rglob('*.md'):
            if page.name == 'research-report.md':
                continue
            data = page.read_text()
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
