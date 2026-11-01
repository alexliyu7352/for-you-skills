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
- `media_status`: complete / partial / not_viewed / unavailable / unknown. Record video coverage in `media_notes`. Unseen is not absent.
- `metric_scope`: post / article_page / carrier_post / owner_analytics / unknown. Missing or null scope becomes `unknown`, which stays separate from every known scope. Public views, Home impressions and unique readers are different measurements. A known scope on another observation cannot establish the scope of an unlabeled count.
- `metrics`: preserve UI strings or exact known integers. K/M and localized abbreviations are rounded. Within one scope and verified timestamp, exact `1000` and `"1,000"` represent the same measurement; `"1K"` is not equated with either exact value. Original representations remain in `source_observations`. Do not guess unlabeled metric meanings.
- `time_precision`: record relative display text and timezone uncertainty. Exact age requires reliable timezone-aware publication and observation times.
- `article_url`, `carrier_post_url`, `thread_root_url`: record verified relationships only. A similar title does not prove identity. Keep each object's metrics separate even when linked to one content item.
- Multiple observations of one post form a time series, not multiple independent samples. The helper selects the latest confirmed timestamp separately for each `(permalink identity, metric_scope)`. All original dated input rows in that bucket, including superseded observations and their source fields, remain in `source_observations` as `{row, record}` entries. `selected_observation_rows` identifies the rows used for the current snapshot. It never carries older text, coverage, metrics or relationships into that snapshot. Without historical snapshots, do not reconstruct earlier views or manufacture growth curves from lifetime views divided by age.
- Complementary records with the same confirmed identity, metric scope and timestamp can be combined: a sparse pinned card must not erase a fuller observation. The helper exposes conflicting measurements and every distinct text alternative in `observation_conflicts`. Unresolved text conflicts keep `body_status=partial` through any number of repeated rows; the displayed text is only a deterministic representative, not a reconciliation. A later timestamp starts an independent snapshot and retains the earlier raw evidence. Review the alternatives before interpreting results.
- A missing, invalid or timezone-less observation timestamp cannot establish a latest snapshot. Such rows remain separate, even alongside a dated observation of the same identity and scope, with `selection_status=unverified_timestamp`. They are never merged merely because their timestamps are both unknown. URL-less evidence also remains separate under its provisional row identity.

## Content relationships and counts

`article_url`, `carrier_post_url` and `thread_root_url` in the selected observations form a transitive content graph. An Article, its carrier and replies linked through a Thread root can share one `content_identity`, while every post/scope keeps its own metrics. An Article ID is the representative when exactly one is present; otherwise a terminal Thread identity is preferred, with a stable identity chosen when no unique terminal exists. Similar text never creates a relationship.

`relationship_conflicts` reports invalid links, cycles, contradictory Thread roots and components containing more than one Article ID. Cycles terminate and do not duplicate a content group. Distinct Articles are never silently joined: their own identities remain separate, and the ambiguous status identities in that component receive `content_identity=null` and `content_identity_status=conflicted`. Reconcile these links against the original source rows before treating the group count as a complete total. All same-time relationship alternatives participate; an overwritten display field cannot hide a contradictory target.

| Output | Meaning |
| --- | --- |
| `unique_posts` | Distinct confirmed permalink identities, regardless of scopes, host/handle aliases or retained observation rows. |
| `retained_observations` | Number of output rows in `posts`; scope and unverified-time records can make this exceed `unique_posts`. |
| `duplicate_rows` | Additional valid input observations of the same confirmed identity and scope. This is not a count of discarded rows or independent samples. |
| `format_counts` | Counts of retained observation rows by format, not unique posts or content groups. |
| `unique_content_items` | Resolved observed content groups only. This is not a complete total when `content_count_complete=false`. |
| `unresolved_identity_records` | Retained URL-less observations, not a count of distinct posts. |
| `unresolved_content_identities` | Confirmed post identities whose Article relationships are contradictory, counted once across scopes. |
| `content_count_complete` | False when any input row is invalid, any identity is unconfirmed, or any content relationship is conflicted. Unknown relationships between otherwise separate posts are never inferred. |

The JSON root must be an array or an object with a `posts` array. A malformed file/root produces a concise nonzero CLI error. Invalid row objects, enum values or consumed field/container types appear in `invalid_rows` with the zero-based row and field-specific reason; other valid evidence is retained. Null enum fields use their documented unknown/default value, while unrecognized supplied categories are rejected rather than silently relabeled.

## Review fields

Attach measured `text_characters` and `text_count_scope`, quoted opening, location of the main finding, observed media notes, separate proposed media plan, reader usefulness, format recommendation and cited claim IDs. Count partial text only as partial. Keep the full applicability/check ledger defined in `knowledge-guide.md`.

Run `python3 scripts/summarize_posts.py --input observations.json` to retain count precision and provenance, select comparable snapshots, calculate reliable ages and summarize coverage. Manually check supplied Article/Thread relationships and all diagnostics. The tool cannot infer reach causes or a format advantage.

Without Python, maintain this same record manually or with an available equivalent runtime: preserve raw metrics, unknown identities and coverage. State which calculations were actually performed. Unavailable calculations are unknown, not estimated as exact.
