# Skill and role routing

Only the root coordinator orchestrates. Each handoff includes the plan version, phase, question, exact working directory, read/write ownership, canonical domain sources, relevant skills by name/path, and expected evidence. Do not send every agent every skill or assume installation means the skill has been read. Use the actual available inventory; surface conflicting guidance before affected work. Agent success reports are inputs to verification, not proof of completion.

| Work or signal                                     | Owner                                               | Guidance to read when relevant                                                       |
| -------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Scope, dependencies, architecture or refactor plan | Planner                                             | Project domain skill, clean-code-architecture; technical skills for affected areas   |
| Implement approved behavior                        | Developer                                           | Project domain skill and applicable technology/conventions                           |
| UI layout, states and interaction                  | Developer and Reviewer                              | frontend-design and accessibility; existing design system first                      |
| Angular code                                       | Developer and Reviewer                              | angular-guidelines only for compatible versions; no unplanned migration              |
| Test design, regression or weak coverage           | Developer or test-specialist                        | testing and relevant runner-specific guidance; test ownership required for writes    |
| Bug, build failure or unexpected result            | Assigned investigator, Developer or test-specialist | systematic-debugging before a fix; scope and role restrictions still apply           |
| Security-sensitive change or review suspicion      | security-reviewer                                   | Security-review workflow, project policy and threat model; read-only findings        |
| Independent review                                 | Reviewer                                            | Domain and affected technical skills; inspect acceptance and test quality separately |

Diagnostics and read-only specialist analysis can happen before plan approval. Corrections, new tests, and documentation writes must remain within approved assignments. A test-specialist does not change production code merely because a test failed. Security remediation belongs to the authorized Developer. Reviewer sends concerns through the coordinator, which assigns them without recursive delegation.

Before implementation, compare requirements, plan, task dependencies and accepted scope. Return inconsistencies for clarification instead of generating a larger backlog. For parallel work, verify ownership covers generated files and checks as well as source. Review the final combined result after integration.

Before closing, the coordinator maps each acceptance criterion to actual evidence on the final revision. Read command exit status and relevant output; report failures, environment limits and checks not run. Lint does not prove build success, a passing unit test does not prove the whole UI works, and a structural skill validator does not prove correct activation. Repeat affected checks after changes; reuse unaffected evidence with its revision identified rather than rerunning everything without reason. Verify the actual diff and untracked files independently of worker summaries.
