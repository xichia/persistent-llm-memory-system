# The Living Repository

Give Codex a project folder it can return to.

In a long chat, useful details get buried: what you are trying to do, what changed, why you made a choice, and what comes next. A small tree of Markdown files gives those details a home. You can read it, correct it, and ask Codex to use it in a fresh chat.

For example, you are planning a skill-share for 12 people. The budget falls from 60 to 40. Save the current budget in the project state, the reason for the change in decisions, and the next action in tasks. Tomorrow, Codex can read those files instead of asking you to explain the project again.

| Benefit | What you do |
| --- | --- |
| Less repeating yourself | Save a short project handoff before leaving |
| A clear next step | Keep current state and open tasks together |
| Visible reasoning | Record decisions and why they changed |
| Easy corrections | Edit the actual text when something is wrong |
| Context you own | Keep ordinary files that people and other tools can read |

**[Start with the practical guide](guide.md).** It walks through opening a local folder in the Codex app, doing one useful task, saving the result, and resuming in a new chat. No programming or command-line knowledge is needed.

Here, “repository” means an organized home for your project material. A Git repository adds version history; that can come later. The starting workflow uses ordinary folders and files.

## Try it

1. Download this repository using GitHub’s **Code → Download ZIP**, then extract it.
2. Copy the extracted [structure/](structure/) folder somewhere you keep your own work. Rename the copy `my-ai-workspace`.
3. Follow [the guide](guide.md) to connect that copy to Codex. Keep your personal working copy separate from this public teaching repository.

The starter includes [collaboration instructions](structure/AGENTS.md), a [file map](structure/index.md), and a [project template](structure/projects/example-project/overview.md). Begin with one project; fill other areas only when useful. Markdown (`.md`) is plain text with simple headings and lists.

## The file tree

```text
my-ai-workspace/
├── README.md                 How to use this folder
├── AGENTS.md                 How Codex should collaborate
├── index.md                  Where to find things
├── projects/
│   └── example-project/
│       ├── overview.md       Purpose and constraints
│       ├── state.md          What is true now
│       ├── decisions.md      Choices and reasons
│       ├── tasks.md          Next actions
│       ├── research.md       Sources and unknowns
│       └── log/              Optional chronology
├── person/                   Optional preferences and working style
├── knowledge/                Notes useful across projects
└── system/                   Rules for reading and updating memory
```

The folder tree is long-term memory. The context window is working memory. Codex still needs to read the relevant files, and you still need to check what it writes. Saving files does not make every chat automatically aware of everything in the folder.

## Explore when useful

| Path | What it offers |
| --- | --- |
| [guide.md](guide.md) | The beginner workflow in the Codex app |
| [structure/](structure/README.md) | A starter folder you can copy |
| [example/](example/README.md) | A fictional skill-share showing saved project context |
| [key-idea.md](key-idea.md) | Why memory belongs in files you control |
| [concepts/](concepts/architecture.md) | Deeper notes on memory and consolidation |
| [retrieval/](retrieval/folder-path.md) | Finding relevant files as the tree grows |
| [use-cases/](use-cases/long-running-projects.md) | Uses in research, learning, and ongoing projects |
| [MIGRATION.md](MIGRATION.md) | How this edition relates to the supplied course ZIPs |

Start with the guide and starter. The other notes are optional background, including the existing Git and search material.
