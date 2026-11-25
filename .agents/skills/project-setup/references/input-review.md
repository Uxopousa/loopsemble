# User input and document review

## Intake

Explain the two input routes before asking project questions. For chat, gather only the five necessary facts in the example brief: new/existing mode, objective and users, initial scope, limits, and success criteria. Existing repository files may answer some of these; ask only for gaps. For file input, require `project-brief.md` at the target root. If the user placed it in the template, a subdirectory, or another project, identify its actual path and the expected path; offer to move a copy after checking for a destination conflict. Do not silently treat a misplaced file as the active brief. The example inside this skill is a model, not a completed user brief.

Requirements, architecture, and roadmap are useful inputs, but not mandatory files at setup. Accept existing equivalents and links. If absent, record what is undecided and propose creating the relevant document as a later task when the project needs it. Do not invent a backlog, task IDs, architecture, technology, release date, or acceptance policy to fill a template field. A first approved implementation plan can define initial documents or scaffolding.

Alternatively, offer optional document creation during setup using `assets/requirements.example.md`, `assets/architecture.example.md`, and `assets/roadmap.example.md`. Propose `docs/requirements.md`, `docs/architecture.md`, and `docs/roadmap.md` only when there are no canonical equivalents. Show the selected documents and exact destination paths together and obtain the user's choice before creating them; declining does not block setup. Fill only known facts and decisions, marking the rest pending. Preserve existing files and tracking tools; never overwrite or duplicate them. Check the final files are at the agreed paths and that links resolve. Review contradictions and improvements with the user, then record the canonical locations (or declined/pending choice) in the profile. These generated documents belong to the project and must survive template cleanup or pack removal.

## Review supplied material

Read every user-supplied document that the profile will rely on. Verify its location relative to the target root, referenced files and links, current Git state, and consistency with code and manifests when the project exists. Look for conflicting scope statements, requirements that cannot be checked, roadmap items without clear completion criteria or dependencies, architecture that contradicts actual modules, and commands that do not exist. For security context, record actual policies/threat models and identify missing context; do not invent assets, attacker assumptions, compliance needs, or trust boundaries. Distinguish facts observed in the repository, the user's decisions, and proposals.

Return a concise review with: valid inputs, concrete inconsistencies (source and effect), missing blocking decisions, and suggested improvements. Let the user decide product or policy conflicts. Do not edit the source documents merely to make the profile look complete; an explicit request can authorize a later documentation change. If a gap does not block the first task, mark it pending instead of delaying setup.

## Readiness

The profile is ready when the target, purpose, initial scope, limits, and a way to judge the first task are clear; installed agents and skills are discoverable; and no unresolved conflict would direct the next task incorrectly. Roadmap format, full architecture, final technology selection for unrelated work, and parallel task decomposition can wait until a concrete approved task needs them. Report which inputs were provided by chat and which by files.
