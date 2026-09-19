---
name: vault-note-update
description: Update an existing note in David Second Brain in-place while keeping timestamps and graph links consistent.
---

# Vault Note Update

Update existing notes according to `UPDATE_PROTOCOL.md`.

## Protocol
1. **Update In-Place**: Never create a duplicate note. Update the target file directly.
2. **Bump Timestamp**: Change `last updated: YYYY-MM-DD` to the current date.
3. **Preserve Single Source of Truth**: Use ``wikilinks`` instead of duplicating facts.
4. **Report to User**: Output a single line: `Updated `Note Name`: <summary of change>`.
