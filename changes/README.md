# Changes

Work in progress on features: new features (route: feature) and changes to existing ones (route: change).
How to run each: the `spec-feature` and `spec-change` skills (`../.claude/skills/`).

One folder per change: `YYYY-MM-DD-<slug>/proposal.md`, copied from `_template/`.

Lifecycle: `Proposed` → `Agreed` (owner approved) → `Implementing` → `Done` + `Synced: yes` → moved to `archive/`.
`scripts/check` fails if an archived change isn't `Done` and synced.

Two open changes must never modify the same rule ID at once. Sequence them.

| Date | Change | Route | Status |
|---|---|---|---|
