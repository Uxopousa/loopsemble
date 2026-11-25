# Two setup modes

## New project

Use when the target directory is empty or contains only this workflow bundle, or when the user explicitly wants to plan a project before writing application code. Confirm the target directory. Obtain the minimum facts through chat or `project-brief.md`; see `references/input-review.md`. Do not invent a framework or build command. If the user has not chosen a stack, record it as undecided and recommend an explicit later decision before stack-dependent implementation. Record chosen technologies as planned, with the user's decision as source. Recommend matching skills but do not claim they have been validated against code. Write a ready profile when the first task can be planned honestly; complete architecture and roadmap may be future tasks. Application scaffolding belongs to a later approved plan.

## Existing project

Use when application code, manifests, or project documentation are present. Inspect the current state and user-supplied files before asking questions; see `references/input-review.md`. Record active technologies and commands with file evidence; identify stale or conflicting configuration. Ask only about product intent, policies, or ambiguous ownership that the repository cannot settle. Preserve existing instructions and changes. If the project has multiple apps, confirm which roots the profile covers. A profile may be refreshed after a stack migration; preserve prior human decisions unless the user changes them.

## Shared completion rule

Both modes produce one `project-profile.md` in the target root and a short report of chosen skills and gaps. The profile must distinguish observed facts from planned choices and unresolved decisions. Choose the installed workflow's visibility near the start, then offer source-template cleanup at the end using `references/setup-cleanup.md` (read from the `project-setup` skill root). The setup request authorizes the profile write; cleanup requires the user's specific choice. It does not authorize application implementation, dependency installation, commits, or a transition into `$team-workflow` without a concrete task and approved plan.

After writing the profile, verify skill and custom-agent discovery in a fresh Codex session. If the project has no `AGENTS.md`, offer a minimal pointer that makes `$team-workflow` auto-invoke on implementation requests while preserving plan approval; if one exists, offer a small additive rule. Do not silently replace project instructions. Use `references/maintenance.md` for exact post-install and update checks.

## Keep setup concise

Present one compact summary of discovered facts, important gaps, and recommended defaults. Ask only decisions that block a correct profile, preferably together. Serial work, the existing client permission settings, and no optional specialist agents are defaults. Parallel execution, additional agents, model selection, and permission changes are optional tuning; explain them only when supported and relevant to the project. Do not require the user to understand internal setting names. Record detailed capability evidence and non-blocking skill recommendations in the profile and final report. Ask separately about the installed files' visibility and source-template cleanup at their defined points; do not mix those choices into a long technical questionnaire.
