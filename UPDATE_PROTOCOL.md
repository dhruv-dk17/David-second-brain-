# David: Knowledge Vault Update Protocol

> **Core Philosophy**: David is not a static repository or a passive filing cabinet. David is a living, persistent memory graph that evolves automatically with every conversation, decision, and breakthrough.

---

## 1. Golden Rules of Maintenance

1. **Single Source of Truth**:
   - Never record the same fact in two different files.
   - If a project depends on an architectural decision documented in an Area or Technique, link to it via ```WikiLink``` rather than copy-pasting the text.

2. **In-Place Updates**:
   - Whenever an update occurs (e.g., a project milestone is met, a tech stack shifts, a goal is adjusted, a habit is logged), edit the target file directly in place.
   - Always update the `last updated: YYYY-MM-DD` property in the note's YAML frontmatter.

3. **Graph Integrity & Wikilinks**:
   - Always use ```Note Name``` (without `.md`) for internal cross-references.
   - Never use standard markdown relative paths `[text](../folder/file.md)` for internal links, because Obsidian and graph visualizers rely exclusively on ```wikilinks``` to compute graph edges.

4. **Synchronize with INDEX.md**:
   - Whenever a new note is created, immediately register it in [[INDEX]] under the appropriate section and routing table.
   - Ensure [[INDEX]] links to every active note in the system so that Obsidian's Graph View displays a clean, unified galaxy centered on [[INDEX]].

5. **One-Line Communication**:
   - When an AI agent modifies or creates a note in David, output exactly one concise line to the user stating what was updated.
   - *Example*: `Updated [[Vinland]]: Marked backend auth milestone complete and updated last updated date.`

---

## 2. When to Create vs. When to Update

| Scenario | Action | Destination |
| :--- | :--- | :--- |
| Quick thought, raw idea, spontaneous spark | Create new Thought or append to Daily Log | `Thoughts/Ideas/` or `Journal/Daily/` |
| New software initiative or active repository | Create new Project note from template | `Projects/Active/` |
| Progress made on existing codebase or task | Update existing Project note in-place | `Projects/<Note>.md` |
| Distilled insight, repeatable pattern, or mental model | Create Technique note | `Techniques/` |
| Meeting notes, conversation summary | Create Meeting note | `Journal/Meetings/` |
| New contact, collaborator, or client | Create Person note | `People/` |
| External article, documentation, or tutorial | Create Resource note | `Resources/<Subfolder>/` |
| Milestone achieved or project completed | Change status to `Completed` or move to Archive | `Archive/Projects/` |

---

## 3. Frontmatter & Schema Standards

Every note in David must begin with a YAML frontmatter block containing at minimum:
```yaml
---
tags:
  - <Type>
last updated: YYYY-MM-DD
---
```
Ensure all property names match `types.json` for seamless filtering in Obsidian Bases (`Projects.base`, `Knowledge.base`, etc.).
