import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class PackagingTests(unittest.TestCase):
    def test_helpers_emit_utf8_under_legacy_console_encoding(self):
        with tempfile.TemporaryDirectory() as d:
            draft = Path(d)/'draft.txt'
            draft.write_text('中文草稿', encoding='utf-8')
            posts = Path(d)/'posts.json'
            posts.write_text(json.dumps([{'text': '截图正文'}], ensure_ascii=False), encoding='utf-8')
            cases = [('knowledge.py', 'original', 'U0001'),
                     ('inspect_draft.py', '--text', str(draft)),
                     ('summarize_posts.py', '--input', str(posts))]
            for case in cases:
                with self.subTest(helper=case[0]):
                    run = subprocess.run([sys.executable, str(ROOT/'tools'/case[0]), *case[1:]],
                                         capture_output=True, env=dict(os.environ, PYTHONIOENCODING='cp1252'))
                    self.assertEqual(run.returncode, 0, run.stderr.decode('utf-8', errors='replace'))
                    decoded = run.stdout.decode('utf-8')
                    json.loads(decoded)
                    self.assertRegex(decoded, r'[\u3400-\u9fff]')

    def test_validation_under_non_utf8_default_encoding(self):
        sys.path.insert(0, str(ROOT/'tools'))
        import validate
        original = Path.read_text

        def legacy_read_text(path, encoding=None, errors=None):
            return original(path, encoding=encoding or 'cp1252', errors=errors)

        with patch.object(Path, 'read_text', legacy_read_text):
            errors, _ = validate.validate_repository()
        self.assertEqual(errors, [])

    def test_packager_available(self):
        self.assertTrue((ROOT/'tools/build.py').is_file(), 'No self-contained packager exists')

    def test_router_routes_have_real_independent_fallbacks(self):
        skill = ROOT/'skills/x-assistant'
        self.assertTrue((skill/'references/routing.json').is_file(), 'Router table missing')
        routes = json.loads((skill/'references/routing.json').read_text(encoding='utf-8'))['routes']
        self.assertEqual(len(routes), 7)
        for route in routes:
            self.assertTrue((skill/route['fallback']).is_file(), route['skill'])

    def test_each_isolated_skill_can_query_and_audit(self):
        import shutil
        paths = sorted((ROOT/'skills').glob('*/SKILL.md'))
        self.assertEqual(len(paths), 8)
        for path in paths:
            with tempfile.TemporaryDirectory() as d:
                dest = Path(d)/'only-skill'
                shutil.copytree(path.parent, dest)
                for args in (['audit'], ['get', 'K03-001'], ['search', 'posting frequency']):
                    run = subprocess.run([sys.executable, str(dest/'scripts/knowledge.py'), *args],
                                         cwd=d, capture_output=True, text=True, encoding='utf-8')
                    self.assertEqual(run.returncode, 0, run.stderr+run.stdout)
                    data = json.loads(run.stdout)
                    if args[0] == 'audit':
                        self.assertEqual(data['errors'], [])
                        self.assertEqual(data['claims'], 578)
                        self.assertEqual(data['unresolved_questions'], 49)

    def test_visual_workflow_works_from_isolated_installations(self):
        import shutil
        for name in ('x-assistant', 'x-publish-checklist', 'x-create-visuals'):
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as d:
                installed = Path(d)/'only-skill'
                self.assertTrue((ROOT/'skills'/name).is_dir(), name+' is missing')
                shutil.copytree(ROOT/'skills'/name, installed)
                helper = installed/'scripts/visual_preferences.py'
                self.assertTrue(helper.is_file(), name+' lacks preference persistence')
                guide = installed/'references/visual-workflow.md'
                self.assertTrue(guide.is_file(), name+' lacks creation fallback')
                state = Path(d)/'private/visual-preferences.json'
                profile = Path(d)/'profile.json'
                profile.write_text(json.dumps({'source':'ai', 'style':'Editorial ink'}), encoding='utf-8')
                for args in (['save', '--input', str(profile)], ['show']):
                    run = subprocess.run([sys.executable, str(helper), '--file', str(state), *args],
                                         cwd=d, capture_output=True, text=True, encoding='utf-8')
                    self.assertEqual(run.returncode, 0, run.stdout+run.stderr)
                    if args[0] == 'show':
                        self.assertEqual(json.loads(run.stdout)['profile']['style'], 'Editorial ink')

    def test_build_check_rejects_drift(self):
        import shutil
        self.assertTrue((ROOT/'tools/build.py').is_file(), 'Packager missing')
        with tempfile.TemporaryDirectory() as d:
            dest = Path(d)/'repo'
            shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            target = dest/'skills/x-explain/SKILL.md'
            self.assertTrue(target.is_file())
            target.write_text(target.read_text(encoding='utf-8')+'\nAccidental drift.\n', encoding='utf-8')
            run = subprocess.run([sys.executable, str(dest/'tools/build.py'), '--check'], capture_output=True, text=True, encoding='utf-8')
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('x-explain/SKILL.md', run.stdout)


if __name__ == '__main__': unittest.main()
