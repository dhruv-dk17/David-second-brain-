# AGENTS.md — Universal AI Agent Protocol

> **System Name**: David (AI Second Brain)  
> **Workspace**: `D:\second brain`  
> **Index**: `INDEX.md`  
> **Update Rules**: `UPDATE_PROTOCOL.md`

All autonomous agents (Google Antigravity, Cursor, Windsurf, OpenAI Codex, Ollama, LangChain, CrewAI) interacting with this vault MUST adhere to this specification.

## Core Rules
1. **Context Discovery**: Begin by reading `INDEX.md` to identify the correct domain note (`Projects/`, `Areas/`, `Goals/`, `Thoughts/`, `Journal/`).
2. **Atomic Updates**: When writing or updating knowledge, apply `UPDATE_PROTOCOL.md`:
   - Never duplicate facts across multiple notes.
   - Use ```wikilinks``` for relationships.
   - Update frontmatter `last updated` timestamp.
3. **Obsidian Compatibility**:
   - Respect frontmatter definitions in `.obsidian/types.json`.
   - Preserve `.base` query views and markdown callout blocks (`> [!info]`, `> [!tip]`, etc.).
