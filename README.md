# Skills & Plugins Marketplace

A personal ChatGPT plugins marketplace for skills used in daily workflows. Each plugin groups related skills and can be packaged independently.

## Plugin catalog

| Plugin | Purpose | Version | Status |
| --- | --- | --- | --- |
| [Vultuk](plugins/vultuk/README.md) | Personal skills for daily workflows | 0.1.17 | Contains 17 skills; available for installation |

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
