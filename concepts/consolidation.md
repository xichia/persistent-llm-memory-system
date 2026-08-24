# Consolidation

Not every conversation should become permanent memory.

Consolidation is the process of turning raw interaction into a small number of durable files — and of refusing to do that when nothing durable happened.

## Raw conversations can remain logs

Keep transcripts if they are useful as evidence or as a diary. Store them as logs, not as the knowledge base.

A log answers: *what happened on this date?*

```
projects/example-project/log/2026-08-25.md
```

Logs are allowed to be messy, incomplete, and local. They may quote the conversation, list dead ends, or record a working session that led nowhere. That is fine, because nothing else is required to read them.

Do not retrieve every log into future context. Retrieve logs when you need chronology ("why did we pause this?") or when consolidating them into structured files.

## Promote stable information into structured memory

After a session — or in a periodic pass — promote only what has settled:

| Promote | Leave in the log (or discard) |
| --- | --- |
| A decision that will constrain future work | The hour of debate before the decision |
| A preference the user confirmed | A one-time "let's try it this way today" |
| Project state that is still true | A resolved blocker |
| A finding with a source | A search query that did not pan out |
| A correction to the profile | A guessed fact that was never confirmed |

Promotion means **writing or updating** `overview.md`, `state.md`, `decisions.md`, person files, or a knowledge topic — not appending the whole session to those files.

If the structured file and the log disagree, fix the structured file. The log can keep the historical wording.

## Separate facts, decisions, and chronology

These three rot at different rates and should not share a page.

**Facts** change when the world changes. "The API is on port 8080." "I am based in Singapore." Put them in profiles, overviews, and knowledge topics. Update in place.

**Decisions** are facts plus rationale, and they are append-mostly. "We chose SQLite FTS5 because we do not want a vector database yet." Later you may supersede a decision; you rarely silently edit the original away. See [use-cases/decision-history.md](../use-cases/decision-history.md).

**Chronology** is what happened, in order. Daily logs, research timelines, incident notes. Chronology explains the path; it is not the current map.

Mixing them produces files that are neither good summaries nor good histories: stale status buried in narrative, or decisions with no date and no "why".

A simple split per project:

```
overview.md     facts about what this is
state.md        facts about where it stands now
decisions.md    decisions and rationale
research.md     findings, sources, open questions
tasks.md        current work
log/YYYY-MM-DD.md   chronology
```

## Avoid treating every conversation as permanent memory

Default to forgetting.

Most chats are scaffolding: debugging, wording tweaks, "what does this function do?", a plan that was replaced an hour later. Writing all of that into long-term memory pollutes retrieval. The model then spends working memory on noise.

Practical rules:

- **No write without a promotion reason.** "We talked" is not a reason. "We decided", "state changed", "preference stated", "finding worth keeping" are.
- **Cap file growth.** If `state.md` is more than a page or two, it is absorbing chronology. Move history to the log and keep `state.md` current.
- **Archive, don't hoard.** Completed projects can move to an `archive/` folder so they stop showing up in default retrieval.
- **Deduplicate on write.** Before adding a bullet, check the target file. Update the existing line.
- **Human veto.** Automated extraction should propose diffs. It is better to miss a memory than to enshrine a wrong one.

Forgetting is a feature. The folder tree stays small enough that retrieval can stay simple — often just opening the right path.

Git versions what you *did* keep. It is not a reason to promote every conversation: history of a small `state.md` is more useful than a repository full of unfiltered transcripts. See [git.md](git.md) if you have never used a repository.

## A consolidation pass

A lightweight periodic pass (end of day, end of week, or end of an agent run):

1. Read new logs and any unprocessed transcripts.
2. Ask: did facts, decisions, state, or preferences change?
3. If no, stop. Leave the log as a log.
4. If yes, patch the structured files and bump `updated`.
5. Optionally delete or archive transcripts that have been fully promoted.

This is the opposite of "save everything." It is how a Markdown tree stays a memory instead of becoming a second email inbox.
