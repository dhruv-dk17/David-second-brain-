---
priority: 1
status: Active
tags:
  - Project
  - Production
  - RealWorld
last updated: 2026-09-19
github: https://github.com/dhruv-dk17/Bombay-fastfood-app
areas:
  - "[[Area - Software Engineering]]"
  - "[[About Dhruv - Identity & Career]]"
---

# Bombay Fastfood Order & Billing System

> [!info] Project Overview
> A production-grade, fullstack restaurant management web application built by Dhruv for **Bombay Fastfood Shop**. It automates front-of-house order taking, kitchen prep queue routing, and customer receipt billing.

## Technical Architecture (from GitHub `Bombay-fastfood-app`)
- **Repository**: [github.com/dhruv-dk17/Bombay-fastfood-app](https://github.com/dhruv-dk17/Bombay-fastfood-app)
- **Frontend**: Vite + React, TypeScript, Tailwind CSS, Lucide React icons, shadcn/ui components (`client/src/components/ui/`).
- **Backend & API**: Node.js, Express, tRPC (`@trpc/server`) for end-to-end type-safe client-server communication.
- **Database & ORM**: PostgreSQL with **Drizzle ORM** (`drizzle/schema.ts`, database migrations).
- **Core Modules**:
  - `client/src/pages/Home.tsx` — Fast POS menu catalog and order taking.
  - `client/src/pages/ReceiptPage.tsx` — Instant itemized invoice rendering and customer receipt printing.
  - `server/routers.ts` & `server/storage.ts` — Order lifecycle, inventory subtotals, and transaction persistence.
  - `client/src/components/AIChatBox.tsx` — AI assistant integration for quick operational queries.

## Real-World Operational Context
- Dhruv operates as cashier on Sundays (500 INR/day).
- Replaced error-prone handwritten paper tokens with a real-time digital kitchen order ticket flow and instant billing printout.

## Next Enhancements
- [ ] Implement daily sales summary reporting (Z-report) for cash reconciliation.
- [ ] Add UPI QR code generation directly onto printed customer receipts.

## Related Notes
- Profile: [[About Dhruv - Identity & Career]]
- Engineering: [[Area - Software Engineering]]
