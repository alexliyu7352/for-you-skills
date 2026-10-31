import importlib.util
import sys
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


if __name__ == '__main__':
    unittest.main()
