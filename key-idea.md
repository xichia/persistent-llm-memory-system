# Key idea

Memory should belong to the user, not to a model, a product, or a session.

A Markdown folder tree can be that memory. The properties below are the point of the design — not extras to add later.

## Model-independent

The files do not care whether the next reader is ChatGPT, Claude, Grok, a local model, or a person. Nothing in long-term memory should be stored in a vendor-specific memory feature, a proprietary embedding store, or a chat transcript that only one product can reopen.

Models come and go. The folder stays.

## Human-readable and editable

Every memory is a file you can open. If the model writes something wrong, you delete the sentence. If a preference changes, you change the file. If a project is over, you archive the folder.

A memory system that only an LLM can inspect is not under your control. Markdown keeps a human in the loop without a special UI.

## Portable

The unit of memory is a directory of text files. It can live in iCloud, a git repository, a USB drive, or next to the project it describes. There is no import/export step. Moving memory is moving files.

## Searchable

Paths, titles, tags, and full text are all queryable. Start with the folder hierarchy, then full-text search. SQLite FTS5 is a simple next step. Embeddings are optional and can be rebuilt. See [retrieval/](retrieval/).

## Optional version history

Memory has history. You can see when a decision flipped, recover a deleted fact, and review what an agent wrote before accepting it.

A **git repository** is the memory folder plus a hidden record of snapshots (commits). You still edit ordinary Markdown. Git remembers previous versions so a bad write is not permanent and two machines can share the same timeline.

This also makes memory *reviewable*. An LLM can propose updates; `git diff` shows the exact lines; you commit only what should stick. GitHub is optional — a website that can host a **private** copy. Git itself runs on your computer.

You can start with ordinary folders, review edits by reading the files, and keep a backup copy before changes. Version history is a later option; [concepts/git.md](concepts/git.md) explains it when you need it. The [practical guide](guide.md) starts with the folder workflow.

## User-controlled

You decide what is stored, what is retrieved, and what is forgotten. Retention is not a product default. You choose which tools can access the folder. When an online AI reads a file, its contents may be sent to that service for processing; keeping files locally does not make that processing offline.

Control includes the right to keep things *out* of memory. Most conversation is not worth keeping. See [concepts/consolidation.md](concepts/consolidation.md).

## `.me/` as a project-local memory

A convenient convention: a `.me/` directory inside a software project holds everything an AI collaborator should know that is **not obvious from the project's ordinary files**.

Ordinary files already say a lot — the README, the code, the tests, the issue tracker. `.me/` is for the rest:

- Why this architecture was chosen over the alternative
- Current working state that is not yet reflected in the repo
- Preferences for how to touch this codebase
- Open questions, dead ends, and "do not try this again"
- Pointers to related personal or cross-project memory

`.me/` can be a subset or a symlink into a larger personal memory tree. The important part is the split:

| Already in the project | Belongs in `.me/` (or the memory tree) |
| --- | --- |
| Source, config, docs the team already maintains | Intent, rationale, and tacit context |
| What the code *is* | What we are *trying to do* |
| Public or shared project truth | Collaborator-only memory |

The folder tree is long-term memory. The context window is working memory. `.me/` is the bridge between a real project and the model sitting in it.
