import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT/'tools/visual_preferences.py'


class VisualPreferencesTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        self.state = self.folder/'private/visual-preferences.json'
        self.profile = {'source': 'mixed', 'provider': 'native',
                        'style': 'Clean editorial cards', 'palette': ['#102030'],
                        'text_language': 'zh-CN', 'aspect_ratio': '4:5'}

    def input_file(self, data, name='input.json'):
        path = self.folder/name
        path.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
        return path

    def run_cli(self, *args, state=None, ok=True, env=None):
        self.assertTrue(HELPER.exists(), 'Missing portable visual preference helper')
        result = subprocess.run([sys.executable, str(HELPER), '--file', str(state or self.state),
                                 *map(str, args)], capture_output=True,
                                env=env or os.environ.copy())
        self.assertEqual(result.returncode == 0, ok, result.stderr.decode('utf-8', errors='replace'))
        return json.loads(result.stdout.decode('utf-8'))

    def save(self, scope='default', profile=None):
        return self.run_cli('save', '--scope', scope, '--input',
                            self.input_file(profile or self.profile))

    def test_first_read_does_not_create_state(self):
        result = self.run_cli('show')
        self.assertIsNone(result['profile'])
        self.assertFalse(self.state.exists())

    def test_saved_unicode_style_survives_new_process(self):
        self.profile['style'] = '简洁信息卡，保留原始证据'
        self.save()
        result = self.run_cli('show', env=dict(os.environ, PYTHONIOENCODING='cp1252'))
        self.assertEqual(result['profile'], self.profile)
        self.assertEqual(result['resolved_scope'], 'default')
        if os.name != 'nt':
            self.assertEqual(self.state.stat().st_mode & 0o777, 0o600)

    def test_scopes_and_read_only_temporary_override(self):
        self.save()
        series = dict(self.profile, style='Blue line art')
        self.save('series:weekly-code', series)
        original = self.state.read_bytes()
        result = self.run_cli('show', '--scope', 'series:weekly-code', '--override',
                              self.input_file({'style': 'Watercolor'}, 'override.json'))
        self.assertEqual(result['profile']['style'], 'Watercolor')
        self.assertEqual(self.state.read_bytes(), original)
        self.assertEqual(self.run_cli('show')['profile'], self.profile)
        self.assertEqual(self.run_cli('show', '--scope', 'account:other')['resolved_scope'], 'default')

    def test_export_import_and_conflict_preserve_existing(self):
        self.save()
        exported = self.folder/'export.json'
        self.run_cli('export', '--output', exported)
        other = self.folder/'other/visual-preferences.json'
        self.run_cli('import', '--input', exported, state=other)
        self.assertEqual(self.run_cli('show', state=other)['profile'], self.profile)
        self.save(profile=dict(self.profile, style='Different'))
        before = self.state.read_bytes()
        self.run_cli('import', '--input', exported, ok=False)
        self.assertEqual(self.state.read_bytes(), before)
        self.run_cli('import', '--input', exported, '--replace')
        self.assertEqual(self.run_cli('show')['profile'], self.profile)

    def test_invalid_schema_and_credentials_cannot_replace_valid_state(self):
        self.save()
        before = self.state.read_bytes()
        for bad in ({'api_key':'secret'}, {'source':'invented'}, {'palette':'blue'},
                    {'unknown_field':True}, {'style':{'nested':'unsupported'}}):
            with self.subTest(bad=bad):
                self.run_cli('save', '--input', self.input_file(bad), ok=False)
                self.assertEqual(self.state.read_bytes(), before)
        for version in (True, 9):
            self.run_cli('import', '--input', self.input_file(
                {'schema_version':version, 'revision':1, 'profiles':{'default':self.profile}}), ok=False)
            self.assertEqual(self.state.read_bytes(), before)

    def test_corrupt_existing_store_is_not_overwritten(self):
        self.state.parent.mkdir()
        self.state.write_text('broken json', encoding='utf-8')
        self.run_cli('save', '--input', self.input_file(self.profile), ok=False)
        self.assertEqual(self.state.read_text(encoding='utf-8'), 'broken json')

    def test_refuses_repo_and_installed_skill_destinations(self):
        for marker in ('.git', 'SKILL.md'):
            folder = self.folder/marker.replace('.', 'test')
            folder.mkdir()
            (folder/marker).write_text('marker', encoding='utf-8')
            blocked = folder/'config/visual-preferences.json'
            self.run_cli('save', '--input', self.input_file(self.profile), state=blocked, ok=False)
            self.assertFalse(blocked.exists())
        blocked = self.folder/'.agents/skills/profile.json'
        self.run_cli('save', '--input', self.input_file(self.profile), state=blocked, ok=False)
        self.assertFalse(blocked.exists())

    def test_environment_override_is_absolute_and_install_independent(self):
        self.assertTrue(HELPER.exists(), 'Missing portable visual preference helper')
        env = dict(os.environ, FOR_YOU_SKILLS_CONFIG_DIR=str(self.folder/'preferences'))
        result = subprocess.run([sys.executable, str(HELPER), 'path'], env=env,
                                capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(Path(json.loads(result.stdout)['path']), self.folder/'preferences/visual-preferences.json')
        env['FOR_YOU_SKILLS_CONFIG_DIR'] = 'relative'
        result = subprocess.run([sys.executable, str(HELPER), 'path'], env=env, capture_output=True)
        self.assertNotEqual(result.returncode, 0)

    def test_stale_revision_cannot_overwrite_newer_choice(self):
        self.save()
        before = self.state.read_bytes()
        self.run_cli('save', '--input', self.input_file(dict(self.profile, style='Old')),
                     '--expect-revision', '0', ok=False)
        self.assertEqual(self.state.read_bytes(), before)

    def test_os_default_locations(self):
        self.assertTrue(HELPER.exists(), 'Missing portable visual preference helper')
        import importlib.util
        spec = importlib.util.spec_from_file_location('visual_preferences', HELPER)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        home = self.folder
        self.assertEqual(module.default_path({}, 'linux', home), home/'.config/for-you-skills/visual-preferences.json')
        self.assertEqual(module.default_path({}, 'darwin', home), home/'Library/Application Support/for-you-skills/visual-preferences.json')
        self.assertEqual(module.default_path({}, 'win32', home), home/'AppData/Roaming/for-you-skills/visual-preferences.json')


if __name__ == '__main__':
    unittest.main()
