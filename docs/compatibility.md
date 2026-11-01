# Compatibility

The package uses the [Agent Skills format](https://agentskills.io/specification) and the [Skills CLI](https://github.com/vercel-labs/skills). It has no mandatory vendor tool names, absolute personal paths, sibling-skill dependency or proprietary invocation syntax.

## What each check means

- **Format validation:** required frontmatter, relative references and bundled files validate.
- **Installation:** the documented installer discovers the package and creates the target agent's project directories.
- **Helper execution:** scripts work from an isolated installed skill with only Python's standard library.
- **Agent behavior:** a real agent reads the skill and completes a representative task.
- **Live X browsing:** a real authorized connector/browser reads actual X pages. Screenshot/fixture review does not establish this.

Installation targets: Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot and OpenCode. The exact checks performed and limitations are recorded in [validation results](validation/results.md). A supported installer target is not a claim that every client/model/browser combination has been tested.

## Runtime requirements

The Skills CLI requires Node.js 22.20+. Optional helpers require Python 3.9+; no pip packages are needed. Helpers read UTF-8 files and emit UTF-8 JSON, including on Windows. Agents without Python can read the English JSON evidence and resolve reference indices directly.

Native skill invocation is optional. The router includes all specialist workflows as local references; a host can execute them in the same agent. It does not require child agents. Hosts with automatic discovery select skills from their descriptions; this remains model- and host-dependent. A host lacking discovery can be given the installed `x-assistant/SKILL.md` path.

Browser capability is separate from skill installation. Follow the host's connector, browser and authentication rules. If a page cannot be read, label the missing coverage and use supplied screenshots/text when appropriate.

## Manual installation

Copy a complete `skills/<name>/` folder to the target agent's documented skill directory. `--copy` is available in the Skills CLI where symlinks are unsuitable. Optional `agents/openai.yaml` files provide UI metadata; the core workflows do not rely on them. Tools resolve resources relative to their own file, so execution does not depend on the shell's current directory.

Every standalone folder includes `LICENSE`, a local `NOTICE.md`, and the research errata. Copy these with the instructions, references and scripts.

The repository's dependency-free frontmatter gate supports exactly `name` and `description` as unique, single-line plain or quoted strings in a complete `---` block. It accepts JSON double quotes and YAML single quotes, plus blank lines and whole-line comments. It rejects ambiguous plain values, inline comments, collections, block scalars and other YAML features instead of pretending to parse them. This is the repository's supported authoring subset, not a restriction of the Agent Skills specification.

## Visual creation and preferences

`x-create-visuals`, `x-assistant` and `x-publish-checklist` each bundle the complete visual workflow and `visual_preferences.py`. The router has seven specialist fallbacks; the checklist can complete an accepted creation handoff without an installed sibling.

Image generation is an optional host/provider capability, discovered at execution time. No image service, credential or vendor-specific CLI is installed by this package. Exact charts and evidence panels use verified source material and suitable rendering tools. Missing generation capability yields a labeled brief/prompts, not a generated-image claim.

Private preference location: Linux uses `$XDG_CONFIG_HOME/for-you-skills` or `~/.config/for-you-skills`; macOS uses `~/Library/Application Support/for-you-skills`; Windows uses `%APPDATA%/for-you-skills` or the user's `AppData/Roaming/for-you-skills`. The filename is `visual-preferences.json`. An absolute `FOR_YOU_SKILLS_CONFIG_DIR` or helper `--file` can select another private location. Git repositories and skill installation directories are rejected by the helper.

All copies in the same OS account share this file. Separate hosts/containers need explicit JSON transfer or a persistent private volume; there is no automatic cross-device synchronization. Export/import preserves explicit default/account/series scopes. Temporary overrides are read-only. Profiles contain style preferences, not secrets or copied reference assets. Without Python, a host with reliable file tools can maintain the same schema; without durable storage, memory is session-only and the assistant offers an export.
