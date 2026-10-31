"""Build self-contained Agent Skills from canonical English workflows and knowledge."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('x-assistant', 'x-explain', 'x-myth-check', 'x-format-advisor',
         'x-publish-checklist', 'x-review-posts', 'x-reach-diagnosis')
SCRIPTS = ('knowledge.py', 'inspect_draft.py', 'summarize_posts.py')


def expected_files(root=ROOT):
    common = {}
    for path in sorted((root/'knowledge').glob('*.json')):
        common['references/knowledge/'+path.name] = path.read_bytes()
    for path in sorted((root/'shared').glob('*.md')):
        common['references/'+path.name] = path.read_bytes()
    common['references/research-report.md'] = (root/'provenance/research-report.zh-CN.md').read_bytes()
    for name in SCRIPTS:
        common['scripts/'+name] = (root/'tools'/name).read_bytes()
    result = {}
    for name in NAMES:
        prefix = 'skills/'+name+'/'
        result[prefix+'SKILL.md'] = (root/'workflows'/f'{name}.md').read_bytes()
        result[prefix+'agents/openai.yaml'] = (root/'metadata'/f'{name}.yaml').read_bytes()
        result.update({prefix+path: content for path, content in common.items()})
        if name == 'x-assistant':
            result[prefix+'references/routing.json'] = (root/'routing.json').read_bytes()
            for other in NAMES[1:]:
                body = (root/'workflows'/f'{other}.md').read_text(encoding='utf-8')
                body = body.replace('](references/', '](../')
                result[prefix+f'references/workflows/{other}.md'] = body.encode('utf-8')
    return result


def check(root=ROOT):
    expected = expected_files(root)
    errors = []
    for path, data in expected.items():
        dest = root/path
        if not dest.is_file() or dest.read_bytes() != data:
            errors.append(path)
    for path in (root/'skills').rglob('*'):
        if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
            relative = path.relative_to(root).as_posix()
            if relative not in expected:
                errors.append(relative+' (unexpected)')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Report generated-file drift without writing.')
    args = parser.parse_args()
    if args.check:
        errors = check()
        print(json.dumps({'generated_file_drift': errors}, indent=2))
        return bool(errors)
    expected = expected_files()
    for path, data in expected.items():
        dest = ROOT/path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    stale = check()
    print(json.dumps({'skills': len(NAMES), 'files_written': len(expected), 'remaining_drift': stale}, indent=2))
    return bool(stale)


if __name__ == '__main__':
    sys.exit(main())
