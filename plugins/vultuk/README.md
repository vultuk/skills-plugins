# Vultuk

Personal skills for daily workflows. Plugin ID: `vultuk`. Version: `0.1.1`.

## Skills

| Skill | Purpose and when to use | Setup |
| --- | --- | --- |
| [how](skills/how/SKILL.md) | Explicit code walkthroughs, subsystem architecture, runtime flow, ownership, and layering questions before changes | Codebase read/search access; optional subagents with sequential fallback |

Example: “Use how to explain how authentication works in this repository.” Automatic invocation is disabled for this skill.

## Attribution

`how` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/how`. It is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/how/LICENSE) is included. See the [root import record](../../README.md#imported-skills) for source links and local adaptations.

## Verification

Manifest, frontmatter, invocation policy, references, and attribution receive static checks. Host installation and end-to-end execution have not been tested. No runtime dependencies or external connections are required.
