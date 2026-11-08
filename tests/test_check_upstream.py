import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'tools/check_upstream.py'


class CheckUpstreamTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.repo = self.directory / 'upstream'
        self.repo.mkdir()
        self.env = dict(os.environ, GIT_AUTHOR_NAME='Test', GIT_AUTHOR_EMAIL='test@example.invalid',
                        GIT_COMMITTER_NAME='Test', GIT_COMMITTER_EMAIL='test@example.invalid')
        self.git('init', '-b', 'main')
        (self.repo / 'algorithm.txt').write_text('reviewed\n', encoding='utf-8')
        self.base = self.commit('Reviewed snapshot')
        self.checkpoint = self.directory / 'checkpoint.json'
        self.write_checkpoint()

    def git(self, *args, input=None):
        return subprocess.run(['git', '-C', str(self.repo), *args], input=input,
                              capture_output=True, text=True, encoding='utf-8',
                              env=self.env, check=True).stdout.strip()

    def commit(self, message):
        self.git('add', '--all')
        self.git('commit', '-m', message)
        return self.git('rev-parse', 'HEAD')

    def write_checkpoint(self, **overrides):
        data = {'schema_version': 1, 'repository': 'xai-org/x-algorithm',
                'snapshot': self.base, 'reviewed_at': '2026-11-08'}
        data.update(overrides)
        self.checkpoint.write_text(json.dumps(data), encoding='utf-8')

    def run_check(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), '--checkpoint', str(self.checkpoint),
                               '--upstream', str(self.repo), *args], capture_output=True,
                              text=True, encoding='utf-8', env=self.env)

    def run_remote_check(self, url=None):
        # Route the actual production HTTPS fetch to a deterministic file transport.
        env = dict(self.env, GIT_CONFIG_COUNT='1',
                   GIT_CONFIG_KEY_0='url.%s.insteadOf' % (url or self.repo.as_uri()),
                   GIT_CONFIG_VALUE_0='https://github.com/xai-org/x-algorithm.git')
        return subprocess.run([sys.executable, str(SCRIPT), '--checkpoint', str(self.checkpoint)],
                              capture_output=True, text=True, encoding='utf-8', env=env)

    def report(self, *args):
        result = self.run_check(*args)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_unchanged_reports_zero_without_writing_checkpoint_or_upstream(self):
        before = self.checkpoint.read_bytes()
        refs = self.git('show-ref')
        report = self.report()
        self.assertEqual(report['status'], 'up_to_date')
        self.assertEqual((report['base'], report['head']), (self.base, self.base))
        self.assertEqual((report['commit_count'], report['changed_file_count']), (0, 0))
        self.assertEqual((report['commits'], report['changed_files']), ([], []))
        self.assertEqual(report['reviewed_at'], '2026-11-08')
        self.assertEqual(self.checkpoint.read_bytes(), before)
        self.assertEqual(self.git('show-ref'), refs)
        self.assertEqual(self.git('status', '--porcelain'), '')

    def test_descendant_requires_review_and_reports_full_changes_in_order(self):
        (self.repo / 'algorithm.txt').write_text('changed\n', encoding='utf-8')
        first = self.commit('Change algorithm')
        (self.repo / 'new-file.txt').write_text('new\n', encoding='utf-8')
        second = self.commit('Add source')
        report = self.report()
        self.assertEqual(report['status'], 'review_required')
        self.assertEqual(report['head'], second)
        self.assertEqual(report['commit_count'], 2)
        self.assertEqual(report['commits'], [
            {'sha': first, 'subject': 'Change algorithm'},
            {'sha': second, 'subject': 'Add source'},
        ])
        self.assertEqual(report['changed_file_count'], 2)
        self.assertEqual(report['changed_files'], ['algorithm.txt', 'new-file.txt'])
        self.assertEqual(report['compare_url'],
                         'https://github.com/xai-org/x-algorithm/compare/' + self.base + '...' + second)

    def test_counts_are_not_limited_by_github_compare_pagination(self):
        for number in range(305):
            (self.repo / ('file-%03d.txt' % number)).write_text('added\n', encoding='utf-8')
        head = self.commit('Add 305 files')
        tree = self.git('rev-parse', 'HEAD^{tree}')
        for number in range(260):
            head = self.git('commit-tree', tree, '-p', head, input='Revision %d\n' % number)
        self.git('update-ref', 'refs/heads/main', head)
        report = self.report()
        self.assertEqual(report['commit_count'], 261)
        self.assertEqual(len(report['commits']), 261)
        self.assertEqual(report['changed_file_count'], 305)
        self.assertEqual(len(report['changed_files']), 305)

    def test_ref_selects_requested_local_branch(self):
        self.git('checkout', '-b', 'candidate')
        (self.repo / 'algorithm.txt').write_text('candidate\n', encoding='utf-8')
        head = self.commit('Candidate change')
        self.assertEqual(self.report()['status'], 'up_to_date')
        self.assertEqual(self.report('--ref', 'candidate')['head'], head)

    def test_diverged_history_fails_instead_of_reporting_clean(self):
        (self.repo / 'algorithm.txt').write_text('reviewed later\n', encoding='utf-8')
        reviewed = self.commit('Reviewed later')
        self.write_checkpoint(snapshot=reviewed)
        self.git('checkout', '-B', 'main', self.base)
        (self.repo / 'algorithm.txt').write_text('different branch\n', encoding='utf-8')
        self.commit('Diverged')
        result = self.run_check()
        self.assertEqual(result.returncode, 2)
        self.assertIn('not an ancestor', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_missing_base_fails_instead_of_reporting_clean(self):
        self.write_checkpoint(snapshot='f' * 40)
        result = self.run_check()
        self.assertEqual(result.returncode, 2)
        self.assertIn('snapshot', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_missing_ref_fails_instead_of_reporting_clean(self):
        result = self.run_check('--ref', 'missing-branch')
        self.assertEqual(result.returncode, 2)
        self.assertIn('ref', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_invalid_checkpoint_is_rejected(self):
        for override in ({'schema_version': 2}, {'schema_version': True},
                         {'repository': '../unsafe'}, {'repository': 'another/repository'},
                         {'snapshot': 'abc'}, {'reviewed_at': '2026-02-30'}):
            with self.subTest(override=override):
                self.write_checkpoint(**override)
                result = self.run_check()
                self.assertEqual(result.returncode, 2)
                self.assertIn('checkpoint', result.stderr)
                self.assertEqual(result.stdout, '')

    def test_malformed_checkpoint_is_rejected(self):
        self.checkpoint.write_text('{', encoding='utf-8')
        result = self.run_check()
        self.assertEqual(result.returncode, 2)
        self.assertIn('checkpoint', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_invalid_repository_path_is_an_error(self):
        self.repo = self.directory / 'not-a-repository'
        result = self.run_check()
        self.assertEqual(result.returncode, 2)
        self.assertIn('upstream', result.stderr)
        self.assertEqual(result.stdout, '')

    @unittest.skipIf(os.name == 'nt', 'Windows does not allow newlines in file names')
    def test_file_names_are_preserved_without_line_splitting(self):
        name = '多语言\nsource.txt'
        (self.repo / name).write_text('new\n', encoding='utf-8')
        self.commit('Add unusual path')
        self.assertEqual(self.report()['changed_files'], [name])

    def test_shallow_local_history_is_rejected_as_incomplete(self):
        (self.repo / 'algorithm.txt').write_text('changed\n', encoding='utf-8')
        self.commit('A later head')
        clone = self.directory / 'shallow'
        subprocess.run(['git', 'clone', '--depth=1', self.repo.as_uri(), str(clone)],
                       capture_output=True, check=True, env=self.env)
        self.repo = clone
        result = self.run_check()
        self.assertEqual(result.returncode, 2)
        self.assertIn('shallow', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_remote_fetch_deepens_until_all_changes_since_snapshot_are_available(self):
        tree = self.git('rev-parse', 'HEAD^{tree}')
        head = self.base
        for number in range(140):
            head = self.git('commit-tree', tree, '-p', head, input='Revision %d\n' % number)
        self.git('update-ref', 'refs/heads/main', head)
        before = self.checkpoint.read_bytes()
        result = self.run_remote_check()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report['commit_count'], 140)
        self.assertEqual(report['head'], head)
        self.assertEqual(report['status'], 'review_required')
        self.assertEqual(self.checkpoint.read_bytes(), before)

    def test_remote_connection_failure_never_reports_clean(self):
        result = self.run_remote_check((self.directory / 'unreachable.git').as_uri())
        self.assertEqual(result.returncode, 2)
        self.assertIn('fetch', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_local_partial_clone_is_rejected_without_lazy_fetch(self):
        self.git('config', 'remote.origin.promisor', 'true')
        self.git('config', 'remote.origin.url', (self.directory / 'unreachable.git').as_uri())
        result = self.run_check()
        self.assertEqual(result.returncode, 2)
        self.assertIn('partial', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_remote_completes_merged_branch_even_when_base_is_already_visible(self):
        tree = self.git('rev-parse', 'HEAD^{tree}')
        side = self.base
        for number in range(150):
            side = self.git('commit-tree', tree, '-p', side, input='Side revision %d\n' % number)
        reviewed = self.git('commit-tree', tree, '-p', self.base, input='Reviewed main\n')
        self.write_checkpoint(snapshot=reviewed)
        head = self.git('commit-tree', tree, '-p', reviewed, '-p', side, input='Merge side\n')
        self.git('update-ref', 'refs/heads/main', head)
        result = self.run_remote_check()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report['commit_count'], 151)
        self.assertEqual(len(report['commits']), 151)
        self.assertEqual(report['head'], head)

    def test_remote_missing_snapshot_is_an_error(self):
        self.write_checkpoint(snapshot='f' * 40)
        result = self.run_remote_check()
        self.assertEqual(result.returncode, 2)
        self.assertIn('snapshot', result.stderr)
        self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    unittest.main()
