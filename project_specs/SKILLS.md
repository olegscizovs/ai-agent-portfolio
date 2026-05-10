# Skills Demonstrated: Local Autonomous AI Agent

## 🎓 Technical Excellence

### 1. Project Planning & Strategy

*   **Sequential Reasoning:** Breaking down complex Markdown specs into actionable multi-stage build plans.
*   **Dependency Strategy:** Identifying optimal libraries and versions via real-time web-lookup before execution.

### 2. Autonomous Learning Loops

*   **Knowledge Persistence:** Implementing a system where the agent reads its own `LEARNINGS.md files like python.md; react.md; rust.md etc. & general.md` to avoid repeating past mistakes. `LEARNING.md files must be separate for each programming language & general.md and stored in "/memory" folder.`
*   **Mentor-Student Integration:** Architecture for ingesting expert feedback (Claude Opus/Gemini) to refine local model performance.

### 3. Cybersecurity & Guardrails

*   **Security Shield (Quarantining):** Isolating untrusted web content in a separate LLM context to prevent indirect prompt injection.
*   **Granular Permission Switches:** Implementation of a safety gate for sensitive system actions (CMD, Bash, Git).
*   **Human-in-the-Loop (HITL):** Designing interactive verification steps for all agentic decisions.

### 4. RAG & Professional Knowledge

*   **Semantic Retrieval:** Using Vector RAG to pull coding standards from historical project audits.
*   **Dynamic Web Crawling:** Utilizing MCP (Model Context Protocol) to bridge local logic with live technical documentation.

### 5. Multi-Modal & Multi-Lingual Engineering

*   **Cross-Language Support:** Automated technical writing and documentation in EN, DE, and RU.
*   **Advanced File Parsing:** Deep comprehension of logic within .py, .rs, .ts, .js, etc. and PDFs.

### 6. Agentic Software Engineering

*   **Workflow Logging:** Creating auditable logs for external review.
*   **Codebase Comprehension:** Mapping and modifying large project structures autonomously.

### 7. **Self-Maintenance & Optimization**
- **Automatic Memory Cleanup:** Logic to monitor `memory/*.md` file sizes.
- **Compaction Triggers:** Automatically summarizing extensive learning files when they exceed 50KB to preserve context window tokens.
- **Model Agnostic Handlers:** Code designed to switch between `qwen3-coder` and `qwen4-coder` via simple config variables.
