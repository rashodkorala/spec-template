---
name: spec-feature
description: The spec repo's FEATURE route. Use when building a new capability that has no folder in features/ yet - specify with EARS rules, clarify, design per part, analyze, write tasks in changes/, implement, converge on validation.md, and close.
---

# Feature: a new capability

Spec Kit's specify → clarify → plan → analyze → tasks → implement → converge, with Kiro's EARS rules
and OpenSpec's archive.

**Use for:** something that doesn't exist yet in `features/`.
**Writes:** `features/<name>/` (spec, part notes, validation) and `changes/YYYY-MM-DD-<slug>/` (tasks).

## Requirements-first or design-first? (from Kiro)

- **Requirements-first (default):** we know the behaviour we want; the "how" is open. Write `spec.md`
  first, then the part notes.
- **Design-first:** hardware or platform limits decide what's possible (e.g. a
  new device capability, an OS API with tight rules). Write the constraints in the part notes first, then derive
  the rules in `spec.md` from them.

## Steps

1. **Specify.** Copy `features/_template/` to `features/<name>/`. Fill `spec.md` with `Status: proposed`:
   purpose, flow, states, rules (`R1`, `R2`… with EARS + scenarios), edge cases, copy, constants.
   Add the feature's row to `parity.md` (`scripts/check` fails without it).
2. **Clarify.** List every ambiguity as a numbered question (max ~10, most important first). The owner
   answers. Answers go into the spec, not the chat.
3. **Design per part.** One notes file per part involved (`ios.md`, `android.md`, `backend.md`,
   ...): how it maps to the rules, approved differences, platform limits. New contract
   needs go into `contracts/` as a change.
4. **Analyze.** Before building, check the spec against: the constitution, the glossary, the contracts,
   and other features it touches. Run `scripts/check`. Fix contradictions now. **Owner approves the
   spec** here.
5. **Tasks.** Copy `changes/_template/` to `changes/YYYY-MM-DD-<slug>/` and add it to the table in
   `changes/README.md`. List tasks per part, each citing the rules it implements. Order cross-part
   dependencies (backend before apps, contracts before both sides).
   - **Device cases.** For every rule only a real device can prove, write a case with the
     `spec-device-tests` skill, with every platform the feature ships on in its table. Add a task per
     platform: "Run DT-… on Android", "Run DT-… on iOS".
6. **Implement.** One agent per repo, in parallel. Each reads the spec, its part notes and the
   contracts. If something's missing, update the spec first (see AGENTS.md).
7. **Converge.** Each part fills `validation.md`: every rule PASS, FAIL or BLOCKED with evidence. Fix
   FAILs and repeat until every rule is PASS, or BLOCKED and accepted by the owner (e.g. waiting on a
   device test). A hardware-only rule turns PASS on a platform when its device case shows ✅ for that
   platform in the `device-tests/` index.
8. **Close.** Spec `Status: draft` → `verified` (with commits) once all PASS. Update `parity.md`.
   Mark the change `Synced: yes`, `Status: Done`, and move it to `changes/archive/`.
