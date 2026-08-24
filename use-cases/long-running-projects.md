# Long-running projects

Preserve project state across conversations so each new session does not start from zero.

Chats end. Projects do not. Without an external store, you re-explain the stack, the current blocker, and last week's decision every time the context window is empty.

## What to keep

Per project folder (see [../structure/projects/example-project/](../structure/projects/example-project/)):

| File | Role across sessions |
| --- | --- |
| `overview.md` | Stable description so the model knows what it is in |
| `state.md` | The only required "where we are" page |
| `tasks.md` | What to do next |
| `decisions.md` | Constraints from the past |
| `log/` | Optional chronology if you need to reconstruct a week |

A new conversation loads `overview` + `state` + `tasks` and is caught up. That is the whole trick.

## Across days, tools, and machines

Because the files are just files:

- Last night's agent run and this morning's chat share `state.md`
- A laptop and a desktop share the same git remote. See [../concepts/git.md](../concepts/git.md) if "remote" is new.
- Stopping for two weeks is safe: the tree still says what was in flight

## Hygiene

- Update `state.md` when the session changes reality, not when it merely happened
- Move finished work out of `tasks.md`
- Archive the folder when the project ends so it drops out of default retrieval

Without this discipline, "long-running" becomes an infinitely growing paste of old chats. Consolidation is what makes the next session cheap. See [../concepts/consolidation.md](../concepts/consolidation.md).
