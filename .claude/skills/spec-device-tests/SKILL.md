---
name: spec-device-tests
description: Write or update a device case in device-tests/<feature>/, or record a person's device-test result into validation.md and the bug or change file. Use when a rule can only be proven on a real device, when a validation row is BLOCKED on hardware, or when the owner reports a device-test run.
---

# Device tests

A device case is a check only a real device can prove. A person runs it; agents
write it and record what it showed. How a person runs a case, and the shared phone setup, are in
`device-tests/README.md`.

Automated tests live in the code repos. A rule that only those tests
cover stays **BLOCKED** in the feature's `validation.md` until its device case passes on that platform.

## Writing a case

- Copy `device-tests/_template.md` to `device-tests/<feature>/DT-<AREA>-<nn>-<slug>.md`, with the
  feature folder named as in `features/`. IDs are permanent and never reused.
- **One case per behaviour, for every platform it applies to.** If the apps match screen for screen,
  write the steps once; split only real differences ("**Android:** … **iOS:** …"), with platform-only
  setup under "Platform notes".
- Write what the person does and sees, with the exact copy on screen, not code. Every case must run
  without asking anyone: what you need, setup, numbered steps each with an **Expect**, pass and fail
  rules, clean-up, and a Results log.
- Fill the platform table. Status per platform: `ready` · `todo` (applies, steps not written yet) ·
  `blocked` (cannot be run yet; say what is missing) · `deferred` (the owner chose to wait; say until
  when) · `n/a` (the behaviour does not exist on that platform) · `retired`. Never type a result into
  the table: the result is the newest row for that platform in the case's **Results** log.
- A case for one platform only marks the other platform `n/a`.
- Run `scripts/device-tests` to regenerate the index in `device-tests/README.md`. Never edit the index
  by hand; `scripts/check` fails when it is stale.

## A feature or change built on both apps at once

1. Write one case with both platforms in its table, each `ready` once that app's build exists.
2. In the change proposal's Tasks table, add one row per platform: "Run DT-… on Android", "Run DT-… on
   iOS".
3. The change (or feature) is done only when every one of its cases shows ✅ for each platform, or ➖,
   or a ⛔ the owner has accepted.

## Recording a result

When the owner says a case was run:

1. Read the newest Results row for that platform. Never record a result you did not see logged there.
2. Run `scripts/device-tests` so the index matches.
3. **PASS:** turn the cited rules' rows for that platform in the feature's `validation.md` to PASS,
   naming the case ID, date and build. Update the bug's Test row (verdict `verified`) or the change's
   task.
4. **FAIL:** record the step number and what was seen in `validation.md` (FAIL) and reopen the bug or
   change (back to Fix).
5. Run `scripts/check`.

