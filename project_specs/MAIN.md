# Local Learnable AI-Agent (LLAA)

## 🎯 Project Goal

Build a private, self-improving AI Engineering Agent that plans, executes, and learns. Using a "Mentor-Student" architecture, it absorbs professional standards from Claude Opus 4.6 and Gemini 3 Pro, storing them in a permanent local memory to bridge the gap between local models and top-tier LLMs.

The project will follow a two-tier generation model. Gemini 3.1 Pro (High) will handle initial code construction and UI generation. Claude Opus 4.6 will act as the final Auditor, responsible for refactoring the output to 'Senior Architect' standards and ensuring all security protocols in memory/ are met.

## 🧠 The Learning & Planning Architecture

1.  **Architectural Planning:** Agent generates a `PLAN.md` before writing code.
2.  **Execution:** Step-by-step coding via Qwen 3 Coder (Ollama).
3.  **Audit Loop:** Agent logs its workflow for Claude/Gemini review.
4.  **Knowledge Absorption:** Expert feedback is saved to dedicated programming language`python.md; react.md; rust.md etc...` & `general.md` and ChromaDB.
5.  **Security Shield:** Web data is sanitized in a zero-privilege "Quarantine" model before ingestion.

## 🔧 System Maintenance
- **Auto-Compaction:** The agent must check file sizes after every write operation.
- **Configurable Backend:** The `model_name` must be a variable in `config.py` to allow easy upgrades (e.g., swapping Qwen 3 for 4 in the future).

## 🖥️ User Interface & Handoff Protocol
- **Two-Tier Generation:** 
    - **Gemini 3 Pro (High):** Construct the core logic and a **Rich-based Terminal UI**.
    - **Claude Opus 4.6:** Audit the code and refine the TUI aesthetics to a 'Senior Architect' level.
- **UI Design Requirements:**
    - **Theme:** Minimalist, High-Contrast Dark Mode (Terminal-based).
    - **Layout:** Use a side-panel for "Memory Updates" and a main panel for "Agent Reasoning."
    - **Interactivity:** Real-time progress bars for web scraping and code generation.
    - **Informative:** Display current CPU/RAM usage and the active `num_ctx` limit in the header.


## 🛠 Key Features

*   ✅ **Self-Improving Memory:** Uses RAG and MCP to remember best practices from previous project feedback.
*   ✅ **Web-Intelligence:** Scrapes NPM, StackOverflow, and W3Schools using Brave Search and Crawl4AI.
*   ✅ **Multi-Lingual Docs:** Documentation and technical specs in English, German, and Russian.
*   ✅ **Safe Execution:** "Human-in-the-loop" permission switches for Terminal, Git, and Dependency installation.
*   ✅ **Project Bootstrapping:** Reads `.md` files to initiate full-stack project structures autonomously.