---
name: spec-quick
description: The spec repo's QUICK route. Use for typos, a clarified spec sentence, a copy tweak the owner already approved, or a cosmetic fix with no behaviour change. Never for a critical area, a contract, or a rule's meaning.
---

# Quick

From Kiro's Quick Spec and Spec Kit's "small changes stay in the PR".

**Use for:** typos, a clarified sentence in a spec, a copy tweak the owner already approved,
cosmetic fixes with no behaviour change.

**Never for** anything touching a critical area (`constitution.md`), a contract, or a rule's
meaning. Those take the `spec-change` or `spec-bugfix` skill.

## Steps

1. Edit the spec (and `copy/`) in place.
2. Make the same edit in each affected repo.
3. Run `scripts/check`. One PR per repo, each linking the spec commit.
