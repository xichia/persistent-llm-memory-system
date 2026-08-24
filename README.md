# llm-memory

Use a Markdown folder tree as persistent LLM memory.

The context window is small, ephemeral, and model-specific. A folder of Markdown files is large, durable, and yours. This repository describes a way to treat the two as complementary memory systems:

| Layer | Role | Analogy |
| --- | --- | --- |
| Folder tree | Long-term memory | What should still be true next month |
| LLM context window | Working memory | What is relevant *right now* |

An LLM does not need to "remember" everything it has ever been told. It needs a place where useful information is written down, and a way to pull only the relevant pages back into context when they matter.

This idea is model-independent. The same tree can serve ChatGPT, Claude, Grok, a local model, or an agent. Humans can read and edit every file. Git can version the whole thing.

## Why Markdown files

- **Source of truth.** Memory lives in files you can open, not in a vendor's hidden state.
- **Human-editable.** You can correct, delete, or reorganize anything an LLM wrote.
- **Portable.** Copy the folder. Sync it however you already sync files.
- **Searchable.** Start with paths, then full-text search, then embeddings if needed.
- **Git-versionable.** History, diffs, and undo apply to memory the same way they apply to code. See [concepts/git.md](concepts/git.md) if you have never used a repository.
- **Disposable indexes.** Embeddings and search databases can be rebuilt from the files. They are caches, not memory.

See [key-idea.md](key-idea.md) for the full list of properties this design is aiming for.

## How it works

1. Conversations happen as usual.
2. Useful information is extracted and classified.
3. Stable facts, decisions, and state are written into Markdown under a predictable layout.
4. Raw conversation logs may be kept, but they are not treated as permanent memory.
5. On the next task, only the relevant files are retrieved and injected into the model context.

The lifecycle is documented in [concepts/memory-lifecycle.md](concepts/memory-lifecycle.md). Consolidation — what gets promoted, what stays a log, what is forgotten — is in [concepts/consolidation.md](concepts/consolidation.md).

## Layout

| Path | Contents |
| --- | --- |
| [README.md](README.md) | Human entry point |
| [AGENTS.md](AGENTS.md) | Instructions for agents working in this repo |
| [key-idea.md](key-idea.md) | Design principles |
| [concepts/](concepts/) | How the memory system works |
| [structure/](structure/index.md) | Starter memory tree |
| [retrieval/](retrieval/) | How to find the right files |
| [use-cases/](use-cases/) | Where this pattern pays off |

## Repository map

```
llm-memory/
├── README.md
│   ├── Idea: use a Markdown folder tree as persistent LLM memory
│   ├── Folder tree = long-term memory
│   └── LLM context window = working memory
│
├── AGENTS.md
│   └── How agents should work in this repository
│
├── concepts/
│   ├── architecture.md
│   │   ├── Markdown files are the source of truth
│   │   ├── Retrieve only relevant memories into context
│   │   └── Keep indexes/embeddings disposable and rebuildable
│   │
│   ├── memory-lifecycle.md
│   │   ├── Conversation
│   │   ├── Extract useful information
│   │   ├── Classify
│   │   ├── Store/update Markdown
│   │   ├── Retrieve when relevant
│   │   └── Inject into LLM context
│   │
│   ├── consolidation.md
│   │   ├── Raw conversations can remain logs
│   │   ├── Promote stable information into structured memory
│   │   ├── Separate facts, decisions and chronology
│   │   └── Avoid treating every conversation as permanent memory
│   │
│   └── git.md
│       ├── Git records snapshots of a folder
│       ├── A repository is the folder plus its history
│       └── GitHub is an optional copy, not git itself
│
├── structure/
│   ├── index.md
│   │   └── Compact map pointing to important memory areas
│   │
│   ├── person/
│   │   ├── profile.md
│   │   ├── preferences.md
│   │   └── communication.md
│   │
│   ├── projects/
│   │   └── example-project/
│   │       ├── overview.md
│   │       ├── state.md
│   │       ├── decisions.md
│   │       ├── research.md
│   │       ├── tasks.md
│   │       └── log/
│   │           └── YYYY-MM-DD.md
│   │
│   ├── knowledge/
│   │   └── topic/
│   │
│   └── system/
│       ├── memory-rules.md
│       └── retrieval-rules.md
│
├── retrieval/
│   ├── folder-path.md
│   │   └── Use hierarchy itself as meaningful context
│   ├── metadata.md
│   │   ├── type
│   │   ├── status
│   │   ├── updated
│   │   └── tags
│   ├── full-text-search.md
│   │   └── SQLite FTS5 suggested as a simple starting point
│   └── semantic-search.md
│       └── Embeddings can be added later
│
├── use-cases/
│   ├── personal-memory.md
│   │   └── Preferences, interests, recurring decisions and knowledge
│   ├── long-running-projects.md
│   │   └── Preserve project state across conversations
│   ├── research.md
│   │   └── Sources, findings, hypotheses and unresolved questions
│   ├── engineering-software.md
│   │   └── Requirements, architecture, experiments, bugs and rationale
│   ├── decision-history.md
│   │   └── Remember what was decided and why
│   ├── learning.md
│   │   └── Track concepts, notes, weaknesses and questions
│   ├── multi-llm.md
│   │   └── Share the same memory across ChatGPT, Claude and local models
│   ├── agents.md
│   │   └── Persistent state between agent executions
│   └── context-compression.md
│       └── Distill many conversations into compact structured knowledge
│
└── key-idea.md
    ├── Memory should be model-independent
    ├── Human-readable and editable
    ├── Portable
    ├── Searchable
    ├── Git-versionable
    ├── User-controlled
    └── .me/ could represent everything an AI collaborator should
        know that is not obvious from the project's ordinary files
```

This repository documents the idea. The starter memory tree is [structure/](structure/). In a live tree that folder *is* the root: paths in the rules look like `person/profile.md` and `projects/<name>/state.md`, not `structure/person/profile.md`.

Copy `structure/`, rename `example-project`, and fill in [structure/person/](structure/person/). A `.me/` directory at the root of an ordinary project is another shape of the same idea: everything an AI collaborator should know that is not obvious from the project's ordinary files. See [key-idea.md](key-idea.md).
