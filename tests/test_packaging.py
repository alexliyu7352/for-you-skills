import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackagingTests(unittest.TestCase):
    def test_packager_available(self):
        self.assertTrue((ROOT/'tools/build.py').is_file(), 'No self-contained packager exists')

    def test_router_routes_have_real_independent_fallbacks(self):
        skill = ROOT/'skills/x-assistant'
        self.assertTrue((skill/'references/routing.json').is_file(), 'Router table missing')
        routes = json.loads((skill/'references/routing.json').read_text())['routes']
        self.assertEqual(len(routes), 6)
        for route in routes:
            self.assertTrue((skill/route['fallback']).is_file(), route['skill'])

    def test_each_isolated_skill_can_query_and_audit(self):
        import shutil
        paths = sorted((ROOT/'skills').glob('*/SKILL.md'))
        self.assertEqual(len(paths), 7)
        for path in paths:
            with tempfile.TemporaryDirectory() as d:
                dest = Path(d)/'only-skill'
                shutil.copytree(path.parent, dest)
                for args in (['audit'], ['get', 'K03-001'], ['search', 'posting frequency']):
                    run = subprocess.run([sys.executable, str(dest/'scripts/knowledge.py'), *args],
                                         cwd=d, capture_output=True, text=True)
                    self.assertEqual(run.returncode, 0, run.stderr+run.stdout)
                    data = json.loads(run.stdout)
                    if args[0] == 'audit':
                        self.assertEqual(data['errors'], [])
                        self.assertEqual(data['claims'], 578)
                        self.assertEqual(data['unresolved_questions'], 49)

    def test_build_check_rejects_drift(self):
        import shutil
        self.assertTrue((ROOT/'tools/build.py').is_file(), 'Packager missing')
        with tempfile.TemporaryDirectory() as d:
            dest = Path(d)/'repo'
            shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            target = dest/'skills/x-explain/SKILL.md'
            self.assertTrue(target.is_file())
            target.write_text(target.read_text()+'\nAccidental drift.\n')
            run = subprocess.run([sys.executable, str(dest/'tools/build.py'), '--check'], capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('x-explain/SKILL.md', run.stdout)


if __name__ == '__main__': unittest.main()
