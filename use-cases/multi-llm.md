# Multi-LLM

Share the same memory across ChatGPT, Claude, Grok, and local models — anything that can read files.

The long-term store is the folder, not a feature inside one product. Each model gets a **working set** copied or retrieved into its context. Writes go back to the same Markdown.

## Why this matters

- You will not use one model forever
- Different models are good at different tasks; they should not keep separate, drifting memories
- Local models should not be second-class citizens with no access to "the real" memory
- Switching tools should not mean re-teaching who you are

## How to share

There is no special format. Any tool that can include files in a prompt can participate:

- Paste or `@`-attach `state.md` and `preferences.md`
- Point a repo-aware agent at the tree (or at `.me/`)
- Run a small retriever that prints paths + contents into stdin
- Keep the tree in a git repository so every machine and every CLI sees the same snapshot. See [../concepts/git.md](../concepts/git.md) if you have never used a repository.

Rules files ([../structure/system/memory-rules.md](../structure/system/memory-rules.md), [../structure/system/retrieval-rules.md](../structure/system/retrieval-rules.md)) travel with the memory so each model is instructed the same way.

## Avoid per-model stores

Do not "also" enable ChatGPT memory, Claude memory, and a local vector store as competing sources of truth. They will diverge. If a product offers built-in memory, treat it as a cache or turn it off.

Embeddings, if you add them, must be rebuildable and optional so a model with no embedder can still use path + grep. See [../retrieval/semantic-search.md](../retrieval/semantic-search.md).

## Write-back

The hard part is not reading; it is agreeing where updates go. Convention:

- Same paths for everyone (`projects/<name>/state.md`, not `claude-state.md`)
- Same frontmatter
- Git (or another sync) before the next tool session if two models might write. If you are using a remote: `git pull`, then work, then `git push`.

If two models edit unsynced copies, you have the ordinary merge problem. That is preferable to two invisible memories you cannot diff.
