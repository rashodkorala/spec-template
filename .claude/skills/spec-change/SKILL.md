---
name: spec-change
description: The spec repo's CHANGE route. Use when changing the behaviour of a feature that already has a spec in features/ - write a proposal with ADDED / MODIFIED / REMOVED rule deltas in changes/, get it agreed, implement, sync the deltas into the spec, and archive.
---

# Change: modify an existing feature

OpenSpec's delta model: describe only what changes, then merge it into the living spec.

**Use for:** new or different behaviour in a feature that already has a spec.
**Writes:** `changes/YYYY-MM-DD-<slug>/proposal.md` from `changes/_template/`, plus a row in the table
in `changes/README.md`.

Lifecycle: `Proposed` → `Agreed` (owner approved) → `Implementing` → `Done` + `Synced: yes` → moved to
`changes/archive/`.

## Steps

1. **Propose.** Fill `proposal.md`: why, which features and contracts, and the deltas:
   - `ADDED`: new rules, with the next free ID in that spec.
   - `MODIFIED`: the rule ID, its current text and its new text.
   - `REMOVED`: the rule ID and why.
2. **Clarify + analyze.** List every ambiguity as a numbered question for the owner (answers go into
   the proposal, not the chat). Check the deltas against the constitution, the glossary, the contracts
   and other features they touch, and run `scripts/check`. Check no other open change in `changes/`
   modifies the same rule IDs. If one does, sequence them; never let two changes edit the same rule in
   parallel.
3. **Owner approves** the proposal (`Status: Agreed`).
4. **Implement** per part, in parallel. Record evidence in the feature's `validation.md` against the
   new or modified rule IDs. Rules only a real device can prove get a device case (the
   `spec-device-tests` skill) covering every part the change touches, with a "Run DT-… on <platform>"
   task per platform; the change is done when each platform shows ✅ (or ➖, or an owner-accepted ⛔).
5. **Sync.** Apply the deltas to `features/<name>/spec.md` (and contracts). A removed rule's ID is
   never reused. Set `Synced: yes`.
6. **Archive.** `Status: Done`, update `parity.md`, move the folder to `changes/archive/`.
   `scripts/check` fails if an archived change isn't synced.
