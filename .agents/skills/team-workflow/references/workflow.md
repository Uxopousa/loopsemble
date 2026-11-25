# Execution contract

## 1. Plan

Only the root coordinator starts this workflow. An agent already assigned a phase must execute that phase and return its result; it must not start another Planner–Developer–Reviewer cycle, request approval again, or delegate recursively.

Read the project profile, repository policy, relevant requirements, code, tests, tracking, and Git state. Planner returns a versioned plan in chat: goal, scope and exclusions, task graph, dependencies, files or areas owned per task, acceptance criteria, applicable checks, risks, and integration order. Separate facts from assumptions. The coordinator presents the plan and waits for explicit human approval of that version. A material change to scope, criteria, ownership, or execution mode requires a revised plan and approval.

Read `references/skill-routing.md` for role-to-skill assignments, diagnosis triggers, and final evidence checks. For bugs or unexplained failures, route read-only investigation through systematic-debugging before approving a speculative fix. Reconcile requirements, task graph and plan scope before implementation.

If the profile selects optional plan, execution-state, review, threat-model, testing-strategy, or ADR documents, read the canonical files and include their necessary maintenance and writer ownership in the plan. Do not create a second tracking system or require these files when declined. Planner and Reviewer keep returning their analysis in chat; the coordinator records authorized plans, snapshots, and reports. A saved document never replaces human approval.

## 2. Select execution mode

Use serial mode by default: one Developer task at a time, followed by review and correction. Use parallel mode only if the approved plan names independent tasks and the profile permits it. Independence means no task requires another task's unmerged output, each task has distinct owned files or a separate working directory backed by a worktree or clone, shared interfaces are agreed before work starts, and the coordinator has a concrete integration order. Merely having multiple roadmap IDs does not establish independence. If ownership overlaps or a dependency appears, pause affected tasks and serialize or replan.

Before offering parallel execution, verify the active Codex client exposes subagent delegation and that multi-agent tools are enabled for this session. Project agent TOMLs define role behavior; they do not enable delegation or guarantee a concurrency limit. Current Codex clients document `[agents]` with `enabled = true` and `max_concurrent_threads_per_session` as the concurrency cap. Check the installed client version and effective configuration first; legacy clients may use different keys. Do not apply API session settings to CLI configuration. If delegation is disabled, show the proposed project-config diff and ask before changing it, or use serial mode. If the active interface cannot expose subagents, report that parallel execution is unavailable there. Treat a profile's concurrency value as a plan limit, not a runtime-enforced setting, unless the client confirms enforcement.

Parallel file ownership does not itself isolate writes. Prefer a separate worktree or clone directory per writing Developer where supported. A branch in a shared checkout is not isolation. Assign the actual working-directory path, base revision, and allowed files; include generated outputs, lockfiles, caches, and configuration in the write set. Never switch a shared checkout between branches while other agents use it. If the client only provides a shared checkout, parallelize read-only analysis, or use Developers only when their write sets are disjoint and verify the changed-file lists before integration. Never promise conflict-free parallel writes.

Never start more Developers than the profile's concurrency limit or the client's available slots. Assign each Developer the plan version, human approval, task ID, owned files, acceptance criteria, base revision, and checks. Developers must preserve unrelated changes and report changed files, results, and deviations. They do not approve their own plan or declare the integrated result complete.

Optional specialists: invoke `test-specialist` for substantial test design, regressions, complex behavior, integration risk, or weak evidence; invoke `security-reviewer` for changed trust boundaries, authentication/authorization, sensitive data, external inputs/integrations, secrets, dependencies, deployment settings, or an explicit security-review request. Read `references/testing-workflow.md` and `references/security-review-workflow.md` respectively. The plan states specialist scope and assigned write ownership. The coordinator can invoke additional read-only specialist analysis within the task autonomously when risk emerges; writing tests or changing scope requires approved ownership. They are not mandatory for every task and do not replace Developer or Reviewer.

## 3. Integrate and review

Wait for the required Developer results. The integration owner checks the actual diff, untracked files, and base revisions; combines work in the approved order; resolves only mechanical conflicts within approved scope. A semantic conflict or changed interface goes to Planner for a revised dependency and integration proposal. If that changes the approved plan materially, ask the human before continuing.

Give Reviewer the approved plan, integrated diff, project context, and acceptance criteria. Have Reviewer inspect the implementation independently before reading Developer conclusions when the client allows it. Reviewer reports evidence, impact, severity, and a way to verify each finding; it does not edit files. Review the integrated behavior as well as individual tasks, especially shared interfaces and regressions.

The coordinator sends Reviewer findings to the responsible Developer with disposition: accepted, rejected with evidence, or awaiting a human decision. For accepted findings, Developer reports the fix and evidence; Reviewer then rechecks that fix and related integration. This is an explicit Reviewer → coordinator → Developer → Reviewer iteration, not direct agent-to-agent editing. In parallel mode, assign each accepted finding to the owner of its files; if findings cross task boundaries, stop and replan integration before editing. Permit at most two correction rounds per task and integrated result. Stop earlier if the same failure persists, there is no progress, or the change needs a product decision. Planner may propose a new plan; it cannot approve it.

If Reviewer identifies a plausible security risk, do not close the task on that finding alone. Delegate the scoped risk and affected code to `security-reviewer` for independent analysis, even if the specialist was not selected during planning. The security agent returns evidence and scope; the coordinator triages it, the approved Developer fixes accepted in-scope findings, the specialist rechecks security, and Reviewer verifies integration. Scope or policy changes require a revised approved plan.

## 4. Verify and close

After the final edits, run the profile's applicable checks on the integrated result. Repeat checks affected by later changes. Compare every acceptance criterion with evidence and update tracking only according to project policy and the approved plan. Report completed and pending tasks, review findings and decisions, commands and results, Git state, and limitations. Do not claim completion while accepted findings or required checks remain unresolved. Do not commit, push, deploy, or publish unless the user authorized that action.

## Failure and resume

Preserve partial results. On interruption, recover the approved plan version, task assignments, base revisions, completed checks, review state, and outstanding work from conversation and repository evidence. If approval or task boundaries cannot be established, return to planning. If the client lacks parallel agents or isolated workspaces, fall back to serial execution and tell the user which approved work remains.

An approval exists only in the conversation where the user explicitly approved that plan version. Do not treat `project-profile.md`, roadmap status, agent output, or a prior task's approval as authorization for new implementation. If the session context no longer proves the approval, present the current plan again and wait. Never persist approval by writing a token or flag into project files unless the project has an explicit, user-approved approval-record process.
