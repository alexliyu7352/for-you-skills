# For You Skills Implementation Plan

> **For agentic workers:** Use executing-plans for integration; independent knowledge translation uses dispatching-parallel-agents. Steps use checkbox syntax.

**Goal:** Ship an English, evidence-backed X assistant with one router and six independently installable specialists.

**Architecture:** Maintain canonical knowledge and workflow sources. Generate self-contained skills and validate generated copies. Keep citation resolution and offline inspection in Python standard-library scripts.

**Tech Stack:** Markdown, JSON, Python 3.9+, Agent Skills, GitHub.

**Spec:** ../specs/2026-10-31-for-you-skills.md

## Global Constraints
- Seven entry points named in the approved spec; no automatic X mutations.
- English runtime instructions and knowledge, multilingual user responses.
- Retain every source-unit mapping, evidence index, unknown reference and numeric boundary.
- Runtime scripts use the Python standard library and relative paths.
- No mandatory vendor tool, absolute personal path, sibling installation or online database.

## Review Focus
- Isolated router installation must still resolve all six workflows.
- Non-English natural-language requests must retrieve English evidence.
- Screenshot/preview/Article-carrier metrics must retain missing-data and identity boundaries.
- Numeric claims must preserve units and pipeline scope.
- Generated skill copies must match the canonical knowledge and workflows.

### Task 1: English knowledge and provenance
Files: knowledge/*.json, knowledge/README.md, provenance/*.md.
Interface: preserve existing claim/source/unit IDs and evidence schema; English human-readable fields.
- [x] Run English-corpus/coverage baseline tests.
- [x] Translate topics and source labels in disjoint files, retain original provenance.
- [x] Audit IDs, complete report coverage, URLs, numbers, conditions and unknown links.

### Task 2: Independent workflows and router
Files: workflows/*.md, routing.json, tools/knowledge.py, tools/inspect_draft.py, tools/summarize_posts.py.
Interface: route descriptions select workflows; all workflows consume the same claim schema and observation records.
- [x] Record baseline discovery and language limitations of the existing two skills.
- [x] Write and validate each specialist workflow; add router with bundled fallback workflows.
- [x] Run fresh-context task probes, including compound requests and follow-up turns.

### Task 3: Reproducible distribution
Files: tools/build.py, tools/validate.py, skills/*, tests/test_distribution.py, README.md, docs/compatibility.md, LICENSE.
Interface: build writes self-contained directories; --check reports drift without mutations.
- [x] Run isolated-install and build-drift tests before implementation.
- [x] Implement packaging and meaningful regression checks.
- [x] Test standalone skills, no-network evidence lookup, source coverage and draft/post scripts.

### Task 4: Verification and release
Files: docs/validation/results.md, CHANGELOG.md.
- [x] Review all outputs from fresh-context application probes and fix failures.
- [x] Independent repository review; run full test suite after fixes.
- [x] Verify installer discovery/installation where supported; label unavailable runtimes honestly.
- [ ] Publish verified repository; install/update all seven personal skills and verify saved paths.
