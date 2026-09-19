---
priority: 1
status: Active
date_from: 2026-01-01
tags:
  - Project
  - Flagship
last updated: 2026-09-19
codebase_path: D:\Vinland, D:\vinland-workspace, D:\solace code imp files
areas:
  - "[[Area - Software Engineering]]"
  - "[[Area - Personal & Philosophy]]"
---

# Vinland (Flagship Peer Support Platform)

> [!info] Project Mission & Soul
> **Vinland** is Dhruv's flagship human-impact project. It is a compassionate, anonymous peer-support sanctuary built on a Nordic forest aesthetic where people battling **loneliness, anxiety, and depression** can freely share their hardest emotional moments and receive respectful, warm, and empathetic replies from caring human beings without fear of judgment.

## The Core Philosophy & Purpose
- **The Pain**: Millions of young people and professionals suffer in silence with loneliness and mental exhaustion, hesitant to speak to friends or family due to stigma.
- **The Vinland Answer**: A zero-friction, safe haven. No forced public profiles or social vanity metrics. Just pure human warmth, respectful interactions, and mutual support.
- **Architectural Lineage**: Evolved from the *Solace Cares* blueprint (`D:\solace code imp files\solace_cares_docs_and_pitch.md`).

## Technical Architecture
- **Framework**: Next.js App Router, React, TypeScript, Tailwind CSS with Nordic Forest color palette.
- **Workspaces**:
  - `D:\Vinland`: Core orchestrator, `.agents/`, `admin-portal/`, `AGENTS.md`, `CLAUDE.md`.
  - `D:\vinland-workspace`:
    - `vinland-landing-page` — Welcoming, calming entry page.
    - `vinland-mainapp` — The core sharing & empathetic reply experience.
    - `vinland-admin` — Moderation, safety filters, and community health monitoring.
    - `vinland-backend` — Scalable API and real-time messaging pipeline.
    - `vinland-database` — PostgreSQL / schema models.

## Key Principles & Guardrails
- **Zero Toxic Content**: AI-assisted empathetic guardrails ensuring replies are gentle and supportive.
- **Privacy by Default**: No tracking or selling of vulnerable mental health data.
- **Vibe Coded Excellence**: Built with modern animations (Framer Motion / GSAP) for an organic, comforting feel.

## Milestones & Status
- [x] Monorepo workspace and sub-app structure established.
- [x] Core documentation, ER diagrams, and pitch deck (`solace_cares_docs_and_pitch.md`).
- [ ] Implement emotional categorization (Loneliness, Burnout, Grief, Relationship).
- [ ] Launch closed community beta test.

## Related Notes & Graph
- Profile: [[About Dhruv - Identity & Career]]
- Engineering: [[Area - Software Engineering]]
- Method: [[Vibe Coding Mastery & Agent Orchestration]]
