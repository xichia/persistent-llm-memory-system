# Architecture

Three rules hold the system together:

1. **Markdown files are the source of truth.**
2. **Retrieve only relevant memories into context.**
3. **Keep indexes and embeddings disposable and rebuildable.**

Everything else — search engines, agent loops, editor plugins — is an interface over those files.

## Markdown files are the source of truth

Long-term memory is the folder tree. If a fact is not in a file (or in the project's ordinary files), it is not remembered.

Consequences:

- Writes go to Markdown, not to a vector database, a chat product's "memory", or an agent's hidden scratchpad.
- Corrections happen by editing files.
- Two tools that share the same tree share the same memory.
- Backup, sync, and versioning are file problems, which are already solved. [git.md](git.md) introduces repositories from scratch.

Derived artifacts — embeddings, FTS indexes, summaries, JSON caches — may exist. They are not authoritative. If they disagree with the files, the files win.

## Retrieve only relevant memories into context

The context window is working memory. It is scarce. Dumping the whole tree into a prompt defeats the design.

Retrieval should answer: *for this task, which files (or sections) are worth loading?*

Typical order of operations (same as [retrieval-rules.md](../structure/system/retrieval-rules.md)):

1. **Read the compact map** if you do not already know the layout. [structure/index.md](../structure/index.md) (in a live tree, `index.md`) points at the important areas.
2. **Navigate by path.** The hierarchy is already a classification. `projects/example-project/state.md` is a better first guess than a search over everything.
3. **Follow links and metadata.** Frontmatter (`type`, `status`, `tags`, `updated`) narrows candidates. See [retrieval/metadata.md](../retrieval/metadata.md).
4. **Search.** Full-text, then embeddings if keyword search is not enough.
5. **Inject a small set.** Prefer a handful of focused files over a pile of loosely related excerpts.

A good retrieval pass is closer to "open these three files" than to "here are forty snippets that loosely match".

## Keep indexes and embeddings disposable

Indexes speed retrieval. They should never become the memory.

| Durable | Disposable |
| --- | --- |
| Markdown files in a git repository | SQLite FTS database |
| Human-edited structure | Embedding vectors |
| Decisions, profiles, state | Chunking caches |
| `.me/` next to a project | Any model-specific memory blob |

Rebuild rules:

- Deleting the index must not delete knowledge.
- Changing embedding model or chunk size is a reindex, not a migration of meaning.
- If an index cannot be reproduced from the files, it has started to store memory and should be redesigned.

This keeps search indexes optional and replaceable. The folder remains portable even if you throw away every search helper.

## Layers

```
┌─────────────────────────────────────────┐
│  LLM context window  (working memory)   │
│  retrieved files + current task         │
└──────────────────▲──────────────────────┘
                   │ retrieve / inject
┌──────────────────┴──────────────────────┐
│  Retrieval helpers  (optional, disposable)│
│  paths · metadata · FTS · embeddings    │
└──────────────────▲──────────────────────┘
                   │ read
┌──────────────────┴──────────────────────┐
│  Markdown folder tree  (long-term memory) │
│  person · projects · knowledge · system │
└─────────────────────────────────────────┘
```

Conversation logs can sit beside this stack. They feed consolidation; they are not the memory itself. See [consolidation.md](consolidation.md).

## What this is not

- Not a second brain that auto-captures every chat.
- Not a replacement for the project's real files (code, READMEs, tickets).
- Not a requirement to run a vector database before the system is useful.

Path-aware, human-editable Markdown is enough to start. Search infrastructure is added only when finding files by hand becomes the bottleneck.
