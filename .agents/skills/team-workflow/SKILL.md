---
name: team-workflow
description: Coordinates implementation, bug fixes, refactors, and other code changes in a configured repository through planning, human approval, specialist agents, verification, and review. The root coordinator uses this for implementation requests when project-profile.md is present; assigned subagents execute their phase without restarting this workflow; do not use for questions, explanations, or review-only requests unless asked.
when_to_use: 'Use automatically for implementation work in a repository configured with this workflow, or when the user requests $team-workflow. Planning can proceed autonomously, but wait for explicit approval before code changes.'
metadata:
  version: 0.1.0
---

# Team workflow

Read `project-profile.md` at the repository root, existing `AGENTS.md` if present, and `references/workflow.md`. The reference defines the phases, parallel eligibility, handoffs, correction loop, and stopping conditions. If the profile is missing or still contains placeholders, invoke `$project-setup` first after the user requests project setup, or ask for the missing facts before implementation. Check that its technology and skill inventory still match this environment and repository; surface unresolved conflicts before planning affected work. Repository instructions and the user's current decisions take precedence over this template.

Only the root coordinator starts this workflow. Assigned subagents follow their existing task and return results without recursively invoking it.

Start with the user's task. Inspect the repository and preserve existing changes. Ask Planner for a plan with acceptance criteria, dependencies, ownership, mode (serial or parallel), integration, and checks. Present the specific plan for human approval. The user's request to implement a feature authorizes planning, not implementation before approval.

Delegate only when the client supports the named agents. Use the profile's relevant skills for each subtask. If agent delegation is unavailable, explain the limitation and use distinct conversations for planning, implementation, and review when possible. Do not describe a self-review as independent.

Use `references/skill-routing.md` to select skills and assign their use explicitly in handoffs. Diagnosis uses systematic-debugging; testing uses the selected testing guidance; security uses the scoped specialist workflow. Apply the same routing during review and correction, without restarting orchestration. Validate the final acceptance-to-evidence mapping before declaring completion.

In parallel mode, each Developer receives an explicit task, owned files or an isolated worktree, dependencies, and a merge/integration point. Wait for all required results before integrated review. Do not run dependent edits concurrently or let workers overwrite one another. Return changed scope or unresolved conflicts to Planner and the human as specified in `references/workflow.md`.
