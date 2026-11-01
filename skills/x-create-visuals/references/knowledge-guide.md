# Evidence lookup and complete review

## Scope and provenance

This corpus distills the complete research report, including its 49 unresolved questions. Its research cutoff is **2026-10-29**, baseline code revision `5ed796374ea48ee26058aab66ab10c266bea2bef`, comparison revision `606b254b45be798bfaecfa8c23f5a9c51bc8000c`. A public default, a function existing, production deployment and measured exposure are different claims.

The English entries are the working reference. `research-report.md` retains the original Chinese source for provenance; an English-speaking user does not need to read it. Source IDs resolve to original URLs, not citations to this skill itself.

Read [research errata](research-errata.md) when an entry has `correction` metadata or when comparing working knowledge with the archived report. Use the corrected entry's conditions and its `correction.sources` alongside the original citations. `origin=original_report` identifies an error inherited from the report; `origin=english_distillation` identifies a later wording error. The archived report and `original U...` command preserve the historical text and may therefore contain the documented error. Do not silently treat an archived sentence as overruling a verified correction, or present an unresolved historical check as independently reproduced.

## Topic map

| Topic | Evidence and questions | Typical relevance |
| --- | --- | --- |
| 00 | Report scope, validation methods, evidence limits, writing references | What was actually verified; freshness |
| 01 | Posting frequency, October changes, candidate pipeline, author diversity, DPP, Threads, all interaction weights, repost/reply audiences | Daily quotas, second-post discounts, interaction rankings |
| 02 | Current reader history, ld retrieval, CREAD thresholds/decoding/loss, four dwell concepts, 1fav/32fav production and consumption, bookmarks, follow relationships, profiles, negatives | Completion, dwell, bookmarks, mutual follows, relevance |
| 03 | Long Post and Article identity/fields, V5/V8.2, 4000/200-character paths, covers/inline media, action events, permissions, comparisons, first images, video indexes and safety gates | Format choice, Article longevity, media order, duration |
| 04 | Full cold-start eligibility, Beta selection, rank targets, NewUser/FairShare, corrections, age/reposts/edits, reply scoring/spam, quote dependencies, links/pinned labels | Low reach, older posts, corrections, links, repeated promotion |
| 05 | Labels/audiences, account aggregation windows/TTLs, copypasta, engagement bait, hashtags, Under the Hood, statistics, full publishing example | Visibility, account evidence, fair comparisons, actionable review |
| 06 | Q01–Q49: known facts, missing evidence, present interpretation | Limits on all preceding mechanisms |

## Retrieve evidence

Use commands from the active skill directory, or substitute its resolved absolute path:

```bash
python3 scripts/knowledge.py catalog
python3 scripts/knowledge.py catalog --topic 03
python3 scripts/knowledge.py search "Article versus long Post"
python3 scripts/knowledge.py get K03-001
```

Select actual IDs from the catalog. `get` resolves original links, preserves any correction evidence and lists related unknowns: read those Q entries before answering. `sources ID` resolves a reference group; `original U...` reads source units; `audit` checks offline structure and coverage.

Search is lexical candidate retrieval, not semantic completeness or an X score. Translate a non-English question into English search concepts and retain exact symbols, numbers and IDs. If retrieval misses, inspect the topic catalog. When Python is unavailable, read the corresponding JSON files directly and resolve `source_id` plus zero-based `link_indices` through `sources.json`; never invent a URL.

Read all relevant entries, not only the first search result. Request full entries in small batches (usually one to three IDs), check whether the host truncated output, and split or reread missing portions before relying on it. Read topic catalogs separately; never parse truncated output as complete JSON. Treat code facts, official documentation, observations, myths, editorial judgments and unresolved questions separately. Check current primary sources for present deployment, product eligibility or newer claims. Label additions as newly researched, retain the historical snapshot, and disclose if current verification is unavailable.

## Apply rather than recite

### Measurement without Python

The Python scripts are optional deterministic helpers. When Python is available, use them. Otherwise use an available equivalent counter that counts Unicode code points (for example `Array.from(text).length` in JavaScript), preserves the actual supplied text and states the counting scope. If no reliable counter is available, label length unmeasured and complete the other checks; do not invent an exact count. The helper reports both raw and trimmed lengths/previews. State which you use, especially near a 4000-character boundary. Neither reproduces an unknown production renderer input or X's product-specific weighted-length rules.

For observations without Python, follow the observation contract directly; do not drop records or pretend a script ran. Missing runtime support must not become a request to install tools before any useful review can proceed.

For a full review, screen **every topic** for applicability. For each applicable topic read its rule catalog and evaluate each relevant entry. Record:

`claim_id | actual text/image/data evidence | pass/change/missing/not_applicable | action or reason to retain | explanation | original citations`

An internal model state unavailable from a draft is `missing`, not an inferred pass/fail. State why a topic is not applicable. Group checks with the same actionable explanation in the answer while preserving traceability; a fixed three- or six-item template must not drop applicable rules.

Give the user the conclusion and concrete action first, then conditions, reasons and sources. Retain numerical units, strict/non-strict boundaries, processing stage, audience and code revision. Separate a predicted probability's coefficient from an observed event count, an indexing condition, candidate count or final display. An opening that attracts attention is an editorial judgment; its wording is not a required code feature.

A proposed numeric publishing schedule must be tied to supplied capacity/materials or explicit experiment assumptions and a reason for the chosen interval; avoid unexplained stock ranges. Unknowns still require a useful answer: explain what is known, what cannot follow, what evidence would discriminate explanations, and what the user can do now. Do not fabricate optimal posting intervals, follower-size classes, upload bonuses, guaranteed reach, a universal format winner or a proprietary recommendation score.

## Updating the corpus

Each entry retains report source-unit IDs, claim-specific evidence and unknown links. Update affected conditions and citations together, preserve older snapshots, then run coverage and translation checks. An offline audit proves reference integrity, not live link availability, semantic truth or production uplift.
