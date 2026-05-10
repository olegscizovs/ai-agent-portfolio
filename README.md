# Local Learnable AI-Agent (LLAA) 🤖

A private, self-improving, local-first AI Engineering Agent. 

LLAA is designed to plan, execute, and learn autonomously. Built on a "Mentor-Student" architecture, it absorbs professional standards and feedback, storing them in a permanent local memory to continuously bridge the gap between local models and top-tier LLMs.

![Terminal UI Dashboard Concept](https://img.shields.io/badge/UI-Terminal_Rich-blue?style=for-the-badge) ![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python) ![Ollama](https://img.shields.io/badge/Local_LLM-Ollama-white?style=for-the-badge)

## ✨ Core Features

*   🧠 **Self-Improving Memory System:** Automatically parses expert feedback and appends it to dedicated `LEARNINGS.md` files (`python.md`, `react.md`, `general.md`). 
*   🔄 **Auto-Compaction:** Monitors memory file sizes. If a file exceeds 50KB, LLAA automatically uses a local LLM to summarize and compress the knowledge, saving context window tokens while preserving critical rules.
*   🛡️ **Safety First (Human-in-the-Loop):** A strict "Safety Gate" intercepts all terminal, git, and pip commands, requiring a `Y/N` user approval before execution.
*   🦠 **Security Shield:** Quarantines untrusted web data by passing it through a zero-privilege LLM context to extract only safe, relevant technical information.
*   🖥️ **Beautiful Terminal UI:** A live-updating, high-contrast dark mode dashboard built with `Rich`, displaying reasoning loops, memory updates, and system stats (CPU/RAM).
*   ⚡ **Hardware Optimized (Intel iGPU):** Implements `OpenVINO` via OpenCL to utilize older Intel integrated graphics (like the HD 620) for embedding tasks, while keeping the main LLM inference on the CPU.

---

## 🛠️ Prerequisites

Before running the agent, ensure you have the following installed on your system (Linux recommended):

1. **Python 3.10+**
2. **Ollama:** [Install Ollama](https://ollama.com/) to run the local models.
3. **Local LLM:** Pull the required model via Ollama. By default, the config looks for `qwen3.5-big`.
   ```bash
   ollama run qwen3.5:9b
   # (Ensure it is mapped/renamed to match the config, or update core/config.py)
   ```
4. **(Optional) Intel OpenCL Drivers:** If you are running on an Intel iGPU and want OpenVINO hardware acceleration:
   ```bash
   sudo apt install intel-opencl-icd
   ```

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:olegscizovs/ai-agent-portfolio.git
   cd ai-agent-portfolio
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Usage & Recommended Commands

### 1. Verify Hardware Acceleration
Check if your system detects the CPU and OpenVINO/iGPU correctly:
```bash
python core/check_gpu.py
```
*This will print out your available inference backends and recommend the best workload split.*

### 2. Launch the Agent Dashboard
Start the main ReAct loop and launch the Terminal UI:
```bash
python main.py
```
*You will immediately see the agent begin its initialization, reasoning phases, and simulated safety checks right in your terminal.*

---

## 📂 Project Structure

```text
ai-agent-portfolio/
├── core/
│   ├── check_gpu.py       # Hardware & OpenVINO diagnostics
│   ├── cleanup.py         # Memory auto-compaction logic
│   ├── config.py          # Global settings (Model name, constraints)
│   ├── memory_manager.py  # Knowledge absorption & backup system
│   ├── safety.py          # Human-in-the-loop (Y/N) permission gate
│   └── shield.py          # Zero-privilege web data sanitization
├── memory/
│   ├── backups/           # Timestamped backups of learning files
│   └── *.md               # Language-specific persistent learnings
├── project_specs/         # Initial architectural goals and skills
├── main.py                # Core ReAct loop and Rich TUI implementation
└── requirements.txt       # Dependencies (OpenVINO, Langchain, Rich, etc.)
```

## 🤝 Architecture Notes
This project was built using a dual-agent generation process:
- **Generation:** Gemini 3.1 Pro (High) constructed the core logic and Rich-based UI.
- **Audit:** Claude Opus 4.6 served as the Senior Architect to audit the code for security and strict adherence to the project specifications.
