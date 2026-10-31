# For You Skills

An evidence-backed X/Twitter assistant for creators. Ask naturally: “Can I publish this?”, “Is that algorithm tip true?”, or “Why is my Article still getting views?” The entry skill selects the appropriate workflow and returns one answer with concrete actions and original sources.

All skill instructions and knowledge entries are English. Responses follow the user's language.

## Install

Use the [Skills CLI](https://github.com/vercel-labs/skills) with Node.js 22.20 or newer:

```bash
npx skills add alexliyu7352/for-you-skills --skill '*'
```

Select your agent when prompted. Installation is project-local by default; add `-g` for a user-wide installation. To target specific agents:

```bash
npx skills add alexliyu7352/for-you-skills --skill '*' -a claude-code -a codex
```

The complete package is recommended. Individual skills remain independently installable:

```bash
npx skills add alexliyu7352/for-you-skills --skill x-assistant -a gemini-cli
npx skills add alexliyu7352/for-you-skills --skill x-publish-checklist -a opencode
```

`x-assistant` includes fallback copies of all six workflows, so installing only the entry skill also works. In a host without automatic discovery, point the agent to the installed `x-assistant/SKILL.md` once. No mandatory MCP server, X API key or paid data service is required. Optional scripts require Python 3.9+ and only its standard library; agents without Python can read the evidence files directly.

For manual installation, copy a complete directory from `skills/` into the skill directory documented by your agent. Copy the whole directory, including references and scripts. See [compatibility](docs/compatibility.md) for the distinction between installation support and verified runtime behavior.

## Skills

| Skill | Purpose |
| --- | --- |
| `x-assistant` | Natural-language routing, follow-up continuity, evidence reuse and a single consolidated answer |
| `x-explain` | Questions about posting, recommendations, weights, reach, media, links and related X behavior |
| `x-myth-check` | Claim-by-claim checks of viral advice and algorithm guides |
| `x-format-advisor` | Choose long Post, Article or Thread for specific material |
| `x-publish-checklist` | Complete prepublication review with specific edits, measured length and media plans |
| `x-review-posts` | Read published posts/accounts or supplied screenshots and recommend improvements |
| `x-reach-diagnosis` | Investigate observed exposure patterns without inventing hidden causes |

Examples:

- “Is the second post each day really penalized?”
- “Here is my draft. Choose a format and check it before publishing.”
- “Review these screenshots and suggest what I should publish next.”
- “My Article has 3K views after a week. Other Posts have hundreds. What does that tell me?”
- “Keep the Article format. Now check only the introduction.”

The router follows intent rather than requiring commands. It chooses only necessary steps, reuses prior observations and respects an explicitly selected specialist. Host skill discovery is model-dependent; this package does not install a global event hook or guarantee automatic activation in every client.

## Evidence and limits

The corpus contains **578 entries**, including **49 unresolved questions**, covering **668 substantive source units**, **100 reference groups** and **396 unique original URLs** from the complete research report. Each entry retains its conditions, practical implication, checking procedure, limitations and original references. Entry counts demonstrate coverage, not the truth of every interpretation.

Research cutoff: **2026-10-29**. Baseline revision: `5ed796374ea48ee26058aab66ab10c266bea2bef`; comparison revision: `606b254b45be798bfaecfa8c23f5a9c51bc8000c`. The skills distinguish code, official documentation, observations, editorial judgments and unknowns. Current deployment/product questions call for fresh primary sources where available.

No script calculates a proprietary X score or predicts guaranteed exposure. Public views, Home impressions, Article page counts, carrier-post counts and unique readers are not interchangeable. The 4000-character inspection is scoped to the documented processing path, not a universal publishing limit. Media recommendations depend on the material, not an invented fixed upload bonus.

Browsing is capability-selected. Use an available authorized connector, Chrome MCP or browser; supplied screenshots and exports are supported. Unread text or images remain unknown. The skills do not publish, edit, delete or engage with posts automatically.

## Maintain and validate

Canonical sources are `workflows/`, `shared/`, `knowledge/`, `routing.json`, `metadata/` and `tools/`. `skills/` is generated, committed distribution output. Edit canonical files, then rebuild:

```bash
python3 tools/build.py
python3 tools/validate.py
python3 tools/build.py --check
python3 -m unittest discover -s tests -v
```

Each installed skill receives its own knowledge and scripts. This duplicates distribution files intentionally while keeping one maintained source. It avoids broken `../../knowledge` or sibling-skill dependencies.

See [evidence maintenance](knowledge/README.md), [validation results](docs/validation/results.md), [release notes](CHANGELOG.md) and [attribution](NOTICE.md). The original Chinese report is archived solely for provenance; English entries and resolved source URLs are sufficient for use.

## License

Original skill instructions, English synthesis and helper code are available under the MIT license. Third-party source material retains its original license and attribution. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
