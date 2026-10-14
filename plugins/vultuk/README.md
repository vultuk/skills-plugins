# Vultuk

Personal skills for daily workflows. Plugin ID: `vultuk`. Version: `0.1.4`.

## Skills

| Skill | Purpose and when to use | Setup |
| --- | --- | --- |
| [how](skills/how/SKILL.md) | Explicit code walkthroughs, subsystem architecture, runtime flow, ownership, and layering questions before changes | Codebase read/search access; optional subagents with sequential fallback |
| [create-verification-skill](skills/create-verification-skill/SKILL.md) | Generate a project-local verification skill and feature map for real app workflows | Target codebase, project runtime/build tools, suitable harness, and disposable fixtures |
| [maintain-verification-skill](skills/maintain-verification-skill/SKILL.md) | Audit and repair verification documentation, feature maps, and owned harnesses using source and live coverage | Existing verification skill and map, runnable test environment, live harness; optional subagents |
| [why](skills/why/SKILL.md) | Investigate historical rationale and tradeoffs with cited, confidence-qualified evidence | Target code/history; available authorized connectors or authenticated `gh`; optional subagents |

Example: “Use how to explain how authentication works in this repository.” For verification authoring, ask “Use create-verification-skill to create a verification workflow for this repository.” For maintenance, ask “Use maintain-verification-skill to audit this repository’s verification skill.” For historical rationale, ask “Use why to investigate why this subsystem was designed this way.” Automatic invocation is disabled for all four skills.

## Attribution

`how` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/how`. It is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/how/LICENSE) is included. See the [root import record](../../README.md#imported-skills) for source links and local adaptations.

`create-verification-skill` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/create-verification-skill`. Its three example files are preserved unchanged. It is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/create-verification-skill/LICENSE) is included. See the [root import record](../../README.md#create-verification-skill) for adaptations and requirements.

`maintain-verification-skill` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/maintain-verification-skill/SKILL.md`. It is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/maintain-verification-skill/LICENSE) is included. See the [root import record](../../README.md#maintain-verification-skill) for adaptations and requirements.

`why` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/why`. It includes all upstream reference files and is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/why/LICENSE) is included. See the [root import record](../../README.md#why) for adaptations and requirements.

## Verification

Manifest, frontmatter, invocation policy, references, and attribution receive static checks. Host installation and end-to-end execution have not been tested. The imported files require no installation. Executing either verification skill requires the target application’s tools and test environment; no target application was exercised during this import.
