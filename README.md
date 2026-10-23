# <project>-spec

The single source of truth for how <project> works across every part: the apps, the backend, and any device or service they talk to.
Specs here describe **behaviour and contracts**.
Each code repo implements them.

> **Using this template?** Follow [SETUP.md](SETUP.md) first, then delete it.

| Repo | Role |
|---|---|
| `../<project>-ios` | iOS app |
| `../<project>-android` | Android app |
| `../<project>-backend` | API |

## How to read this repo

1. `constitution.md`: rules that hold everywhere and are never broken.
2. `glossary.md`: one name per thing. Use these words in code, specs and copy.
3. `AGENTS.md`: which route a piece of work takes. Each route's steps are a skill in `.claude/skills/`.
4. `parity.md`: what exists on which part today. `ROADMAP.md`: what to build next, in order (finished items: `ROADMAP-done.md`).
5. `features/<name>/spec.md`: what a feature does, end to end, then the per-part notes beside it.
6. `contracts/`: the boundaries between parts (API, auth, sync, ...). Both sides must match these exactly.

## Layout

```
constitution.md      non-negotiable rules
glossary.md          shared vocabulary
parity.md            feature × part status matrix
ROADMAP.md           ranked work plan
ROADMAP-done.md      finished roadmap items
features/<name>/     spec.md + one notes file per part (ios.md, android.md, backend.md, ...) + validation.md
contracts/<name>/    README index + one file per section
components/          how each part is built, run, tested and released
design/              tokens, type, screen inventory
copy/                user-facing text
assessments/         "does this deserve investment?" decisions (go / needs-clarification / kill)
bugs/                bug reports: assess → fix → test
changes/             features and changes in progress → changes/archive/ when done
decisions/           ADRs, including approved platform differences
device-tests/        manual cases only a real device can prove
.claude/skills/      route skills (explore · assess · feature · change · bugfix · quick) + device tests
scripts/check        validator: run before every commit
scripts/spec_config.py   the parts and device platforms this project has
```

## How work flows

Pick a route in `AGENTS.md` (each one is a skill in `.claude/skills/`):

| Route | For |
|---|---|
| Explore | Thinking an idea through, nothing written |
| Assess | Deciding whether an idea deserves investment |
| Feature | Building something new |
| Change | Changing an existing feature (deltas, then sync into the spec) |
| Bugfix | Fixing broken behaviour (current / expected / unchanged) |
| Quick | Typos and copy tweaks |

Whatever the route: no behaviour change merges without its spec update, each part records evidence (PASS / FAIL / BLOCKED), and `parity.md` stays current.

## Trust levels

Every spec file starts with a status block:

```
Status: proposed | draft | verified
Verified against: ios@<sha> · android@<sha> · backend@<sha>
```

- **proposed**: agreed behaviour that isn't built yet.
- **draft**: seeded from older docs or code; not yet fully checked. If it disagrees with code, the code is right and the spec gets fixed.
- **verified**: checked against the commits listed. From then on the spec is the reference, and code that disagrees is the bug.

## Where the ideas come from

GitHub Spec Kit (constitution, assess flow, bug stage rules, converge), Kiro (EARS rules, bugfix current / expected / unchanged, quick path), OpenSpec (living specs, deltas + archive, rules with scenarios, validate, a shared spec repo for many code repos).
See `decisions/0001-adopt-a-spec-repo.md`.
