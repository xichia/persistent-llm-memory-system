# Context compression

Distill many conversations into compact structured knowledge.

The context window cannot hold a month of chats. It should not try. Compression here is not "summarize this thread into three bullets in the prompt". It is **promotion into files that stay small on purpose**.

## From volume to structure

```
many conversations
    → logs (optional, bulky, rarely loaded)
    → structured files (small, loaded on demand)
    → a few files in the current prompt
```

Each arrow drops information on purpose. That is [consolidation](../concepts/consolidation.md).

A good `state.md` is already a compression of everything that happened. A good `decisions.md` is a compression of every debate. A good `profile.md` is a compression of every time you corrected the model about yourself.

## What to compress toward

| Raw | Compact form |
| --- | --- |
| A week of "where are we?" | `state.md` |
| Arguments about a library | one dated entry in `decisions.md` |
| Repeated tone complaints | a line in `communication.md` |
| Ten papers | findings + sources in `research.md` or `knowledge/<topic>/` |
| A sprawling thread about tasks | a short `tasks.md` |

The compact form should be the working set. If you still need to paste the original threads, compression failed or you are doing archaeology (then open a log).

## What not to do

- Do not replace the tree with an ever-growing "master summary.md". That file becomes another transcript.
- Do not auto-summarize every chat into the tree. Most chats compress to *nothing*.
- Do not keep both the full dump and the summary in the default retrieval set. Default to the structured file.

## Working memory as a budget

Treat injection as a size budget. If the retrieved set is large, the tree needs a better summary file, not a bigger context window. Often the missing compression is: update `state.md` and stop loading logs.

The folder tree is long-term memory because it can be large. The context window is working memory because it must stay small. Compression is the discipline that connects them.
