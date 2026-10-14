# Repository instructions

## Purpose

This repository houses a ChatGPT plugin containing a growing collection of skills for the owner's daily workflows. Keep skills focused, reusable, and easy to discover.

## Maintain the skill catalog

Treat the root `README.md` as the user-facing entry point to the plugin. Whenever a skill is added, changed, moved, or removed, update its README entry in the same change. Create the README if it does not exist.

For every skill, include its name, purpose, when to use it, and a link to its local `SKILL.md`. Document any required tools, connections, or setup. Group skills by workflow when useful as the collection grows, and preserve the README's existing style.

## Document imported skills

Whenever you import, copy, or vendor a skill from another repository, update the root `README.md` in the same change. Create `README.md` if it does not exist.

For each imported skill, document:

- Its name and a short description of what it does.
- Its local path in this repository.
- The source repository URL and original skill path.
- The source commit, tag, or version, when available.
- Any setup requirements, local modifications, and required license or attribution information.

Keep this information in an **Imported skills** section. Update existing entries when skills are refreshed, moved, or removed rather than adding duplicate entries. Preserve unrelated README content and follow its existing style.

Before finishing, verify that every skill imported by the change has an accurate README entry and that its local path exists. Do not invent missing provenance; explicitly mark unavailable source details as unknown.
