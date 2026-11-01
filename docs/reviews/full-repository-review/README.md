# Full independent repository review

**Remediation update:** the findings below describe the frozen reviewed version. See the [1.1.1 remediation record](remediation.md) for the 22 fixes, independent acceptance and remaining verification limits.

[简体中文](README.zh-CN.md)

**Result: 22 open findings — 14 P2 (medium) and 8 P3 (low). Changes are needed before this release can be described as passing a strict whole-repository review.** No critical or high-priority security defect was established; this is not a security certification. The findings do not invalidate every answer the skills produce, but several can change an answer or corrupt a diagnostic summary.

Reviewed commit: [`9193233`](https://github.com/alexliyu7352/for-you-skills/tree/9193233924df388727296c4e76948db919ac32eb). Review completed 2026-11-01 UTC. This is a frozen-version review; its findings are not automatically findings against later commits.

Six fresh-context agents reviewed separate scopes without relying on the authors' earlier verdicts: four covered the knowledge corpus, one the workflows, and one the engineering. The coordinating reviewer reconciled all coverage IDs, read the findings and primary-source excerpts, and reproduced selected helper failures. These are independent agent reviews within one harness, not an external human audit. **This publication adds review records only; all 22 findings remain open.**

## What was actually checked

| Scope | Executed coverage | Boundary |
| --- | --- | --- |
| Knowledge | All 578 entries, every field, compared with mapped Chinese passages; cited source evidence inspected | 578 reviewed does not mean 578 source-verified |
| Original mappings | All 669 source units structurally checked; 668 substantive units covered | Two historical provenance claims remain partly unreconstructed |
| Repository | All 60 canonical files accounted for; all 158 generated files verified byte for byte | Generated duplicate corpora were not counted as independent semantic rereads |
| Sources | All 392 URLs selected by claim evidence appear in reviewer ledgers; 165 source files freshly retrieved for 374 registry URLs; 357 anchored ranges in bounds | Access attempts are distinct from successful verification; the live Under the Hood endpoint returned 403 |
| Workflows | All eight skills; 12 actual reviewer-executed tasks with saved inputs and outputs | No measured automatic invocation across six external model clients |
| Engineering | 43 existing tests pass; 10 additional findings have executed reproductions | Passing the existing suite did not detect these defects |
| Installation | Local frozen-source installation to six CLI targets; 316 copied files verified in two shared physical distributions | Installer compatibility, not six native model executions |
| Preferences | Temporary-store read/write, import/export, conflict, permissions and concurrent-save checks | No claim of cross-host durability, image-provider auth or actual generated-image quality |

Every claim has a separate translation and evidence status:

| Dimension | Verified within scope | Finding | Not applicable | Unverified |
| --- | ---: | ---: | ---: | ---: |
| English fidelity | 572 | 6 | 0 | 0 |
| Evidence | 460 | 13 | 101 | 4 |

Evidence `not_applicable` covers editorial/methodological entries without an external factual proposition to verify. For open-question entries, `verified` means that the known mechanism and stated evidence gap are supported; it does not resolve their unknown production behavior. The 49 preserved research questions remain intentionally open where their missing evidence is still unavailable.

The **12 knowledge findings affect 13 claims**. Six findings are introduced by English distillation; six are inherited from the Chinese report. Corrections to inherited errors need explicit errata while retaining the original report and migration record. The **10 engineering findings** include both defects under valid inputs and insufficient rejection of malformed future changes. The current corpus itself passed the independent structural/hash check.

## Findings

All entries below are **open**. Detailed reports provide frozen file locations, source evidence or executable reproductions, practical impact and proposed corrections. P2 means a correctness/distribution fix is needed; P3 means a narrower condition, identifier or input-handling correction.

| ID | Priority | Affected scope | Problem | Evidence and reproduction |
| --- | --- | --- | --- | --- |
| KA-001 | P2 | K01-017 | Commit timestamps are described as first-publication timestamps. | [knowledge-a](knowledge-a.md) |
| KB-F01 | P2 | K04-049 | Original-post retrieval is made a universal prerequisite not established by the cited path. | [knowledge-b](knowledge-b.md) |
| KB-F02 | P3 | K04-046, K04-047 | The age-filter description omits rejection when age cannot be decoded. | [knowledge-b](knowledge-b.md) |
| KB-F03 | P3 | K04-077 | A zero-score cache-publication statement is generalized beyond its score gate. | [knowledge-b](knowledge-b.md) |
| KB-F04 | P3 | K02-089 | The bio input cap is called unavailable even though the cited renderer defines MAX_BIO=500. | [knowledge-b](knowledge-b.md) |
| C-01 | P2 | K03-018 | Content-feature transmission omits the debias switch and uncached-request conditions. | [knowledge-c](knowledge-c.md) |
| C-02 | P2 | K03-101 | MediaInjected is incorrectly said to require prior NSFW results to exist. | [knowledge-c](knowledge-c.md) |
| C-03 | P3 | K03-077 | VQV eligibility omits the querying viewer follower-count guard. | [knowledge-c](knowledge-c.md) |
| KD-01 | P2 | K05-061 | No publicly established hashtag formula becomes an assertion that no formula exists. | [knowledge-d](knowledge-d.md) |
| KD-02 | P3 | K05-047 | Exact duplicate-text job names omit their bbq_ prefix. | [knowledge-d](knowledge-d.md) |
| KD-03 | P3 | K05-034 | A verification step compares the configured threshold instead of the matching-record count. | [knowledge-d](knowledge-d.md) |
| KD-04 | P2 | K05-069 | Under the Hood post-label statistics omit authored-post cohorts and observation horizons. | [knowledge-d](knowledge-d.md) |
| ENG-01 | P2 | Engineering | Unchecked source-unit metadata | [engineering](engineering.md) |
| ENG-02 | P2 | Engineering | Schema accepts values that crash lookup | [engineering](engineering.md) |
| ENG-03 | P2 | Engineering | Incomplete frontmatter passes gate | [engineering](engineering.md) |
| ENG-04 | P2 | Engineering | Metric scopes silently mixed | [engineering](engineering.md) |
| ENG-05 | P2 | Engineering | Unresolved text conflict regains complete status | [engineering](engineering.md) |
| ENG-06 | P2 | Engineering | CRLF normalization changes raw code-point count | [engineering](engineering.md) |
| ENG-07 | P2 | Engineering | Standalone copies omit license and notice | [engineering](engineering.md) |
| ENG-08 | P2 | Engineering | One-hop content identity grouping | [engineering](engineering.md) |
| ENG-09 | P3 | Engineering | Equivalent exact counts conflict | [engineering](engineering.md) |
| ENG-10 | P3 | Engineering | Malformed JSON root raises traceback | [engineering](engineering.md) |

## What worked, and what remains unverified

The workflow reviewer found no confirmed routing/workflow defect after executing the 12 recorded cases. The checklist case inspected the opening, measured a 4,789-code-point input, identified its delayed result, produced revised copy, selected a format and proposed ordered, evidence-specific images. Other cases covered Article reach, posting frequency, myth checks, missing tools, ambiguous routing and a temporary visual-style override. These outputs are retained in [workflows.md](workflows.md) and its [execution record](coverage/workflows.json); they are not a guarantee of every model's future behavior.

Four claim records retain explicit evidence limitations:

- **K00-002:** the shared-conversation/version-7 assembly lineage was not independently reconstructible; snapshot metadata and the retained 23-page report were checked.
- **K00-003:** the exact historical set of 14 expanded visibility rule/field groups was not located. A separate 14-file renderer comparison is not evidence for that count.
- **K04-091 and K05-066:** the pinned Under the Hood implementation was inspected, but its live endpoint returned 403. Current/account-specific availability was not established.

No authenticated X browsing session, real screenshot-pixel inspection, actual image-generation run, six-client model execution or causal exposure experiment was completed. Third-party studies were checked as records of their own claims; their unpublished row-level data were not independently reanalyzed. Public code still does not reveal all production settings, models or rollout paths.

## Repair and acceptance order

1. Correct the 12 knowledge findings, record the six inherited-report errata, and review each correction against its exact source conditions. Preserve the frozen original report.
2. Fix observation merging, conflict retention, transitive content grouping, equivalent exact counts and raw newline handling. Add regressions using the reproduced inputs before changing behavior.
3. Strengthen mapping/schema/frontmatter validation and malformed-input errors. Confirm negative fixtures fail cleanly; retain the current positive checks.
4. Include license and attribution in every standalone skill, rebuild and repeat isolated installation checks.
5. Independently review the fixes. Run actual browsing/image/native-client tests before adding claims about those capabilities; do not relabel the current unexecuted paths as passed.

## Review records

- [Topics 00, 01 and 06: 157 entries](knowledge-a.md) · [per-entry ledger](coverage/knowledge-a.json)
- [Topics 02 and 04: 199 entries](knowledge-b.md) · [per-entry ledger](coverage/knowledge-b.json)
- [Topic 03: 113 entries](knowledge-c.md) · [per-entry ledger](coverage/knowledge-c.json)
- [Topic 05: 109 entries](knowledge-d.md) · [per-entry ledger](coverage/knowledge-d.json)
- [Eight workflows and 12 executions](workflows.md) · [inputs, outputs and file coverage](coverage/workflows.json)
- [Engineering, packaging and 10 reproductions](engineering.md) · [218-file inventory and checks](coverage/engineering.json)
- [Review manifest and reconciled counts](manifest.json) · [machine-readable findings](findings.json) · [fresh source retrieval hashes](source-manifest.json)

Individual reports may reference temporary execution paths. Their checked-in ledgers retain the relevant hashes, URLs and fixture inputs; those paths are not installation requirements. The source manifest records October 31 in America/Los_Angeles; this completion record and November 1 reviewer timestamps use UTC.
