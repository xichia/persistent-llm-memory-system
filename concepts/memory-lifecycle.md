# Memory lifecycle

A conversation is not memory. Memory is what you keep after the conversation.

The loop:

```
Conversation
    → Extract useful information
    → Classify
    → Store or update Markdown
    → Retrieve when relevant
    → Inject into LLM context
```

Then the next conversation starts, already holding a small, relevant **working set** — the files injected into the context window.

## Conversation

Work happens in a chat, an agent run, an IDE session, or a note you write yourself. That activity *fills* working memory: it is messy, local, and mostly disposable.

Do not treat the transcript as the system of record. Transcripts are raw material. Most of them should stay logs, or not be kept at all.

## Extract useful information

After (or during) a session, pull out only what would still matter later:

- Stable facts about a person, project, or topic
- Decisions and the reasons for them
- Current state ("blocked on X", "chose Y")
- Preferences that should affect future behavior
- Sources, findings, and open questions worth revisiting
- Corrections to something already stored

Throw away:

- Small talk and one-off troubleshooting that did not change the world
- Information already obvious from project files
- Speculative asides that were not adopted
- Duplicates of what the tree already says

Extraction can be done by a human, by an LLM pass over the transcript, or both. The output should be small.

## Classify

Decide *where* the information belongs. Classification is mostly a folder question. Paths below are relative to the memory tree root (in this repository that root is [../structure/](../structure/)):

| Kind of information | Typical home |
| --- | --- |
| Who someone is | `person/profile.md` |
| How they like to work | `person/preferences.md`, `person/communication.md` |
| What a project is | `projects/<name>/overview.md` |
| Where a project stands | `projects/<name>/state.md` |
| What was decided and why | `projects/<name>/decisions.md` |
| Sources and findings | `projects/<name>/research.md` or `knowledge/<topic>/` |
| Work to do | `projects/<name>/tasks.md` |
| What happened today | `projects/<name>/log/YYYY-MM-DD.md` |
| How this memory system itself behaves | `system/` |

If it is chronology, it goes in a log. If it is a durable conclusion, it goes in a structured file. Do not mix those two. See [consolidation.md](consolidation.md).

## Store or update Markdown

Write the smallest change that makes the tree true.

- **Update in place** when a profile, preference, or project state has changed.
- **Append** to logs and to decision lists (decisions are rarely rewritten silently; they are superseded).
- **Do not duplicate.** If `state.md` already says the deploy is blocked, the daily log can point at it instead of restating it.
- **Record metadata.** `type`, `status`, `updated`, `tags` on the file help later retrieval. See [retrieval/metadata.md](../retrieval/metadata.md).

Prefer editing an existing file over creating a new one. A memory tree that grows a file per thought becomes unretrievable.

## Retrieve when relevant

On a new task, load the files that are likely to matter — not the whole tree.

Start with [index.md](../structure/index.md) if you need the layout, then path, then metadata, then full-text search, and only then embeddings. Details in [retrieval/](../retrieval/).

Retrieval is part of the lifecycle, not a separate product. If you cannot find a memory, it might as well not have been stored.

## Inject into LLM context

Place the retrieved files (or the relevant sections) into the prompt as the working set, alongside the current user request.

Good injections are:

- **Small.** A few files beat a dump.
- **Located.** Include the path so the model knows where the knowledge lives and can propose updates to the right file.
- **Current.** Prefer `state.md` over an old log when they disagree; the structured file is supposed to be the summary.

The model then works, and the cycle repeats: extract, classify, write.

## Ownership of each step

| Step | Who can do it |
| --- | --- |
| Conversation | Human, model, agent |
| Extract / classify / store | Human, model with review, or a scheduled consolidation pass |
| Retrieve / inject | The tool wrapping the model: a skill, a script, an agent, or a human pasting files |

The Markdown tree does not require an autonomous writer. It works if you update files by hand. Automation is useful once the layout is stable.
