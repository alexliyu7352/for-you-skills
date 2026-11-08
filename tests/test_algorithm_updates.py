"""Versioned upstream findings must accompany, never replace, the source report."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('algorithm_knowledge', ROOT / 'tools/knowledge.py')
knowledge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(knowledge)
BASE = '606b254b45be798bfaecfa8c23f5a9c51bc8000c'
SNAPSHOT = '3b6919f87532e57063bb3f1e85c2f509323b513e'
PREFIX = 'https://github.com/xai-org/x-algorithm/'
UPDATE = {
    'schema_version': 1,
    'repository': 'xai-org/x-algorithm',
    'reviewed_at': '2026-11-08',
    'base_snapshot': BASE,
    'snapshot': SNAPSHOT,
    'commits': ['1' * 40, '2' * 40, '3' * 40, '4' * 40, '5' * 40, '6' * 40, SNAPSHOT],
    'entries': [{
        'id': 'A20261108-01',
        'title': 'Updated dwell comparison',
        'status': 'changed',
        'topics': ['01', '06'],
        'affects': ['K01-001', 'Q03'],
        'summary': 'The current source introduces cta_click_prediction.',
        'details': ['Compare the published implementation with its earlier snapshot.'],
        'practical_meaning': 'Describe observed source changes separately from historical weights.',
        'limits': ['Public source does not establish live deployment.'],
        'evidence': [{'label': 'Current implementation',
                      'url': PREFIX + 'blob/' + SNAPSHOT + '/home-mixer/Scorer.scala#L10-L20'}],
    }],
}


class AlgorithmUpdateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'installed-skill'
        self.kroot = self.root / 'references/knowledge'
        shutil.copytree(ROOT / 'knowledge', self.kroot)
        shutil.copyfile(ROOT / 'provenance/research-report.zh-CN.md',
                        self.root / 'references/research-report.md')
        (self.root / 'scripts').mkdir()
        shutil.copyfile(ROOT / 'tools/knowledge.py', self.root / 'scripts/knowledge.py')
        self.document = copy.deepcopy(UPDATE)
        self.write_updates()

    def write_updates(self):
        (self.kroot / 'algorithm-updates.json').write_text(
            json.dumps(self.document, ensure_ascii=False), encoding='utf-8')

    def load_updates(self, **kwargs):
        self.assertTrue(callable(getattr(knowledge, 'load_updates', None)),
                        'A public validated update loader is required')
        return knowledge.load_updates(self.kroot, **kwargs)

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(self.root / 'scripts/knowledge.py'), *args],
                              cwd=self.temp.name, capture_output=True, text=True, encoding='utf-8')

    def cli_json(self, *args):
        run = self.run_cli(*args)
        self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
        return json.loads(run.stdout)

    def test_get_keeps_dated_weights_and_original_citations_with_current_update(self):
        before = {p.name: p.read_bytes() for p in self.kroot.glob('*.json')}
        got = self.cli_json('get', 'Q03', 'K01-001')
        self.assertIn('current_updates', got)
        self.assertEqual([u['id'] for u in got['current_updates']], ['A20261108-01'])
        self.assertIn('0.004 on 10/9 and 0.006 on 10/13', got['claims'][0]['conclusion'])
        original = next(c for c in knowledge.load(self.kroot)[3] if c['id'] == 'Q03')
        self.assertEqual(got['claims'][0]['evidence'][0]['source_id'], original['evidence'][0]['source_id'])
        registry = json.loads((self.kroot / 'sources.json').read_text(encoding='utf-8'))
        evidence = original['evidence'][0]
        self.assertEqual(got['claims'][0]['evidence'][0]['links'],
                         [registry['sources'][evidence['source_id']]['links'][i]
                          for i in evidence['link_indices']])
        self.assertEqual(got['research_through'], '2026-10-29')
        self.assertEqual(got['current_coverage']['reviewed_at'], '2026-11-08')
        self.assertEqual(got['current_coverage']['snapshot'], SNAPSHOT)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.kroot.glob('*.json')})

    def test_search_discovers_new_field_without_historical_match(self):
        got = self.cli_json('search', 'cta_click_prediction')
        self.assertEqual(got['results'], [])
        self.assertIn('current_updates', got)
        self.assertEqual([u['id'] for u in got['current_updates']], ['A20261108-01'])
        self.assertEqual(got['current_updates'][0]['evidence'][0]['url'],
                         PREFIX + 'blob/' + SNAPSHOT + '/home-mixer/Scorer.scala#L10-L20')

    def test_search_includes_update_for_affected_claim_even_without_word_overlap(self):
        got = self.cli_json('search', 'Q03', '--limit', '1')
        self.assertEqual(got['results'][0]['id'], 'Q03')
        self.assertIn('current_updates', got)
        self.assertEqual(got['current_updates'][0]['id'], 'A20261108-01')

    def test_exact_new_field_precedes_generic_synonym_matches(self):
        self.document['entries'][0]['summary'] = 'The new field is NewPredictionWeight.'
        generic = copy.deepcopy(self.document['entries'][0])
        generic.update(id='A20261108-02', title='Weight coefficient prediction ranking',
                       summary='Generic coefficient discussion.', affects=[])
        self.document['entries'].append(generic)
        self.write_updates()
        got = self.cli_json('search', 'NewPredictionWeight', '--limit', '1')
        self.assertEqual([u['id'] for u in got['current_updates']], ['A20261108-01'])

    def test_updates_catalog_and_explicit_entry_work_in_isolated_install(self):
        catalog = self.cli_json('updates')
        self.assertEqual(catalog['entries'][0]['id'], 'A20261108-01')
        self.assertEqual(catalog['current_coverage']['update_count'], 1)
        self.assertNotIn('details', catalog['entries'][0])
        selected = self.cli_json('updates', 'A20261108-01')
        self.assertEqual(selected['entries'], UPDATE['entries'])
        run = self.run_cli('updates', 'A20261108-99')
        self.assertNotEqual(run.returncode, 0)
        self.assertIn('Unknown update IDs', run.stderr)
        self.assertNotIn('Traceback', run.stderr)

    def test_catalog_and_audit_distinguish_report_and_update_coverage(self):
        for command in ('catalog', 'audit'):
            with self.subTest(command=command):
                got = self.cli_json(command)
                self.assertEqual(got.get('research_through'), '2026-10-29')
                self.assertIn('current_coverage', got)
                self.assertEqual(got['current_coverage']['update_count'], 1)
                self.assertEqual(got['current_coverage']['affected_claim_count'], 2)
                self.assertEqual(got['current_coverage']['changed_count'], 1)
                self.assertEqual(got['current_coverage']['snapshot'], SNAPSHOT)
                if command == 'audit':
                    self.assertEqual(got['claims'], 578)
                    self.assertEqual(got['errors'], [])

    def test_load_updates_validates_default_and_explicit_claim_id_sets(self):
        self.assertEqual(self.load_updates(), UPDATE)
        self.assertEqual(self.load_updates(claim_ids={'K01-001', 'Q03'}), UPDATE)
        with self.assertRaisesRegex(knowledge.KnowledgeError, 'unknown affected claim.*Q03'):
            self.load_updates(claim_ids={'K01-001'})

    def test_historical_corpus_without_supplement_still_loads(self):
        (self.kroot / 'algorithm-updates.json').unlink()
        self.assertEqual(len(knowledge.load(self.kroot)[3]), 578)
        self.assertEqual(self.cli_json('get', 'Q03')['claims'][0]['id'], 'Q03')
        got = self.cli_json('updates')
        self.assertEqual(got['entries'], [])
        self.assertIsNone(got['current_coverage'])
        with self.assertRaisesRegex(knowledge.KnowledgeError, 'algorithm-updates.json'):
            self.load_updates()

    def test_malformed_roots_and_commit_endpoints_are_rejected(self):
        cases = [None, [], {}, dict(UPDATE, schema_version=True),
                 dict(UPDATE, repository='other/repository'), dict(UPDATE, repository=[]),
                 dict(UPDATE, reviewed_at='2026-02-30'),
                 dict(UPDATE, unexpected='value'), dict(UPDATE, base_snapshot='main'),
                 dict(UPDATE, snapshot=BASE), dict(UPDATE, commits=[]),
                 dict(UPDATE, commits=[BASE, SNAPSHOT]),
                 dict(UPDATE, commits=['1' * 40, SNAPSHOT, '2' * 40]),
                 dict(UPDATE, commits=['1' * 40, '1' * 40, SNAPSHOT]),
                 dict(UPDATE, commits=[{}, SNAPSHOT]), dict(UPDATE, entries=None)]
        for document in cases:
            with self.subTest(document=document):
                self.document = document
                self.write_updates()
                with self.assertRaises(knowledge.KnowledgeError):
                    self.load_updates()

    def test_malformed_entry_fields_duplicates_and_references_are_rejected(self):
        entry = UPDATE['entries'][0]
        cases = [None, {}, dict(entry, id='K01-001'), dict(entry, title=''),
                 dict(entry, status='verified'), dict(entry, topics=['99']),
                 dict(entry, topics=['01', '01']), dict(entry, affects=['K99-999']),
                 dict(entry, affects=['Q03', 'Q03']), dict(entry, affects=[{}]),
                 dict(entry, details=[]), dict(entry, limits=None),
                 dict(entry, practical_meaning=0), dict(entry, evidence=[]),
                 dict(entry, evidence=[None]), dict(entry, evidence=[{'label': 'Missing URL'}]),
                 dict(entry, extra=True)]
        for replacement in cases:
            with self.subTest(entry=replacement):
                self.document = dict(UPDATE, entries=[replacement])
                self.write_updates()
                with self.assertRaises(knowledge.KnowledgeError):
                    self.load_updates()
        self.document = dict(UPDATE, entries=[entry, entry])
        self.write_updates()
        with self.assertRaisesRegex(knowledge.KnowledgeError, 'duplicate update ID'):
            self.load_updates()

    def test_duplicate_json_fields_cannot_silently_replace_reviewed_metadata(self):
        raw = json.dumps(UPDATE)
        raw = raw.replace('"schema_version": 1', '"schema_version": 0, "schema_version": 1')
        (self.kroot / 'algorithm-updates.json').write_text(raw, encoding='utf-8')
        with self.assertRaisesRegex(knowledge.KnowledgeError, 'duplicate JSON field'):
            self.load_updates()

    def test_only_pinned_repository_evidence_is_accepted(self):
        valid = [PREFIX + 'blob/' + BASE + '/home-mixer/Scorer.scala',
                 PREFIX + 'commit/' + SNAPSHOT,
                 PREFIX + 'compare/' + BASE + '...' + SNAPSHOT]
        invalid = [PREFIX + 'blob/main/home-mixer/Scorer.scala',
                   PREFIX + 'blob/' + 'a' * 40 + '/Scorer.scala',
                   PREFIX + 'commit/' + 'b' * 40,
                   PREFIX + 'compare/main...' + SNAPSHOT,
                   PREFIX + 'compare/' + SNAPSHOT + '...' + BASE,
                   PREFIX + 'blob/' + SNAPSHOT + '/',
                   PREFIX + 'blob/' + SNAPSHOT + '/Scorer.scala?ref=main',
                   'https://github.com/other/repository/blob/' + SNAPSHOT + '/Scorer.scala',
                   'https://github.com.evil.example/xai-org/x-algorithm/commit/' + SNAPSHOT]
        for url in valid + invalid:
            with self.subTest(url=url):
                self.document['entries'][0]['evidence'] = [{'label': 'Evidence', 'url': url}]
                self.write_updates()
                if url in valid:
                    self.assertEqual(self.load_updates()['entries'][0]['evidence'][0]['url'], url)
                else:
                    with self.assertRaisesRegex(knowledge.KnowledgeError, 'pinned'):
                        self.load_updates()

    def test_every_cli_command_rejects_invalid_supplement_without_traceback(self):
        self.document['entries'][0]['affects'] = ['K99-999']
        self.write_updates()
        for args in (('catalog',), ('get', 'Q03'), ('search', 'dwell'), ('updates',),
                     ('sources', 'S001'), ('original', 'U0001'), ('audit',)):
            with self.subTest(command=args[0]):
                run = self.run_cli(*args)
                self.assertNotEqual(run.returncode, 0)
                self.assertNotIn('Traceback', run.stderr)
                self.assertIn('unknown affected claim', run.stdout + run.stderr)
                if args[0] == 'audit':
                    self.assertTrue(json.loads(run.stdout)['errors'])

    def test_repository_validation_requires_current_review_file(self):
        repository = Path(self.temp.name) / 'repository'
        shutil.copytree(ROOT, repository, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        update_path = repository / 'knowledge/algorithm-updates.json'
        if update_path.exists():
            update_path.unlink()
        run = subprocess.run([sys.executable, str(repository / 'tools/validate.py')],
                             cwd=self.temp.name, capture_output=True, text=True, encoding='utf-8')
        self.assertNotEqual(run.returncode, 0)
        self.assertNotIn('Traceback', run.stderr)
        errors = json.loads(run.stdout)['errors']
        self.assertTrue(any('algorithm-updates.json' in error and 'cannot read' in error
                            for error in errors), errors)


class ActualCorpusUpdateTests(unittest.TestCase):
    def test_coefficient_review_accompanies_every_affected_historical_claim(self):
        affected_ids = ('K01-025', 'K01-026', 'K01-027', 'K01-028', 'K01-029',
                        'K01-030', 'K01-031', 'K01-058', 'K01-086', 'K01-090',
                        'Q04', 'Q05')
        for claim_id in affected_ids:
            with self.subTest(claim_id=claim_id):
                run = subprocess.run([sys.executable, str(ROOT / 'tools/knowledge.py'),
                                      'get', claim_id], cwd=ROOT, capture_output=True,
                                     text=True, encoding='utf-8')
                self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
                got = json.loads(run.stdout)
                self.assertEqual([c['id'] for c in got['claims']], [claim_id])
                self.assertIn('A20261108-01', [u['id'] for u in got['current_updates']])


if __name__ == '__main__':
    unittest.main()
