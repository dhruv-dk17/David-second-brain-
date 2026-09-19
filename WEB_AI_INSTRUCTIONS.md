# 🌐 How to Use "David" Anywhere (Web & Apps)

You can use David across **every AI tool you use**, whether on desktop, web, or mobile. Here is the exact setup for each:

---

## 1. Local AI Apps & IDEs (Zero Setup Needed)
Your local apps interact with the full live folder directly:
- **Google Antigravity**: Already connected via `GEMINI.md` and `.agents/skills/`.
- **Claude Code (CLI)**: Open terminal in `D:\second brain` and type `claude`. It automatically reads `CLAUDE.md`.
- **Claude Desktop (Cowork Mode)**: Click "Choose Folder" -> select `D:\second brain`.
- **Cursor / Windsurf / VS Code**: Open `D:\second brain` as a workspace. It reads `AGENTS.md`.

---

## 2. Web AIs (Claude.ai, ChatGPT, Gemini Web, Perplexity)
Web AIs cannot browse your local `D:\` drive directly, so we use the **Universal Bundle** pattern:

### Step 1: Generate / Refresh the Bundle
Run the included one-click script whenever you want to update your web snapshot:
```powershell
python "D:\second brain\generate_ai_bundle.py"
```
This generates **`DAVID_AI_CORE.md`** inside your vault (a clean, compressed snapshot of your identity, projects, index, and roadmap).

### Step 2: Use in Web Platforms
- **Claude.ai (Recommended)**:
  1. Create a **Project** in Claude called **"David (Second Brain)"**.
  2. Upload `DAVID_AI_CORE.md` into Project Knowledge.
  3. In Project Instructions, paste:
     > *"You are David, my AI Second Brain. You have full context on my life, projects, and goals from the attached knowledge file. Follow UPDATE_PROTOCOL rules."*
  4. Now every chat inside this project knows everything about you!
- **ChatGPT (GPT-4o / Projects / Custom GPTs)**:
  1. Create a **Custom GPT** or **Project** called **David**.
  2. Upload `DAVID_AI_CORE.md` as Knowledge.
  3. In Instructions, tell it to use the knowledge file as your personal context.
- **Gemini Web / Gems**:
  1. Create a custom **Gem** called **David**.
  2. Copy-paste the text of `DAVID_AI_CORE.md` into the Gem instructions or attach the document.
- **Mobile Apps (Claude / ChatGPT / Perplexity on Phone)**:
  - Simply open the "David" Project / Custom GPT you set up on the web — it is immediately available on your iPhone/Android phone!

---

## 3. Two-Way Sync Back to Obsidian
When you have a long chat or make new decisions on web/mobile AI, simply copy the takeaways and paste them into today's daily log in `Journal/Daily/` or tell Antigravity: *"Add this to David"*. David will update the graph notes automatically!
