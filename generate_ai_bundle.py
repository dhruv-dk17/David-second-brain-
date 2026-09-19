import os, datetime

vault_root = r"D:\second brain"
output_bundle = os.path.join(vault_root, "DAVID_AI_CORE.md")

priority_notes = [
    os.path.join(vault_root, "INDEX.md"),
    os.path.join(vault_root, "HOW_TO_USE_DAVID.md"),
    os.path.join(vault_root, "Areas", "Career", "About Dhruv - Identity & Career.md"),
    os.path.join(vault_root, "Areas", "Career", "Career Pivot - SAP S4HANA MM & MBA Logistics.md"),
    os.path.join(vault_root, "Goals", "Goals - Master Roadmap.md"),
    os.path.join(vault_root, "Goals", "Immigration & Global Mobility - Switzerland.md"),
    os.path.join(vault_root, "Projects", "Active", "Vinland.md"),
    os.path.join(vault_root, "Projects", "Active", "AI Agent - Deniel.md"),
    os.path.join(vault_root, "Projects", "Active", "Bombay Fastfood Order & Billing System.md"),
    os.path.join(vault_root, "Projects", "Incubating", "Cold Coffee & Tiramisu Side Venture.md"),
    os.path.join(vault_root, "Areas", "Software Engineering", "Vibe Coding Mastery & Agent Orchestration.md"),
    os.path.join(vault_root, "Techniques", "Ponytail - Pragmatic Minimal Engineering.md"),
    os.path.join(vault_root, "Techniques", "SAP S4HANA MM Procure to Pay Cycle.md"),
    os.path.join(vault_root, "UPDATE_PROTOCOL.md")
]

bundle = []
bundle.append(f"# DAVID — Master AI Context Bundle for Dhruv")
bundle.append(f"> Auto-generated snapshot: {datetime.date.today().isoformat()}")
bundle.append(f"> Use this single file as System Instructions or Knowledge Upload in Claude.ai, ChatGPT, Gemini Web, Perplexity, or any mobile AI app.\\n")

for p in priority_notes:
    if os.path.exists(p):
        fname = os.path.basename(p)
        bundle.append(f"\\n{'='*60}\\nFILE: {fname}\\n{'='*60}\\n")
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            bundle.append(f.read().strip())

with open(output_bundle, "w", encoding="utf-8") as f:
    f.write("\\n".join(bundle) + "\\n")

print(f"Generated universal web bundle: {output_bundle} (Size: {os.path.getsize(output_bundle)} bytes)")
