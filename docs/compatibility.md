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

The Skills CLI requires Node.js 22.20+. Optional helpers require Python 3.9+; no pip packages are needed. Agents without Python can read the English JSON evidence and resolve reference indices directly.

Native skill invocation is optional. The router includes all specialist workflows as local references; a host can execute them in the same agent. It does not require child agents. Hosts with automatic discovery select skills from their descriptions; this remains model- and host-dependent. A host lacking discovery can be given the installed `x-assistant/SKILL.md` path.

Browser capability is separate from skill installation. Follow the host's connector, browser and authentication rules. If a page cannot be read, label the missing coverage and use supplied screenshots/text when appropriate.

## Manual installation

Copy a complete `skills/<name>/` folder to the target agent's documented skill directory. `--copy` is available in the Skills CLI where symlinks are unsuitable. Optional `agents/openai.yaml` files provide UI metadata; the core workflows do not rely on them. Tools resolve resources relative to their own file, so execution does not depend on the shell's current directory.
