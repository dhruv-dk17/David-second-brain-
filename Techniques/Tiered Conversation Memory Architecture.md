---
tags:
  - Technique
areas:
  - "[[Area - AI & Autonomous Agents]]"
last updated: 2026-09-19
---

# Tiered Conversation Memory Architecture

> [!info] Method Summary
> A 4-tier memory pattern for conversational agents that prevents context-window saturation while guaranteeing persistent, high-precision recall.

## The 4 Tiers
1. **Tier 1: Conversation Buffer** — Live context window (volatile, active turn-by-turn).
2. **Tier 2: Short-Term Session Store** — Cached interaction facts within the current task.
3. **Tier 3: Long-Term Knowledge Graph** — Persistent filesystem markdown files (`Projects/`, `Areas/`, `INDEX.md`).
4. **Tier 4: Entity Memory** — Authoritative profile records (`About Dhruv`, `People/`, `Ascendra Hub`).

## Integration in David
- Managed via `INDEX.md` routing table and `UPDATE_PROTOCOL.md`.
