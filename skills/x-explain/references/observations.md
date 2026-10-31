# Observation contract

## Record

Use a JSON array of posts or an object containing `posts`. Missing data is `null` or `unknown`, never zero. This example illustrates the schema; it is not a real observation:

```json
{"posts":[{"url":"https://x.com/example/status/123","author":"example","format":"article_carrier","article_url":null,"carrier_post_url":null,"thread_root_url":null,"published_at":null,"observed_at":"2026-10-31T12:00:00Z","time_precision":"unknown","body_status":"partial","text":"Only the text actually observed","media_status":"not_viewed","media_notes":[],"metric_scope":"carrier_post","metrics":{"views":"3.2K","likes":null,"replies":null,"reposts":null,"quotes":null,"bookmarks":null},"pinned":null,"supporting_post_urls":[],"source_method":"user_screenshot","evidence_notes":"Article body not supplied"}]}
```

## Definitions

- `url` may be null when a screenshot/export does not establish a permalink. Retain its actual text, metrics and coverage. The helper gives URL-less rows provisional IDs and `identity_status=unconfirmed`, without deduplicating them or counting them as confirmed unique posts/content. An optional `observation_id` can identify the supplied screenshot/crop; it does not prove post identity. Do not invent a URL or discard the observation.
- `format`: post / long_post / thread_root / thread_reply / quote / repost / article / article_carrier / unknown. Length alone does not establish an Article.
- `body_status`: complete / partial / preview / blocked / unknown. Track Article body and carrier independently.
- `media_status`: complete / partial / not_viewed / unavailable. Record video coverage in `media_notes`. Unseen is not absent.
- `metric_scope`: post / article_page / carrier_post / owner_analytics / unknown. Public views, Home impressions and unique readers are different measurements.
- `metrics`: preserve UI strings or exact known integers. K/M and localized abbreviations are rounded. Do not guess unlabeled metric meanings.
- `time_precision`: record relative display text and timezone uncertainty. Exact age requires reliable timezone-aware publication and observation times.
- `article_url`, `carrier_post_url`, `thread_root_url`: record verified relationships only. A similar title does not prove identity. Keep each object's metrics separate even when linked to one content item.
- Multiple observations of one post form a time series, not multiple independent samples. Preserve raw snapshots. Without historical snapshots, do not reconstruct earlier views or manufacture growth curves from lifetime views divided by age.
- Complementary records with the same confirmed timestamp can be combined: a sparse pinned card must not erase a fuller observation. The helper preserves known fields at that exact timestamp and exposes conflicting values in `observation_conflicts`; review those conflicts before interpreting results. It never carries older complete text or unknown metrics forward into a later snapshot.

## Review fields

Attach measured `text_characters` and `text_count_scope`, quoted opening, location of the main finding, observed media notes, separate proposed media plan, reader usefulness, format recommendation and cited claim IDs. Count partial text only as partial. Keep the full applicability/check ledger defined in `knowledge-guide.md`.

Run `python3 scripts/summarize_posts.py --input observations.json` to retain count precision, deduplicate identities, calculate reliable ages and summarize coverage. `unique_posts` counts distinct record URLs; `unique_content_items` uses supplied verified Article/Thread relationships. Manually check those relationships. The tool cannot infer reach causes or a format advantage.

Without Python, maintain this same record manually or with an available equivalent runtime: preserve raw metrics, unknown identities and coverage. State which calculations were actually performed. Unavailable calculations are unknown, not estimated as exact.
