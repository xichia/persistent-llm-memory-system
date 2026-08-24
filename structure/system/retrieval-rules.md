---
type: rules
status: active
updated: 2026-08-25
tags: [system, read]
---

# Retrieval rules

How to load memory into a model context. Load before searching or injecting files.

The context window is working memory. The files you inject into it are the **working set**. Retrieve the smallest set that makes the task well-informed. Paths in this file are relative to the memory tree root.

## Default order

1. Read [../index.md](../index.md) if you do not already know the layout.
2. Choose files by **path**. The hierarchy is the first classifier.
3. Filter on **metadata** (`type`, `status`, `tags`, `updated`) when listing candidates.
4. **Full-text search** if the path is unknown. See [../../retrieval/full-text-search.md](../../retrieval/full-text-search.md).
5. **Semantic search** only if keyword search misses. See [../../retrieval/semantic-search.md](../../retrieval/semantic-search.md).
6. Inject a handful of files (or sections), each with its path.

## What to load for common tasks

| Task | Load first |
| --- | --- |
| Continue a project | `overview.md`, `state.md`, `tasks.md`; `decisions.md` if changing course |
| Write as this person | `person/communication.md`, then `preferences.md` |
| Personal question | `person/profile.md` and `preferences.md` |
| "Why did we…?" | `decisions.md`, then a log if the rationale is thin |
| Research a topic | `knowledge/<topic>/`, then project `research.md` |
| New agent run | `state.md` + `tasks.md` + these rules |
| Anything | Do **not** load the whole tree |

## What not to load by default

- Daily logs (`log/YYYY-MM-DD.md`) — chronology only
- Archived projects (`status: archived`)
- Templates with no real content
- Duplicate files that restated something already in `state.md`

## Injection format

When placing files in context:

- Include the **path** so updates can go back to the same file
- Prefer whole small files over many tiny chunks
- If a file is large, inject the relevant section and say so
- If retrieved files conflict, prefer structured files over logs, and newer `updated` over older — then fix the files

## Budget

Aim for a few files, not dozens. If you need more than about five, the tree is probably missing a summary (`state.md` or the index) or the task is actually several tasks.

## After the task

If something durable changed, follow [memory-rules.md](memory-rules.md) and write it back. Retrieval without a write path is amnesia with extra steps.
