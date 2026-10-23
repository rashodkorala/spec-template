# 0002. Branch model and guard rails: `main`, `dev`, `f/`, `b/`, owner approval

Date: YYYY-MM-DD
Status: Accepted
Parts affected: all

## Context

`main` should hold only verified, releasable code, and nothing should merge without the owner's approval.
Coding agents often run as the owner's GitHub account, so GitHub alone can't tell them apart.

## Decision

### Branches

| Branch | Holds | Branches from | Merges into |
|---|---|---|---|
| `main` | Released code. Every merge is tagged `vX.Y.Z` and released | n/a | n/a |
| `dev` | Verified-in-progress work. **Default branch** in code repos | `main` (once) | `main`, by a release PR |
| `f/<slug>` | One feature or change | `dev` | `dev` |
| `b/<slug>` | One bug fix | `dev` | `dev` |
| `h/<slug>` | Emergency fix for released code only | `main` | `main`, then `main` is merged back into `dev` |

`<slug>` is lowercase `a-z 0-9 . _ -`. Dependabot's `dependabot/...` branches are allowed.

**The spec repo has no `dev`.** It ships nothing to users: `f/`, `b/` and `h/` branch from `main` and merge straight into `main`, with the same owner approval, required checks (`branch-name`, `source-branch`, `spec-check`) and merge commits.

### Guard rails

| Rule | `dev` | `main` |
|---|---|---|
| Change only by pull request | yes | yes |
| Approval by the owner (CODEOWNERS, code-owner review required) | 1 | 1 |
| A new push dismisses the approval | yes | yes |
| All review conversations resolved | yes | yes |
| Required CI checks | yes | yes |
| Source branch | `f/`, `b/`, `dependabot/` | `dev` or `h/` only (CI check `source-branch`) |
| Merge method | merge commit | merge commit |
| Force-push, deletion | blocked | blocked |

- **Merge commits only.** Squashing can leave the SHAs `validation.md` cites unreachable.
- **Release tags** `v*`: created only on `main`, never moved or deleted.

### Agents

- `AGENTS.md`: branch `f/` or `b/`, PR into the right base. Never push to `dev` or `main`, never approve, merge, tag, release or change repo settings.
- `.claude/settings.json` denies the commands that would do those things. Deny rules match command patterns, so they are a guard, not a wall.
- The owner reviews and merges every agent PR.

## Consequences

- An author can't approve their own PR, so the owner's and agents' PRs merge through the logged admin bypass.
- Every code repo needs a `dev` branch, CODEOWNERS, and the two small CI checks (`branch-name`, `source-branch`).
