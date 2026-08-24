---
type: decisions
status: active
updated: 2026-08-25
tags: [project, example, decisions]
---

# example-project — decisions

What was decided, when, and why. Append new decisions. If one is reversed, mark it superseded and add the replacement. Do not silently rewrite history.

## 2026-08-25 — Markdown files are the source of truth

**Decision:** Store long-term memory as a folder of Markdown, not in a vendor memory feature or a vector store.

**Why:** Human-editable, portable, git-versionable, model-independent. Indexes can be rebuilt; files cannot be inferred from indexes.

**Supersedes:** —

## 2026-08-25 — Context window is working memory only

**Decision:** Never treat "paste the whole tree" as retrieval. Load a small relevant set.

**Why:** Context is scarce. Irrelevant memory crowds out the task. Path + index + search should pick a handful of files.

**Supersedes:** —

## 2026-08-25 — Defer embeddings

**Decision:** Start with folder hierarchy, metadata, and full-text search (SQLite FTS5 if needed). Add embeddings later if keyword search fails.

**Why:** Embeddings are disposable and lock in a model. They are not required for a useful tree.

**Supersedes:** —

Each entry should be understandable without the original chat. If the rationale is "we talked about it", it is not a decision yet.
