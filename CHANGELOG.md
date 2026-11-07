# Changelog

## Unreleased

- Remove internal planning, review and progress documents from the repository and release-tag histories. Keep public validation instructions and demonstration evidence.
- Pin the Python 3.9 CI job to Ubuntu 24.04, where the requested interpreter is available.

- Host the Chinese and English demos on YouTube. Remove the two MP4 files and animated preview from Git history; retain captions, static covers and execution evidence.

- Repair the fresh-reader handoff: include the full reading procedure, rubric and output rules, plus the actual draft scope and user constraints; keep previous verdicts and drafting notes out of the reviewer context.
- Preserve plan-only and partial-draft review. Distinguish no-copy, missing-text and quick-check outcomes from a completed reader pass, and distinguish cold review from self-review.
- Replace the unconditional revision loop with a default budget of three reviewer passes and explicit unresolved outcomes for unavailable facts, protected wording, repeated stalls or exhausted budget. Verify that a PASS and the final measurements refer to the delivered version.

## 1.2.0

- Add a reader-review stage to `x-publish-checklist` (and to the router's bundled fallback): after the evidence review, the draft is read cold as a first-time reader. A pure read produces a stall log against three cause-defined classes — unresolved reference, unexplained term, broken chain — and, where the host supports it, a fresh-context reviewer returns PASS or FAIL quoting the offending sentences, looping until the draft passes. Hosts without a fresh reviewer use a labeled self-review instead.
- Add the no-compression standard the stage enforces: every central mechanism states its consequence for the reader, every specialized term is explained at first use (or earlier, or replaced by an everyday example), and no causal step the conclusion needs is left off the page.
- The stage is editorial judgment, kept separate from the algorithm evidence: it cites no knowledge entries, adds no knowledge entries, and its outcome (verdict, rounds, stall classes found) is reported with the review. It may be skipped for a quick check only when the delivery states that it was skipped.

## 1.1.1

- Correct the 12 knowledge findings from the full review, with explicit per-claim correction evidence and bundled errata. Preserve the original report, IDs, source-unit mappings and original citations.
- Keep different observation scopes separate, retain original snapshots and unresolved text alternatives, and resolve explicit Article/Thread relationships without merging their metrics.
- Preserve Windows newline code points in raw draft counts and return clear errors for malformed input.
- Validate nested evidence schemas, every source-unit range and hash, and complete supported frontmatter before consumption.
- Include license and attribution in every independent skill installation.
- Add regression coverage for the corrected behavior; unexecuted live capabilities remain explicitly unverified.

## 1.1.0

- Add `x-create-visuals` and route image requests from the natural-language entry and draft review.
- Discover available image tools, carry the actual review brief, and distinguish generated illustration from real evidence and exact charts.
- Add private default/account/series style profiles, read-only one-off overrides, and validated import/export, independent of skill updates.
- Bundle the complete creation fallback and preference helper in the router and checklist as well as the standalone visual skill.
- Preserve the 578-entry research corpus and original citations unchanged.

## 1.0.0

- Add `x-assistant`, a natural-language router with six self-contained fallback workflows.
- Separate general explanations, myth checks, format advice, prepublication review, published-content review and reach diagnosis.
- Migrate the complete report-derived corpus to English while preserving original evidence, coverage and 49 unresolved questions.
- Add reproducible independent skill bundles, offline evidence helpers and distribution checks.
- Replace the earlier `x-review-draft` role with `x-publish-checklist`; retain and narrow `x-review-posts` to published-content inspection.

Research snapshot: 2026-10-29. Validation scope and runtime limitations are recorded in `docs/validation/results.md`.
