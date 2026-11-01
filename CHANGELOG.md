# Changelog

## 1.1.1

- Correct the 12 knowledge findings from the full review, with explicit per-claim correction evidence and bundled errata. Preserve the original report, IDs, source-unit mappings and original citations.
- Keep different observation scopes separate, retain original snapshots and unresolved text alternatives, and resolve explicit Article/Thread relationships without merging their metrics.
- Preserve Windows newline code points in raw draft counts and return clear errors for malformed input.
- Validate nested evidence schemas, every source-unit range and hash, and complete supported frontmatter before consumption.
- Include license and attribution in every independent skill installation.
- Record regression and independent-review evidence in the [remediation record](docs/reviews/full-repository-review/remediation.md); unexecuted live capabilities remain explicitly unverified.

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
