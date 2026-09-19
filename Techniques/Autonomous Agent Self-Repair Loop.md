---
tags:
  - Technique
areas:
  - "[[Area - AI & Autonomous Agents]]"
last updated: 2026-09-19
---

# Autonomous Agent Self-Repair Loop

> [!info] Method Summary
> An automated evaluation and correction cycle where an AI agent attempts an execution, captures compiler/runtime errors or test failures, and uses the diagnostics to repair its own output in a tight loop.

## Approach & Step-by-Step Protocol
1. **Generate**: Agent creates implementation or code changes.
2. **Execute**: Sandbox executes unit tests, linter, or compiler.
3. **Capture**: Standard error (`stderr`) and stack traces are captured.
4. **Diagnose & Mutate**: Agent analyzes failure diff and modifies code.
5. **Verify**: Loop continues until green or until a 3-strike threshold escalates to user review.

## Implementations
- Implemented in [[AI Agent - Deniel]] (`test_repair.py`, `benchmark_agent_eval.py`).
