# Full-text search

When the path is unknown, search the text.

Start simple. For a personal or single-project tree, `grep` or [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) over Markdown is often enough. When the tree grows, or you want ranked queries from an agent without shelling out, **SQLite FTS5** is a good next step.

## Why FTS5 first

- Ships with SQLite; no extra service
- Understands words, prefixes, and boolean queries
- Can store path, `type`, `status`, `tags`, and `updated` as columns next to the text
- Rebuildable from the folder in seconds
- Model-independent and easy to inspect (`sqlite3 memory.db`)

Embeddings answer "things like this". FTS answers "files that mention this". Most memory lookups are the second kind: a project name, an error string, a person, a library.

## A minimal shape

Index each Markdown file as a row:

| Column | Source |
| --- | --- |
| `path` | Relative path (primary key) |
| `type` | Frontmatter |
| `status` | Frontmatter |
| `updated` | Frontmatter |
| `tags` | Frontmatter |
| `title` | First heading |
| `body` | File text, FTS5 virtual table |

Rebuild:

1. Walk the tree.
2. Parse frontmatter.
3. Insert or replace rows.
4. Delete rows whose files no longer exist.

The database is a cache. Deleting `memory.db` must be safe. See [../concepts/architecture.md](../concepts/architecture.md).

## Querying

Typical agent queries:

- `body: "FTS5" AND status: active`
- `tags: oncall AND type: decisions`
- `path: projects/example-project/*` then filter by date

Always return **paths**, not just snippets. The next step is to open the file and inject it, not to treat the snippet as the memory.

Rank is useful; it is not authority. A perfect keyword hit in an archived log still should not beat `state.md` for "where is the project now?". Combine FTS with [folder-path.md](folder-path.md) and [metadata.md](metadata.md).

## When `grep` is enough

Skip the database while:

- The tree is small enough to search in milliseconds
- You (or the tool) already know the likely folder
- You do not need ranked search across everything

Add FTS5 when global keyword search becomes a daily operation or when an agent needs a structured query API.

## What not to do yet

- Do not chunk files into overlapping windows for FTS. Index the file, then open it.
- Do not store the only copy of a note in SQLite.
- Do not build a custom query language. FTS5 plus metadata columns is enough until it is not.
