# Canonical knowledge corpus

## Structure

- `topic-00.json` through `topic-06.json`: English claims, checks and unresolved questions.
- `sources.json`: original reference registry with English descriptive labels and unchanged URLs.
- `source-units.json`: exact report positions and original text hashes; section names are translated metadata.
- `../provenance/research-report.zh-CN.md`: unchanged original report.
- `../provenance/migration-baseline.json`: frozen identity, evidence and URL mappings used to detect migration loss.

Each claim has `id`, `title`, `kind`, `conclusion`, `conditions`, `practical_meaning`, `check`, `limits`, `source_units`, `evidence` and `related_unknowns`. `check` contains `when`, `needed`, `verify`, and `if_missing`. Evidence links use `source_id` plus zero-based `link_indices`; `supports` states exactly what the cited material supports.

`kind` distinguishes code, official statements, observations, editorial judgments, claims being checked and unresolved questions. Do not infer that a whole entry is a production guarantee because one supporting link points to code.

## Query

From the repository root:

```bash
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
4. Retain IDs where the claim identity persists. Record intentional coverage changes in versioned migration metadata and release notes; never silently drop an unknown or rewrite the baseline to hide drift.
5. Rebuild, validate and exercise affected user scenarios. Offline structure checks are not source availability or live deployment verification.

The initial corpus retains all original entries for traceability. Consolidation is possible in a future release only with an explicit old-to-new mapping and unchanged report coverage.
