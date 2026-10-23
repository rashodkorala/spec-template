---
name: spec-explore
description: The spec repo's EXPLORE route. Use when the owner floats a fuzzy idea, a "what if", or asks how something could work in the product, and nothing has been decided yet. Writes nothing in the spec repo.
---

# Explore

From OpenSpec's `explore`: think before committing to anything.

**Use for:** a fuzzy idea, a "what if", a question about how something could work.
**Writes:** nothing in this repo.

## Steps

1. State the idea in one or two sentences.
2. Read what's relevant (specs, constitution, contracts, and code if needed) and answer:
   - Which features and parts would it touch?
   - Does it conflict with the constitution or an ADR?
   - Can both platforms do it? Does it need backend or contract work?
   - Roughly how big is it: hours, days, weeks?
3. The owner picks one:
   - **Drop it.** Nothing is recorded.
   - **Assess it.** Worth a proper decision → the `spec-assess` skill.
   - **Just build it.** Small, clearly worth it, and nothing to argue about → the `spec-feature` or
     `spec-change` skill.
