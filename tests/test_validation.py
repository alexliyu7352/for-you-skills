"""Reject broken evidence before a lookup or an installer can consume it."""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import knowledge
import validate


REPORT = 'First source paragraph.\n\nSecond source paragraph.\n'
REGISTRY = {
    'report_sha256': 'f36daeeeb155a4d5306bf6ded340a06b08dd8a8938294f865df53343a3250cc8',
    'snapshot': 'a' * 40, 'comparison_snapshot': 'b' * 40,
    'research_through': '2026-10-29',
    'sources': {'S001': {'number': 1, 'title': 'Original evidence', 'links': [
        {'label': 'Original code', 'url': 'https://example.org/original'}]}},
}
UNITS = [
    {'id': 'U0001', 'kind': 'prose', 'line_start': 1, 'line_end': 1,
     'section': 'Report', 'source_ids': ['S001'],
     'sha256': '306857781718660e60ed127739d4f4ce88ad11d2ba6714583a45c59f3e821b3f'},
    {'id': 'U0002', 'kind': 'prose', 'line_start': 3, 'line_end': 3,
     'section': 'Report', 'source_ids': [],
     'sha256': '6a931fbfd94a4da9033dc4b42b4c03fdf5d8e8103d263961e4e4d2f0e74f0caa'},
]
CLAIM = {
    'id': 'K00-001', 'kind': 'code', 'title': 'Posting frequency',
    'conclusion': 'Candidate counts are not daily posting quotas.',
    'conditions': ['Within one request'], 'limits': ['Deployment is unknown.'],
    'practical_meaning': 'Check the scope before giving advice.',
    'check': {'when': 'Posting frequency', 'needed': ['Request scope'],
              'verify': ['Check the counted unit'], 'if_missing': 'State the uncertainty.'},
    'source_units': ['U0001', 'U0002'], 'related_unknowns': [],
    'evidence': [{'source_id': 'S001', 'link_indices': [0], 'supports': 'Counted unit'}],
}
CORRECTION = {
    'review_finding': 'KN-TEST', 'origin': 'original_report', 'date': '2026-10-31',
    'summary': 'Clarifies the counted unit.',
    'sources': [{'label': 'Correction evidence', 'url': 'https://example.org/correction'}],
}


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.kroot = self.root / 'references' / 'knowledge'
        self.kroot.mkdir(parents=True)
        (self.root / 'scripts').mkdir()
        shutil.copyfile(ROOT / 'tools' / 'knowledge.py', self.root / 'scripts' / 'knowledge.py')
        self.registry = copy.deepcopy(REGISTRY)
        self.units = copy.deepcopy(UNITS)
        self.claim = copy.deepcopy(CLAIM)
        self.write_corpus()

    def write_corpus(self):
        self.write_json('sources.json', self.registry)
        self.write_json('source-units.json', {'units': self.units})
        self.write_json('topic-00.json', {'topic': 'Posting scope', 'claims': [self.claim]})
        # The registry hashes exact UTF-8 bytes; text-mode writes translate LF on Windows.
        (self.root / 'references' / 'research-report.md').write_bytes(REPORT.encode('utf-8'))

    def write_json(self, name, data):
        (self.kroot / name).write_text(json.dumps(data), encoding='utf-8')

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(self.root / 'scripts' / 'knowledge.py'), *args],
                              cwd=self.root, capture_output=True, text=True, encoding='utf-8')

    def validation_errors(self, claims=None, sources=None, units=None):
        try:
            return knowledge.validate([self.claim] if claims is None else claims,
                                      self.registry['sources'] if sources is None else sources,
                                      self.units if units is None else units)
        except Exception as exc:
            self.fail('Validation crashed instead of reporting malformed input: ' + repr(exc))

    def assert_cli_rejects(self, command, *arguments, contains=None):
        run = self.run_cli(command, *arguments)
        self.assertNotEqual(run.returncode, 0, run.stdout)
        self.assertNotIn('Traceback', run.stderr)
        detail = run.stdout + run.stderr
        if contains:
            self.assertIn(contains.lower(), detail.lower())
        if command == 'audit':
            self.assertTrue(json.loads(run.stdout)['errors'])

    def test_valid_corpus_can_audit_and_read_exact_original(self):
        run = self.run_cli('audit')
        self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
        self.assertEqual(json.loads(run.stdout)['errors'], [])
        run = self.run_cli('original', 'U0002')
        self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
        self.assertEqual(json.loads(run.stdout)[0]['text'], 'Second source paragraph.')

    def test_duplicate_unit_ids_fail_without_losing_the_duplicate(self):
        self.units[1]['id'] = 'U0001'
        errors = self.validation_errors()
        self.assertTrue(any('duplicate' in e.lower() and 'unit' in e.lower() for e in errors), errors)

    def test_unit_metadata_mutations_block_audit_and_original(self):
        cases = [
            ('bounds', {'line_start': 999999, 'line_end': 999999}, 'range'),
            ('reversed', {'line_start': 2, 'line_end': 1}, 'range'),
            ('zero', {'line_start': 0}, 'line_start'),
            ('boolean', {'line_start': True}, 'line_start'),
            ('hash', {'sha256': '0' * 64}, 'hash'),
            ('source', {'source_ids': ['S404']}, 'source'),
            ('null sources', {'source_ids': None}, 'source_ids'),
            ('object ID', {'id': {}}, 'id'),
        ]
        for label, mutation, expected in cases:
            with self.subTest(mutation=label):
                self.units = copy.deepcopy(UNITS)
                self.units[0].update(mutation)
                self.write_corpus()
                self.assert_cli_rejects('audit', contains=expected)
                self.assert_cli_rejects('original', 'U0001', contains=expected)

    def test_overlapping_or_out_of_order_unit_slices_are_rejected(self):
        for units in ([UNITS[1], UNITS[0]], [UNITS[0], dict(UNITS[0], id='U0002')]):
            with self.subTest(units=units):
                self.units = copy.deepcopy(units)
                self.write_corpus()
                self.assert_cli_rejects('audit', contains='order')
                self.assert_cli_rejects('original', 'U0001', contains='order')

    def test_wrong_report_snapshot_blocks_original(self):
        (self.root / 'references' / 'research-report.md').write_text('Changed report.\n', encoding='utf-8')
        self.assert_cli_rejects('original', 'U0001', contains='hash')

    def test_substantive_fields_require_nonempty_strings(self):
        for field in ('id', 'title', 'conclusion', 'practical_meaning'):
            for value in ({'not': 'prose'}, 12, '   ', None):
                with self.subTest(field=field, value=value):
                    claim = copy.deepcopy(CLAIM)
                    claim[field] = value
                    errors = self.validation_errors(claims=[claim])
                    self.assertTrue(any(field in e for e in errors), errors)

    def test_claim_containers_and_elements_are_checked_before_iteration(self):
        for field in ('conditions', 'limits', 'source_units', 'related_unknowns', 'evidence'):
            for value in (None, {}, 'not a list', [None], [{}]):
                with self.subTest(field=field, value=value):
                    claim = copy.deepcopy(CLAIM)
                    claim[field] = value
                    errors = self.validation_errors(claims=[claim])
                    self.assertTrue(any(field in e for e in errors), errors)

    def test_check_fields_are_validated_before_search(self):
        for field, value in (('when', 42), ('if_missing', {}), ('needed', None),
                             ('verify', ['ok', 4]), ('needed', [''])):
            with self.subTest(field=field):
                self.claim = copy.deepcopy(CLAIM)
                self.claim['check'][field] = value
                errors = self.validation_errors()
                self.assertTrue(any('check.' + field in e for e in errors), errors)
                self.write_corpus()
                self.assert_cli_rejects('search', 'posting frequency', contains='check.' + field)

    def test_evidence_shape_types_and_indices_are_validated(self):
        for mutation in ({'source_id': []}, {'supports': 7}, {'link_indices': None},
                         {'link_indices': '0'}, {'link_indices': [True]},
                         {'link_indices': [-1]}, {'link_indices': [1]}, {'link_indices': []}):
            with self.subTest(mutation=mutation):
                self.claim = copy.deepcopy(CLAIM)
                self.claim['evidence'][0].update(mutation)
                errors = self.validation_errors()
                self.assertTrue(any('evidence' in e or 'link index' in e for e in errors), errors)

    def test_nonobject_claims_units_and_sources_report_errors(self):
        for claims in ('wrong', [None], [7], [[]]):
            with self.subTest(claims=claims):
                self.assertTrue(self.validation_errors(claims=claims))
        for units in ('wrong', [None], [7], [[]]):
            with self.subTest(units=units):
                self.assertTrue(self.validation_errors(units=units))
        for sources in ('wrong', [], {'S001': None}, {'S001': []}):
            with self.subTest(sources=sources):
                self.assertTrue(self.validation_errors(sources=sources))

    def test_source_link_objects_are_checked_before_evidence_resolution(self):
        for field, value in (('title', 7), ('links', None), ('links', [None]),
                             ('links', [{'label': 7, 'url': 'https://example.org'}]),
                             ('links', [{'label': 'Code', 'url': []}])):
            with self.subTest(field=field, value=value):
                self.registry = copy.deepcopy(REGISTRY)
                self.registry['sources']['S001'][field] = value
                self.assertTrue(self.validation_errors())
                self.write_corpus()
                self.assert_cli_rejects('get', 'K00-001', contains='sources')

    def test_unnumbered_external_sources_remain_usable(self):
        self.registry['sources']['E001'] = {
            'number': None, 'title': 'External reference',
            'links': [{'label': 'External guidance', 'url': 'https://example.org/guidance'}],
        }
        self.claim['evidence'].append({'source_id': 'E001', 'link_indices': [0], 'supports': 'Guidance'})
        self.write_corpus()
        run = self.run_cli('get', 'K00-001')
        self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
        self.assertEqual(json.loads(run.stdout)['claims'][0]['evidence'][1]['links'][0]['url'],
                         'https://example.org/guidance')

    def test_malformed_documents_fail_without_cli_tracebacks(self):
        cases = [('sources.json', None), ('sources.json', {'sources': []}),
                 ('source-units.json', []), ('source-units.json', {'units': None}),
                 ('topic-00.json', []), ('topic-00.json', {'topic': 3, 'claims': [CLAIM]}),
                 ('topic-00.json', {'topic': 'Scope', 'claims': None}),
                 ('topic-00.json', {'claims': [CLAIM]})]
        for filename, data in cases:
            with self.subTest(filename=filename, data=data):
                self.write_corpus()
                self.write_json(filename, data)
                self.assert_cli_rejects('audit', contains=filename)
                self.assert_cli_rejects('catalog', contains=filename)
        self.write_corpus()
        (self.kroot / 'topic-00.json').write_text('{ broken json', encoding='utf-8')
        self.assert_cli_rejects('audit', contains='topic-00.json')

    def test_invalid_correction_fields_fail_cleanly(self):
        mutations = [None, [], {}, dict(CORRECTION, review_finding=''),
                     dict(CORRECTION, origin='unverified'), dict(CORRECTION, date='2026-02-30'),
                     dict(CORRECTION, summary=3), dict(CORRECTION, sources=[]),
                     dict(CORRECTION, sources=[None]), dict(CORRECTION, unexpected='field'),
                     dict(CORRECTION, sources=[{'label': 'Evidence', 'url': 'http://example.org'}]),
                     dict(CORRECTION, sources=[{'label': '', 'url': 'https://example.org'}]),
                     dict(CORRECTION, sources=[{'label': 'Evidence', 'url': 'https://'}])]
        for correction in mutations:
            with self.subTest(correction=correction):
                self.claim['correction'] = correction
                errors = self.validation_errors()
                self.assertTrue(any('correction' in e for e in errors), errors)

    def test_get_returns_correction_metadata_without_changing_original_citations(self):
        self.claim['correction'] = copy.deepcopy(CORRECTION)
        self.write_corpus()
        run = self.run_cli('get', 'K00-001')
        self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
        got = json.loads(run.stdout)['claims'][0]
        self.assertEqual(got['correction'], CORRECTION)
        self.assertEqual(got['evidence'][0]['source_id'], 'S001')
        self.assertEqual(got['evidence'][0]['link_indices'], [0])
        self.assertEqual(got['evidence'][0]['links'][0]['url'], 'https://example.org/original')

    def test_expanded_claim_cannot_mutate_original_or_correction_sources(self):
        self.claim['correction'] = copy.deepcopy(CORRECTION)
        got = knowledge.expand_claim(self.claim, self.registry['sources'])
        got['correction']['sources'][0]['url'] = 'https://example.org/changed'
        got['evidence'][0]['links'][0]['url'] = 'https://example.org/changed'
        self.assertEqual(self.claim['correction'], CORRECTION)
        self.assertEqual(self.registry['sources']['S001']['links'][0]['url'], 'https://example.org/original')


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def errors(self):
        try:
            return validate.validate_repository(self.root)[0]
        except Exception as exc:
            self.fail('Repository validation crashed instead of reporting malformed input: ' + repr(exc))

    def test_repository_validation_checks_unit_slice_metadata(self):
        path = self.root / 'knowledge' / 'source-units.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['units'][0]['sha256'] = '0' * 64
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('hash' in e.lower() and 'U0001' in e for e in self.errors()))

    def test_repository_returns_errors_for_malformed_corpus_json(self):
        path = self.root / 'knowledge' / 'topic-00.json'
        path.write_text('null', encoding='utf-8')
        self.assertTrue(any('topic-00.json' in e for e in self.errors()))

    def test_incomplete_duplicate_and_unsupported_frontmatter_are_rejected(self):
        path = self.root / 'skills' / 'x-explain' / 'SKILL.md'
        cases = [
            '---\nname: x-explain\ndescription: Valid prose\n# Missing closer\n',
            '---\nname: x-explain\nname: x-explain\ndescription: Valid prose\n---\n',
            '---\nname: x-explain\ndescription: First\ndescription: Second\n---\n',
            '---\nname: x-explain\ndescription: [unclosed\n---\n',
            '---\nname: x-explain\ndescription: |\n  Block scalar\n---\n',
            '---\nname: x-explain\ndescription: true\n---\n',
            '---\nname: x-explain\ndescription: nested: mapping\n---\n',
            '---\nname: x-explain\ndescription: trailing:\n---\n',
            '---\nname: x-explain\ndescription: +.inf\n---\n',
        ]
        for header in cases:
            with self.subTest(header=header):
                path.write_text(header + '\n# Body\n', encoding='utf-8')
                errors = self.errors()
                self.assertTrue(any('frontmatter' in e.lower() and 'x-explain' in e for e in errors), errors)

    def test_plain_and_quoted_scalar_frontmatter_are_supported(self):
        path = self.root / 'skills' / 'x-explain' / 'SKILL.md'
        for description in ('Plain prose.', '"Quoted: prose."', "'It''s quoted prose.'"):
            with self.subTest(description=description):
                path.write_text('---\nname: x-explain\ndescription: ' + description + '\n---\n# Body\n', encoding='utf-8')
                errors = self.errors()
                self.assertFalse(any('frontmatter' in e.lower() for e in errors), errors)


if __name__ == '__main__':
    unittest.main()
