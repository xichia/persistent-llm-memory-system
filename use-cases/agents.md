# Agents

Persistent state between agent executions. The process dies; the folder does not.

An agent run is a conversation with tools and a time limit. Anything it should still know on the next run has to land on disk before the process exits.

## What an agent should persist

- **State** — what is true now (`state.md`)
- **Tasks** — remaining work, including what this run did not finish
- **Decisions** made during the run
- **Lessons** — failed approaches, environment quirks, "do not do X"
- **Pointers** — paths, PR numbers, command output worth keeping (short)

The agent's scratchpad, tool traces, and token-by-token plan belong in a log or nowhere.

## Working set at start

A typical boot prompt is not "here is the repo plus all history". It is:

1. [../structure/system/retrieval-rules.md](../structure/system/retrieval-rules.md) and [../structure/system/memory-rules.md](../structure/system/memory-rules.md)
2. Project `overview.md` + `state.md` + `tasks.md`
3. Extra files the task actually needs (retrieved, not dumped)

That is enough to continue. The agent can search the tree if it must.

## Write before halt

Make persistence part of the run, not an afterthought:

- Update `state.md` and `tasks.md` as reality changes
- Append decisions when a choice is made
- Write `log/YYYY-MM-DD.md` (or a run-id file) for chronology
- Do not rely on the chat UI to still have the transcript tomorrow

If the agent is not allowed to write the tree unsupervised, have it produce a patch or a proposed Markdown diff for review. Wrong autonomous memory is a long-lived bug.

## Multiple runs, one tree

Runs may overlap (parallel agents) or chain (handoff). The files are the coordination point:

- One `state.md` so two agents do not invent two currents
- Tasks as a shared work list (use a real tracker if you need locking)
- Git commits as the record of who wrote what. Each commit is a snapshot; see [../concepts/git.md](../concepts/git.md) if that is new.

This is the same idea as long-running projects, with a stricter requirement: the human might not be there to recap. See [long-running-projects.md](long-running-projects.md).
