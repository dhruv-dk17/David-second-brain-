---
priority: 2
status: Active
date_from: 2026-04-01
tags:
  - Project
last updated: 2026-09-19
codebase_path: D:\job finder
areas:
  - "[[Area - Software Engineering]]"
---

# Job Finder

> [!info] Project Objective
> Unified Job Finder and Application Tracker system combining an Express TypeScript backend with a dedicated Chrome browser extension to streamline opportunity discovery and status tracking.

## Architecture & Components

- **Backend**: Node.js, Express, TypeScript (`src/server.ts`), compiled via `tsc` to `dist/server.js`.
- **Browser Extension**: Packaged Chrome extension (`extension/`, `extension.zip`) for in-browser job scraping and 1-click tracking.
- **Design Spec**: Outlined in `design.md`.
- **Location**: `D:\job finder`

## Deliverables
- [x] Extension manifest and background capture scripts.
- [x] Express API server for job persistence and aggregation.
- [ ] Advanced filter engine and duplicate vacancy detection.
- [ ] Automated resume tailoring integration.

## Related Notes & Graph
- Area: [[Area - Software Engineering]]
