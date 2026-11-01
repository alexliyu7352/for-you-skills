# For You Skills — X.com / Twitter Algorithm Skills

**English** | [简体中文](README.zh-CN.md)

**Make your AI posting assistant show its sources.**

For You Skills turns a detailed analysis of the **X.com / Twitter recommendation algorithm's public source code** into an assistant you can use on your next post. Give it a draft, a screenshot, or an algorithm claim. Get specific changes, the evidence behind them, and a clear account of what remains unknown.

Choose between a long Post, an Article and a Thread. Check your opening and first image. Investigate why an Article keeps gaining views. Follow a recommendation back to its code, constants and applicable conditions.

**8 skills · 578 knowledge entries · 396 original source URLs · 49 unresolved questions preserved**

[Read the full research](https://blog.go5.si/posts/x-algorithm-teardown/) · [Follow the author for updates](https://x.com/alexlee20122022)

```bash
npx skills add alexliyu7352/for-you-skills --skill '*'
```

Then ask in your own words:

> Review this draft for X.com / Twitter. Tell me what to change, whether it should be an Article or a long Post, and what the first image should show. Explain which recommendations the code supports.

Installation checked for **Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot and OpenCode**. Instructions and knowledge are English; replies follow your language. [Installation details](#installation) · [Validation report](docs/validation/results.md)

## What changes when you check the code?

A number can be real and the advice built around it can still be wrong. These examples come from the research bundled with the skills:

| Question | What the analysis found | What to do with it |
| --- | --- | --- |
| **“Does my second post of the day lose about 40% of its reach?”** | The `0.625` author-diversity multiplier concerns an author's second-ranked candidate **within one scoring operation**. That function does not count daily posts. [Code](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237) | Plan the next post around a new question, evidence or update. Treat a proposed interval as something to test; this multiplier supplies no universal daily quota or four-hour reset. |
| **“Which image should go first?”** | One V8.2 media-selection path returns the **first available image**. A result left only in image four is absent from that selection. [Code](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L285-L314) | Put the most useful supported result and its key conditions in the first image; state the main finding in the text too. This is evidence about that processing path, not a promise of higher reach. |
| **“Must a long Post stay under 4,000 characters?”** | A specific V8.2 text-rendering path truncates body text at **4,000 characters**. That establishes a processing boundary, not a universal publishing limit. [Code](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L33-L50) | Measure the draft and check where the central finding lands. Keep the full argument when it earns its length; explain the scope of the boundary before choosing a format. |

The skills carry the conditions alongside each finding. They distinguish source-code facts, official documentation, local observations, writing judgments and unresolved questions. **You can inspect why an answer was given.**

## Bring a draft. Leave with changes you can use.

A prepublication review works through every applicable topic in the research. It should give you:

- **An opening you can publish.** It quotes your actual first lines, checks the promise they make, and supplies a concrete revision when needed.
- **A measured length review.** It counts the supplied text, states the unit and checks where the important material falls.
- **An image plan for this draft.** It explains whether images would help, what the first one should convey, and what each additional image contributes. Missing attachments still receive a concrete recommendation.
- **A format decision with reasons.** It weighs a long Post, Article or Thread against the material and your goal.
- **The remaining publishing checks.** Links, reading payoff, video conditions, hashtags, visibility labels, duplication, interaction and corrections are reviewed where relevant, with evidence and explicit gaps.
- **A reader pass with a clear result.** Where a fresh context is available, a reader who did not write the draft receives the complete review standard and reports unclear references, unexplained terms and missing reasoning steps. Otherwise, the review is labeled self-review. Revisions have a default budget of three reader passes; missing facts or unresolved problems are reported explicitly. Plan-only requests continue without inventing copy, and excerpts receive only a scoped verdict. This stage is editorial judgment, reported separately from the algorithm evidence.

Already published? Supply post links, account links, screenshots or exports. The review workflow can use an authorized browser or Chrome MCP when available, record what it actually sees, and suggest specific changes. Reach diagnosis separates observations from possible explanations and tells you what evidence would distinguish them.

## Turn the image plan into images

Ask **“Create the images from this review, and keep this series visually consistent.”** The assistant carries the draft, sources and image order into `x-create-visuals`; you do not need to explain the material again.

It checks the tools actually available, tells you when it can generate images directly, and offers your own assets, real screenshots, AI generation or a mixture. The first time, it asks for the missing source/provider and style choices. Later, you can reuse the saved style, change it just for this post, or save a new series style. **A one-time change leaves your default untouched.**

Preferences live in a private user configuration file, outside the installed skills and public repository. Default, account and series profiles support JSON export/import between agents and devices. A new installation on the same OS account reads the same file; separate hosts need an explicit transfer. When durable storage is unavailable, the assistant says so and offers an export.

Real evidence stays real: screenshots and code panels use source material, exact charts use verified data, and AI illustration is used where appropriate. The assistant checks text, numbers, cropping and image order before delivery. If no creation tool is available, it supplies clearly labeled briefs and prompts. Image generation depends on your host and chosen provider; the package supplies no provider credentials and promises no exposure bonus.

## One entry point, seven specialists

Ask naturally. **`x-assistant` selects the workflow**, carries context into follow-up questions and combines the findings into one answer. You can also install or invoke a specialist on its own.

| Skill | Use it for |
| --- | --- |
| [`x-assistant`](skills/x-assistant/SKILL.md) | The default entry: questions, mixed requests and follow-ups |
| [`x-explain`](skills/x-explain/SKILL.md) | X.com / Twitter algorithm, ranking weights, posting frequency, reading signals, media and links |
| [`x-myth-check`](skills/x-myth-check/SKILL.md) | Check an algorithm tip or guide claim by claim, with original sources |
| [`x-format-advisor`](skills/x-format-advisor/SKILL.md) | Choose a long Post, Article or Thread for your material |
| [`x-publish-checklist`](skills/x-publish-checklist/SKILL.md) | Review an unpublished draft and provide concrete edits |
| [`x-review-posts`](skills/x-review-posts/SKILL.md) | Inspect published content or screenshots and suggest improvements |
| [`x-reach-diagnosis`](skills/x-reach-diagnosis/SKILL.md) | Investigate reach patterns and identify the next useful check |
| [`x-create-visuals`](skills/x-create-visuals/SKILL.md) | Create useful images and save, reuse or transfer your visual style |

Try these:

> My Article has 3K views after a week and still gains views daily. My other Posts have hundreds. What can we conclude, and what should I publish next?

> Check this X.com / Twitter algorithm guide. For every claim, show the evidence, any misreading and what the code does not establish.

> Create two images for this post. Reuse the weekly-code style, but change the palette for this post only.

> Keep the Article format. Now rewrite only the introductory Post: give readers the established findings, the unknowns and the recommended actions.

Automatic discovery depends on the host and model. If needed, point your agent to `x-assistant/SKILL.md` once. The entry skill bundles all seven workflows, so it also works when installed alone.

## The research ships with the skills

The complete report was distilled into **578 English entries, including 49 unresolved questions**, covering **668 substantive source units**, **100 reference groups** and **396 unique original URLs**. The original Chinese report is retained for provenance.

Each entry records the conclusion, its conditions, practical implications, what to check, what to say when evidence is missing, its limits and its original citations. Relevant references include source files, line ranges, constants, formulas and change history.

**The unknowns are part of the knowledge base.** An account-specific reach question can remain unresolved even when the underlying code is public. The skills preserve that distinction and still propose a useful next step.

Every installed skill includes the evidence it needs. Lookup works offline; live verification and account inspection use the tools available in your agent. There is no mandatory paid data service, X.com / Twitter API key or particular MCP server. See the [knowledge guide](knowledge/README.md) and [original research](provenance/research-report.zh-CN.md).

## Read the research and follow updates

Want to understand the reasoning behind the skills? Read the original research for the code analysis, formulas, worked examples and limits behind the publishing advice:

- [Full research in English](https://blog.go5.si/posts/x-algorithm-teardown/)
- [完整中文研究文档](https://blog.go5.si/posts/zh/x-algorithm-teardown/)

The research and skills will be updated as the [X.com / Twitter algorithm repository's main branch](https://github.com/xai-org/x-algorithm) evolves. Updates will identify the analyzed revision and research date so findings remain traceable. Follow [@alexlee20122022 on X.com](https://x.com/alexlee20122022) for new findings, research progress and skill updates.

The research cutoff listed below describes the current bundled knowledge; installing the skills does not automatically pull future upstream changes.

## Installation

Use the command above with the [Skills CLI](https://github.com/vercel-labs/skills), which requires **Node.js 22.20+**. Select your agent when prompted. Installation is project-local by default; add `-g` for a user-wide installation.

To select specific agents:

```bash
npx skills add alexliyu7352/for-you-skills --skill '*' -a claude-code codex
```

To install only the entry skill or one specialist:

```bash
npx skills add alexliyu7352/for-you-skills --skill x-assistant -a gemini-cli
npx skills add alexliyu7352/for-you-skills --skill x-publish-checklist -a opencode
```

For manual installation, copy the entire `skills/<name>/` directory into your agent's skill directory, including references and scripts. Optional helpers use **Python 3.9+** and its standard library. Agents without Python can read the evidence files directly. Browser access is a separate host capability. [Compatibility details](docs/compatibility.md)

## What has been verified

The [full independent review](docs/reviews/full-repository-review/README.md) examined **all 578 knowledge entries**, eight workflows and the complete package. It found **22 issues** that the original 43-test suite had not caught. The [remediation record](docs/reviews/full-repository-review/remediation.md) tracks each correction, its regression or source check, and independent acceptance.

The [validation record](docs/validation/results.md) distinguishes automated tests, actual agent task cases, isolated helper execution, six-target installation and Linux/Windows CI. Test counts and exact release results live there so historical checks are not mistaken for verification of a later release.

The task cases cover multilingual questions, combined requests, follow-ups, draft review and supplied published-post records. Six separate external CLI/model executions, live X.com browser collection and exposure-uplift experiments have **not** been performed. [Full results and fixes](docs/validation/results.md)

## Research scope

Research cutoff: **2026-10-29**. Baseline revision: `5ed796374ea48ee26058aab66ab10c266bea2bef`; comparison revision: `606b254b45be798bfaecfa8c23f5a9c51bc8000c`. These are public-code snapshots. Questions about current product behavior or deployment require fresh primary sources where available.

The package does not calculate a proprietary exposure score or guarantee distribution. Public views, Home impressions, Article page counts and unique readers retain their different meanings. It reviews and advises; publishing, editing, deleting or engaging with live posts requires a separate user request and the host's authorization.

<details>
<summary><strong>Maintain the package</strong></summary>

Canonical sources are `workflows/`, `shared/`, `knowledge/`, `routing.json`, `metadata/` and `tools/`. The `skills/` directory is generated distribution output. Workflow source links use the installed skill's directory layout and may return 404 when followed from `workflows/` on GitHub; use the [workflow index and generated copies](workflows/README.md) to browse working links. Edit canonical files, then run:

```bash
python3 tools/build.py
python3 tools/validate.py
python3 tools/build.py --check
python3 -m unittest discover -s tests -v
```

Each skill carries its own references and scripts while sharing one maintained source. See [evidence maintenance](knowledge/README.md), [release notes](CHANGELOG.md) and [attribution](NOTICE.md).

</details>

## License

Original skill instructions, English synthesis and helper code are available under the [MIT license](LICENSE). Third-party source material retains its original license and attribution. See [NOTICE.md](NOTICE.md).
