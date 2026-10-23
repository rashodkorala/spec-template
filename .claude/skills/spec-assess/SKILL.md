---
name: spec-assess
description: The spec repo's ASSESS route. Use when deciding whether an idea deserves investment (a new product idea, big feature, platform expansion, or anything costly or hard to undo) and writing assessments/<date>-<slug>/assessment.md with the scorecard and a go / needs-clarification / kill verdict.
---

# Assess: does this deserve investment?

From Spec Kit's idea assessment (intake → research → define → shape → decide), in one file.

**Use for:** new product ideas, big features, platform expansions, anything costly or hard to undo.
**Writes:** `assessments/YYYY-MM-DD-<slug>/assessment.md` from `assessments/_template/`.
**Never:** changes code, or starts building because the verdict was go.

## Steps

Each step fills one section of `assessment.md`. Pause for the owner after Problem and after Decision.

1. **Intake.** What is proposed, who asked, and why now. One paragraph.
2. **Research.** Evidence for and against. Each claim is either **cited** (a link, a file:line, a
   support ticket, a metric) or marked **uncited**. Include: what each part does
   today, platform limits (App Store / Play policy, OS APIs), what competitors do.
3. **Problem.** Who is affected, the goal, non-goals, and how we'd measure success.
4. **Options.** Two to four concept-level options, always including "do nothing". No architecture,
   no tasks. Note which parts each option touches.
5. **Decision.** Fill the scorecard, then the verdict (the owner decides it):

| Verdict | Meaning | Next |
|---|---|---|
| `go` | Evidence supports doing it | Owner schedules it → the `spec-feature` or `spec-change` skill |
| `needs-clarification` | Named unknowns block a call | List them; update only the affected sections and re-decide |
| `kill` | Not justified now | Record why. Stopping is a valid, useful outcome |

Add the assessment to the table in `assessments/README.md`.

## Scorecard

Score 1 (bad) to 5 (good), with one line of reasoning each.

| Criterion | Asks |
|---|---|
| User value | Does it serve the user, or protect the core promise? |
| Evidence | How much of the research is cited vs assumed? |
| Cost per part | Effort per part (5 = trivial, 1 = weeks) |
| Hardware impact | Needs a device, firmware or infrastructure change? (5 = none) |
| Parity | Can both platforms deliver the same experience? (5 = identical) |
| Store / policy risk | App Store or Play review risk (5 = none) |
| Reversibility | Easy to remove if it doesn't work? |
| Constitution fit | Any conflict with the constitution? A conflict needs an ADR to proceed |
