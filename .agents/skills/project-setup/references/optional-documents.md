# Optional coordination and specialist documents

Offer these only when useful; do not present six mandatory questions or create empty files by default. Reuse canonical equivalents, including external trackers. Adapt proposed destinations to repository conventions and obtain the user's selection and exact paths before writing. The user may defer or decline every model. Read existing sources before filling a document; mark unknowns pending, report contradictions and improvements, and verify the agreed locations and links after creation. Never overwrite existing files.

| Model                                     | Offer when                                                                       | Suggested destination            |
| ----------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------- |
| `assets/work-plan.example.md`             | Multi-step or parallel work benefits from a durable plan                         | `docs/work/plans/<task>.md`      |
| `assets/execution-state.example.md`       | Long work or session handoffs need a current snapshot not covered by tracking    | `docs/work/state.md`             |
| `assets/review-report.example.md`         | Findings and revalidation need a durable record                                  | `docs/work/reviews/<task>.md`    |
| `assets/threat-model.example.md`          | Trust boundaries, sensitive data, or external integrations need security context | `docs/security/threat-model.md`  |
| `assets/test-strategy.example.md`         | Several test levels or substantial verification risk need shared guidance        | `docs/testing/strategy.md`       |
| `assets/architecture-decision.example.md` | A consequential technical decision needs its rationale preserved                 | `docs/decisions/<id>-<title>.md` |

These paths are suggestions, not prescribed project structure. Record chosen canonical paths and owners in `project-profile.md`. Project documents survive source-template cleanup and pack removal; apply their visibility according to the user's document policy, not the installed pack's ownership hashes.

During setup, create only the requested initial drafts from known project facts. During feature work, creating or maintaining these files must be included in the approved task scope. Planner and Reviewer return content in chat; the coordinator persists plans, state snapshots, and reports when authorized. Specialists provide analysis; document authoring requiring edits must be assigned to an authorized writer. This preserves read-only agent boundaries.

Plan and state files do not prove authorization. Keep the existing approval and resume rules. Avoid a second backlog: the roadmap or tracker owns progress; execution state links to tasks and records temporary handoff evidence. ADRs preserve rationale and link to the canonical architecture rather than replacing it. Reports record findings and their resolution rather than declaring new scope.
