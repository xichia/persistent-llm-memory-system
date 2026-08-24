# Decision history

Remember what was decided and why, so the next session does not re-open a closed question — or does so on purpose.

Models are good at generating options. They are bad at knowing which options you already killed. Without `decisions.md`, every new context window is a blank ballot.

## What to record

For each decision, enough to act on it later:

- **Date**
- **Decision** — the commitment, in one or two sentences
- **Why** — constraints and the rejected alternative, briefly
- **Supersedes** — pointer to an older decision if this replaces it

See the template in [../structure/projects/example-project/decisions.md](../structure/projects/example-project/decisions.md).

## What not to record

- The full debate
- Options that were never seriously on the table
- Implementation details that the code now shows
- "We should maybe…" — that is a task or a hypothesis, not a decision

## Append, don't overwrite

Silent edits destroy the point. If you reverse a decision, mark the old one superseded and add a new entry. Future-you (and a future model) can see that the change was deliberate.

Chronology of *how the meeting went* belongs in `log/`. The decision file is the index of commitments.

## Using the history

- Changing course: load `decisions.md` first so you argue with the actual rationale
- Implementing: you may not need the file at all if `state.md` already reflects the choice
- Onboarding a new model or teammate: `overview.md` + `decisions.md` is a faster brief than the chat archive

A short, dated list beats a generated "summary of all our conversations" that no one can verify.
