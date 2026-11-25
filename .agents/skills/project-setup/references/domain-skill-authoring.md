# Project domain skill authoring

## Select and collect

During setup, inspect existing domain guidance before proposing another skill. If an adequate skill exists, record and reuse it. Otherwise offer project-domain skill creation as an explicit choice: show the proposed name, purpose, canonical sources, and exact target `.agents/skills/<chosen-name>/`. Check names across repository and environment; do not overwrite an existing skill or apply another project's domain rules to this product. The user may defer creation; report which domain-dependent tasks lack sufficient context.

Use `assets/domain-brief.example.md` as a concise intake checklist, accepting chat or a file at an agreed path. Verify the actual file location and existing destination before moving or copying it. Read referenced requirements first; ask only missing questions. Not every domain needs state transitions, roles, persistence, or backend rules. Mark non-applicable concerns explicitly rather than inventing them.

Summarize confirmed terms, rules and examples back to the user. Separate observed implementation, user decisions, inferred hypotheses, and conflicts. Obtain confirmation of unresolved business decisions and the creation destination. Code behavior alone is not approval of a business rule. A chat-confirmed rule may be cited by its decision context; do not invent a document reference. Offer canonical documentation separately if needed.

## Draft and install

Use `assets/domain-skill.example.md` as the structure. Match the frontmatter name to the selected directory; write a one-line description naming the domain, relevant operations and exclusions, under 1024 characters. Use only confirmed rules, with traceable sources. Keep detailed rules in canonical requirements; the skill tells agents how to find and apply them. Avoid copying framework examples, storage choices or status names from another project.

Add `agents/openai.yaml` with a display name, a short description of 25–64 characters and a default prompt mentioning the exact `$skill-name`. Permit implicit invocation only for the specific domain operations described; discovery is not guaranteed until checked in Codex. The skill must respect assigned roles, plan approval, and read-only restrictions without restarting orchestration.

If information is insufficient, keep a clearly labelled draft in a user-agreed document outside skill discovery directories. Do not install placeholder instructions as an active skill. Unknown rules must not be replaced with plausible defaults. Once the user has selected creation and the readiness checks below pass, install the skill and metadata at the agreed path, verify discovery, and add its purpose and source paths to `project-profile.md`.

## Universal quality checks

Before claiming readiness, verify:

- **Grounding:** every normative business rule has a confirmed source; no invented fields, limits, transitions, permissions, or failure policy.
- **Consistency:** compare rules, examples and existing documents; surface contradictions for user resolution. Implementation drift is reported, not silently treated as the new requirement.
- **Actionability:** the skill states when to use it, what to read, how to apply rules, what to verify and when to ask. It does more than repeat the requirements.
- **Proportion:** narrow scope, no duplicate domain skill or second requirements document, no unrelated framework policy.
- **Structure:** valid YAML frontmatter, matching name/directory, readable metadata, existing references resolved from the correct root, no unfinished template placeholders in active instructions.
- **Role boundaries:** no new implementation authority, recursive delegation, forbidden edits or claims of technical enforcement.
- **Examples:** representative valid, invalid and boundary cases tied to rules; include a multi-rule scenario when relevant and an unrelated request that must not activate the skill. Use “not applicable” only with a concrete explanation.
- **Evaluation honesty:** distinguish structural validation, manual walkthrough of examples, and observed model behavior. Do not claim model-level quality from formatting alone.

Walk through the examples against the confirmed rules and record the outcome and unresolved gaps in the profile or canonical review record. For actual behavior evaluation, use a fresh context and representative prompts without revealing expected answers; compare activation and answers with the source rules and report which cases were not run. Do not claim parity with an established domain skill without that evidence.

## Ownership and maintenance

The generated domain skill belongs to the project, not the original pack inventory. Include its visibility in the user's setup choices. Preserve it during source-template cleanup, pack upgrades and removal. On domain changes, recheck canonical sources, examples and triggers; preserve user-owned changes and obtain decisions for new business rules. Document model-evaluation gaps without blocking unrelated tasks.
