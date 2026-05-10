# React, Next.js, and JS Security Knowledge Base (2026 Edition)

This document serves as the primary security and architectural reference for AI agents managing this codebase.

## 1. Package Management & Supply Chain (pnpm)
To maintain a secure local environment, the project strictly uses **pnpm**.
- **Phantom Dependency Prevention:** pnpm’s non-flat `node_modules` structure is mandatory. Never use `npm` or `yarn` as they allow "phantom dependencies" that can leak vulnerabilities.
- **Lifecycle Script Blocking:** pnpm v10+ blocks `preinstall` and `postinstall` scripts by default. Agents must not bypass this without manual verification of the package.
- **Integrity Verification:** Always use `pnpm install --frozen-lockfile` in CI/CD and deployment to ensure the `pnpm-lock.yaml` is never unexpectedly modified.
- **New Package Quarantine:** Use the `minimumReleaseAge` setting (1 day) to block newly published packages that haven't been vetted by the community.
- **Safety_gate_rules:** The agent must present every pnpm command to the user via the Safety Gate. It is strictly forbidden to bypass the (Y/N) prompt for dependency installation.

## 2. React Security Best Practices
- **XSS Prevention:** Trust React’s default escaping. Never use `dangerouslySetInnerHTML` unless the content is sanitized with a library like `DOMPurify`.
- **Direct DOM Access:** Avoid `refs` for manual DOM manipulation; use React state to prevent bypasses of the built-in XSS protection.
- **Client-Side Secrets:** Never prefix sensitive environment variables with `NEXT_PUBLIC_`. These are bundled into the client-side JS and are visible to users.

## 3. Next.js App Router Security
- **Server Action Validation:** Every Server Action must be treated as an open API endpoint. 
    - **Rule:** Re-verify user authentication and authorization *inside* the action body, even if the page is protected by middleware.
    - **Zod Validation:** Use `zod` to strictly type and validate all input coming from the client.
- **Data Privacy (RSC):** Use `server-only` to ensure sensitive logic or private keys never leak to the client bundle.
- **CSRF Protection:** Next.js Server Actions include built-in protection, but custom Route Handlers (API routes) require manual CSRF token validation or `SameSite: Strict` cookie settings.

## 4. General JavaScript & Header Security
- **Security Headers:** Every response must include:
    - `Content-Security-Policy`: Use a nonce-based script-src to block unauthorized scripts.
    - `Strict-Transport-Security`: Force HTTPS.
    - `X-Content-Type-Options: nosniff`: Prevent MIME-type sniffing.
- **Dependency Audits:** Run `pnpm audit` regularly. Any vulnerability with a "High" or "Critical" rating must be patched immediately.

## 5. Agent Instructions for Code Generation
When generating or refactoring code:
1. **Prefer pnpm commands** (e.g., `pnpm add -D` instead of `npm install --save-dev`).
2. **Prioritize Server Components** for data fetching to keep credentials off the client.
3. **Apply Type-Safety:** Use strict TypeScript types and avoid `any` to prevent logic-based security flaws.
4. **Refer to Local Docs:** If unsure of a Next.js 15+ feature, use the Search Tool to check the latest docs on nextjs.org instead of relying on local node_modules paths.
5. **DO NOT:** 
    - DO NOT use `process.env` directly in components; use a central `env.ts` validated with Zod.
    - DO NOT use default fetch(); use a wrapped version with a 10s timeout to prevent agent-hanging.
6. **Accessibility (A11y):** 
    - Every interactive element must have an `aria-label` attribute.
    - Every image must have a descriptive `alt` tag (no 'Image' or 'Picture' placeholders).
7. **Forms and User Input:**
    - Use `react-hook-form` with `zod` for validation.
    - DO NOT trust `innerHTML` from user input; always sanitize with `DOMPurify`.
8. **Build Optimization:**
    - **Bundle Size:** Keep the initial client-side JS bundle per-page under 200KB. Use dynamic imports (`import()`) for large components or libraries. Avoid loading the entire 'heavy' library on the first page load. Prefer 'lightweight' alternatives if available (e.g., `date-fns` over `Moment.js`).
9. **Performance:**
    - Use `React.memo()` for functional components to prevent unnecessary re-renders.
    - Use `useMemo()` and `useCallback()` hooks to memoize expensive calculations and function references.
    - Prefer Server Components for data fetching to reduce client-side load.
10. **Testing:**
    - Use Jest for unit testing and React Testing Library for component testing.
    - Aim for at least 80% code coverage.
11. **Component Testability:** 
    - Use `data-testid` on interactive elements to ensure tests don't break when CSS classes change.
    - Decouple business logic from UI: Keep complex calculations in separate `.ts` files so they can be unit tested without mounting a React component.
12. **Atomic Modularity:** Divide large files into smaller, single-purpose components/modules. No file should exceed 250 lines. This ensures fast debugging, easier testing, and prevents the agent from exceeding its context window during refactors.