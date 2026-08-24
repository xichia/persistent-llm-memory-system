---
type: research
status: active
updated: 2026-08-25
tags: [project, example, research]
---

# example-project — research

Sources, findings, hypotheses, and unresolved questions. Separate from [decisions.md](decisions.md): research can be wrong; decisions are commitments.

## Sources

- This repository's own [concepts](../../../concepts/) and [key-idea.md](../../../key-idea.md)
- Adjacent practices: Zettelkasten, personal knowledge management, `.cursor/rules`, agent memory files, git-backed wikis

## Findings

- Hierarchy is already retrieval: a good path often beats a search
- Conversation logs make poor default context; they need consolidation
- Many "AI memory" products hide state in a vendor. A folder does not.

## Hypotheses

- A `.me/` directory in a code repo is enough local memory for most engineering work, with a larger personal tree for cross-project facts
- SQLite FTS5 will cover early search needs; embeddings only after false negatives show up

## Unresolved

- How aggressively should an agent write to the tree without review?
- Where do secrets belong? (Probably not in this tree.)
- One tree per person vs. one tree per household/team vs. both, linked

Move a finding into `decisions.md` only when it becomes a commitment. Move lasting, project-independent knowledge into [../../knowledge/](../../knowledge/).
