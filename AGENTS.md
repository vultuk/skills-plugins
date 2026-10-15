# Repository instructions

## Purpose

This repository is a ChatGPT plugins marketplace containing independently packaged plugins for the owner's daily workflows. Each plugin may contain multiple related skills. Keep skills focused, reusable, and easy to discover.

## Marketplace structure

- Keep the catalog at `.agents/plugins/marketplace.json` and independent plugin packages in `plugins/<plugin-name>/`.
- Give each plugin its own portable `plugin.json`, `README.md`, and `skills/<skill-name>/SKILL.md` files with YAML name and description fields.
- Keep plugins self-contained; supporting files must not depend on sibling plugins or absolute machine paths.
- Use `templates/plugin/` only as an authoring starter. Never list unfinished templates in the marketplace.
- Match catalog names and paths to manifests. Version plugins independently with SemVer and bump versions for releases.
- Follow `CONTRIBUTING.md`; update the catalog, root README, and affected plugin README together.
- Add MCP configuration, connections, hooks, and dependencies only when required. Never commit credentials.
- Verify JSON, skill frontmatter, local references, and README coverage. Distinguish static checks from actual installation and runtime testing.

## Maintain the skill catalog

Treat the root `README.md` as the user-facing entry point to the plugin. Whenever a skill is added, changed, moved, or removed, update its README entry in the same change. Create the README if it does not exist.

For every skill, include its name, purpose, when to use it, and a link to its local `SKILL.md`. Document any required tools, connections, or setup. Group skills by workflow when useful as the collection grows, and preserve the README's existing style.

## Document imported skills

Until the user says otherwise, import all skills into the **pstack** plugin at `plugins/pstack/skills/<skill-name>/`. Do not create another plugin or choose a different destination for imports unless the user requests it. Update both the root `README.md` and `plugins/pstack/README.md` for each import.

After each completed skill import, run the relevant verification, commit the import and its required documentation or metadata changes, and push to `main`. The user has explicitly authorized this recurring commit-and-push workflow. Keep unrelated changes out of the commit, preserve others' work, and never force-push. If verification fails or a push is blocked, report the issue rather than claiming completion.

Whenever you import, copy, or vendor a skill from another repository, update the root `README.md` in the same change. Create `README.md` if it does not exist.

For each imported skill, document:

- Its name and a short description of what it does.
- Its local path in this repository.
- The source repository URL and original skill path.
- The source commit, tag, or version, when available.
- Any setup requirements, local modifications, and required license or attribution information.

Keep this information in an **Imported skills** section. Update existing entries when skills are refreshed, moved, or removed rather than adding duplicate entries. Preserve unrelated README content and follow its existing style.

Before finishing, verify that every skill imported by the change has an accurate README entry and that its local path exists. Do not invent missing provenance; explicitly mark unavailable source details as unknown.
