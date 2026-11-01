# Full repository engineering review

Reviewed commit: 9193233924df388727296c4e76948db919ac32eb.
Review date: 2026-11-01. Reviewer: independent engineering agent.
Scope: complete canonical tooling, tests, build/CI, documentation, routing/workflow contracts, metadata, licensing, and structural evidence integrity. This is not a latest-diff review.

The existing suite passes, but ten independently reproduced findings remain: eight medium-priority correctness/distribution issues and two low-priority input-handling issues. No critical or high-priority security issue was established. The current corpus passes independent structural checks; the evidence-validator findings below describe undetected future corruption, not existing corrupt claim data.

No repository source, generated skill, Git index, branch, or user preference was modified. Mutation probes used isolated temporary copies. The only written review artifacts are this report and coverage/engineering.json.

## Verification and coverage

- Python 3.12.14: all 43 existing tests passed in 2.616 seconds.
- tools/validate.py: 578 claims, 49 Q entries, 668 required and covered units, 100 source groups, 396 unique URLs, errors=[].
- tools/build.py --check: generated_file_drift=[].
- A complete rebuild in a temporary copy produced eight skills and 158 files, with remaining_drift=[]; the subsequent check also passed.
- Independent structural checks examined all 578 claims, all 657 evidence records, all 669 source units, all source registry entries and the migration baseline. Every current source-unit text hash matches its exact report slice; all ranges are in bounds, all unit source IDs resolve, and all tested field types are correct. All 578 exact-ID searches return the requested ID first. The 49 preserved Q entries are not the same as the count of all entries whose kind is unknown.
- Candidate lookup probes covered English/Chinese frequency, first images, 4000, bookmarks and video 10000, as well as an unrelated query. Results behave as candidate retrieval, consistent with the documented requirement to read the relevant catalog and claims. No search score is treated as a truth or exposure score.
- All six canonical Python files parse under Python 3.9 grammar; imports are standard-library modules or the repository's own build/knowledge modules. The 3.9 grammar check is not a local Python 3.9 execution.
- A fresh, isolated, offline-cached Skills CLI 1.7.4 installation with Node 24.22.1 installed the local frozen repository for Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot and OpenCode. Six target selections produced 16 physical skill directories because locations are shared; 316 copied files (two complete physical copies of the 158-file distribution) matched byte for byte. This was installer execution, not execution of six external agent/model runtimes.
- The GitHub connector independently read jobs for the documented Actions run 41261980741. Ubuntu/Python 3.9, Ubuntu/Python 3.12 and Windows/Python 3.12 all report success for integrity validation, build comparison and the unittest step. These are the recorded run's results, not a new Windows or Python 3.9 run by this reviewer.
- The complete 60-file canonical inventory and its SHA-256 values are in coverage/engineering.json. Forty-nine files received direct code/prose review. Eleven corpus/provenance JSON/report files received structural and hash review; substantive rereading of every claim and every source is assigned to the separate evidence reviewers. All 158 generated files were verified against the builder, rather than rereading duplicated corpora.

The baseline commands were:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
PYTHONDONTWRITEBYTECODE=1 python3 tools/validate.py
PYTHONDONTWRITEBYTECODE=1 python3 tools/build.py --check
~~~

## Findings

### ENG-01 — P2 / medium: source-unit positions and hashes are never validated

Location: tools/knowledge.py:99 and tools/validate.py:16. The original-unit reader consumes these unchecked positions at tools/knowledge.py:200.

The validator checks that claim unit IDs exist and that required IDs are referenced. It does not check unit ID uniqueness, bounds/order of line ranges, each unit's SHA-256, or unit source_ids against the registry. Changing a unit's line range, hash and source IDs and rebuilding the generated copies still passes the full repository validator. The original command then returns empty or unrelated report text as the claimed original evidence.

Reproduction, from the repository root; all edits are temporary:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import json, shutil, subprocess, sys, tempfile
from pathlib import Path
sys.path.insert(0, 'tools')
import build, validate
with tempfile.TemporaryDirectory() as d:
    r = Path(d) / 'repo'
    shutil.copytree(Path.cwd(), r,
                    ignore=shutil.ignore_patterns('.git', '__pycache__', 'reviews'))
    p = r / 'knowledge/source-units.json'
    data = json.loads(p.read_text(encoding='utf-8'))
    data['units'][0].update(line_start=999999, line_end=999999,
                           sha256='0'*64, source_ids=['S_DOES_NOT_EXIST'])
    p.write_text(json.dumps(data), encoding='utf-8')
    for rel, content in build.expected_files(r).items():
        (r / rel).write_bytes(content)
    print(validate.validate_repository(r)[0])
    result = subprocess.run([sys.executable, str(r/'tools/knowledge.py'),
                             'original', 'U0001'], capture_output=True, text=True)
    print(result.returncode, repr(json.loads(result.stdout)[0]['text']))
PY
~~~

Actual output:

~~~text
[]
0 ''
~~~

The temporary full CLI validation also exited 0 with errors=[] and the original 668/668 coverage count. A duplicate unit ID is likewise accepted by the lower-level validator.

Effect: future accidental mapping edits can invalidate evidence traceability while CI remains green. The current frozen units were independently hashed and are valid.

Proposed fix: validate unit objects before use, reject duplicate IDs and invalid ranges/source IDs, and recompute every unit hash from the frozen report slice. Make original fail on invalid mappings instead of silently slicing to empty text. Add negative tests that change each of these properties while leaving the report itself unchanged.

### ENG-02 — P2 / medium: schema validation accepts data that crashes lookup

Location: tools/knowledge.py:110-117; runtime consumer tools/knowledge.py:78.

Nonempty objects and numbers satisfy the substantive-field truthiness check. Nested check field types and list element types are not checked. Conversely, a null list field is reported and then iterated, raising TypeError rather than returning validation errors.

Minimal reproduction:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import sys
sys.path.insert(0, 'tools')
import knowledge as k
registry, units, _, claims = k.load()
claims[0]['conclusion'] = {'not': 'prose'}
print(k.validate(claims, registry['sources'], units))
try:
    k.search_claims(claims, 'posting frequency')
except Exception as e:
    print(type(e).__name__ + ': ' + str(e))
PY
~~~

Actual output:

~~~text
[]
TypeError: sequence item 0: expected str instance, dict found
~~~

A temporary regenerated repository with this mutation also passed the full validator. Replacing check values with wrong types returned []; setting evidence or source_units to null raised TypeError: 'NoneType' object is not iterable.

Effect: malformed future corpus edits can pass CI and break every search. The current frozen claim types pass an independent stricter check.

Proposed fix: validate complete shapes and types, including nonempty strings, string-list elements, check fields, source/link objects and evidence records, before any iteration or runtime use. Return errors without continuing through invalid containers. Test that malformed inputs fail validation cleanly and cannot reach search.

### ENG-03 — P2 / medium: invalid frontmatter passes the format gate but cannot install

Location: tools/validate.py:44-49. Documentation promise: docs/compatibility.md:7.

The checker looks for a starting delimiter and name/description lines, but never requires a closing delimiter or parses the actual frontmatter. Removing the closing delimiter from a canonical workflow, rebuilding, and validating succeeds. The real installer then skips that skill.

Reproduction:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import shutil, sys, tempfile
from pathlib import Path
sys.path.insert(0, 'tools')
import build, validate
with tempfile.TemporaryDirectory() as d:
    r = Path(d) / 'repo'
    shutil.copytree(Path.cwd(), r,
                    ignore=shutil.ignore_patterns('.git', '__pycache__', 'reviews'))
    p = r / 'workflows/x-explain.md'
    delimiter = chr(10) + '---' + chr(10)
    p.write_text(p.read_text(encoding='utf-8').replace(delimiter, chr(10), 1),
                 encoding='utf-8')
    for rel, content in build.expected_files(r).items():
        (r / rel).write_bytes(content)
    print(validate.validate_repository(r)[0])
PY
~~~

Actual output: [].

The same temporary fixture was tested with the real cached Skills CLI 1.7.4, selecting only x-explain. Validator exit: 0. Installer exit: 1. Its JSON result was:

~~~json
[
  {
    "name": "x-explain",
    "status": "skipped",
    "reason": "No matching skill found in source"
  }
]
~~~

Its diagnostic identified missing required frontmatter fields name and description.

Effect: CI's advertised format validation can green-light an uninstallable release. All current frozen frontmatter files install; this is a mutation-test gap.

Proposed fix: require a complete frontmatter block and validate its parsed shape, types and constraints with a supported validator, or reject syntax outside an explicitly supported dependency-free subset. Add missing-closer, invalid-YAML and duplicate-field tests. Keep local-reference/build checks as separate checks.

### ENG-04 — P2 / medium: duplicate merge silently changes metric meaning

Location: tools/summarize_posts.py:67-74 and tools/summarize_posts.py:124-126.
Contract: shared/observations.md:17 and shared/observations.md:22.

Two observations with the same permalink and timestamp but different metric_scope values are merged. The later row overwrites metric_scope, while missing later metrics are filled from the earlier scope. The result attaches the new scope to values observed under the old scope, without reporting a conflict.

Minimal reproduction uses the contract's supported post and owner_analytics scopes:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import sys
sys.path.insert(0, 'tools')
from summarize_posts import summarize
base = {'url': 'https://x.com/demo/status/123',
        'observed_at': '2026-10-30T12:00:00Z'}
p = summarize([
    dict(base, metric_scope='post', metrics={'views': '100', 'likes': '5'}),
    dict(base, metric_scope='owner_analytics', metrics={'replies': '2'})
])['posts'][0]
print(p['metric_scope'], p['metrics']['views']['value'],
      p['metrics']['likes']['value'], p['metrics']['replies']['value'],
      p.get('observation_conflicts'))
PY
~~~

Actual output:

~~~text
owner_analytics 100 5 2 None
~~~

Effect: public observations can be represented as private analytics, undermining the central separation between public counts, impressions and unique readers.

Proposed fix: retain separate observations or metric buckets by identity, verified timestamp and metric scope. Do not promote unknown-scope metrics into a known scope. Count unique posts by permalink identity independently of the number of scope records. Retain source provenance and explicitly flag incompatible scope observations.

### ENG-05 — P2 / medium: a third duplicate restores complete coverage despite unresolved text conflict

Location: tools/summarize_posts.py:67-70 and tools/summarize_posts.py:89-94.

The second differing text sets body_status to partial, but the next same-timestamp duplicate can overwrite that status with complete. The old conflict remains, so output claims complete coverage and unresolved contradictory text simultaneously. Adding a third different text also overwrites the prior conflict alternatives instead of retaining all of them.

Reproduction:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import sys
sys.path.insert(0, 'tools')
from summarize_posts import summarize
base = {'url': 'https://x.com/demo/status/123',
        'observed_at': '2026-10-30T12:00:00Z', 'body_status': 'complete'}
p = summarize([dict(base, text='Version A'), dict(base, text='Version B'),
               dict(base, text='Version B')])['posts'][0]
print(p['body_status'], p['observation_conflicts'])
PY
~~~

Actual output:

~~~text
complete {'text': ['Version A', 'Version B']}
~~~

Effect: repeated timeline/pinned observations can make conflicted evidence appear complete. This is a valid-input defect in current code, not a future mutation case.

Proposed fix: accumulate distinct text alternatives and derive coverage from unresolved conflicts after merging fields. A repeated conflicting snapshot must not clear partial/conflicted status. Define how a later timestamp or explicit reconciliation resolves conflicts, and test three or more duplicate rows.

### ENG-06 — P2 / medium: the CLI's raw character count silently normalizes Windows newlines

Location: tools/inspect_draft.py:57; contrary raw-string wording at tools/inspect_draft.py:19.

Path.read_text uses universal-newline translation before inspect_text sees the input. Consequently the output describes a normalized string as raw and can move the first-4000 boundary. This happens on Linux too when supplied a CRLF file.

Reproduction:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import json, subprocess, sys, tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / 'draft.txt'
    p.write_bytes(bytes([65, 13, 10]) * 2000)
    run = subprocess.run([sys.executable, 'tools/inspect_draft.py', '--text', str(p)],
                         capture_output=True, text=True, check=True)
    got = json.loads(run.stdout)['text']
    print(len(p.read_bytes().decode('utf-8')), got['raw_characters'],
          got['after_4000_characters'])
PY
~~~

Actual output:

~~~text
6000 4000 0
~~~

There are 6000 supplied Unicode code points, and trimming only leading/trailing whitespace would leave 5998. The reported raw string has lost every CR; its raw preview also no longer preserves the supplied file string.

Effect: common Windows text files receive incorrect raw counts and boundary analysis under the stated semantics. This does not establish any X production length rule.

Proposed fix: read UTF-8 text with newline='' using an explicit open call compatible with Python 3.9, then apply only documented normalization. Alternatively expose newline-normalized fields separately and explicitly label their transformation; raw fields must preserve the decoded input. Add LF/CRLF/lone-CR CLI boundary regressions.

### ENG-07 — P2 / medium: standalone distributions drop their own license and attribution

Location: tools/build.py:15-24 and tools/build.py:26-30.
Relevant distribution promise: docs/compatibility.md:25. Repository condition: LICENSE:12-13.

Every standalone bundle contains the original helper code, instructions, synthesis and research report, but neither LICENSE nor NOTICE.md is copied. Manual installation explicitly instructs users to copy only the skill folder; the real Skills CLI copy installation likewise contained only those generated files.

Reproduction:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import sys
from pathlib import Path
sys.path.insert(0, 'tools')
import build
files = build.expected_files()
print([p for p in files if Path(p).name.lower() in ('license', 'notice.md')])
print(len(files))
PY
~~~

Actual output:

~~~text
[]
158
~~~

Effect: the independently distributed copies omit the copyright/permission notice that the repository's own MIT text says must accompany copies or substantial portions. They also lose the repository's distinction between original MIT material and third-party source material. This is a concrete packaging omission; it is not an opinion on the legality of every third-party quotation.

Proposed fix: bundle LICENSE and a suitable attribution/provenance notice in every skill root or documented local reference, making any links valid inside an isolated installation. Add a packaging assertion for these files. Separately retain the source-by-source license/quotation review boundary; a blanket MIT file does not relicense third-party material.

### ENG-08 — P2 / medium: content deduplication stops after one verified relationship

Location: tools/summarize_posts.py:132-140 and tools/summarize_posts.py:151.

The identity table records immediate targets only. A Thread whose root is an Article carrier is split between the Article ID and the carrier's status ID, although all relationships are explicitly supplied. Adding the Article relationship splits what was previously one Thread content group.

Reproduction:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import sys
sys.path.insert(0, 'tools')
from summarize_posts import summarize
r = summarize([
    {'url': 'https://x.com/demo/status/111',
     'article_url': 'https://x.com/i/article/222'},
    {'url': 'https://x.com/i/article/222'},
    {'url': 'https://x.com/demo/status/333',
     'thread_root_url': 'https://x.com/demo/status/111'}
])
print(r['unique_content_items'])
print([p['content_identity'] for p in r['posts']])
PY
~~~

Actual output:

~~~text
2
['article:222', 'article:222', 'status:111']
~~~

Effect: the supposedly deduplicated content count can count one verified Article/carrier/Thread group twice and overstate independent review samples. Metrics correctly remain separate by URL in this fixture; the issue is the content grouping.

Proposed fix: resolve verified relationships to a stable canonical group, using transitive traversal or union-find, without merging metrics. Handle cycles and contradictory links explicitly. Add Article-as-Thread-root and input-order tests.

### ENG-09 — P3 / low: equivalent exact metric representations become false conflicts

Location: tools/summarize_posts.py:83-85.

Raw equality is tested before parse_count. An exact integer and the equivalent comma-formatted UI string are treated as conflicting measurements, causing an otherwise known count to become unknown.

Reproduction:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import sys
sys.path.insert(0, 'tools')
from summarize_posts import summarize
b = {'url': 'https://x.com/demo/status/123',
     'observed_at': '2026-10-30T12:00:00Z', 'metric_scope': 'post'}
p = summarize([dict(b, metrics={'views': 1000}),
               dict(b, metrics={'views': '1,000'})])['posts'][0]
print(p['metrics']['views'])
print(p['observation_conflicts'])
PY
~~~

Actual output:

~~~text
{'raw': None, 'value': None, 'precision': 'unknown'}
{'metrics.views': [1000, '1,000']}
~~~

Effect: combining valid screenshot/export representations introduces needless missing data and manual reconciliation.

Proposed fix: compare parsed exact values within the same metric scope while preserving both raw forms and provenance. Do not automatically equate rounded and exact values or different metric scopes. Add equivalent-integer-string and genuinely-conflicting-value tests.

### ENG-10 — P3 / low: malformed JSON root shapes bypass the CLI's intended input errors

Locations: tools/summarize_posts.py:170 and tools/inspect_draft.py:60.

The CLI accesses object methods/keys before verifying that the decoded root is an object. Valid JSON null, scalars, or a media object lacking media yield raw tracebacks instead of the parser's useful schema error.

Reproduction:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import subprocess, sys, tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
    p = Path(d)
    (p/'bad.json').write_text('null', encoding='utf-8')
    (p/'draft.txt').write_text('draft', encoding='utf-8')
    for args in [
        ['tools/summarize_posts.py', '--input', str(p/'bad.json')],
        ['tools/inspect_draft.py', '--text', str(p/'draft.txt'),
         '--media-json', str(p/'bad.json')]
    ]:
        r = subprocess.run([sys.executable, *args], capture_output=True, text=True)
        print(r.returncode, r.stderr.strip().splitlines()[-1])
PY
~~~

Actual output:

~~~text
1 AttributeError: 'NoneType' object has no attribute 'get'
1 TypeError: 'NoneType' object is not subscriptable
~~~

Effect: malformed user-supplied data receives an implementation exception rather than an actionable input diagnosis. The tools do fail rather than emit fabricated results.

Proposed fix: validate the root as list/object before member access, handle missing media/posts keys, and produce concise parser/JSON errors. Extend row-level validation to reject invalid enum/container types before Counter and other consumers use them.

## Storage, privacy and error-path results

The preference helper received independent tests beyond its existing suite, always with private temporary fixtures:

| Probe | Observed result |
| --- | --- |
| 24 concurrent save processes, distinct series | 9 successful saves and 15 clean busy-lock errors in the observed run; every successful scope persisted; revision 9; no lock files remained |
| POSIX permissions after save | File 0600; newly created immediate parent 0700 |
| Invalid UTF-8 import | Exit 1 with JSON error; existing store byte-identical |
| Symlinked destination resolving inside a Git fixture | Rejected; no preference file written |
| Existing corrupt store / unsupported schema | Existing tests independently rerun; rejected unchanged |
| Stale expected revision | Existing regression independently rerun; rejected unchanged |
| Temporary override | Existing byte-preservation regression independently rerun |
| Export collision / conflicting import | Existing regressions independently rerun; no unintended overwrite |
| OS-specific default selection and absolute override | Existing tests independently rerun; paths are installation-independent |
| Isolated installed visual helpers | Existing packaging tests independently rerun for router, checklist and visual specialist |

Concurrent success/failure counts depend on scheduling; the invariant checked is that no successful update disappeared, revision equals successful writes, and failures were explicit busy responses. The helper has no network calls or subprocess execution. Profiles are treated as data by the workflow, and credentials/provider access are not inferred from saved names.

A killed writer can leave an exclusive-create lock that requires operator reconciliation; this is fail-closed behavior, and the guide already says not to bypass a busy lock. A power-loss durability test, hostile multi-user parent-directory race test, Windows ACL test, and destroyed-container persistence test were not performed. The guide already distinguishes local storage from durable cross-host persistence. No unsupported claim of those guarantees is made here.

## Documentation, dependencies and compatibility assessment

The README files, compatibility document, changelog, implementation plans/specs and validation history were read directly. Their distinction between installation, helper execution, agent behavior, live browsing and exposure testing is appropriate. Historical review conclusions were not used as proof. Current code/tests and independently fetched CI status supplied the verification above.

Current primary documentation was checked on 2026-11-01:

- The official Skills CLI repository README and package.json specify Node >=22.20.0, project-local default installation and -g for global installation. They corroborate those repository claims. URLs: https://github.com/vercel-labs/skills and https://github.com/vercel-labs/skills/blob/main/package.json .
- The Agent Skills specification requires YAML frontmatter containing name and description and permits additional files such as a bundled license. URL: https://agentskills.io/specification . The current frozen bundles satisfy the practical installer check; ENG-03 concerns the weaker internal gate.
- A direct fetch of https://github.com/vercel-labs/skills/blob/main/docs/cli-reference.md failed with DisabledError. No claim relies on that inaccessible page; actual local installer execution verified the exercised flags.
- The documented CI run was read through the GitHub connector: https://github.com/alexliyu7352/for-you-skills/actions/runs/41261980741 . All three jobs and their relevant steps reported success.

The package itself has no third-party Python runtime dependency. Node/Skills CLI is an optional installer dependency, and external browsing/image tools remain host capabilities. The CI uses read-only contents permission; no publishing or credential-exfiltration step was found. Action version tags are mutable, but no exploitable workflow finding was established. GitHub-source installation was not repeated by this reviewer; the local frozen-source install is independently verified, and the historical remote-install statement remains historical.

License and provenance review confirms the root MIT/NOTICE distinction but finds the standalone omission in ENG-07. Source code quotations and upstream licenses require claim/source-level consideration by the evidence reviewers; this engineering review does not certify ownership of the entire research report.

## Recommended regression coverage

The existing 43 tests are useful and all passed. The missing high-value regressions correspond directly to the findings: corrupt unit metadata with unchanged report; nested malformed schema; invalid frontmatter that the installer rejects; mixed metric scopes; three or more conflicting duplicates; CRLF CLI text; isolated license/notice presence; transitive Article/Thread grouping; exact metric equivalence; malformed CLI root shapes.

No tests or fixes were added during this frozen review.
