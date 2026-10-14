# Maintaining the marketplace

## Add a plugin

1. Copy `templates/plugin/` into `plugins/<plugin-name>/`. Use a stable lowercase kebab-case name.
2. Replace every placeholder in `plugin.json` and the plugin README. Match the manifest name to the directory name, use a semantic version, and keep the listing subtitle at most 30 characters. Add accurate author/publisher metadata before distribution.
3. Replace the example skill with at least one usable skill under `skills/<skill-name>/SKILL.md`. Its YAML frontmatter must contain a matching name and a description explaining when to use it. Keep skill names unique within the plugin.
4. Keep supporting scripts, references, and assets inside that plugin. Portable skills are discovered from `skills/`; do not add a top-level `skills` field to the portable manifest. Add `mcp.json` only when an actual MCP server is required.
5. Add an entry to `.agents/plugins/marketplace.json`, replacing `my-plugin` with the real name:

   ```json
   {
     "name": "my-plugin",
     "source": {"source": "local", "path": "./plugins/my-plugin"},
     "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
     "category": "Productivity"
   }
   ```

   Source paths resolve from the repository root, not the catalog directory. Preserve existing entries and ordering.
6. Update the root README plugin and skill catalogs and the plugin README in the same change.

## Import a skill

Place the skill inside the plugin that owns its workflow. Review its instructions and supporting files, preserve required licenses and notices, and document required tools or connections. Check that the source permits redistribution before listing it for others.

Add an entry under **Imported skills** in the root README with:

- Skill name, purpose, when to use it, and local `SKILL.md` link.
- Source repository URL and original skill path.
- Source commit SHA, tag, or version; explicitly mark unavailable details as unknown.
- Local modifications and setup requirements.
- License and attribution details, with links to retained notices.

Refresh that entry when updating the import. Preserve unrelated README content and upstream attribution.

## Verify a change

- Parse edited JSON manifests and YAML frontmatter as data.
- Check that registered plugin names match their manifests, versions use SemVer, and catalog paths resolve inside this repository.
- Check that skill names match their directories and referenced local files exist inside their plugin.
- Confirm no placeholder skills are listed and the root README documents every plugin and skill added by the change.
- Exercise the affected workflow with representative input when tools and connections are available. Report skipped installation or runtime checks explicitly.

This scaffold requires no package manager, dependency installation, or build. A future plugin that needs a runtime should document its checks and use one package manager and lockfile.

## Distribution

Version plugins independently. Keep installation, account upload, public submission, and Git pushes as separate explicitly requested actions. Export only the individual plugin folder, including required licenses and supporting files. Exclude the marketplace, templates, credentials, and unrelated plugins.

Format reference: [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins).
