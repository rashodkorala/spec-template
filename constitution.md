# <Project> constitution

Status: draft
Verified against: not yet

These rules hold on every part.
Breaking one needs an ADR in `decisions/` that the owner approved.
Every rule should come from a bug that shipped or nearly shipped, or a promise the product makes.
Items marked **(verify)** changed recently and must be re-checked against current code.

## The promise

1. <What the product must always do for the user, stated exactly.>

## Critical areas

List the areas that never take the QUICK route (for example payments, auth, sync, anything on a device).

2. …

## Auth, sync, data

3. Offline is not expiry. Only a rejected refresh, a signed-out state or a 401 ends a session.
4. After account deletion, no credentials remain on the device.
5. Per-user data is keyed by user. Capture the user id before each sync; discard mismatched results.
6. Send every required JSON key and no extra keys.
7. Wire values are stable codes, never display labels. An enum changes on both sides together.

## UI and copy

8. No em dashes in user-facing strings.
9. Disabled buttons have their own colours. Destructive flows take two taps.
10. Previews and tests never touch real storage, notifications or hardware.

## Process

11. Verify, don't assert. "Builds" means the build ran. "Works" means it ran on a device. Hardware-only checks are BLOCKED until run on real hardware.
