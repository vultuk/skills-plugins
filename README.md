# Skills & Plugins Marketplace

A personal ChatGPT plugins marketplace for skills used in daily workflows. Each plugin groups related skills and can be packaged independently.

## Plugin catalog

| Plugin | Purpose | Version | Status |
| --- | --- | --- | --- |
| [Vultuk](plugins/vultuk/README.md) | Personal skills for daily workflows | 0.1.43 | Contains 43 skills; available for installation |

Vultuk includes [how](plugins/vultuk/skills/how/SKILL.md) for explicit code walkthroughs and architecture questions. It requires codebase read/search access; subagents are optional. The [plugin template](templates/plugin/) remains an authoring starter, not a marketplace entry.

When adding a plugin, list its name, purpose, version, and local README here. List every skill with its purpose, when to use it, setup requirements, and a link to its `SKILL.md`.

## Imported skills

### how

- Purpose: explain subsystem architecture, runtime flow, code ownership, and layering before making changes.
- Use: explicitly request the `how` skill, for example, “Use how to explain how authentication works in this repository.”
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/how`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/how).
- Local skill: [how](plugins/vultuk/skills/how/SKILL.md), including both upstream reference prompts.
- Setup: access to the codebase and read/search tools. Subagent support is preferred; a sequential fallback is included. No install, API credentials, or external service is required.
- Adaptations: replaced Cursor Task/model/rule dependencies with host-native read-only delegation and inherited model settings; added a sequential fallback; removed the unavailable sibling `why` skill recommendation; replaced Cursor read-tool names; translated explicit-only invocation into `agents/openai.yaml` with `allow_implicit_invocation: false`.
- License: MIT, copyright (c) 2026 Lauren Tan. Full [license and attribution](plugins/vultuk/skills/how/LICENSE) retained.
- Verification: static package checks only; host installation and end-to-end skill execution have not been tested.


### create-verification-skill

- Purpose: generate a project-local verification skill and feature map grounded in the app's real user workflows.
- Use: explicitly request “Use create-verification-skill to create a verification workflow for this repository.”
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/create-verification-skill`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/create-verification-skill).
- Local skill: [create-verification-skill](plugins/vultuk/skills/create-verification-skill/SKILL.md), including all three feature-map examples.
- Setup: a target codebase, its documented runtime/build tools, an appropriate UI/CLI/API harness, and disposable test data. Requirements are discovered per project; the Notes examples are illustrative, not dependencies.
- Adaptations: default generated output to `.agents/skills/` while respecting project conventions; preserve explicit-only invocation through `agents/openai.yaml`; make the maintenance sibling optional; clarify example-only commands, scope limits, project tool requirements, and draft reporting when execution is blocked.
- License: MIT, copyright (c) 2026 Lauren Tan. Full [license and attribution](plugins/vultuk/skills/create-verification-skill/LICENSE) retained.
- Verification: static package checks; host installation and generation/execution against a target application have not been tested.

### maintain-verification-skill

- Purpose: audit an existing project verification skill and feature map against source and live behavior, correcting documentation or harness drift without editing product code.
- Use: explicitly request “Use maintain-verification-skill to audit this repository’s verification skill.”
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/maintain-verification-skill/SKILL.md`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/maintain-verification-skill).
- Local skill: [maintain-verification-skill](plugins/vultuk/skills/maintain-verification-skill/SKILL.md). Upstream contains no supporting files for this skill.
- Setup: an existing project verification skill and feature map, source access, runnable test environment, and its live harness. Subagents are preferred with a sequential fallback. The companion [create-verification-skill](plugins/vultuk/skills/create-verification-skill/SKILL.md) is included in Vultuk.
- Adaptations: recognize `.agents/skills/` and existing project skill locations; use host-native bounded delegation with inherited models and sequential fallback; preserve explicit invocation through `agents/openai.yaml`; require explicit authorization for PRs and applicable authorization for commits/pushes; clarify scope, live-check requirements, and unscheduled manual execution.
- License: MIT, copyright (c) 2026 Lauren Tan. Full [license and attribution](plugins/vultuk/skills/maintain-verification-skill/LICENSE) retained.
- Verification: static package checks only; host installation and an end-to-end maintenance run against a target application have not been tested.

### why

- Purpose: investigate design rationale, historical constraints, regressions, and thresholds using cited evidence while separating facts, inference, and unknowns.
- Use: explicitly request “Use why to investigate why this subsystem was designed this way.” Use the companion `how` skill for runtime mechanics.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/why`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/why).
- Local skill: [why](plugins/vultuk/skills/why/SKILL.md), including all 12 upstream reference files (confidence framework, prompts, playbook index, and source playbooks).
- Setup: target source and available history; authenticated source-control access via a connector or `gh` for PR evidence. Other evidence categories use available, authorized connectors. Missing tools, history, authentication, and access are reported as coverage gaps. Subagents are optional; sequential review is supported.
- Adaptations: replace Cursor model/rule/tool assumptions with host-native discovery and bounded delegation; preserve explicit invocation through `agents/openai.yaml`; add sequential fallback and read-only authorization boundaries; handle missing source-control access; treat warehouse columns as examples requiring discovery; avoid triggering Seer analysis jobs.
- License: MIT, copyright (c) 2026 Lauren Tan. Full [license and attribution](plugins/vultuk/skills/why/LICENSE) retained.
- Verification: static package checks only; host installation and an end-to-end investigation using connected sources have not been tested.

### poteto-mode

- Purpose: explicitly requested engineering workflow/style guidance, with playbooks for investigation, implementation, verification, orchestration, and delivery.
- Use: “Use poteto-mode for this task.” Invocation alone does not authorize external actions.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/poteto-mode`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/poteto-mode).
- Local skill: [poteto-mode](plugins/vultuk/skills/poteto-mode/SKILL.md), with all 46 upstream files, including playbooks, reference material, helpers, tests, package manifest, and Bun lockfile.
- Setup: see [compatibility and helper requirements](plugins/vultuk/skills/poteto-mode/compatibility.md). Core guidance needs no runtime; helpers require Bun/Node/Git and sometimes authenticated `gh`. Other pstack skills, Cursor agents, and Origin are optional upstream integrations, not bundled.
- Adaptations: normalize skill name; translate explicit invocation to `agents/openai.yaml`; replace Cursor model/agent defaults; constrain autonomy and PR triggers to user authorization; add a compatibility guide covering missing siblings, tool mapping, helper bootstrap installs, and the Cursor-only limits of worktree auditing. Upstream helper implementations and playbooks are retained.
- License: MIT, copyright (c) 2026 Lauren Tan. Full [license](plugins/vultuk/skills/poteto-mode/LICENSE) retained.
- Verification: 68 fixture tests passed, TypeScript strict typecheck passed, shell/Node syntax checks passed, and all 46 upstream files and executable modes were checked (45 files unchanged); host installation, live PR/merge/cleanup actions, and full workflows are not verified.

### principle-attack-the-premise

- Purpose and when to use: Apply when two or more fixes that share one premise have failed the same gate. Take a census of which actors hold the imbalance before the next fix, then question the premise instead of writing another fix that assumes it.
- Invocation: explicitly request `principle-attack-the-premise`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-attack-the-premise](plugins/vultuk/skills/principle-attack-the-premise/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-attack-the-premise`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-attack-the-premise).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-attack-the-premise/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-boundary-discipline

- Purpose and when to use: Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions.
- Invocation: explicitly request `principle-boundary-discipline`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-boundary-discipline](plugins/vultuk/skills/principle-boundary-discipline/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-boundary-discipline`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-boundary-discipline).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy; qualify internal trust with validated invariants. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-boundary-discipline/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-build-the-lever

- Purpose and when to use: Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Build the tool that does it or proves it (codemod, script, generator, or a skill your subagents follow) instead of working by hand. The tool is the artifact a reviewer can rerun.
- Invocation: explicitly request `principle-build-the-lever`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-build-the-lever](plugins/vultuk/skills/principle-build-the-lever/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-build-the-lever`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-build-the-lever).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-build-the-lever/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-encode-lessons-in-structure

- Purpose and when to use: Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script instead of more text.
- Invocation: explicitly request `principle-encode-lessons-in-structure`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-encode-lessons-in-structure](plugins/vultuk/skills/principle-encode-lessons-in-structure/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-encode-lessons-in-structure`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-encode-lessons-in-structure).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-encode-lessons-in-structure/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-exhaust-the-design-space

- Purpose and when to use: Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. Build 2-3 competing prototypes and compare side by side before committing.
- Invocation: explicitly request `principle-exhaust-the-design-space`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-exhaust-the-design-space](plugins/vultuk/skills/principle-exhaust-the-design-space/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-exhaust-the-design-space`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-exhaust-the-design-space).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-exhaust-the-design-space/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-experience-first

- Purpose and when to use: Apply when product, UX, or feature-scope tradeoffs come up. Choose user delight over implementation convenience; ship fewer polished features over more rough ones.
- Invocation: explicitly request `principle-experience-first`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-experience-first](plugins/vultuk/skills/principle-experience-first/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-experience-first`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-experience-first).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-experience-first/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-explain-the-number

- Purpose and when to use: Apply before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result. Find what limits it, and rule out that it measured something other than the work you think.
- Invocation: explicitly request `principle-explain-the-number`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-explain-the-number](plugins/vultuk/skills/principle-explain-the-number/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-explain-the-number`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-explain-the-number).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-explain-the-number/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-fix-root-causes

- Purpose and when to use: Apply when debugging. Trace each symptom to its root cause and fix it there; reproduce first, ask why until you reach it, resist nil-check guards that silence crashes.
- Invocation: explicitly request `principle-fix-root-causes`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-fix-root-causes](plugins/vultuk/skills/principle-fix-root-causes/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-fix-root-causes`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-fix-root-causes).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy; scope repeated-instance fixes. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-fix-root-causes/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-foundational-thinking

- Purpose and when to use: Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so downstream code becomes obvious.
- Invocation: explicitly request `principle-foundational-thinking`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-foundational-thinking](plugins/vultuk/skills/principle-foundational-thinking/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-foundational-thinking`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-foundational-thinking).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-foundational-thinking/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-guard-the-context-window

- Purpose and when to use: Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads.
- Invocation: explicitly request `principle-guard-the-context-window`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-guard-the-context-window](plugins/vultuk/skills/principle-guard-the-context-window/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-guard-the-context-window`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-guard-the-context-window).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy; sequential fallback when delegation is unavailable. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-guard-the-context-window/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-laziness-protocol

- Purpose and when to use: Apply when refactoring, evaluating diff size, or tempted to add abstractions, layers, or signal threading. Bias toward deletion and the smallest change that solves the problem.
- Invocation: explicitly request `principle-laziness-protocol`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-laziness-protocol](plugins/vultuk/skills/principle-laziness-protocol/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-laziness-protocol`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-laziness-protocol).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-laziness-protocol/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-make-operations-idempotent

- Purpose and when to use: Apply when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries. Converge to the same end state regardless of partial prior runs.
- Invocation: explicitly request `principle-make-operations-idempotent`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-make-operations-idempotent](plugins/vultuk/skills/principle-make-operations-idempotent/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-make-operations-idempotent`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-make-operations-idempotent).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-make-operations-idempotent/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-migrate-callers-then-delete-legacy-apis

- Purpose and when to use: Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers.
- Invocation: explicitly request `principle-migrate-callers-then-delete-legacy-apis`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-migrate-callers-then-delete-legacy-apis](plugins/vultuk/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-migrate-callers-then-delete-legacy-apis`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-migrate-callers-then-delete-legacy-apis).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-migrate-callers-then-delete-legacy-apis/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-minimize-reader-load

- Purpose and when to use: Apply when reviewing or shaping code that's hard to trace. Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope.
- Invocation: explicitly request `principle-minimize-reader-load`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-minimize-reader-load](plugins/vultuk/skills/principle-minimize-reader-load/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-minimize-reader-load`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-minimize-reader-load).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-minimize-reader-load/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-model-the-domain

- Purpose and when to use: Apply when writing stateful logic, or when code branches a lot or repeats a shape assumption across files.
- Invocation: explicitly request `principle-model-the-domain`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-model-the-domain](plugins/vultuk/skills/principle-model-the-domain/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-model-the-domain`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-model-the-domain).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-model-the-domain/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-never-block-on-the-human

- Purpose and when to use: Apply when tempted to ask 'should I do X?' on reversible work.
- Invocation: explicitly request `principle-never-block-on-the-human`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-never-block-on-the-human](plugins/vultuk/skills/principle-never-block-on-the-human/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-never-block-on-the-human`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-never-block-on-the-human).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy; explicit scope and approval boundaries. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-never-block-on-the-human/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-outcome-oriented-execution

- Purpose and when to use: Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code.
- Invocation: explicitly request `principle-outcome-oriented-execution`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-outcome-oriented-execution](plugins/vultuk/skills/principle-outcome-oriented-execution/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-outcome-oriented-execution`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-outcome-oriented-execution).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-outcome-oriented-execution/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-prove-it-works

- Purpose and when to use: Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles.'
- Invocation: explicitly request `principle-prove-it-works`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-prove-it-works](plugins/vultuk/skills/principle-prove-it-works/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-prove-it-works`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-prove-it-works).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-prove-it-works/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-redesign-from-first-principles

- Purpose and when to use: Apply when integrating a new requirement into an existing design.
- Invocation: explicitly request `principle-redesign-from-first-principles`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-redesign-from-first-principles](plugins/vultuk/skills/principle-redesign-from-first-principles/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-redesign-from-first-principles`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-redesign-from-first-principles).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-redesign-from-first-principles/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-separate-before-serializing-shared-state

- Purpose and when to use: Apply when concurrent actors might write to the same file, branch, key, or state object. Eliminate the sharing first; serialize structurally only when one shared writer is a real invariant.
- Invocation: explicitly request `principle-separate-before-serializing-shared-state`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-separate-before-serializing-shared-state](plugins/vultuk/skills/principle-separate-before-serializing-shared-state/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-separate-before-serializing-shared-state`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-separate-before-serializing-shared-state).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-separate-before-serializing-shared-state/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-sequence-verifiable-units

- Purpose and when to use: Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the sequence proves itself to a reviewer.
- Invocation: explicitly request `principle-sequence-verifiable-units`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-sequence-verifiable-units](plugins/vultuk/skills/principle-sequence-verifiable-units/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-sequence-verifiable-units`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-sequence-verifiable-units).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-sequence-verifiable-units/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-subtract-before-you-add

- Purpose and when to use: Apply when sequencing an addition, refactor, or rewrite. Remove dead code, redundant validators, and stub references first, then build on the simpler base.
- Invocation: explicitly request `principle-subtract-before-you-add`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-subtract-before-you-add](plugins/vultuk/skills/principle-subtract-before-you-add/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-subtract-before-you-add`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-subtract-before-you-add).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-subtract-before-you-add/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-test-behavior-not-implementation

- Purpose and when to use: Apply when you write, change, or keep a test. Call the code as its users do and assert the exact result they see. Rewrite or delete a test that would pass if every imported function returned undefined.
- Invocation: explicitly request `principle-test-behavior-not-implementation`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-test-behavior-not-implementation](plugins/vultuk/skills/principle-test-behavior-not-implementation/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-test-behavior-not-implementation`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-test-behavior-not-implementation).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-test-behavior-not-implementation/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### principle-type-system-discipline

- Purpose and when to use: Apply when designing types, reviewing a function signature, or writing code in any statically-typed language. Make illegal states unrepresentable, brand semantic primitives, parse external data at boundaries, refuse to lie to the compiler, exhaust variants, derive from authoritative schemas.
- Invocation: explicitly request `principle-type-system-discipline`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [principle-type-system-discipline](plugins/vultuk/skills/principle-type-system-discipline/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/principle-type-system-discipline`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/principle-type-system-discipline).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/principle-type-system-discipline/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### architect

- Purpose and when to use: Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape.
- Invocation: explicitly request `architect`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [architect](plugins/vultuk/skills/architect/SKILL.md). Includes all 4 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/architect`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/architect).
- Setup: Relevant code or current-conversation context and host-native subagents when available. Sequential fallback and review limitations are explicit.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance; removed Cursor model rules and respected design-only scope. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/architect/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### arena

- Purpose and when to use: Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape.
- Invocation: explicitly request `arena`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [arena](plugins/vultuk/skills/arena/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/arena`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/arena).
- Setup: Relevant code or current-conversation context and host-native subagents when available. Sequential fallback and review limitations are explicit.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance; replaced Cursor model pool and Task launch settings. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/arena/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### benchmark-checklist

- Purpose and when to use: Vet a perf measurement (limiter, tuning, limits, errors, repeatability, relevance, and whether the work happened) before you report or act on it. Use when you run a benchmark or report a speedup or regression you measured.
- Invocation: explicitly request `benchmark-checklist`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [benchmark-checklist](plugins/vultuk/skills/benchmark-checklist/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/benchmark-checklist`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/benchmark-checklist).
- Setup: A runnable target benchmark and OS/runtime measurement tools appropriate to the project.
- Adaptations: normalized portable metadata and explicit invocation policy; portable CPU-count command. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/benchmark-checklist/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### bro

- Purpose and when to use: Restate the last message in plain human language, with no jargon.
- Invocation: explicitly request `bro`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [bro](plugins/vultuk/skills/bro/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/bro`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/bro).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/bro/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### control-cli

- Purpose and when to use: Build or adapt a local harness to drive, inspect, and profile an interactive CLI or TUI without external services. Use for CLI UX checks, startup regressions, memory leaks, hangs, prompt flows, or terminal demos.
- Invocation: explicitly request `control-cli`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [control-cli](plugins/vultuk/skills/control-cli/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `cursor-team-kit/skills/control-cli`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/cursor-team-kit/skills/control-cli).
- Setup: A local target application, its existing test/runtime tools, and host-supported terminal or browser control. No external service is bundled.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance; preserve verification evidence during cleanup. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Cursor; full [license and attribution](plugins/vultuk/skills/control-cli/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### control-ui

- Purpose and when to use: Build or adapt a local browser/CDP harness to drive and inspect a web, IDE, or Electron UI. Use for local UI verification, screenshots, accessibility snapshots, perf profiles, visual diffs, or reproducing UI bugs.
- Invocation: explicitly request `control-ui`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [control-ui](plugins/vultuk/skills/control-ui/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `cursor-team-kit/skills/control-ui`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/cursor-team-kit/skills/control-ui).
- Setup: A local target application, its existing test/runtime tools, and host-supported terminal or browser control. No external service is bundled.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance; honor host browser/GUI restrictions over generic CDP examples. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Cursor; full [license and attribution](plugins/vultuk/skills/control-ui/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### deslop

- Purpose and when to use: Remove AI-generated code slop and clean up code style
- Invocation: explicitly request `deslop`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [deslop](plugins/vultuk/skills/deslop/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `cursor-team-kit/skills/deslop`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/cursor-team-kit/skills/deslop).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Cursor; full [license and attribution](plugins/vultuk/skills/deslop/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### figure-it-out

- Purpose and when to use: Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the task, runs a hypothesis loop, and logs decisions. Use for /figure-it-out or 'figure it out'.
- Invocation: explicitly request `figure-it-out`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [figure-it-out](plugins/vultuk/skills/figure-it-out/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/figure-it-out`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/figure-it-out).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/figure-it-out/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### interrogate

- Purpose and when to use: Use for "interrogate", "adversarial review", "multi-model review", "challenge this", "stress test this code", "find blind spots", or "tear this apart". Multiple LLM reviewers challenge changes from independent angles.
- Invocation: explicitly request `interrogate`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [interrogate](plugins/vultuk/skills/interrogate/SKILL.md). Includes all 5 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/interrogate`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/interrogate).
- Setup: Relevant code or current-conversation context and host-native subagents when available. Sequential fallback and review limitations are explicit.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance; removed unsupported reviewer models and automatic configuration PR. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/interrogate/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### ketchup

- Purpose and when to use: Catch the user up on what changed in this chat since their last message, in a few plain sentences and small visuals. Give each action item just enough context to make the call. Use for /ketchup.
- Invocation: explicitly request `ketchup`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [ketchup](plugins/vultuk/skills/ketchup/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/ketchup`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/ketchup).
- Setup: Relevant project or text context; no new runtime dependency. Follow applicable project tools and permissions.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/ketchup/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### no-comments

- Purpose and when to use: Review scoped comments, remove supported redundancy, preserve contracts and safety constraints, and propose enforceable alternatives.
- Invocation: explicitly request `no-comments`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [no-comments](plugins/vultuk/skills/no-comments/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/no-comments`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/no-comments).
- Setup: Relevant code or current-conversation context and host-native subagents when available. Sequential fallback and review limitations are explicit.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance; replaced missing Comment Sicko agent with an explicit conservative review brief; retained ambiguous safety and contract information. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/no-comments/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### reflect

- Purpose and when to use: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
- Invocation: explicitly request `reflect`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [reflect](plugins/vultuk/skills/reflect/SKILL.md). Includes all 5 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/reflect`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/reflect).
- Setup: Relevant code or current-conversation context and host-native subagents when available. Sequential fallback and review limitations are explicit.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance; current-conversation transcript access, read-only reviewers, approved backlog writes, and portable authoring fallback. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/reflect/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### setup-pstack

- Purpose and when to use: Configure explicit, supported model and reasoning preferences for Vultuk pstack roles in the current session or approved project guidance.
- Invocation: explicitly request `setup-pstack`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [setup-pstack](plugins/vultuk/skills/setup-pstack/SKILL.md). Includes all 1 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/setup-pstack`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/setup-pstack).
- Setup: Host-exposed model capabilities and explicit user preferences; persistence is opt-in and not automatically loaded.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance; rewrote Cursor global model configuration as explicit portable project/session preferences with capability validation. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/setup-pstack/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

### show-me-your-work

- Purpose and when to use: Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). Local by default; commit it when a reviewer needs the trail to trust the result. Use for /show-me-your-work, autonomous or multi-phase runs, or work a human reviews after stepping away.
- Invocation: explicitly request `show-me-your-work`, or use it as a named companion workflow after reading its instructions. Automatic invocation is disabled.
- Local skill: [show-me-your-work](plugins/vultuk/skills/show-me-your-work/SKILL.md). Includes all 3 upstream files for this skill.
- Source: [cursor/plugins](https://github.com/cursor/plugins), `pstack/skills/show-me-your-work`, commit [`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`](https://github.com/cursor/plugins/tree/1e5c90a4b6f249917bd21fe361b3a2a7deb741b8/pstack/skills/show-me-your-work).
- Setup: Bash for the bundled TSV helper; current-conversation evidence. Optional authorized independent review.
- Adaptations: normalized portable metadata and explicit invocation policy; host tools, scope, authorization, and review-coverage guidance; removed Cursor transcript-path and mandatory cross-model assumptions. Forward dependency links are pinned upstream until the companion is imported, then linked locally.
- License: MIT, copyright (c) 2026 Lauren Tan; full [license and attribution](plugins/vultuk/skills/show-me-your-work/LICENSE) retained.
- Verification: metadata, references, provenance, and package checks; end-to-end host execution is not verified.

## Repository layout

```text
.agents/plugins/marketplace.json  Marketplace catalog
plugins/                         Independent plugin packages
templates/plugin/                Starter package (not listed)
AGENTS.md                        Repository instructions for agents
CONTRIBUTING.md                   Adding and importing plugins and skills
```

## Download a plugin archive

Every push to `main` runs [Release plugin archive](.github/workflows/release-plugins.yml) and publishes a separate GitHub release. Download **vultuk.tar.gz** from [Releases](https://github.com/vultuk/skills-plugins/releases), not GitHub's automatic source-code archives. A SHA-256 checksum is attached alongside it.

The archive has `plugin.json` at its root and includes only the committed Vultuk plugin files, with all skills, references, and licenses. Marketplace configuration and templates are excluded. The workflow checks the archive layout; it does not test installation in ChatGPT or execute the skills.

Release tags use `main-<workflow-run-id>`, allowing every push to produce an archive even when the plugin version is unchanged. Re-running the same run replaces its assets. Plugin versions remain managed separately in `plugin.json`.

To reproduce packaging locally, run `python3 scripts/package-plugin.py`. This packages **HEAD**, so commit plugin edits first. Output is written to ignored `dist/`. No dependencies or build are required.

## Getting started

Follow [CONTRIBUTING.md](CONTRIBUTING.md) to add skills to Vultuk or create another plugin.

Once the catalog contains a completed plugin, the documented Codex registration command, run from this repository root, is:

```sh
codex plugin marketplace add .
```

Then use the desktop Plugins Directory to select **Skills & Plugins**, install the desired plugin, and test it in a new chat. Restart the desktop app if necessary to refresh local discovery. Repository marketplace availability varies by client; this scaffold has not been installed or tested in a host.

A repository marketplace is a local/team distribution catalog. Publishing to the public ChatGPT directory is a separate submission process. Export individual plugin folders, not the whole marketplace.

See the official [plugin packaging and marketplace documentation](https://developers.openai.com/plugins/build/plugins) for supported formats and installation options.
