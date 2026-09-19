---
priority: 1
status: Active
date_from: 2026-02-01
tags:
  - Project
  - AI
last updated: 2026-09-19
codebase_path: D:\ai agent
areas:
  - "[[Area - AI & Autonomous Agents]]"
---

# AI Agent — Deniel

> [!info] Project Objective
> **Deniel** is Dhruv's custom autonomous AI agent engine that runs locally on his laptop. Powered by local LLMs via Ollama, Deniel executes multi-step tasks, diagnoses code, self-repairs errors, and runs benchmark evaluations in a secure sandbox.

## System Components & Architecture
- **Engine Core**: Python execution loops, Ollama integration (`http://127.0.0.1:11434`), interactive frontend dashboard.
- **Directory**: `D:\ai agent`
- **Launcher**: `start_deniel.bat` (automated checks for Ollama daemon, launches local models).
- **Self-Repair Engine**: `test_repair.py` automatically catches syntax errors and unit test failures, looping until resolved.
- **Benchmark Eval**: `benchmark_agent_eval.py` tests agent reasoning and tool usage efficiency.
- **Sandbox Environment**: `sandbox/` isolates tool modifications from host system.

## Relationship with David (Obsidian Second Brain)
- Deniel can read from David's knowledge vault (`INDEX.md`, `Projects/`, `Areas/`) to receive deep personalized context on Dhruv's preferences, project trees, and coding standards!

## Current Milestones
- [x] One-click launcher (`start_deniel.bat`) with Ollama health checks.
- [x] Self-repair loop and eval harness.
- [ ] Connect Deniel to David's [[INDEX]] for instantaneous vault memory recall.
- [ ] Multi-agent coordination with Antigravity and Claude Code.

## Related Notes & Graph
- Domain: [[Area - AI & Autonomous Agents]]
- Methodology: [[Autonomous Agent Self-Repair Loop]]
