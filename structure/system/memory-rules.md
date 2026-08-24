---
type: rules
status: active
updated: 2026-08-25
tags: [system, write]
---

# Memory rules

How to write to this tree. Load before extracting or updating memory. Paths in this file are relative to the memory tree root.

## Source of truth

- Durable knowledge lives in Markdown files in this tree (or in the project's ordinary files).
- Do not treat chat transcripts, embeddings, or vendor "memory" as authoritative.
- If two sources disagree, update the Markdown so it is correct.

## What to store

Store when at least one is true:

- A fact about the person, a project, or a topic will still matter later
- A decision was made and will constrain future work
- Project state changed
- A preference or communication rule was stated or corrected
- A source or finding is worth revisiting

Do not store:

- The conversation itself, unless a log entry is genuinely useful
- Information already obvious from code, README, or tickets
- Guesses, discarded plans, and one-off debugging
- Secrets (API keys, passwords, private tokens)

## Where to put it

| Information | File |
| --- | --- |
| Identity and standing facts | `person/profile.md` |
| Recurring defaults | `person/preferences.md` |
| Tone and format | `person/communication.md` |
| What a project is | `projects/<name>/overview.md` |
| Where it stands | `projects/<name>/state.md` |
| What was chosen and why | `projects/<name>/decisions.md` |
| Sources, findings, questions | `projects/<name>/research.md` or `knowledge/<topic>/` |
| Open work | `projects/<name>/tasks.md` |
| What happened today | `projects/<name>/log/YYYY-MM-DD.md` |

Facts, decisions, and chronology stay in different files. See [../../concepts/consolidation.md](../../concepts/consolidation.md).

## How to update

- Prefer editing an existing file to creating a new one.
- Update `profile`, `preferences`, `state`, and `overview` **in place**.
- **Append** to `decisions.md` and to daily logs. Mark superseded decisions; do not rewrite them silently.
- Remove done tasks from `tasks.md`.
- Set `updated` in frontmatter on every write.
- Add a line to [../index.md](../index.md) only when a new durable area appears.
- Write the smallest change that makes the tree true.

## Promotion

Logs may stay logs. Promote into structured files only after information has settled. A consolidation pass may propose a diff; it should not dump a transcript into `state.md`.

## Size

- `state.md` should stay about one screen.
- Daily logs can be longer; they are not default retrieval targets.
- If a file cannot be retrieved usefully, split or cut it.

## Review

When an LLM writes memory, prefer a proposed diff over a silent rewrite of standing facts. Wrong memory is worse than missing memory.

## Commit

If this tree is a git repository, snapshot durable writes:

- Read `git diff` before `git commit`. The diff *is* the review.
- Commit when a fact, decision, preference, or state change should stick — not after every conversation.
- Do not commit secrets or rebuildable indexes.

New to git? [../../concepts/git.md](../../concepts/git.md). A repository is the folder plus a history of snapshots; GitHub is optional.
