# Vultuk

Personal skills for daily workflows. Plugin ID: `vultuk`. Version: `0.1.13`.

## Skills

| Skill | Purpose and when to use | Setup |
| --- | --- | --- |
| [how](skills/how/SKILL.md) | Explicit code walkthroughs, subsystem architecture, runtime flow, ownership, and layering questions before changes | Codebase read/search access; optional subagents with sequential fallback |
| [create-verification-skill](skills/create-verification-skill/SKILL.md) | Generate a project-local verification skill and feature map for real app workflows | Target codebase, project runtime/build tools, suitable harness, and disposable fixtures |
| [maintain-verification-skill](skills/maintain-verification-skill/SKILL.md) | Audit and repair verification documentation, feature maps, and owned harnesses using source and live coverage | Existing verification skill and map, runnable test environment, live harness; optional subagents |
| [why](skills/why/SKILL.md) | Investigate historical rationale and tradeoffs with cited, confidence-qualified evidence | Target code/history; available authorized connectors or authenticated `gh`; optional subagents |
| [poteto-mode](skills/poteto-mode/SKILL.md) | Explicit engineering workflow and style guidance with task-specific playbooks | [Compatibility guide](skills/poteto-mode/compatibility.md); optional Bun/Node/Git helpers and authorized GitHub access |
| [principle-attack-the-premise](skills/principle-attack-the-premise/SKILL.md) | Apply when two or more fixes that share one premise have failed the same gate. Take a census of which actors hold the imbalance before the next fix, then question the premise instead of writing another fix that assumes it. | Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions. |
| [principle-boundary-discipline](skills/principle-boundary-discipline/SKILL.md) | Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions. | Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions. |
| [principle-build-the-lever](skills/principle-build-the-lever/SKILL.md) | Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Build the tool that does it or proves it (codemod, script, generator, or a skill your subagents follow) instead of working by hand. The tool is the artifact a reviewer can rerun. | Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions. |
| [principle-encode-lessons-in-structure](skills/principle-encode-lessons-in-structure/SKILL.md) | Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script instead of more text. | Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions. |
| [principle-exhaust-the-design-space](skills/principle-exhaust-the-design-space/SKILL.md) | Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. Build 2-3 competing prototypes and compare side by side before committing. | Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions. |
| [principle-experience-first](skills/principle-experience-first/SKILL.md) | Apply when product, UX, or feature-scope tradeoffs come up. Choose user delight over implementation convenience; ship fewer polished features over more rough ones. | Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions. |
| [principle-explain-the-number](skills/principle-explain-the-number/SKILL.md) | Apply before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result. Find what limits it, and rule out that it measured something other than the work you think. | Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions. |
| [principle-fix-root-causes](skills/principle-fix-root-causes/SKILL.md) | Apply when debugging. Trace each symptom to its root cause and fix it there; reproduce first, ask why until you reach it, resist nil-check guards that silence crashes. | Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions. |

Example: “Use how to explain how authentication works in this repository.” For verification authoring, ask “Use create-verification-skill to create a verification workflow for this repository.” For maintenance, ask “Use maintain-verification-skill to audit this repository’s verification skill.” For historical rationale, ask “Use why to investigate why this subsystem was designed this way.” Automatic invocation is disabled for all bundled skills.

## Attribution

`how` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/how`. It is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/how/LICENSE) is included. See the [root import record](../../README.md#imported-skills) for source links and local adaptations.

`create-verification-skill` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/create-verification-skill`. Its three example files are preserved unchanged. It is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/create-verification-skill/LICENSE) is included. See the [root import record](../../README.md#create-verification-skill) for adaptations and requirements.

`maintain-verification-skill` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/maintain-verification-skill/SKILL.md`. It is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/maintain-verification-skill/LICENSE) is included. See the [root import record](../../README.md#maintain-verification-skill) for adaptations and requirements.

`why` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/why`. It includes all upstream reference files and is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/why/LICENSE) is included. See the [root import record](../../README.md#why) for adaptations and requirements.

`poteto-mode` is imported from `cursor/plugins` at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/poteto-mode`, with all 46 upstream files. It is MIT-licensed, copyright (c) 2026 Lauren Tan; the [license](skills/poteto-mode/LICENSE) is included. See the [import record](../../README.md#poteto-mode) and [compatibility guide](skills/poteto-mode/compatibility.md). Request “Use poteto-mode for this task” explicitly.

`principle-attack-the-premise` comes from `cursor/plugins` at `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/principle-attack-the-premise`. MIT, copyright (c) 2026 Lauren Tan; [license](skills/principle-attack-the-premise/LICENSE), [source and adaptations](../../README.md#principle-attack-the-premise).

`principle-boundary-discipline` comes from `cursor/plugins` at `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/principle-boundary-discipline`. MIT, copyright (c) 2026 Lauren Tan; [license](skills/principle-boundary-discipline/LICENSE), [source and adaptations](../../README.md#principle-boundary-discipline).

`principle-build-the-lever` comes from `cursor/plugins` at `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/principle-build-the-lever`. MIT, copyright (c) 2026 Lauren Tan; [license](skills/principle-build-the-lever/LICENSE), [source and adaptations](../../README.md#principle-build-the-lever).

`principle-encode-lessons-in-structure` comes from `cursor/plugins` at `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/principle-encode-lessons-in-structure`. MIT, copyright (c) 2026 Lauren Tan; [license](skills/principle-encode-lessons-in-structure/LICENSE), [source and adaptations](../../README.md#principle-encode-lessons-in-structure).

`principle-exhaust-the-design-space` comes from `cursor/plugins` at `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/principle-exhaust-the-design-space`. MIT, copyright (c) 2026 Lauren Tan; [license](skills/principle-exhaust-the-design-space/LICENSE), [source and adaptations](../../README.md#principle-exhaust-the-design-space).

`principle-experience-first` comes from `cursor/plugins` at `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/principle-experience-first`. MIT, copyright (c) 2026 Lauren Tan; [license](skills/principle-experience-first/LICENSE), [source and adaptations](../../README.md#principle-experience-first).

`principle-explain-the-number` comes from `cursor/plugins` at `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/principle-explain-the-number`. MIT, copyright (c) 2026 Lauren Tan; [license](skills/principle-explain-the-number/LICENSE), [source and adaptations](../../README.md#principle-explain-the-number).

`principle-fix-root-causes` comes from `cursor/plugins` at `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, path `pstack/skills/principle-fix-root-causes`. MIT, copyright (c) 2026 Lauren Tan; [license](skills/principle-fix-root-causes/LICENSE), [source and adaptations](../../README.md#principle-fix-root-causes).

## Verification

Manifest, frontmatter, invocation policy, references, and attribution receive static checks. Host installation and end-to-end execution have not been tested. The imported files require no installation. Executing either verification skill requires the target application’s tools and test environment; no target application was exercised during this import.
