# <Feature name>

Status: proposed | draft | verified
Verified against: ios@ · android@ · backend@
Parts: iOS · Android · Backend   (delete the ones not involved)
Contracts: `contracts/...`   (every contract this feature relies on)

## Purpose

One or two sentences: what the user gets and why it matters.

## User flow

Numbered steps from the user's point of view. Link screens in `design/screens/`.

1. …

## States

| State | Entered when | Shows | Leaves when |
|---|---|---|---|

## Rules

Each rule has a permanent ID (never reused, even after removal), a short name, one EARS sentence, and
1–3 scenarios. Scenarios are concrete examples that tests can be written from. Exact values only.

EARS forms: `WHEN <trigger>, THE <part> SHALL …` · `WHILE <state>, WHEN <trigger>, THE <part> SHALL …`
· `IF <unwanted condition>, THEN THE <part> SHALL …` · `THE <part> SHALL …`

### R1. <Short name>
WHEN …, THE app SHALL ….
- Scenario: <name>. GIVEN … WHEN … THEN …
- Scenario: <name>. GIVEN … WHEN … THEN …

### R2. <Short name>
WHILE …, WHEN …, THE backend SHALL ….
- Scenario: <name>. GIVEN … WHEN … THEN …

## Edge and failure cases

| Case | Expected behaviour | Rule |
|---|---|---|
| Offline | | |
| Session expired (401) | | |
| Device or service unreachable | | |
| App killed / phone rebooted | | |
| Permission denied | | |
| Double tap / repeated action | | |

## Copy

Exact user-facing strings, or keys into `copy/`. No em dashes.

| Where | Text |
|---|---|

## Timing and constants

| Constant | Value | Owner part |
|---|---|---|

## Data

What is stored, where (device / account / server), and when it is cleared (logout, account deletion).

## Out of scope

## Decisions

Answers from the clarify step, dated.

## Open questions

- [ ] …
