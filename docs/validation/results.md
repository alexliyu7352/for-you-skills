# Validation results

## 1.1.0 visual workflow — 2026-11-01

- **43 automated tests passed** locally, including 10 new preference tests and isolated visual-helper execution in the router, checklist and new specialist. The original 578 entries, 49 unresolved questions, 668 source units and 396 URLs remain unchanged. The build contains eight skills and 158 generated files.
- The preference tests exercise fresh-process UTF-8 readback, scoped profiles, byte-preserving temporary overrides, OS default paths, absolute configuration overrides, import/export, conflicts, invalid schema/fields, corrupt existing files, forbidden repository/skill destinations and stale revisions.
- The old-package baseline exposed no durable preferences or creation handoff. A fresh-context first-use case with **mock generation capability** then selected the creation workflow, read a nonexistent private fixture without writing, offered available production methods and asked for missing style choices. A standalone-checklist follow-up reused the existing brief instead of collecting it again.
- A second fresh-context agent executed real helper operations in temporary private storage: read an existing series, apply a temporary green palette, save a separate green series, export the document and import into another store. Temporary overrides left bytes identical; default and original series profiles remained unchanged. Missing image-generation capability was mocked and the response labeled its deliverable as production instructions.
- An independent reviewer ran all 43 tests, the build check and corpus validation. Additional probes confirmed shared state across the three helper copies and preservation after malformed/conflicting imports. No blocking findings.
- These are **workflow and persistence checks, not completed image generation**. No image-provider authentication, output-quality experiment, live X operation, exposure test or durable cross-device synchronization was performed. Temporary fixtures establish save/readback and transfer, not persistence across destroyed hosts. The host can impose image-generation rules that override preference questioning; the first-use mock case does not establish identical behavior in every host.

The real Skills CLI installed all eight skills from both the local repository and GitHub into temporary project directories for Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot and OpenCode. All 158 distributed files matched byte for byte. This is installation evidence, not six external model runs.

The first 1.1.0 CI run passed Linux/Python 3.12 but exposed a Windows test assertion comparing `RUNNER~1` against the canonical `runneradmin` directory. The helper correctly resolved both to the same private location. The test now canonicalizes its expected path too; no runtime change was needed. That failure cancelled the parallel Python 3.9 job. The corrected run is linked from [GitHub Actions](https://github.com/alexliyu7352/for-you-skills/actions); previous-release evidence remains below.

## 1.0.0 validation record

Initial release validation: 2026-10-31; publication and cross-platform follow-up: 2026-11-01. These checks establish packaging, evidence integrity and observed task behavior; they do not measure exposure improvement.

## Automated checks

- `python3 tools/validate.py`: passed. 578 English entries, 49 unresolved questions, 668/668 substantive source units, 100/100 reference groups and 396 unique URLs. No missing IDs, reference-index errors, untranslated knowledge prose or local-reference failures.
- Immutable migration mapping: claim IDs/kinds, source-unit references, related unknowns, original source URLs and link order preserved. Original report SHA-256 verified.
- `python3 tools/build.py --check`: passed for all seven generated skills.
- `python3 -m unittest discover -s tests -v`: **32 tests passed**. Includes exact citation resolution, invalid references, English/Chinese retrieval, independent skill copies, build drift, raw/trimmed Unicode counts, strict video-duration predicate, unknown media, approximate metrics, Article/carrier identity, timestamp validity, URL-less observations, same-snapshot duplicate handling, non-UTF-8 default file encoding and UTF-8 JSON output under a legacy console encoding.
- Each skill passed the skill-creator frontmatter validator.
- Each skill was copied alone to a temporary directory and successfully ran offline `audit`, `get` and `search` from an unrelated working directory.

## Installer checks

Test environment: Linux, Node.js 24.22.1, Skills CLI 1.7.4, Python 3.12.

The real Skills CLI installed all seven skills from both the local repository and the published `alexliyu7352/for-you-skills` GitHub source with `--copy` to the six selected project targets: **Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot and OpenCode**. Its JSON results reported every skill installed for all six targets. The installer uses a shared `.agents/skills` location for several targets and a separate Claude directory; these are not six model executions.

The initial discovery command combined `--list` and `--json`, which this CLI rejects. The successful noninteractive installation used `--skill '*' -a claude-code codex gemini-cli cursor github-copilot opencode --copy -y --json`. No unrelated global agent installation was changed.

Every skill installed from GitHub also passed its offline evidence audit from an unrelated working directory. After the encoding fix, GitHub installation was repeated for all six targets; all 133 distributed files matched the canonical source byte for byte.

## Personal installation

All seven skills were saved and verified in the requesting user's skill environment, including the final UTF-8 helpers. The previous `x-review-draft` entry was updated to `x-publish-checklist`; `x-review-posts` was updated in place. Persisted workflow, reference and script content matched the distribution; host-managed optional UI metadata was checked semantically.

## Agent task probes

Fresh-context agents executed **10 user cases** against the packaged skills:

1. A second-daily-post reach claim and practical posting advice.
2. Invoice-test material needing format selection and a publishing review.
3. An Article continuing to gain views after a week versus lower-view Posts.
4. A Chinese screenshot-based account-review request without supplied screenshots.
5. A follow-up keeping Article format and reviewing only the introduction.
6. The supplied Chinese security draft: actual 2,856-character normalized count, opening rewrite, two-image plan, scoped format recommendation and applicable checks. News facts were explicitly outside this test's verification scope.
7. A standalone published-content review of four synthetic post records plus a pinned duplicate: distinct content/metric scopes, partial coverage, concrete revisions and unknown video metadata.
8. English conceptual bookmark question.
9. Traditional Chinese conceptual bookmark question.
10. Spanish completion-versus-dwell question.

All six specialist workflows were exercised. Answers used actual corpus lookup and original source links, preserved question-specific missing data and did not claim account access. The introduction-only follow-up measured the actual 111-character excerpt without reopening format selection. Conceptual questions did not require an account or draft.

The previous two-skill baseline showed overlapping general-Q&A entry descriptions, no distinct router/QA package and predominantly Chinese instructions. It did **not** demonstrate that their existing screenshot or follow-up procedures were absent; those capabilities were preserved.

## Findings and fixes

- Router fallback paths initially had an ambiguous base. Paths now explicitly resolve from the installed router root. A regression failed before correction and passed afterward.
- URL-less screenshot records were dropped by the observation helper. They now retain text, metrics and coverage under provisional row identities, excluded from confirmed-unique-post counts. Failing-then-passing tests cover both screenshot-only and mixed input.
- A sparse pinned duplicate at the same exact timestamp erased richer evidence. Complementary same-snapshot data is now preserved, conflicting values are explicit, and a later snapshot does not inherit older complete text or unknown metrics. Regression tests cover these distinctions.
- The length helper now reports raw and trimmed counts/previews and its Unicode/whitespace semantics. A boundary test verifies the distinction.
- No-Python counting and observation procedures are explicit; unavailable calculations stay unmeasured.
- Large evidence output can exceed a host's display budget. The guide requires small batches and checking for truncation; agents recovered by rereading missing entries. Lexical search remains candidate retrieval, so a highly ranked irrelevant match never substitutes for reading the topic catalog.

An independent reviewer ran the automated suite and checked architecture, workflow boundaries and nine numeric/scope-sensitive translations against the original entries. The reviewer did not independently reread all 578 translations. The identified data-loss defect and portability/measurement points were addressed as above.

## Cross-platform publication checks

The first GitHub Actions run passed both Linux jobs (Python 3.9 and 3.12) and failed the Windows Python 3.12 validation step. A local regression reproduced implicit file decoding failure under CP1252; another reproduced Chinese JSON output failure under a legacy console encoding for all three helpers. Repository text reads now request UTF-8, helpers emit UTF-8 JSON, and `.gitattributes` preserves LF bytes for provenance hashes and generated files. Both regressions pass. A fresh clone with `core.autocrlf=true` passed the full integrity and generated-file checks.

The corrected [GitHub Actions run](https://github.com/alexliyu7352/for-you-skills/actions/runs/41255040736) at commit `d3a217603e47f8a8153cceac90f8312e543cbac0` passed all three jobs: Ubuntu with Python 3.9, Ubuntu with Python 3.12 and Windows with Python 3.12. Each job ran integrity validation, generated-file comparison and the 32-test suite.

## Limits

- Agent application probes ran in this session's agent harness. The six external CLI/model runtimes were **not** executed.
- No live X account or end-to-end browser/Chrome MCP collection was tested. The published-content case used supplied synthetic records.
- Some current primary-source web lookups succeeded; others returned access errors. The corpus retains its dated scope. There was no claim that all 396 URLs were freshly fetched or that live production configuration was verified.
- No exposure-uplift experiment was run.
