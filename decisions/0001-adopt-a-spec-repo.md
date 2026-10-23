# 0001. Adopt a spec repo as the source of truth

Date: YYYY-MM-DD
Status: Accepted
Parts affected: all

## Context

<Project> ships several parts (apps, backend, ...) that must behave the same.
Reading one part's code to build another, or relying on one-off handoff documents, goes stale quickly and produces contract bugs.

## Decision

- A separate `<project>-spec` repo holds behaviour specs, contracts, design, copy and decisions for every part.
- It is **spec-anchored**: specs are edited whenever behaviour changes and are never generated from code or used to generate it.
- Behaviour changes update the spec first. Agents implement from the spec in each repo, in parallel, and record per-part evidence in `validation.md`.
- Specs start as `draft` (code wins) and become `verified` (spec wins) once checked against named commits.

Ideas taken from: GitHub Spec Kit (constitution), Kiro (EARS acceptance criteria), OpenSpec (change proposals + archive), spec-driven-mobile-development (per-platform validation, BLOCKED status), Lyft (one name per thing, not done until every platform ships).

## Consequences

- One place to read before working on any part.
- Extra step on every behaviour change: the spec PR.
- Seeding and verifying the first version is a large one-time read across every repo.
