# Agent instructions (<project>-spec)

You are working on <Project>.
<One sentence on what the product is and the promise it must never break.>
This repo is the spec.
The code lives in the sibling repos listed in `README.md`.

## First: pick the route

Every task takes one route.
Say which route you're on before starting, then load its skill and follow its steps and stage rules.
If unsure, ask the owner.

```
Is something broken (behaves differently from the spec, or obviously wrong)?
├─ yes → is it a typo / copy / cosmetic fix with no behaviour change?
│        ├─ yes → QUICK
│        └─ no  → BUGFIX
└─ no  → is it a new idea we haven't decided to build?
         ├─ yes → still fuzzy? → EXPLORE, then ASSESS if it's worth a decision
         └─ no  → does the feature already exist in features/?
                  ├─ yes → CHANGE
                  └─ no  → FEATURE
```

| Route | Skill | Writes | Ends with |
|---|---|---|---|
| Explore | `spec-explore` | nothing | "assess it", "drop it" or "just build it" |
| Assess | `spec-assess` | `assessments/<date>-<slug>/assessment.md` | go / needs-clarification / kill |
| Feature | `spec-feature` | `features/<name>/` + `changes/<date>-<slug>/` | every rule PASS or accepted BLOCKED, archived |
| Change | `spec-change` | `changes/<date>-<slug>/` with deltas | deltas synced into the spec, archived |
| Bugfix | `spec-bugfix` | `bugs/<date>-<slug>/bug.md` | verified on every affected part |
| Quick | `spec-quick` | edits in place | a PR |

Skills live in `.claude/skills/<skill>/SKILL.md`.
An agent without skill support reads that file directly.
Never QUICK anything touching a contract or the areas the constitution lists as critical.

## Before you write code in any <project> repo

1. Read `constitution.md` and `glossary.md`.
2. Read the feature folder you are touching: `features/<name>/spec.md`, then the notes file for the part you are changing (`ios.md`, `android.md`, `backend.md`, ...).
3. For every contract the feature references, read `contracts/<name>/README.md` (status, citation prefixes, file index), then only the section files you need. Rule IDs are in `rules.md`.
4. Check the spec's status block. `proposed` = agreed, not built yet. `draft` = verify what you rely on against the code first (code wins). `verified` = the spec wins; code that disagrees is the bug.

## Rules

- **Spec first.** If the behaviour you need isn't in the spec, or the spec is wrong, update the spec (or open a change) before writing code. Never decide behaviour silently in code: the other part's agent won't see it.
- **Humans decide, agents prepare.** Verdicts, spec approval and bug assessments wait for the owner.
- **Copy values, don't paraphrase them.** Timings, IDs, byte values, colours, copy and error text come from the spec exactly. Never copy them from another part's code.
- **Don't "fix" approved differences.** If part notes or an ADR in `decisions/` say a platform differs on purpose, keep the difference.
- **Contracts change on both sides together.** A contract change lists every repo it affects and is not done until each one is updated.
- **Bugfix stage rules.** Assess and Test never edit code. Fix stays inside the assessed scope. Never edit code to make a test pass. Always check whether the other platform has the same bug.
- **Record evidence.** Fill the feature's `validation.md` for your part: PASS (how it was checked), FAIL (what broke) or BLOCKED (the exact check still needed). Never mark PASS on belief.
- **Hardware checks are device cases.** A BLOCKED row that needs a real device gets a case in `device-tests/<feature>/`. A person runs it and logs the result per platform there before that platform's row turns PASS. Writing a case or recording its result: the `spec-device-tests` skill.
- **A change isn't done until it's synced.** Apply its deltas to the spec, set `Synced: yes`, update `parity.md`, then archive.
- **Git (ADR 0002).** `f/<slug>` for a feature or change, `b/<slug>` for a bug. This repo has no `dev`: branch from `main` and open the PR into `main`. Never push to `dev` or `main`, never approve, merge or tag: the owner does.
- Use the words in `glossary.md`. If you need a new term, add it there.
- No em dashes in user-facing strings. Wire values are stable codes, never display labels.
- Run `scripts/check` before committing to this repo.

## Writing specs

- Start from the templates: `features/_template/`, `changes/_template/`, `bugs/_template/`, `assessments/_template/`.
- Rules: `### R<n>. <Name>`, one EARS sentence, 1–3 scenarios. IDs are permanent and never reused.
- Write exact values (`3 s`, `#BD9B60`, `404`), not adjectives ("quickly", "gold").
- Describe behaviour without platform APIs in `spec.md`. Platform mechanics go in the part notes.
- Keep files short. Don't create notes files for parts that aren't involved.
