import importlib.util
import itertools
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HELPER = Path(__file__).resolve().parents[1] / "tools/summarize_posts.py"



class PostRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert HELPER.is_file(), 'post record helper has not been implemented'
        spec = importlib.util.spec_from_file_location('post_records', HELPER)
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def test_counts_retain_precision_and_unknown(self):
        for raw, value, precision in [('3.2K',3200,'rounded'),('1.2万',12000,'rounded'),('1,234',1234,'exact'),('0',0,'exact'),(None,None,'unknown'),('未显示',None,'unknown'),('0:10',None,'unknown')]:
            result = self.module.parse_count(raw)
            self.assertEqual((result['value'],result['precision']),(value,precision))

    def test_canonical_url_deduplicates_queries_and_legacy_host(self):
        self.assertEqual(self.module.canonical_url('https://twitter.com/demo/status/123?s=20'), 'https://x.com/demo/status/123')

    def test_sparse_same_time_cards_preserve_complete_observed_coverage(self):
        base = {'url':'https://x.com/demo/status/1', 'observed_at':'2026-10-30T12:00:00Z'}
        rows = [dict(base, body_status='complete', media_status='complete',
                     text='Full text', media_notes=['First image', 'Second image']),
                dict(base, body_status='preview', media_status='partial',
                     media_notes=['First image']),
                dict(base, pinned=True)]
        for ordered in itertools.permutations(rows):
            with self.subTest(order=ordered):
                post = self.module.summarize(list(ordered))['posts'][0]
                self.assertEqual(post['body_status'], 'complete')
                self.assertEqual(post['media_status'], 'complete')
                self.assertEqual(post['text'], 'Full text')
                self.assertCountEqual(post['media_notes'], ['First image', 'Second image'])
                self.assertNotIn('observation_conflicts', post)
                self.assertEqual(len(post['source_observations']), 3)

    def test_snapshot_dedup_preserves_missing_metrics(self):
        base={'url':'https://x.com/demo/status/123','observed_at':'2026-10-30T12:00:00Z','published_at':'2026-10-23T12:00:00Z','format':'article','body_status':'complete','metrics':{'views':'3.2K'}}
        duplicate=dict(base,url='https://twitter.com/demo/status/123?s=20',observed_at='2026-10-30T12:01:00Z')
        result=self.module.summarize([base,duplicate])
        self.assertEqual(result['unique_posts'],1)
        self.assertEqual(result['duplicate_rows'],1)
        self.assertIsNone(result['posts'][0]['metrics']['bookmarks']['value'])
        self.assertAlmostEqual(result['posts'][0]['age_hours'],168+1/60)

    def test_unknown_or_invalid_dates_are_not_zero_age(self):
        result=self.module.summarize([{'url':'https://x.com/demo/status/2','metrics':{'views':'20'},'published_at':'bad','observed_at':'2026-10-30T12:00:00Z','body_status':'partial'}])
        self.assertIsNone(result['posts'][0]['age_hours'])
        self.assertEqual(result['posts'][0]['body_status'],'partial')

    def test_incomparable_ages_are_visible(self):
        result=self.module.summarize([
            {'url':'https://x.com/demo/status/1','published_at':'2026-10-23T12:00:00Z','observed_at':'2026-10-30T12:00:00Z','format':'article','metrics':{'views':'3K'}},
            {'url':'https://x.com/demo/status/2','published_at':'2026-10-30T06:00:00Z','observed_at':'2026-10-30T12:00:00Z','format':'post','metrics':{'views':'300'}}])
        self.assertEqual([p['age_hours'] for p in result['posts']],[168,6])
        self.assertNotIn('article_lift',result)
        self.assertNotIn('shadowbanned',result)

    def test_article_and_carrier_keep_metrics_but_share_content_identity(self):
        result=self.module.summarize([
            {'url':'https://x.com/demo/status/111','article_url':'https://x.com/i/article/222','format':'article_carrier','metrics':{'views':'3K'},'metric_scope':'carrier_post'},
            {'url':'https://x.com/i/article/222','format':'article','metrics':{'views':'2K'},'metric_scope':'article_page'}])
        self.assertEqual(result['unique_content_items'],1)
        self.assertEqual(len(result['posts']),2)
        self.assertEqual([p['metrics']['views']['value'] for p in result['posts']],[3000,2000])

    def test_invalid_url_is_a_record_error_not_a_crash(self):
        result=self.module.summarize([{'url':'https://[invalid/status/123'}])
        self.assertEqual(result['unique_posts'],0)
        self.assertEqual(len(result['invalid_rows']),1)

    def test_screenshots_without_urls_retain_evidence_without_claiming_identity(self):
        result = self.module.summarize([
            {'url':None, 'source_method':'user_screenshot', 'text':'Visible opening',
             'body_status':'partial', 'metrics':{'views':'3K'}},
            {'source_method':'user_screenshot', 'text':'Another crop', 'metrics':{'views':None}}])
        self.assertEqual(len(result['posts']), 2)
        self.assertEqual(result['posts'][0]['text'], 'Visible opening')
        self.assertEqual(result['posts'][0]['metrics']['views']['precision'], 'rounded')
        self.assertEqual(result['posts'][0]['body_status'], 'partial')
        self.assertEqual(result['unique_posts'], 0)
        self.assertEqual(result['unique_content_items'], 0)
        self.assertEqual(result.get('unresolved_identity_records'), 2)
        self.assertIsNone(result['posts'][0]['url'])
        self.assertIsNone(result['posts'][0]['content_identity'])
        self.assertNotEqual(result['posts'][0]['provisional_id'], result['posts'][1]['provisional_id'])

    def test_unidentified_screenshot_does_not_merge_with_verified_post(self):
        result = self.module.summarize([
            {'url':'https://x.com/demo/status/123', 'text':'same'},
            {'url':'', 'text':'same', 'observation_id':'screenshot-1'}])
        self.assertEqual(len(result['posts']), 2)
        self.assertEqual(result['unique_posts'], 1)
        self.assertEqual(result['unique_content_items'], 1)
        self.assertEqual(result.get('unresolved_identity_records'), 1)

    def test_same_snapshot_sparse_pin_retains_richer_observation(self):
        common = {'url':'https://x.com/demo/status/123', 'observed_at':'2026-10-30T12:00:00Z'}
        rich = dict(common, text='Read in full', body_status='complete', metrics={'views':'3.2K','likes':'21'})
        sparse = dict(common, pinned=True, body_status='unknown', metrics={'views':'3.2K','likes':None})
        result = self.module.summarize([rich, sparse])
        self.assertEqual(result['posts'][0]['metrics']['likes']['value'], 21)
        self.assertEqual(result['posts'][0]['body_status'], 'complete')
        self.assertEqual(result['posts'][0]['text'], 'Read in full')
        self.assertTrue(result['posts'][0]['pinned'])
        self.assertEqual(result['unique_posts'], 1)

    def test_same_snapshot_conflicting_metrics_remain_explicit(self):
        common = {'url':'https://x.com/demo/status/123', 'observed_at':'2026-10-30T12:00:00Z'}
        result = self.module.summarize([dict(common, metrics={'views':'3K'}), dict(common, metrics={'views':'4K'})])
        self.assertIsNone(result['posts'][0]['metrics']['views']['value'])
        self.assertEqual(result['posts'][0].get('observation_conflicts', {}).get('metrics.views'), ['3K','4K'])

    def test_later_sparse_snapshot_does_not_inherit_old_complete_text(self):
        first = {'url':'https://x.com/demo/status/123','observed_at':'2026-10-30T12:00:00Z','text':'Old version','body_status':'complete','metrics':{'likes':'21'}}
        later = dict(first, observed_at='2026-10-31T12:00:00Z', text='New excerpt', body_status='partial', metrics={})
        result = self.module.summarize([first, later])
        self.assertEqual(result['posts'][0]['text'], 'New excerpt')
        self.assertEqual(result['posts'][0]['body_status'], 'partial')
        self.assertIsNone(result['posts'][0]['metrics']['likes']['value'])

    def test_scopes_keep_separate_latest_measurements_and_source_records(self):
        common = {'url':'https://x.com/demo/status/123', 'observed_at':'2026-10-30T12:00:00Z'}
        rows = [
            dict(common, metric_scope='post', metrics={'views':'100'}, source_method='public_page'),
            dict(common, metric_scope='owner_analytics', metrics={'replies':'2'}, source_method='owner_export'),
            dict(common, metrics={'likes':'7'}, source_method='screenshot'),
            dict(common, metric_scope='post', observed_at='2026-10-31T12:00:00Z', metrics={'views':'120'}, source_method='public_page'),
        ]
        for ordered in itertools.permutations(rows):
            with self.subTest(order=[row['source_method'] for row in ordered]):
                result = self.module.summarize(list(ordered))
                self.assertEqual(len(result['posts']), 3)
                self.assertEqual(result['unique_posts'], 1)
                self.assertEqual(result.get('retained_observations'), 3)
                self.assertEqual(result['duplicate_rows'], 1)
                posts = {post['metric_scope']:post for post in result['posts']}
                self.assertEqual(posts['post']['metrics']['views']['value'], 120)
                self.assertIsNone(posts['owner_analytics']['metrics']['views']['value'])
                self.assertEqual(posts['owner_analytics']['metrics']['replies']['value'], 2)
                self.assertEqual(posts['unknown']['metrics']['likes']['value'], 7)
                self.assertIsNone(posts['post']['metrics']['likes']['value'])
                raw = [source['record'] for post in result['posts'] for source in post.get('source_observations', [])]
                self.assertCountEqual(raw, rows)

    def test_three_text_alternatives_survive_repeated_snapshot_merges(self):
        common = {'url':'https://x.com/demo/status/123', 'observed_at':'2026-10-30T12:00:00Z', 'body_status':'complete'}
        for texts in set(itertools.permutations(['Version A', 'Version B', 'Version C', 'Version B'])):
            with self.subTest(texts=texts):
                post = self.module.summarize([dict(common, text=text) for text in texts])['posts'][0]
                self.assertEqual(post['body_status'], 'partial')
                self.assertEqual(post.get('observation_conflicts', {}).get('text'), ['Version A', 'Version B', 'Version C'])
                self.assertEqual(len(post.get('source_observations', [])), 4)

    def test_equivalent_exact_counts_keep_raw_forms_without_false_conflict(self):
        common = {'url':'https://x.com/demo/status/123', 'observed_at':'2026-10-30T12:00:00Z', 'metric_scope':'post'}
        rows = [dict(common, metrics={'views':1000}, source_method='export'),
                dict(common, metrics={'views':'1,000'}, source_method='screenshot')]
        for ordered in itertools.permutations(rows):
            post = self.module.summarize(list(ordered))['posts'][0]
            self.assertEqual(post['metrics']['views']['value'], 1000)
            self.assertEqual(post['metrics']['views']['precision'], 'exact')
            self.assertNotIn('metrics.views', post.get('observation_conflicts', {}))
            self.assertCountEqual([source['record'] for source in post.get('source_observations', [])], rows)

    def test_repeated_conflicting_counts_retain_distinct_measurements(self):
        common = {'url':'https://x.com/demo/status/123', 'observed_at':'2026-10-30T12:00:00Z'}
        for values in itertools.permutations([1000, '1,000', '1K', 2000]):
            post = self.module.summarize([dict(common, metrics={'views':value}) for value in values])['posts'][0]
            self.assertIsNone(post['metrics']['views']['value'])
            conflicts = post.get('observation_conflicts', {}).get('metrics.views', [])
            self.assertEqual(len(conflicts), 3)
            self.assertIn('1K', conflicts)
            self.assertIn(2000, conflicts)
            self.assertEqual(len(post.get('source_observations', [])), 4)

    def test_transitive_article_carrier_thread_group_is_order_independent(self):
        rows = [
            {'url':'https://x.com/demo/status/111', 'article_url':'https://x.com/i/article/222', 'metrics':{'views':'10'}},
            {'url':'https://x.com/i/article/222', 'metrics':{'views':'20'}},
            {'url':'https://x.com/demo/status/333', 'thread_root_url':'https://x.com/demo/status/111', 'metrics':{'views':'30'}},
            {'url':'https://x.com/demo/status/444', 'thread_root_url':'https://x.com/demo/status/333', 'metrics':{'views':'40'}},
        ]
        for ordered in itertools.permutations(rows):
            result = self.module.summarize(list(ordered))
            self.assertEqual(result['unique_content_items'], 1)
            self.assertEqual(result['unique_posts'], 4)
            self.assertEqual({post['content_identity'] for post in result['posts']}, {'article:222'})
            self.assertCountEqual([post['metrics']['views']['value'] for post in result['posts']], [10,20,30,40])
            self.assertFalse(result.get('relationship_conflicts'))

    def test_thread_cycle_is_flagged_without_double_counting(self):
        rows = [
            {'url':'https://x.com/demo/status/1', 'thread_root_url':'https://x.com/demo/status/2'},
            {'url':'https://x.com/demo/status/2', 'thread_root_url':'https://x.com/demo/status/1'},
            {'url':'https://x.com/demo/status/3', 'thread_root_url':'https://x.com/demo/status/2'},
        ]
        for ordered in itertools.permutations(rows):
            result = self.module.summarize(list(ordered))
            self.assertEqual(result['unique_content_items'], 1)
            self.assertEqual({post['content_identity'] for post in result['posts']}, {'status:1'})
            self.assertIn('cycle', [conflict['type'] for conflict in result.get('relationship_conflicts', [])])

    def test_contradictory_carriers_never_merge_distinct_articles(self):
        rows = [
            {'url':'https://x.com/demo/status/1', 'article_url':'https://x.com/i/article/10'},
            {'url':'https://x.com/i/article/10', 'carrier_post_url':'https://x.com/demo/status/1'},
            {'url':'https://x.com/i/article/20', 'carrier_post_url':'https://x.com/demo/status/1'},
            {'url':'https://x.com/demo/status/3', 'thread_root_url':'https://x.com/demo/status/1'},
        ]
        for ordered in itertools.permutations(rows):
            result = self.module.summarize(list(ordered))
            posts = {post['url']:post for post in result['posts']}
            self.assertEqual(posts['https://x.com/i/article/10']['content_identity'], 'article:10')
            self.assertEqual(posts['https://x.com/i/article/20']['content_identity'], 'article:20')
            self.assertIsNone(posts['https://x.com/demo/status/1']['content_identity'])
            self.assertIsNone(posts['https://x.com/demo/status/3']['content_identity'])
            self.assertEqual(result['unique_content_items'], 2)
            self.assertEqual(result.get('unresolved_content_identities'), 2)
            self.assertIs(result.get('content_count_complete'), False)
            self.assertIn('multiple_articles', [conflict['type'] for conflict in result.get('relationship_conflicts', [])])

    def test_conflicting_same_time_relationships_retain_both_targets(self):
        common = {'url':'https://x.com/demo/status/1', 'observed_at':'2026-10-30T12:00:00Z'}
        rows = [dict(common, article_url='https://x.com/i/article/10'),
                dict(common, article_url='https://x.com/i/article/20'),
                {'url':'https://x.com/i/article/10'}, {'url':'https://x.com/i/article/20'}]
        for ordered in itertools.permutations(rows):
            result = self.module.summarize(list(ordered))
            carrier = next(post for post in result['posts'] if post['url'] == common['url'])
            self.assertIsNone(carrier['content_identity'])
            self.assertEqual(result['unique_content_items'], 2)
            self.assertEqual(len(carrier.get('source_observations', [])), 2)

    def test_contradictory_thread_roots_are_explicit(self):
        common = {'url':'https://x.com/demo/status/1', 'observed_at':'2026-10-30T12:00:00Z'}
        rows = [dict(common, thread_root_url='https://x.com/demo/status/2'),
                dict(common, thread_root_url='https://x.com/demo/status/3'),
                {'url':'https://x.com/demo/status/2'}, {'url':'https://x.com/demo/status/3'}]
        for ordered in itertools.permutations(rows):
            result = self.module.summarize(list(ordered))
            self.assertEqual(result['unique_content_items'], 1)
            self.assertIn('contradictory_thread_roots', [conflict['type'] for conflict in result.get('relationship_conflicts', [])])

    def test_unverified_timestamps_retain_independent_measurements(self):
        common = {'url':'https://x.com/demo/status/1', 'metric_scope':'post'}
        rows = [dict(common, metrics={'views':'10'}), dict(common, metrics={'views':'20'}),
                dict(common, observed_at='2026-10-30T12:00:00Z', metrics={'views':'30'})]
        for ordered in itertools.permutations(rows):
            result = self.module.summarize(list(ordered))
            self.assertEqual(result['unique_posts'], 1)
            self.assertEqual(len(result['posts']), 3)
            self.assertCountEqual([post['metrics']['views']['value'] for post in result['posts']], [10,20,30])

    def test_cli_rejects_malformed_roots_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'posts.json'
            for data in [None, 7, True, 'posts', {}, {'posts':None}, {'posts':{}}, {'posts':'bad'}]:
                with self.subTest(data=data):
                    path.write_text(json.dumps(data), encoding='utf-8')
                    run = subprocess.run([sys.executable, str(HELPER), '--input', str(path)], capture_output=True, text=True)
                    self.assertNotEqual(run.returncode, 0)
                    self.assertNotIn('Traceback', run.stderr)
                    self.assertIn('posts', run.stderr)

    def test_cli_rejects_invalid_json_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'posts.json'
            path.write_text('{"posts":', encoding='utf-8')
            run = subprocess.run([sys.executable, str(HELPER), '--input', str(path)], capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertNotIn('Traceback', run.stderr)
            self.assertIn('JSON', run.stderr)

    def test_cli_row_errors_are_actionable_and_valid_urlless_evidence_survives(self):
        mutations = [
            ('format', []), ('format', 'mystery'), ('metric_scope', {}), ('metric_scope', 'impressions'),
            ('metrics', []), ('body_status', []), ('media_status', {}), ('text', []),
            ('media_notes', {}), ('supporting_post_urls', 'bad'), ('metrics', {'views':[]}),
        ]
        rows = [dict({'url':'https://x.com/demo/status/1'}, **{field:value}) for field, value in mutations]
        rows.extend([None, {'url':None, 'text':'Visible text', 'metrics':{'views':'3K'}, 'source_method':'user_screenshot'}])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'posts.json'
            path.write_text(json.dumps({'posts':rows}), encoding='utf-8')
            run = subprocess.run([sys.executable, str(HELPER), '--input', str(path)], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertNotIn('Traceback', run.stderr)
            result = json.loads(run.stdout)
            self.assertEqual([error['row'] for error in result['invalid_rows']], list(range(12)))
            for error, (field, _) in zip(result['invalid_rows'], mutations):
                self.assertIn(field, error['reason'])
            self.assertEqual(len(result['posts']), 1)
            self.assertEqual(result['posts'][0]['text'], 'Visible text')
            self.assertEqual(result['posts'][0]['metrics']['views']['value'], 3000)
            self.assertEqual(result['unique_posts'], 0)


if __name__ == '__main__':
    unittest.main()
