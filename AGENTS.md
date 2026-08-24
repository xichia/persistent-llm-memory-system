# Agent instructions

This is a concept and starter-template repository for **persistent LLM memory**: a Markdown folder tree as long-term memory, with the model context window as working memory. It is not an application codebase.

Read [README.md](README.md) and [key-idea.md](key-idea.md) before editing. Do not restate the full argument in this file.

## Layout

| Path | Put here | Do not put here |
| --- | --- | --- |
| `concepts/` | How the system works (architecture, lifecycle, consolidation, git) | A live person's profile or project state |
| `structure/` | The starter memory tree (copy this as a live tree's root) | A second copy of `concepts/` |
| `retrieval/` | How to find files (path, metadata, FTS, embeddings) | Index databases or embedding files |
| `use-cases/` | Where the pattern pays off | Implementation code |
| `README.md` | Short human entry point and annotated map | A duplicate of every note |
| `AGENTS.md` | Instructions for agents | The design argument |
| `key-idea.md` | Design principles | How-to git (that is `concepts/git.md`) |

- Markdown files are the source of truth. Search indexes are disposable; do not commit them.
- In this repository the starter tree lives under `structure/`. In a live memory tree that folder *is* the root: `person/profile.md`, not `structure/person/profile.md`.
- New durable areas must be linked from [structure/index.md](structure/index.md) and from the annotated map in [README.md](README.md).

## Writing

- Prefer editing an existing note over adding a parallel file.
- Keep facts, decisions, and chronology in different files. See [concepts/consolidation.md](concepts/consolidation.md).
- Do not treat every conversation as memory. Promote only settled facts, decisions, state, and preferences.
- When you write memory, propose a diff. Wrong memory is worse than missing memory.
- Match existing terms: *folder tree* (long-term memory), *context window* (working memory), *working set* (files injected into context).
- Retrieval order: index → path → metadata → full-text → embeddings.

## Git

This working tree uses a separate git directory at `~/Projects/persistent-llm-memory-system.git`, same pattern as other projects in this set. Do not run `git init` inside the working tree in a way that replaces the `.git` file with a nested `.git/` directory.

Commit messages: sentence-case, say what changed and why. Read `git diff` before committing.

## Scope

Do not turn this into a hosted product, a required vector database, or an auto-capture of every chat. If you add a retrieval helper, keep it optional and rebuildable from the Markdown.
