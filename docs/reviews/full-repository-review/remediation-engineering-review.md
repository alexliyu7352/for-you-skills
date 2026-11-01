# Independent remediation engineering review

Review date: 2026-11-01 UTC. Base: `13834c3160e6f0e59fd19601001c6db46f213896`. Reviewed runtime HEAD: `5992e2fbeb587f9ab63c9866fdf79715982bb02f`.

The ten original engineering findings have targeted repairs and passing regressions. Independent execution found no remaining high- or medium-severity defect in those repairs. One low-severity coverage-selection issue remains below. This report reviews the remediation plan against canonical code, tests, shared contracts and isolated distributions; it does not reread duplicated generated corpora as independent source evidence.

## Coverage and observed verification

The reviewer read the remediation plan and original ENG-01 through ENG-10, all changed canonical executable files (`knowledge.py`, `validate.py`, `summarize_posts.py`, `inspect_draft.py`, `build.py`), their changed tests, observation/knowledge contracts and attribution changes.

Independently executed on Python 3.12.14, rather than relying on the implementers' results:

- `python3 -m unittest discover -s tests -v`: **80 tests passed**, 6.265 seconds.
- `python3 tools/validate.py`: **zero errors**; 578 claims, 49 unknown IDs, 100 source groups, 668 required/covered units, 396 unique URLs.
- `python3 tools/build.py --check`: **zero generated-file drift**.
- All canonical tools parsed with `ast.parse(..., feature_version=(3, 9))`; no new third-party import/dependency is introduced.
- An independent 410-case nested mutation probe substituted nulls, booleans, numbers, strings, lists and objects into representative claim, evidence, source and unit paths. `knowledge.validate` returned diagnostics without exceptions in every case. The supplied test suite additionally exercised malformed standalone corpus/root inputs and `audit`, `original`, `get`, `search`, and catalog error handling.
- All 24 permutations of four same-time observations jointly mixing three text alternatives and counts `1000`, `"1,000"`, `"1K"`, and `2000` preserved all three text alternatives, three distinct metric alternatives, partial text coverage, unknown conflicted count and all four provenance records.
- The full tests exercised all permutations of separate public/owner/unknown scopes, later sparse snapshots, Article/carrier/Thread transitivity, cyclic Threads, contradictory Thread roots and multiple-Article components. Read-through confirmed scope is part of the bucket key and relationship analysis consumes every selected source record, not only overwritten display fields. No cross-scope metric promotion or silent multiple-Article union was reproduced.
- Independently copied each of the eight skill directories to temporary isolated locations. Every license matched the repository license. Every local Markdown reference outside the intentionally historical report existed and stayed inside its installed directory. Each bundled `knowledge.py audit` and a corrected-claim `get`, invoked from `/tmp`, passed; correction metadata matched its bundled JSON.
- Git comparison showed no change to `provenance/`, `knowledge/sources.json` or `knowledge/source-units.json` between base and reviewed HEAD. Working-guide changes explicitly distinguish corrected working knowledge from historical report text and retain the existing date/snapshot/live-production limitations.

| Original finding | Reviewed repair and acceptance evidence |
| --- | --- |
| ENG-01 | Unique unit IDs, bounds, ordering, source IDs, report/slice hashes checked before CLI reads; negative audit/original tests pass. |
| ENG-02 | Consumed nested corpus types validated before lookup; mutation probe and negative tests produce diagnostics. |
| ENG-03 | Complete frontmatter and an explicitly restricted scalar subset enforced; malformed/missing/duplicate tests pass. |
| ENG-04 | Identity-plus-scope buckets; unknown scope remains unknown; raw historical records retained. |
| ENG-05 | Persistent distinct text alternatives and partial status through repeated same-time conflicts; 24 combined independent permutations pass. |
| ENG-06 | UTF-8 input read with `newline=''`; CRLF/LF/lone-CR CLI boundary regressions pass. |
| ENG-07 | All eight isolated distributions contain license, notice and usable internal links. |
| ENG-08 | Iterative transitive graph groups explicit relationships; cycles and contradictions are reported without merging Article identities. |
| ENG-09 | Parsed exact-value equivalence with raw source representations retained; rounded counts stay distinct. |
| ENG-10 | Invalid standalone roots/rows diagnosed cleanly; URL-less valid evidence remains available. |

## Remaining finding

### REM-ENG-01 — P3 / low: complementary sparse observations downgrade retained coverage

Location: `tools/summarize_posts.py:92`–`94` (generic field overwrite), with deterministic same-time sorting at line 258. Contract: `shared/observations.md`, complementary-record rule that a sparse pinned card must not erase a fuller observation.

Two complementary same-time records can retain the complete text but replace its `body_status=complete` with `preview`, and replace complete media coverage with `partial`. The merge excludes unknown/not-viewed values but otherwise treats coverage fields as arbitrary overwriteable metadata. Sorting makes this deterministic; it does not make coverage selection semantically correct. This is conservative mislabeling rather than fabricated completeness, and original evidence remains available, so severity is low.

Reproduce from the repository root, without modifying files:

```sh
python3 - <<'PY'
import itertools, sys
sys.path.insert(0, 'tools')
from summarize_posts import summarize
b = {'url': 'https://x.com/a/status/1',
     'observed_at': '2026-10-30T12:00:00Z'}
rows = [dict(b, text='Full text', body_status='complete', media_status='complete'),
        dict(b, body_status='preview', media_status='partial'),
        dict(b, pinned=True)]
for order in itertools.permutations(rows):
    p = summarize(list(order))['posts'][0]
    print(p['body_status'], p['media_status'], p['text'],
          p.get('observation_conflicts'))
PY
```

Observed six times: `preview partial Full text None`.

Expected: complementary sparse metadata should preserve established complete coverage for the retained full observation, unless actual conflicting text/evidence requires a downgrade. Add a three-or-more-row permutation regression with explicit preview/partial fields, not only `unknown`; derive the coverage fields intentionally rather than via generic overwrite. Keep the existing unresolved-text-conflict override and later-timestamp independence.

## Limits and review integrity

No runtime files, tests, generated distributions, Git state or real visual preferences were edited by this reviewer. Temporary copies were used for isolation; this report is the only requested review artifact written. The coordinator was concurrently updating release documentation, which is outside this runtime review's frozen scope.

Python 3.9 syntax compatibility is not a Python 3.9 runtime test. No Windows runtime, live X/browser/native-model execution, Skills CLI installation, remote CI run, or third-party license/legal audit was performed in this independent review. The eight-directory isolation check verifies packaged execution and links, not six agent products. Substantive primary-source truth of corrected knowledge belongs to the separate evidence review. No live deployment, exposure uplift or total semantic correctness is inferred from passing offline checks.

Coordinator provenance note: the reviewed local commit was published with an identical Git tree (`36017698399f753f37aa5c6645fdf409c238f45f`) under the commit ID shown above. See [remediation](remediation.md) for subsequent fixes and release verification.
