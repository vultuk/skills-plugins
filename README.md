# Skills & Plugins Marketplace

A personal ChatGPT plugins marketplace for skills used in daily workflows. Each plugin groups related skills and can be packaged independently.

## Plugin catalog

| Plugin | Purpose | Version | Status |
| --- | --- | --- | --- |
| [Vultuk](plugins/vultuk/README.md) | Personal skills for daily workflows | 0.1.1 | Contains `how`; available for installation |

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


## Repository layout

```text
.agents/plugins/marketplace.json  Marketplace catalog
plugins/                         Independent plugin packages
templates/plugin/                Starter package (not listed)
AGENTS.md                        Repository instructions for agents
CONTRIBUTING.md                   Adding and importing plugins and skills
```

## Getting started

Follow [CONTRIBUTING.md](CONTRIBUTING.md) to add skills to Vultuk or create another plugin.

Once the catalog contains a completed plugin, the documented Codex registration command, run from this repository root, is:

```sh
codex plugin marketplace add .
```

Then use the desktop Plugins Directory to select **Skills & Plugins**, install the desired plugin, and test it in a new chat. Restart the desktop app if necessary to refresh local discovery. Repository marketplace availability varies by client; this scaffold has not been installed or tested in a host.

A repository marketplace is a local/team distribution catalog. Publishing to the public ChatGPT directory is a separate submission process. Export individual plugin folders, not the whole marketplace.

See the official [plugin packaging and marketplace documentation](https://developers.openai.com/plugins/build/plugins) for supported formats and installation options.
