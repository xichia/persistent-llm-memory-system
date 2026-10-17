# Your memory folder

Keep useful context in Markdown files so you and Codex can return to a project without starting over. You can read, correct, move, or delete every note yourself.

This folder is a starter. Copy it to a location of your choice, then open that folder as a project in Codex. Keep personal information in your own copy. You can start with ordinary files; setting up version history or publishing anything can wait.

## Start with one project

1. Rename `projects/example-project/` for your project.
2. Fill in its `overview.md` with the purpose and desired outcome.
3. Write today's position in `state.md` and the next few actions in `tasks.md`.
4. Update the links in [index.md](index.md) to match the new name.
5. Start a chat in Codex and ask it to read `AGENTS.md`, `index.md`, and your project's overview, state, and tasks before working.

The other files are available when you need them. Empty templates are prompts to fill in, not facts about you.

## Continue in a new chat

Try this prompt, replacing `<project-name>`:

> Read AGENTS.md and index.md, then projects/<project-name>/overview.md, state.md, and tasks.md. Tell me where the project stands and help me with the next task. Read other files only if relevant.

At the end of useful work, ask:

> Propose the smallest memory update that would help us continue next time. Show the files and changes before editing. Keep confirmed facts, decisions, and open questions separate.

Review the proposal before accepting it. Before a substantial edit or reorganisation, make a backup copy of the folder. Compare the changed files afterwards and correct anything inaccurate.

## Where things belong

- [index.md](index.md) is the map.
- [projects/example-project/overview.md](projects/example-project/overview.md) starts a project; its neighbouring files hold current state, decisions, research, and tasks.
- [person/profile.md](person/profile.md), [preferences.md](person/preferences.md), and [communication.md](person/communication.md) are optional personal context.
- [knowledge/topic/overview.md](knowledge/topic/overview.md) holds reusable topic notes.
- [system/memory-rules.md](system/memory-rules.md) explains updates; [retrieval-rules.md](system/retrieval-rules.md) explains what to read.
- [AGENTS.md](AGENTS.md) gives Codex instructions for this folder.

Use only the parts that help. A useful project can begin with overview, state, and tasks. Nothing in this workflow requires sharing or publishing your folder.
