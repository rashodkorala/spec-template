---
name: spec-bugfix
description: The spec repo's BUGFIX route. Use when behaviour is wrong (differs from the spec or is obviously broken) on any part, including parity FAILs - report, assess without touching code, fix inside the approved scope, test, and close bugs/<date>-<slug>/bug.md.
---

# Bugfix

Spec Kit's assess → fix → test, with Kiro's current / expected / unchanged behaviour.

**Use for:** behaviour that is wrong. Not for typos or copy (→ the `spec-quick` skill).
**Writes:** `bugs/YYYY-MM-DD-<slug>/bug.md` from `bugs/_template/`, plus a row in the table in
`bugs/README.md`.

## Stage rules (from Spec Kit)

| Stage | May edit code? | Rule |
|---|---|---|
| Assess | **No** | Diagnose only. The owner reviews the assessment before any fix |
| Fix | Yes, the **only** stage that does | Stay inside the assessed scope. Anything beyond it is written down and approved |
| Test | **No** | Never edit code to make a test pass. A failing test goes back to Fix |

## Steps

1. **Report.** Symptom, where seen (part, version, device), reproduction steps, logs. Reproduce it the
   way a user would before going further.
2. **Assess** (no code changes):
   - **Verdict:** `confirmed` · `not-a-bug` (works as specced) · `spec-gap` (the spec never said) ·
     `duplicate` (link it) · `cannot-reproduce`.
   - **Severity:**
     - **S1**: the core promise is broken, data loss, or security.
     - **S2**: a core flow is broken but has a workaround.
     - **S3**: minor.
     - **S4**: cosmetic.
   - **Behaviour** (from Kiro), citing spec rule IDs where they exist:
     - Current: `WHEN … THEN the app …` (what it wrongly does)
     - Expected: `WHEN … THEN the app SHALL …`
     - **Unchanged:** `WHEN … THEN the app SHALL CONTINUE TO …`. List the nearby rules the fix must
       not break. For anything in a critical area (`constitution.md`), this list is mandatory.
   - **Root cause** with file:line.
   - **Other platform:** does iOS / Android have the same bug? Check, don't guess. If yes, the bug
     covers both.
   - **Proposed fix and scope:** which files, per part.
   - A `spec-gap` verdict goes to the `spec-change` skill (or a spec fix in this bug), and the owner
     decides the expected behaviour first.
3. **Owner approves** the assessment.
4. **Fix.** Write a test that reproduces the bug first (it must fail), then fix. Record what changed
   per part.
5. **Test.** Per part: the reproduction test passes, the **unchanged** rules still pass, and the
   regular test suite is green.
   - Verdicts: `verified` · `BLOCKED` (names the exact check still needed, e.g. "needs a real device") ·
     `failed` (back to Fix).
   - A check only a device can do becomes a device case (the `spec-device-tests` skill); the bug's
     Test row names it, and the verdict turns `verified` when the case shows ✅ for that platform.
6. **Close.** If the bug revealed a missing rule or edge case, add it to the feature spec. Add the
   case to the feature's `validation.md` and the part notes' Gotchas. Set `Status: Closed` and update
   the row in `bugs/README.md`.
