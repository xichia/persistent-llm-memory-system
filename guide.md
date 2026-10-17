# Work with Codex from a folder

A chat is a useful place to think. A folder gives that thinking somewhere to live.

Keep your plans, decisions, and current work in Markdown (`.md`) files. Codex can read the relevant files, help with a task, and update them. When you return in a fresh chat, the files give you a starting point without retelling the whole story.

The benefits are practical:

- **Continuity:** the latest plan survives a change of chat.
- **Visibility:** you can open a file and see what Codex is relying on.
- **Control:** correct a mistake or remove an outdated fact in its file.
- **Organization:** each project has a home for its state, decisions, and next steps.
- **Portability:** the work is ordinary text in folders you can copy and keep.

Think of this as a repository of your work: a place to collect and maintain it. Start with an ordinary folder. You do not need to set up Git or publish anything to use this guide.

## 1. Copy the starter folder

In Finder or File Explorer, copy this repository's entire [structure](structure/) folder somewhere you keep your work. Rename the copy `my-ai-workspace`.

Copy the whole folder so its instructions and links stay together. Inside your copy, the layout looks like this:

```text
my-ai-workspace/
├── README.md                 Start here
├── AGENTS.md                 Instructions for Codex
├── index.md                  Map of the files
├── person/                   Your relevant preferences and context
├── projects/
│   └── example-project/
│       ├── overview.md       Purpose and constraints
│       ├── state.md          Current position and next step
│       ├── decisions.md      Choices and their reasons
│       ├── research.md       Findings and sources
│       ├── tasks.md          Work still to do
│       └── log/              Dated history, when useful
├── knowledge/                Notes useful across projects
└── system/                   Rules for maintaining the files
```

You can leave most files as templates until you need them. Begin with one project.

Before practice edits, duplicate `my-ai-workspace` as a backup. If an edit goes wrong, compare the changed file with the backup and restore the affected text.

## 2. Give Codex access to the folder

Open the Codex desktop app and add a local project connected to `my-ai-workspace`. Choose local work in that folder for this walkthrough. You need the desktop app installed and signed in with access to Codex; opening the public repository in a web browser does not give Codex access to your copied folder. If the project already exists, its menu provides **Edit project** to add or change its folders. Make your workspace the primary folder so new chats start there. Labels can vary by app version; see the [official project instructions](https://learn.chatgpt.com/docs/projects).

Start a chat inside that project. Ask Codex to confirm its location before changing files:

```text
Tell me the exact folder you are working in. It should be my-ai-workspace.
Read AGENTS.md and index.md, then projects/example-project/overview.md
and state.md. Summarize what you found. Do not change files yet.
```

If it cannot find those files, reconnect the folder before continuing.

## 3. Do one useful task

For a first example, give Codex a small plan to maintain. The starter asks Codex to show proposed edits before saving them. Review the proposal, request corrections if needed, then tell it to apply the agreed changes. Use that same review step for later updates and the final handoff.

```text
Turn example-project into a skill-share planning project called skill-share.
There will be 12 people. The total project budget is $60. We have not chosen
a venue. Replace the template content with those facts and update index.md
to point to the renamed folder. Suggest a simple session plan within the budget;
label any estimated costs. Show me which files changed and what you saved.
```

Ask Codex, “Open the saved project state.md in the app so I can inspect it.” Read the text in the file panel. If you spot an error, say, “Correct this sentence in state.md: …; show me the saved file again.” Check the actual files Codex changed. The overview should describe the skill-share, the state should retain the unknown venue, and the tasks should include choosing one. Suggestions should remain suggestions until you accept them.

Then try a change:

```text
The total project budget is now $40. Revise the plan for 12 people, record the
budget change in decisions.md, and update the current state and tasks.
Keep the venue marked as unknown. Check that no current plan still uses $60.
```

The old budget can remain in the decision history; the current plan should use $40.

You can compare your result with the fictional [worked example](example/README.md).

## 4. Save a handoff

Before leaving, ask:

```text
Save a short handoff in projects/skill-share/state.md: current facts,
unresolved questions, the next useful step, and a pointer to decisions.md. Update tasks.md
if needed. Read back the saved files and summarize what changed.
```

Open those files yourself. A message saying “saved” is less useful than seeing the right information on disk.

## 5. Resume in a fresh chat

Start another chat in the same local project:

```text
Confirm you are working in my-ai-workspace. Read AGENTS.md and index.md,
then projects/skill-share/overview.md, state.md, decisions.md, and tasks.md.
Tell me the current headcount, budget, unresolved questions, and next step.
```

It should find 12 people, a $40 budget, and an undecided venue from the files. If it does not, correct the files before continuing.

Repeat the same cycle for real work: read the relevant files, complete one task, review the changes, and save the next starting point.
