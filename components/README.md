# Components

How each part is built, run, tested and released.
Feature behaviour lives in `features/`; this is the "how do I work on this repo" side.

| Folder | Repo | Seed from |
|---|---|---|
| `ios/` | `../<project>-ios` | its `CLAUDE.md` / `AGENTS.md` and docs |
| `android/` | `../<project>-android` | its `CLAUDE.md` / `AGENTS.md` and docs |
| `backend/` | `../<project>-backend` | `README.md`, schema docs |

Each `README.md` covers: stack and versions · architecture (one diagram) · build and run · tests (how to run, what they cover) · release · environments and secrets (names only, never values) · known gotchas.
