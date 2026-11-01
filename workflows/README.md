# Workflow sources

These files are the canonical source templates used by [the build script](../tools/build.py). Their relative links, such as `references/knowledge-guide.md`, resolve from the installed skill directory. Following those links directly from a source file here on GitHub can return 404.

**To read a workflow with working links, open its generated `SKILL.md` below. To install it, copy the entire corresponding skill directory.** Edit the source file when maintaining the package, then rebuild; do not edit generated files directly.

| Source template | Generated workflow with working links |
| --- | --- |
| [x-assistant.md](x-assistant.md) | [x-assistant/SKILL.md](../skills/x-assistant/SKILL.md) |
| [x-explain.md](x-explain.md) | [x-explain/SKILL.md](../skills/x-explain/SKILL.md) |
| [x-myth-check.md](x-myth-check.md) | [x-myth-check/SKILL.md](../skills/x-myth-check/SKILL.md) |
| [x-format-advisor.md](x-format-advisor.md) | [x-format-advisor/SKILL.md](../skills/x-format-advisor/SKILL.md) |
| [x-publish-checklist.md](x-publish-checklist.md) | [x-publish-checklist/SKILL.md](../skills/x-publish-checklist/SKILL.md) |
| [x-review-posts.md](x-review-posts.md) | [x-review-posts/SKILL.md](../skills/x-review-posts/SKILL.md) |
| [x-reach-diagnosis.md](x-reach-diagnosis.md) | [x-reach-diagnosis/SKILL.md](../skills/x-reach-diagnosis/SKILL.md) |
| [x-create-visuals.md](x-create-visuals.md) | [x-create-visuals/SKILL.md](../skills/x-create-visuals/SKILL.md) |

The router also bundles specialist workflows under its own `references/workflows/` directory. The build adjusts their reference links for that location. The generated packages are self-contained; this source layout does not require extra files in an installed skill.
