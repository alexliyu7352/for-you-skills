# Canonical knowledge corpus

## Structure

- `algorithm-updates.json`: dated follow-up findings, affected historical IDs, fixed-revision evidence and the last reviewed upstream checkpoint. These are separate from the 578 original claims.

- `topic-00.json` through `topic-06.json`: English claims, checks and unresolved questions.
- `sources.json`: original reference registry with English descriptive labels and unchanged URLs.
- `source-units.json`: exact report positions and original text hashes; section names are translated metadata.
- `../provenance/research-report.zh-CN.md`: unchanged original report.
- `../provenance/migration-baseline.json`: frozen identity, evidence and URL mappings used to detect migration loss.
- `../shared/research-errata.md`: English corrections to working claims, with primary evidence and a distinction between inherited report errors and later distillation errors.

Each claim has `id`, `title`, `kind`, `conclusion`, `conditions`, `practical_meaning`, `check`, `limits`, `source_units`, `evidence` and `related_unknowns`. `check` contains `when`, `needed`, `verify`, and `if_missing`. Evidence links use `source_id` plus zero-based `link_indices`; `supports` states exactly what the cited material supports.

A corrected claim also has an optional `correction` object with exactly `review_finding`, `origin`, `date`, `summary`, and `sources`. `origin` is `original_report` for an inherited error or `english_distillation` for an error introduced in the English working reference. `sources` is a nonempty list of `{label, url}` objects with HTTPS primary-source URLs. The full-review correction date is `2026-10-31`. Lookup preserves this metadata; read its evidence together with the original citations and the [research errata](../shared/research-errata.md).

Working claims can correct historical text without changing its provenance. The original report, source-unit hashes, registry URLs and order, migration mappings, claim IDs, evidence indices, and related-unknown links remain intact. `original U...` returns the archived wording, including any documented error; it does not supersede the corrected working claim. K00-002 and K00-003 separately identify historical assembly and comparison records that have not been independently reconstructed. Those limits are not findings that the historical statements are false.

`kind` distinguishes code, official statements, observations, editorial judgments, claims being checked and unresolved questions. Do not infer that a whole entry is a production guarantee because one supporting link points to code.

## Query

From the repository root:

```bash
python3 tools/knowledge.py updates
python3 tools/knowledge.py updates A20261108-01
python3 tools/knowledge.py catalog
python3 tools/knowledge.py search "posting frequency"
python3 tools/knowledge.py get K03-001
python3 tools/knowledge.py sources S001
python3 tools/knowledge.py original U0001
python3 tools/knowledge.py audit
```

These commands are offline and require Python 3.9+. Inside an installed skill, replace `tools/` with `scripts/`. Search is lexical retrieval; inspect relevant topic catalogs if it misses. Agents translate non-English questions to English search concepts while preserving exact numbers and identifiers.

## Update policy

1. Capture the new primary source, exact code revision/path/line or official URL, date and scope.
2. Identify every affected claim, condition and unresolved question. Preserve historic interpretations when the difference matters.
3. Update conclusions, checks, practical implications and citations together. Separate source facts from an editorial inference.
   For a correction, add its finding, origin, date, summary, and primary evidence to `correction` and document it in the errata. Put additional source URLs in `correction.sources`; do not change original citation indices or silently amend the archived report.
4. Retain IDs where the claim identity persists. Record intentional coverage changes in versioned migration metadata and release notes; never silently drop an unknown or rewrite the baseline to hide drift.
5. Rebuild, validate and exercise affected user scenarios. Offline structure checks are not source availability or live deployment verification.

The initial corpus retains all original entries for traceability. Consolidation is possible in a future release only with an explicit old-to-new mapping and unchanged report coverage.

## Repeatable upstream review

The latest review and complete commit interval are in [ALGORITHM_CHANGELOG.md](../ALGORITHM_CHANGELOG.md). Run `python tools/check_upstream.py` from the repository root to compare the recorded checkpoint with upstream `main`. The weekly/manual GitHub workflow only reports differences; neither command edits the corpus or advances the checkpoint.

For each synchronization, inspect the complete diff and intermediate commits (a setting can change and revert), trace relevant call sites and feature switches, then update the dated findings, affected-ID mappings, public research supplement and changelog together. Keep original research provenance unchanged. Archive each reviewed state through a version tag, append a new changelog section with exact base/head, and advance the checkpoint only after review and validation. Rebuild all eight skills and publish the tested version. Installed copies update when reinstalled or updated by their host; monitoring does not silently replace them.
