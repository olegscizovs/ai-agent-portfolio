## 🧪 General Testability & Code Quality
- **The "Pure Function" Rule:** Logic-heavy functions must be pure. They should not rely on global variables or hidden states.
- **SOLID Principles:** Follow Single Responsibility. If a function is longer than 30 lines, it likely needs to be broken down.
- **Error Handling:** Every async operation must have a `try/catch` block and return a structured error object, not just `null`.
- **Atomic Modularity:** Divide large files into smaller, single-purpose components/modules. No file should exceed 250 lines. This ensures fast debugging, easier testing, and prevents the agent from exceeding its context window during refactors.
- **Performance:** Prefer lighter, more efficient libraries. Avoid using heavy dependencies for simple tasks (e.g., using a full date-fns library when simple string formatting suffices).