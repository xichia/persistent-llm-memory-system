# Folder path

The hierarchy is already a retrieval system. Use it before search.

A path is a classification decision someone (or some model) already made. Paths below are relative to the memory tree root (in this repository, [../structure/](../structure/)):

```
projects/example-project/decisions.md
          │                └─ kind of information
          └─ which project
```

That is more precise than a vector neighbor. It also travels with the file: anyone who sees the path knows what the file is *for*.

## Why path comes first

- **It is meaningful context.** Even without opening the file, the path tells the model "this is current project state" vs "this is a daily log" vs "this is a standing preference".
- **It is stable.** Search rankings change with the index. Paths change when you reorganize, which is a deliberate act.
- **It is cheap.** Listing a directory or reading `index.md` does not require embeddings or a database.
- **It matches how people already think.** "Look in the project folder" is the right instinct.

## Practical use

1. Identify the area from the task: person, project name, topic, or system rules.
2. Open the index if the name is unknown: [../structure/index.md](../structure/index.md) (`index.md` in a live tree).
3. Read the obvious file for that area (`state.md`, `profile.md`, …).
4. Follow links from that file. Do not start a global search yet.

Examples:

| Question | First path |
| --- | --- |
| Who is this for? | `person/profile.md` |
| What should I work on in X? | `projects/X/tasks.md` and `projects/X/state.md` |
| Why SQLite? | `projects/X/decisions.md` |
| How should I write memory? | `system/memory-rules.md` |
| What happened last Tuesday? | `projects/X/log/YYYY-MM-DD.md` |

## Naming as API

Treat directory and file names as a contract:

- `projects/<slug>/` — one slug per project, stable even if the title changes
- `log/YYYY-MM-DD.md` — ISO dates, one file per day
- `knowledge/<topic>/` — one topic per folder
- Fixed filenames (`overview.md`, `state.md`, `decisions.md`) so tools can find them without guessing

If you rename, update `index.md` ([../structure/index.md](../structure/index.md) in this repository) in the same change.

## When path is not enough

Use path until it fails: you do not know which project, the name is wrong, or the fact could live in several places. Then use [metadata.md](metadata.md) and [full-text-search.md](full-text-search.md).

Do not skip straight to embeddings. If the tree is laid out well, most retrieval is opening a file whose name you already know.
