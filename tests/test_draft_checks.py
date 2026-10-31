import importlib.util
import sys
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


if __name__ == '__main__':
    unittest.main()
