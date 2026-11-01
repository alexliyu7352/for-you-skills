import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HELPER = Path(__file__).resolve().parents[1] / "tools/inspect_draft.py"



class DraftChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert HELPER.is_file(), 'draft inspection helper has not been implemented'
        spec = importlib.util.spec_from_file_location('draft_checks', HELPER)
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def test_unicode_is_counted_as_python_characters(self):
        value = self.module.inspect_text('字' * 3999 + '😀尾', '题' * 201)
        self.assertEqual(value['characters'], 4001)
        self.assertEqual(value['after_4000_characters'], 1)
        self.assertEqual(value['preview_4000'][-1], '😀')
        self.assertEqual(len(value['article_title_preview_200']), 200)

    def test_exact_boundary_and_empty_text(self):
        self.assertEqual(self.module.inspect_text('字' * 4000)['after_4000_characters'], 0)
        self.assertEqual(self.module.inspect_text('')['preview_4000'], '')

    def test_whitespace_normalization_and_raw_boundary_are_explicit(self):
        text = '  ' + 'a' * 4000 + 'X\n'
        result = self.module.inspect_text(text)
        self.assertEqual(result.get('raw_characters'), 4004)
        self.assertEqual(result.get('raw_preview_4000'), text[:4000])
        self.assertEqual(result['characters'], 4001)
        self.assertIn('whitespace', result.get('normalization', ''))

    def test_duration_is_strictly_greater_than_ten_seconds(self):
        for duration, expected in [(10000, 'fails'), (10001, 'passes')]:
            result = self.module.inspect_video_gate([{'type': 'video', 'duration_ms': duration}])
            self.assertEqual(result['status'], expected)

    def test_mixed_media_fails_this_gate(self):
        result = self.module.inspect_video_gate([{'type':'video','duration_ms':15000},{'type':'image'}])
        self.assertEqual(result['status'], 'fails')

    def test_unknown_duration_is_not_zero(self):
        for item in [{'type':'video'}, {'type':'video','duration_ms':None}, {'type':'video','duration_ms':True}]:
            self.assertEqual(self.module.inspect_video_gate([item])['status'], 'unknown')

    def test_absent_or_incomplete_media_is_not_passed(self):
        self.assertEqual(self.module.inspect_video_gate([])['status'], 'not_applicable')
        self.assertEqual(self.module.inspect_video_gate([{'type':'unknown'}])['status'], 'unknown')
        self.assertEqual(self.module.inspect_video_gate([{'type':'video','duration_ms':15000}], complete=False)['status'], 'unknown')

    def test_cli_preserves_crlf_lf_and_lone_cr_before_counting(self):
        # Universal-newline conversion must not erase supplied code points.
        for raw, raw_count, trimmed_count, tail in [
            (b'A\r\n' * 2000, 6000, 5998, 1998),
            (b'A\n' * 2000, 4000, 3999, 0),
            (b'A\r' * 2000, 4000, 3999, 0),
        ]:
            with self.subTest(newline=raw[:3]), tempfile.TemporaryDirectory() as d:
                path = Path(d) / 'draft.txt'
                path.write_bytes(raw)
                run = subprocess.run([sys.executable, str(HELPER), '--text', str(path)],
                                     capture_output=True, text=True, encoding='utf-8')
                self.assertEqual(run.returncode, 0, run.stderr)
                got = json.loads(run.stdout)['text']
                self.assertEqual(got['raw_characters'], raw_count)
                self.assertEqual(got['characters'], trimmed_count)
                self.assertEqual(got['after_4000_characters'], tail)
                self.assertEqual(got['raw_preview_4000'], raw.decode('utf-8')[:4000])

    def test_cli_reports_malformed_media_without_traceback(self):
        for raw in ['null', '42', '"media"', '{}', '{"complete":true}',
                    '{"media":null}', '{"media":[null]}', '{"media":[],"complete":"yes"}', '{']:
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as d:
                draft, media = Path(d)/'draft.txt', Path(d)/'media.json'
                draft.write_text('draft', encoding='utf-8')
                media.write_text(raw, encoding='utf-8')
                run = subprocess.run([sys.executable, str(HELPER), '--text', str(draft),
                                      '--media-json', str(media)], capture_output=True, text=True, encoding='utf-8')
                self.assertEqual(run.returncode, 2, run.stderr)
                self.assertIn('media', run.stderr.lower())
                self.assertNotIn('Traceback', run.stderr)
                self.assertEqual(run.stdout, '')

    def test_cli_reports_unreadable_or_invalid_utf8_draft_cleanly(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/'draft.txt'
            for raw in (None, b'\xff'):
                if raw is not None:
                    path.write_bytes(raw)
                run = subprocess.run([sys.executable, str(HELPER), '--text', str(path)],
                                     capture_output=True, text=True, encoding='utf-8')
                self.assertEqual(run.returncode, 2, run.stderr)
                self.assertNotIn('Traceback', run.stderr)
                self.assertIn('draft', run.stderr.lower())


if __name__ == '__main__':
    unittest.main()
