# <Change name>

Status: Proposed | Agreed | Implementing | Done
Synced: no | yes
Route: feature | change
Features: `features/...`
Contracts: `contracts/...`
Parts affected: iOS · Android · Backend
Date: YYYY-MM-DD

## Why

## Deltas

Rule IDs refer to the feature's `spec.md`. A new rule takes the next free ID. IDs are never reused.
For a new feature (route: feature), the rules live in the new `spec.md`; list them here as ADDED.

### ADDED
#### R<n>. <Name> (`features/<name>`)
WHEN …, THE … SHALL ….
- Scenario: …

### MODIFIED
#### R<n>. <Name> (`features/<name>`)
- Was: …
- Now: …

### REMOVED
#### R<n>. <Name> (`features/<name>`)
- Why: …

## Tasks

Each task cites the rules it implements. Order across parts where it matters.

| # | Part | Task | Rules | Depends on | Status | Evidence |
|---|---|---|---|---|---|---|
| 1 | Spec | Apply deltas (sync) | all | | | |
| 2 | Backend | | | | | |
| 3 | iOS | | | 2 | | |
| 4 | Android | | | 2 | | |

## Rollout and compatibility

Order between parts (e.g. backend before apps), behaviour of older app versions,
migrations.
