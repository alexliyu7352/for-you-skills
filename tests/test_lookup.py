import copy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('knowledge', ROOT/'tools/knowledge.py')
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


class LookupTests(unittest.TestCase):
    def setUp(self):
        self.sources = {'S001': {'links': [{'label': 'code', 'url': 'https://example.org/code'}]}}
        self.units = [{'id': 'U0001', 'kind': 'prose', 'source_ids': ['S001']}]
        self.claim = {'id': 'K01-001', 'title': 'Posting frequency and author diversity', 'kind': 'code',
            'conclusion': 'The count concerns candidates in this request, not a daily posting quota.',
            'conditions': ['Same author within the candidate set'], 'practical_meaning': 'Publish useful new information.',
            'check': {'when': 'Posting frequency', 'needed': ['Candidate set'], 'verify': ['Check the unit of counting'],
                      'if_missing': 'The candidate position is unknown.'}, 'limits': ['No optimal interval established'],
            'source_units': ['U0001'], 'evidence': [{'source_id': 'S001', 'link_indices': [0], 'supports': 'Counted object'}],
            'related_unknowns': []}

    def test_original_citation_resolves_without_mutating_claim(self):
        original = copy.deepcopy(self.claim)
        got = kb.expand_claim(self.claim, self.sources)
        self.assertEqual(got['evidence'][0]['links'][0]['url'], 'https://example.org/code')
        self.assertEqual(original, self.claim)

    def test_invalid_reference_and_uncovered_evidence_fail(self):
        self.claim['evidence'][0]['link_indices'] = [1]
        self.claim['source_units'] = []
        errors = kb.validate([self.claim], self.sources, self.units)
        self.assertTrue(any('link index' in e for e in errors))
        self.assertTrue(any('uncovered' in e for e in errors))

    def test_unknown_and_duplicate_ids_fail(self):
        self.claim['related_unknowns'] = ['Q49']
        errors = kb.validate([self.claim, self.claim], self.sources, self.units)
        self.assertTrue(any('duplicate' in e for e in errors))
        self.assertTrue(any('related_unknown' in e for e in errors))

    def test_english_and_chinese_retrieve_english_frequency_claim(self):
        for question in ('How often should I post each day?', '一天能发几条', '每天應該發幾條？'):
            self.assertEqual(kb.search_claims([self.claim], question)[0][1]['id'], 'K01-001')

    def test_empty_and_unrelated_queries_have_no_match(self):
        for query in ('', 'the and to', 'unrelated_xyz'):
            self.assertEqual(kb.search_claims([self.claim], query), [])


if __name__ == '__main__':
    unittest.main()
