# Validation results

Initial release validation: 2026-10-31. These checks establish packaging, evidence integrity and observed task behavior; they do not measure exposure improvement.

## Automated checks

- `python3 tools/validate.py`: passed. 578 English entries, 49 unresolved questions, 668/668 substantive source units, 100/100 reference groups and 396 unique URLs. No missing IDs, reference-index errors, untranslated knowledge prose or local-reference failures.
- Immutable migration mapping: claim IDs/kinds, source-unit references, related unknowns, original source URLs and link order preserved. Original report SHA-256 verified.
- `python3 tools/build.py --check`: passed for all seven generated skills.
- `python3 -m unittest discover -s tests -v`: **30 tests passed**. Includes exact citation resolution, invalid references, English/Chinese retrieval, independent skill copies, build drift, raw/trimmed Unicode counts, strict video-duration predicate, unknown media, approximate metrics, Article/carrier identity, timestamp validity, URL-less observations and same-snapshot duplicate handling.
- Each skill passed the skill-creator frontmatter validator.
- Each skill was copied alone to a temporary directory and successfully ran offline `audit`, `get` and `search` from an unrelated working directory.

## Installer checks

Test environment: Linux, Node.js 24.22.1, Skills CLI 1.7.4, Python 3.12.

The real Skills CLI installed all seven skills with `--copy` to the six selected project targets: **Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot and OpenCode**. Its JSON results reported every skill installed for all six targets. The installer uses a shared `.agents/skills` location for several targets and a separate Claude directory; these are not six model executions.

The initial discovery command combined `--list` and `--json`, which this CLI rejects. The successful noninteractive installation used `--skill '*' -a claude-code codex gemini-cli cursor github-copilot opencode --copy -y --json`. No unrelated global agent installation was changed.

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

## Limits

- Agent application probes ran in this session's agent harness. The six external CLI/model runtimes were **not** executed.
- No live X account or end-to-end browser/Chrome MCP collection was tested. The published-content case used supplied synthetic records.
- Some current primary-source web lookups succeeded; others returned access errors. The corpus retains its dated scope. There was no claim that all 396 URLs were freshly fetched or that live production configuration was verified.
- No exposure-uplift experiment was run.
- Windows and Python 3.9 are included in the repository CI configuration; their remote execution result is recorded separately if available after publication.
