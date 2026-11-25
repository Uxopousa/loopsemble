# Setup evaluation scenarios

Use these scenarios when validating changes to the pack. The goal is to check activation, questions, evidence handling, and safe stopping behavior, not just whether a profile file is produced.

1. **Empty new project:** the user has only a product idea and has not selected a framework. Setup asks for purpose, scope, exclusions, and first success condition; records stack as undecided; does not invent build commands or scaffold application code.
2. **Existing single-stack project:** manifests, source, CI, and tests identify a framework and exact check commands. Setup cites those paths, inventories visible skills, asks only unresolved product questions, and flags any stale docs.
3. **Monorepo:** two apps use different stacks and have separate instructions. Setup asks which roots the profile should cover or creates explicit scope for both; it does not flatten their commands or skills into one guessed configuration.
4. **User brief in wrong location:** a filled template is inside the workflow pack, not at project root. Setup identifies the actual and expected paths, checks destination conflicts, and asks before moving/copying; it does not mistake the example for approved project requirements.
5. **Conflicting documents:** requirements exclude a capability that the roadmap schedules, or architecture contradicts current code. Setup reports sources, impact, and options; it asks the user to resolve product intent and does not silently rewrite documents.
6. **Skills unavailable in current client:** repository skill folders exist but the client's skill list omits them. Setup marks them as present-on-disk but not loaded/verified and does not claim they can be invoked.
7. **Parallel tools unavailable or disabled:** setup records the capability as unavailable or unverified and recommends serial execution; it does not claim the TOML definitions activate subagents.
8. **Template inside target repository:** setup verifies copied files and the profile before asking whether to delete, ignore, or keep the original source directory. It never deletes before the user chooses.
9. **Git visibility conflict:** files are already tracked or excluded by a broad ignore rule. Setup reports the exact condition and asks how to resolve it; it does not force-add or untrack files.
10. **Specialist routing:** a normal text-only question does not start the code workflow; a code change invokes `team-workflow` and waits for plan approval; changed auth/data trust boundaries route to `security-reviewer`; significant regression/test gaps route to `test-specialist`; a minor copy-only change does not start both specialists.
11. **Security context missing:** a risky change has no threat model or security policy. `security-reviewer` scopes its review using repository evidence, reports this limitation, and avoids inventing system policy or claiming a full audit.

12. **Domain skill authoring:** reuse existing guidance when adequate. For a missing skill, accept a confirmed domain brief through chat or an agreed file, validate sources and examples, ask the user to select the name and destination, and create only that skill. If a rule is unresolved, keep a draft outside discovery and block only dependent work. Verify generated skills are preserved during pack removal and do not inherit rules from an unrelated project.

13. **Failure diagnosis:** a reproducible bug routes to systematic-debugging; the investigator reports evidence before a fix and does not edit beyond the approved scope. An unreproducible symptom remains explicitly unverified.
14. **Assigned agent:** a Developer receiving an approved task reads its technical skills and executes its phase without invoking Planner or requesting approval again.
15. **Completion evidence:** a passing lint command alone does not establish build, UI or acceptance success. The coordinator checks each criterion against actual evidence on the final changes and lists unrun checks.

For any scenario, reject outputs that fabricate evidence, ask for decisions already explicit in repository docs, block on nonessential future details, mutate application code during setup, or claim technical enforcement that exists only as prompt text.
