# Engineering and software

Requirements, architecture, experiments, bugs, and rationale — the parts of a software project that ordinary files do not always capture well.

Code, tests, and the README are already memory. Do not duplicate them. Store what the project's ordinary files do *not* make obvious.

## What belongs in the memory tree (or `.me/`)

- **Requirements and intent** — what we are optimizing for, who it is for, explicit non-goals
- **Architecture rationale** — why this shape, what was rejected
- **Experiments** — what we tried, outcome, whether to retry
- **Bugs and incidents** — the ones whose *lesson* should persist after the ticket is closed
- **Working state** — branch in flight, blockers, "do not rebase X yet"
- **How to touch this repo** — generate vs hand-write, test commands that are easy to forget, landmines

A practical home is `.me/` at the project root: a project-local slice of the same layout (`overview`, `state`, `decisions`, `tasks`). Cross-project facts stay in the personal tree. See [../key-idea.md](../key-idea.md).

## What stays in the repo proper

- The implementation
- Public docs the team already maintains
- Tests as the spec that runs
- Issues/PRs if that is where the team actually works

If a decision is important to every contributor, it may belong in `docs/` rather than `.me/`. `.me/` is collaborator context, not a shadow documentation site.

## Experiments and bugs

Record experiments as short entries: date, hypothesis, setup, result, next. That prevents the next session from rerunning a failed approach with fresh confidence.

For bugs, prefer: symptom, cause, fix, *why it was possible*. The ticket tracker owns status; memory owns the lesson.

## Retrieval for an engineering session

Typical working set:

1. `.me/state.md` or `projects/<name>/state.md`
2. `decisions.md` if the task might violate an old choice
3. Relevant code (ordinary project files — not this tree)
4. `communication.md` / project conventions if writing for a human

Logs and old experiment notes stay on disk until the task is "what did we already try?".
