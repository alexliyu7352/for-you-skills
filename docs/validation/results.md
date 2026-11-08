# Validation

## Reproduce the checks

Run these commands from the repository root with Python 3.9 or later:

```bash
python tools/validate.py
python tools/build.py --check
python -m unittest discover -s tests -v
```

The current suite contains **113 tests**. Integrity validation checks **578 knowledge entries**, including **49 unresolved questions**, **668 source units**, **100 source groups** and **396 original URLs**. A separate follow-up review adds **14 dated entries**, seven reviewed upstream commits and 73 affected historical IDs. The build check compares the eight generated skill bundles with their canonical sources. The tests cover evidence schemas and lookup, standalone bundles, text measurements, observation handling, UTF-8 portability and visual-preference storage. Additional tests cover current-versus-historical retrieval, pinned update citations, missing review files, independent installed lookup, and complete or failed upstream comparisons.

## Continuous integration

The [validation workflow](../../.github/workflows/validate.yml) runs all three commands on:

| Runner | Python |
| --- | --- |
| Ubuntu 24.04 | 3.9 |
| Ubuntu latest | 3.12 |
| Windows latest | 3.12 |

The Python 3.9 job is pinned to Ubuntu 24.04 so it can install the requested interpreter. See [GitHub Actions](https://github.com/alexliyu7352/for-you-skills/actions/workflows/validate.yml) for each commit's results; a passing historical run does not establish that a later commit passes.

The separate [upstream comparison workflow](../../.github/workflows/check-upstream.yml) runs weekly on Mondays at 08:17 UTC and supports manual execution and relevant main-branch changes. It preserves the full JSON result as a 30-day workflow artifact and reports new commits without changing the checkpoint or skills. It is a change detector, not a test of production X behavior.

## Installation and public examples

Installation has been checked for Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot and OpenCode. This verifies installer layout and distributed files, not six separate native-client model executions. See [compatibility](../compatibility.md) for installation requirements.

The public [installation and Q&A record](../demo/live/README.md) preserves an actual ChatGPT Work run, its installation log, source checks and answer. A separate [draft-review example](../demo/run-record.zh-CN.md) includes the original question, full answer and review result. Each record states its own execution scope and limitations.

## Limits

These checks do not verify live X.com account collection, current production recommendation settings, image-provider output quality or improved reach. The original report cutoff remains **2026-10-29**; the follow-up source review is dated **2026-11-08**, through upstream `3b6919f`. Current platform claims need fresh primary-source verification, and unavailable account evidence remains explicitly unknown.
