# DT-<AREA>-<nn>: <What should happen, in one plain sentence>

Feature: `features/<name>`   Rules: R…
Change: `changes/<date>-<slug>` (when a change built it)   Bug: `bugs/<date>-<slug>` (when it proves a fix)
Needs: phones, hardware, accounts, tools (only what this case needs)
Time: about N min (including any waiting)

| Platform | Status | Build to test | Notes |
|---|---|---|---|
| Android | ready | branch or commit, debug if `run-as` is used | |
| iOS | ready | branch or commit | |

<!-- Status per platform: ready · todo (applies, steps not written) · blocked (say what is missing) ·
     deferred (say until when) · n/a (the behaviour does not exist on this platform) · retired.
     The last result is not typed here: it is the newest Results row for that platform. -->

## Why

One or two sentences: what could go wrong for a real user if this broke.

## Before you start

- Signed in as …, other state: …
- [Shared setup](../README.md#shared-setup) done for the phone you test on.

## Platform notes

### Android

Setup that only Android needs (for example an `adb` command). Steps marked **Android:** use it.

### iOS

Setup that only iOS needs (for example the Console.app filter). Steps marked **iOS:** use it.

## Steps

Write each step once, in what the person does and sees (if the apps match screen for screen). Split a step only where
the platforms really differ.

1. Do this.
   **Expect:** exactly what you should see or hear (copy on screen in quotes).
2. **Android:** do this. **iOS:** do that.
   **Expect:** …

## Pass if

- …

## Fail if

- …

## Clean up

- Put the phone back the way it was: …

## Results

One row per run. Platform is `Android` or `iOS`; Result is `PASS` or `FAIL`.

| Date | Platform | Tester | Phone / OS | App build | Hardware / backend | Result | Notes |
|---|---|---|---|---|---|---|---|
