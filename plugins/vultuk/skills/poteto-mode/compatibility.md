# ChatGPT/Codex compatibility

These rules adapt the retained upstream playbooks. Apply them before following any playbook instruction.

- User and project instructions govern scope, approvals, storage, builds, GUI use, and cleanup. Importing or invoking this style does not authorize external messages, PRs, merges, releases, deployments, destructive cleanup, or schedules.
- Translate Cursor Task/poteto-agent calls to available host-native delegation. Inherit model settings. Missing independent reviewers must be reported, not simulated as verified review.
- Treat references to other pstack skills, principle leaves, cursor-team-kit, create-skill, Origin, and Cursor model rules as optional integrations. Only how, why, create-verification-skill, and maintain-verification-skill are included alongside this skill. Read installed skills before claiming to apply them; otherwise use concrete local playbook guidance and disclose material gaps.
- Use the host's supported question, task tracking, browser, and computer tools. Prefer the project's existing skill location, otherwise `.agents/skills/`. Cursor transcript paths are not Codex transcript paths. Do not invent replacements or claim absent transcripts establish inactivity.
- Upstream playbooks that say to open a PR, merge, send a message, or publish apply only when the user authorized that action. Otherwise finish local reviewable work and report the pending action.
- Cleanup requires checking ownership, live processes, uncommitted/untracked/ignored data, and remote preservation under the project's storage policy. Never force-remove a worktree. The retained worktree audit helper reads Cursor transcript locations and cannot establish Codex task ownership; use it only as partial diagnostic evidence, never as deletion authority.

## Bundled helper requirements

The `scripts/` directory retains upstream helpers and tests. Bun is required for orchestration and PR watching; Node.js is required for the plan checker; Git and authenticated `gh` are required for GitHub reads/actions. Some playbooks mention optional Origin tooling. No service connection or credentials are bundled.

From `scripts/`, install with `bun install --frozen-lockfile`, respecting the project's install runner and preflight policy. Run `bun run test` and `bun run typecheck` for fixture tests and TypeScript checks. No mixed package manager or shared node_modules symlink.

The upstream bootstrap may install dependencies automatically on first helper invocation. Complete installation explicitly through the required project runner before invoking wrappers, or run the wrapper through that runner so any bootstrap install is covered. Scripts can modify local orchestration state or GitHub state depending on command; inspect the relevant playbook and command before use. Do not run live drive/merge/cleanup commands merely to test an import.

The retained examples and helper tests do not prove host integration, live PR operations, cleanup safety, or complete autonomous workflows.
