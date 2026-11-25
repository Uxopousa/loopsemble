# Install, verify, update, and remove

## Verify an installation

After `install.sh` succeeds, start a fresh Codex session with the project root open and invoke `$project-setup`. Confirm that the skill's instructions load. Check that Planner, Developer, Reviewer, test-specialist, and security-reviewer appear in the active client's available-agent list before claiming custom-agent delegation works. If the skill is absent, confirm the path is exactly `.agents/skills/<skill-name>/SKILL.md`, reload/restart the Codex client, and open the repository root as the workspace. If agent definitions are absent, confirm `.codex/agents/*.toml`, project trust, and client support. Report each capability as discovered, missing, or unverified. Use serial work if delegation cannot be confirmed.

Do not invent a universal validation command: client commands differ by surface and version. Use a CLI diagnostic only when documented for the installed client version. A successful file copy proves installation to disk, not discovery by Codex.

## Installation record and recovery

`.agent-workflow-install.json` records the pack version, exact relative file paths, SHA-256 hashes, and the source-template path only when inside the project. Validate every path stays within the root and compare hashes before treating a file as unmodified. It is an inventory, not proof of discovery or successful installation. Ordinary errors and SIGINT/SIGTERM roll back newly created files; power loss or SIGKILL cannot be handled. After an abrupt interruption, compare the record and bundle, show missing or modified files, and remove only confirmed unchanged partial-install files after the user chooses recovery. Preserve changed files. Then retry installation. Do not delete all of `.agents/` or `.codex/`.

## Update

The installer is intentionally no-clobber and is for first installation only. Read the recorded version and hashes first to identify local edits. To update, compare every installed skill and agent listed in the installation record with the current pack. Show changed files and preserve project-specific edits. Merge reviewed changes manually or through a dedicated approved task; do not rerun the installer over existing files, replace directories wholesale, or infer ownership from a matching filename. Re-run skill validation and the client discovery check after an update.

## Remove

The installer deploys `.agents/agent-workflow/uninstall.py` so removal remains available after source-template cleanup. Run it with Python 3.9+ and the absolute project root. Default mode is preview; `--apply` is the explicit removal request. The source pack also provides `scripts/uninstall.py` and `uninstall.sh`.

The tool validates the entire inventory and refuses invalid paths or a missing record before deleting anything. It deletes only recorded files whose hashes still match; modified files, symlinks, unknown files, generated domain skills, documents and project configuration remain. Only empty parent directories are removed. For partial removal it keeps the record and the unchanged uninstall tool for retry and exits with code 1. For complete removal it removes its own unchanged copy and the record last. If the tool itself is customized, it is preserved like any other changed file. Repeated operations after interruption recheck the current filesystem; the record is not rewritten or treated as permission to delete user changes.

Review references in `AGENTS.md`, profile and Git rules after removal; the tool reports these as project-owned follow-up instead of editing them. Tracked deletions remain visible in Git; the tool does not stage, commit or untrack anything. If the installed copy cannot run, use the source pack's tool with the same record. Without a valid record, manual ownership review is required.

## Resume

Follow the team-workflow skill’s resume contract. Conversation approval is not recoverable evidence after its context is lost. If the exact approved plan and its authorization are unavailable, stop implementation and present the plan again. A profile records durable project facts, not approval for a particular change.
