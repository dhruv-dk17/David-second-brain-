# 🧠 David — AI-Augmented Second Brain

<div align="center">

![Obsidian 1.8+](https://img.shields.io/badge/Obsidian-1.8%2B%20Bases-7C3AED?logo=obsidian&logoColor=white)
![Methodology](https://img.shields.io/badge/Methodology-CODE%20%7C%20PARA-10B981)
![AI Ready](https://img.shields.io/badge/AI%20Agents-Claude%20%7C%20Antigravity%20%7C%20Cursor%20%7C%20Ollama-3B82F6)
![Graph Integrity](https://img.shields.io/badge/Graph-100%25%20Resolved%20Links-F59E0B)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

**A self-evolving personal knowledge graph and autonomous AI memory engine.**  
Built with [Obsidian](https://obsidian.md/), Tiago Forte's **CODE / PARA** methodology, and modern **Multi-Agent Memory Protocols**.

[Quickstart](#-quickstart) • [How It Works](#-how-it-works) • [Vault Structure](#-vault-structure) • [Using With AI](#-using-david-with-any-ai) • [Creator](#-built-by)

</div>

---

## 🌟 What is "David"?

Most note apps and "second brains" end up as **passive digital graveyards** — places where ideas go to be forgotten.

**David is different.** David is an **active digital collaborator**:
1. **It remembers everything you do**: All your projects, thoughts, daily logs, career milestones, and study materials are interconnected in a clean knowledge graph.
2. **It talks to your AI tools**: Whether you use **Claude Code**, **Google Antigravity**, **Cursor**, **ChatGPT**, or **Local LLMs (Ollama)**, David serves as their permanent external memory so they never forget who you are or what you are building.
3. **It updates itself in real-time**: Whenever you make a decision, solve a bug, or hit a goal, the AI updates the relevant notes in place without duplicating data.
4. **It works everywhere**: Use it visually on your desktop in Obsidian, via terminal in your IDE, or on the web and phone through one-click AI snapshots.

> *"Your second brain shouldn't just store what you know. It should help you build what's next."*

---

## ⚡ The 4 Core Pillars

```
┌────────────────────────────────────────────────────────┐
│                        DAVID                           │
├───────────────────┬────────────────────────────────────┤
│ 📂 1. PARA System │ Structured folders for actionability│
│ 🔗 2. Graph Hub   │ Wikilinks connecting every idea    │
│ 🤖 3. Agent Rules │ INDEX routing & in-place updates   │
│ 🌐 4. Portability │ 1-click snapshot for Web & Mobile  │
└───────────────────┴────────────────────────────────────┘
```

### 1. 📂 Structured Knowledge Store (PARA + CODE)
Everything is sorted by **actionability** based on Tiago Forte's PARA system:
- **Projects**: Active initiatives with deadlines and deliverables (`Vinland`, `Bombay Fastfood`, `Deniel`).
- **Areas**: Long-term spheres of activity (`Career`, `Software Engineering`, `Finances`, `Health`).
- **Resources**: Reference articles, documentation, and technical cheat sheets.
- **Archive**: Completed or inactive projects kept for historical reference.
- **Plus**: Time logs (`Journal/`), unwritten sparks (`Thoughts/`), life milestones (`Goals/`), and contacts (`People/`).

### 2. 🔗 Plain-Text Knowledge Graph
Every single note connects to related concepts using simple `[[wikilinks]]`. In Obsidian's **Graph View**, David forms a clean, beautiful galaxy centered around `INDEX.md`, with zero broken or detached links.

### 3. 🤖 Autonomous Agent Memory Engine
David comes pre-configured with agent control files:
- **`INDEX.md`**: The Master Routing Hub. When an AI reads David, it checks `INDEX.md` first to know *exactly* which file to open, saving tokens and eliminating hallucinations.
- **`UPDATE_PROTOCOL.md`**: Strict operational rules telling AI agents how to update notes in place, bump timestamps, and maintain a single source of truth.
- **`CLAUDE.md` / `AGENTS.md` / `GEMINI.md`**: Instant system prompt configurations for Claude Code, Cursor, Windsurf, and Google Antigravity.

### 4. 🌐 Universal Web & Mobile AI Snapshot
Because web AIs (ChatGPT, Claude.ai) cannot browse your local computer drive, David includes a built-in generator:
- Run `python generate_ai_bundle.py`
- It instantly bundles your core identity, active projects, and roadmap into a single file: **`DAVID_AI_CORE.md`**.
- Upload it to Claude Projects or a Custom GPT, and your second brain works right on your phone!

---

## 📂 Vault Structure

```text
David-second-brain/
├── INDEX.md                     # Master Routing Table & Graph Center
├── HOW_TO_USE_DAVID.md          # Everyday user handbook
├── UPDATE_PROTOCOL.md           # Rules for AI in-place updates
├── CLAUDE.md                    # Instructions for Claude Code & Cowork
├── AGENTS.md                    # Universal AI agent protocol
├── GEMINI.md                    # Google Antigravity configuration
├── DAVID_AI_CORE.md             # Single-file snapshot for Web & Mobile AI
├── generate_ai_bundle.py        # 1-click bundle generator
│
├── Projects/                    # Active codebases & real-world software
│   ├── Active/                  # Vinland, Deniel, Bombay Fastfood, Telecode...
│   ├── Incubating/              # Cold Coffee & Tiramisu Cake side hustle...
│   ├── Academic/                # SASCMA College BCA coursework, C++, Cloud, SPSS...
│   └── Client & Freelance/      # Dental Store, Garage Web, Subham Portfolio...
│
├── Areas/                       # Long-term knowledge & responsibilities
│   ├── Career/                  # About Dhruv, SAP S/4HANA MM & MBA Logistics pivot
│   ├── Software Engineering/    # Vibe Coding, Agent Orchestration, Architecture
│   ├── AI & Agents/             # Local LLMs, Ollama, autonomous loops, Deniel
│   ├── Business/                # Ascendra Hub, F&B side hustles, legal agreements
│   ├── Personal Finances/       # Cash flow, Sunday earnings, college funding
│   └── Health & Fitness/        # Focus protection, mental wellness, physical training
│
├── Goals/                       # Multi-year roadmap & milestones
│   ├── Goals - Master Roadmap.md
│   └── Immigration & Global Mobility - Switzerland.md
│
├── Thoughts/                    # Unwritten ideas, sparks, and future concepts
│   └── Thoughts - Master Incubator.md
│
├── Techniques/                  # Distilled playbooks & mental models
│   ├── Vibe Coding Protocol
│   ├── Ponytail Minimal Engineering
│   ├── Gstack Rapid Delivery & Taste
│   └── SAP S/4HANA MM Procure to Pay Cycle
│
├── Journal/                     # Time-based capture
│   ├── Daily/                   # Day-to-day execution logs and brain dumps
│   ├── Weekly/                  # High-level weekly reviews
│   └── Meetings/                # Meeting notes & action items
│
├── _Templates/                  # 10 strongly-typed YAML templates
├── .obsidian/                   # Graph physics, color themes, bases, properties
└── *.base                       # 6 Native Obsidian Bases (interactive tables)
```

---

## 🚀 Quickstart

### 1. Clone the Vault
```bash
git clone https://github.com/dhruv-dk17/David-second-brain-.git "D:\second brain"
```

### 2. Open in Obsidian
1. Download and install [Obsidian](https://obsidian.md/) (v1.8+ recommended).
2. Click **"Open folder as vault"**.
3. Select your cloned folder (`D:\second brain`).
4. Press `Ctrl + G` (or `Cmd + G` on Mac) to open **Graph View** and explore the interconnected constellation!

---

## 🤖 Using David With Any AI

### Option A: Local AI Tools (Antigravity, Claude Code, Cursor)
1. Open the vault folder in your editor or terminal.
2. The AI automatically discovers `INDEX.md` and `UPDATE_PROTOCOL.md`.
3. Simply talk to it:
   > *"David, what's my current progress on Vinland?"*  
   > *"David, I have an idea for Cold Coffee packaging, add it."*  
   > *"David, update the Bombay Fastfood note with today's changes."*

### Option B: Web & Mobile AIs (Claude.ai, ChatGPT, Gemini)
1. Run the bundle generator:
   ```bash
   python generate_ai_bundle.py
   ```
2. Open **Claude.ai** (create a Project called "David") or **ChatGPT** (create a Custom GPT).
3. Upload the generated **`DAVID_AI_CORE.md`** file into project knowledge.
4. Now you have your entire second brain on your phone wherever you go!

---

## 🛠️ The Vibe Coding Philosophy

This entire vault was engineered using **Vibe Coding**:

> **"Be the Chief Conductor and Architect. Let autonomous AI agents handle manual boilerplate syntax while you stay in charge of vision, empathy, and enterprise impact."**

By combining high-level system design with autonomous coding agents, one person can design, build, and maintain complex ecosystems — from empathetic peer-support apps like **Vinland** to restaurant POS automation and enterprise **SAP S/4HANA** workflows.

---

## 👤 Built By

**Dhruv**  
*Student, Product Architect & Future SAP S/4HANA Consultant*  
- 🌐 **Portfolio**: [dk17-portfolio.vercel.app](https://dk17-portfolio.vercel.app/)
- 💻 **GitHub**: [@dhruv-dk17](https://github.com/dhruv-dk17)
- 👔 **LinkedIn**: [linkedin.com/in/dhruv-dk17](https://www.linkedin.com/in/dhruv-dk17)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to fork, adapt, and use this vault structure to build your own AI-augmented second brain!
