# Test specialist workflow

Use the `test-specialist` agent when the task has meaningful test design or verification work: new behavior, a regression, complex domain rules, risky integrations, flaky tests, or a gap found during review. Read-only analysis may inform planning before approval; writing requires an approved assignment. Small changes with clear existing coverage may use the Developer's focused checks without another agent.

1. Read the profile's test policy, existing test files and configuration, the target behavior, and relevant local testing skills. Identify the observable contract and failure risks before proposing tests.
2. Return a compact test matrix: behavior/risk, test level, scenario, expected result, and exact repository command if known. Prefer focused unit or component tests for isolated behavior; recommend integration or end-to-end tests only when the risk crosses those boundaries.
3. In planning, assign test implementation to a Developer or to `test-specialist` with explicit files, acceptance criteria, and approval. The specialist may implement only assigned test files; it must not rewrite production code to make tests pass. If the plan assigns analysis only, return recommendations without editing.
4. Run only verified project commands within the approved scope. Report actual results and distinguish tests not run, failed tests, environment failures, and preexisting failures. A passing test suite is evidence for covered cases, not proof of correctness.
5. After fixes, rerun affected tests. The independent Reviewer still checks test quality and integrated behavior.

Do not add tests solely to mirror implementation details, duplicate existing coverage, or inflate counts. Do not install testing dependencies or change test configuration without an approved plan.
