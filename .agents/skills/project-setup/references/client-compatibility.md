# Client compatibility boundary

This pack targets Codex CLI and the Codex editor experience that discovers repository `.agents/skills/` and `.codex/agents/`. At setup, verify actual discovery in the active client instead of inferring it from a version number. If skills or custom agents are not discovered, explain which files were found and which capabilities are unavailable. Offer the documented manual fallback only when the user wants to proceed.

Do not claim cross-client portability. Other clients may support the Agent Skills folder format but use different skill directories, custom-agent definitions, invocation syntax, permissions, and delegation controls. Porting requires a separate adapter and validation for that client; never copy Codex TOMLs into a different client's configuration directory by guesswork.

For Codex, `.agents/skills/` and `.codex/agents/` are repository-scoped artifacts. User-level skill locations, plugin packages, and API hosted capability directories are separate distribution mechanisms. This installer copies project-scoped files; it does not install a user-level plugin or configure an Agents API session.
