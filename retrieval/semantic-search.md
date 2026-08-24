# Semantic search

Embeddings can be added later.

They are useful when you need "notes like this" and the words do not match: a paraphrase, a half-remembered idea, a concept filed under a name you forgot. They are not a prerequisite for this memory system, and they are not the source of truth.

## Add them when

- Path, metadata, and FTS miss real files you later find by hand
- The tree is large enough that you no longer remember the vocabulary you used
- You are matching a *question* to *notes that answer it*, not looking up a known term

If those are not happening, skip this layer. A vector index you do not need still has to be rebuilt, versioned, and distrusted.

## Keep them disposable

- Embed the Markdown files (or stable sections), never "instead of" the files
- Record the embedding model and chunking rules next to the index so a rebuild is possible
- Changing model = full reindex, not a memory migration
- Retrieval still returns **paths**. The chunk is a pointer into a file you then open

This matches the architecture rule: indexes are caches. See [../concepts/architecture.md](../concepts/architecture.md).

## How they fit the order

```
path → metadata → full-text → embeddings
```

Use semantic search as a fallback or as a second list merged with FTS, not as the only retriever. Folder path often already has the right file. Embeddings should not outrank `projects/foo/state.md` on a question about foo's status just because a log contains similar language.

## Chunking

If you chunk:

- Prefer headings and existing files over sliding windows
- Keep the path and heading with every chunk
- Do not embed daily logs into the default index, or tag them so they can be excluded
- Re-embed a file when it changes; do not accumulate stale vectors

Small files (`state.md`, `profile.md`) can be one chunk each. That is a feature of keeping memory compact.

## Cost and lock-in

Embeddings choose a model, a distance function, and usually a vendor or a local weight file. That is the opposite of the [key idea](../key-idea.md) unless the vectors stay optional.

Practical compromise:

- Generate embeddings locally when you can
- Store them next to the repo or in a rebuildable DB, listed in `.gitignore` so git does not snapshot them ([../concepts/git.md](../concepts/git.md))
- Never require the index in order to use the tree by hand

The Markdown remains readable if the vectors disappear.
