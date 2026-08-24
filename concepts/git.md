# Git repositories

This page is for readers who have never used git. It covers only what you need in order to give a Markdown memory tree a history. You do not need to be a programmer.

Git is how this design keeps memory **versioned**: you can see what changed, undo a bad edit, and keep the same files in sync across machines. The [key idea](../key-idea.md) calls that *git-versionable*. The rest of git — branches, pull requests, rebasing — can wait.

## Git is not GitHub

Git and GitHub are easy to confuse:

| | What it is | Do you need it? |
| --- | --- | --- |
| **Git** | A program on *your computer* that records snapshots of a folder | Yes, if you want history |
| **GitHub** (or GitLab, Codeberg, …) | A *website* that can store a copy of that folder | No. Optional backup and sync |

Git works fully offline. A GitHub account is only useful later, if you want a remote copy. Personal memory should almost always be a **private** copy if you put it on a website at all.

## A repository is a folder with history

A **repository** (often shortened to **repo**) is an ordinary folder that git has started watching.

When you turn a folder into a repository, git creates a hidden directory named `.git` inside it. You never edit `.git` by hand. It is the filing cabinet of snapshots. Your Markdown files stay ordinary files in the same folder; git just remembers how they change.

```
my-memory/                 ← the folder you work in (the "working tree")
├── person/
│   └── profile.md         ← a normal file you can open
├── projects/
└── .git/                  ← git's private history (do not edit)
```

Analogy: the folder is the notebook you write in. Git is a stack of dated photocopies. You still write in the notebook. You choose when to take a photocopy. Each photocopy is a **commit**.

That is the whole idea. Everything else is a way to make a commit, look at old commits, or copy the notebook-plus-photocopies to another place.

## Why a memory tree wants this

Markdown is already memory. Git adds time.

- **See when something flipped.** "When did I decide against a vector database?" is `git log` on `decisions.md`.
- **Undo a bad write.** If a model overwrites your profile with something wrong, an older commit still has the previous text.
- **Review before accepting.** `git diff` shows the exact lines an agent changed. You commit only if they are true.
- **Sync without a vendor memory feature.** A laptop and a desktop can share the same history.
- **Diff beats a chat recap.** Two snapshots of `state.md` are checkable. A generated "summary of our conversations" is not.

Git is a particularly good fit because it tracks **lines of text**. Markdown is lines of text. A binary database of embeddings is not — which is one reason those indexes stay disposable. See [architecture.md](architecture.md).

## Five words

| Word | Meaning |
| --- | --- |
| **Repository** | A folder git is tracking, including the hidden `.git` history |
| **Commit** | One snapshot of the files, with a date, an author, and a short message |
| **Diff** | The lines that changed between two snapshots (or between now and the last snapshot) |
| **Remote** | A copy of the repository somewhere else (another folder, or a host like GitHub) |
| **Clone** | A full copy of a repository, files *and* history, usually from a remote |

You will also see **working tree**: that just means the files as they look right now, on disk, as opposed to the snapshots in `.git`.

## Install git

In a terminal, run:

```bash
git --version
```

If you get a version number, git is installed. If not:

- **macOS:** install the Xcode command-line tools when the system offers them, or install git via Homebrew (`brew install git`).
- **Windows:** install from [git-scm.com](https://git-scm.com).
- **Linux:** use your package manager (`sudo apt install git`, `sudo dnf install git`, …).

Once, tell git who you are. These strings are stored on each commit. They do not have to match an email you publish, but they should be stable:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

`--global` means "for every repository on this machine." You can override them later in one repo if you need to.

## Turn a memory folder into a repository

Examples below assume your repository root *is* the memory tree (`person/`, `projects/`, …). In this documentation repository those folders live under `structure/`.

In a terminal, go to the folder that holds the Markdown tree (a copy of `structure/`, or this project if you are versioning the docs too):

```bash
cd path/to/your-memory-folder
git init
```

`git init` creates `.git/`. The folder is now a repository. Nothing has been snapshotted yet.

If your computer hides "dot files," you may not see `.git` in the Finder. That is normal.

## The daily loop

You will do these five steps over and over. Editing the Markdown is the real work; git only records it.

### 1. Edit files as usual

Change `person/preferences.md`, update a project's `state.md`, whatever the [memory lifecycle](memory-lifecycle.md) calls for. Save the files.

### 2. Ask what changed

```bash
git status
```

Git lists files that differ from the last commit: new, modified, or deleted. Until you have made a first commit, *everything* looks new.

### 3. Read the diff (this is the review step)

```bash
git diff
```

This prints the lines added and removed in files you have not yet staged. A line starting with `+` was added; a line starting with `-` was removed.

If an LLM or an agent wrote the change, **read this before you snapshot it.** Wrong memory is worse than missing memory.

### 4. Choose what belongs in the next snapshot

```bash
git add person/preferences.md
git add projects/example-project/state.md
```

Or, when you mean "everything currently different":

```bash
git add -A
```

`git add` does not upload anything. It only marks files for the **next** commit. This marking step is called *staging*. Think of it as loading a box before you seal it.

### 5. Seal the snapshot

```bash
git commit -m "Note preference: prefer local models for personal memory"
```

The quoted sentence is the **commit message**. Write it so that future you can scan a list of messages and know what happened.

Useful messages for this tree look like:

- `Update example-project state: FTS5 still deferred`
- `Record decision: Markdown is the source of truth`
- `Correct profile location`

Useless messages look like `updates`, `WIP`, or `stuff`.

A commit is local. It lives in `.git` on your machine. It is not on GitHub unless you later push it.

### First commit

The first time, after `git init`:

```bash
git add -A
git commit -m "Start memory tree"
```

You now have history of length one.

## Look at the past

```bash
git log --oneline
```

One line per commit: a short id and the message.

```bash
git log -p -- person/profile.md
```

The history of one file, including the diffs.

```bash
git show HEAD
```

`HEAD` means "the commit I am on right now," usually the latest. `git show` prints that snapshot's message and diff.

To put one file back the way it was in the last commit (throw away uncommitted edits to that file):

```bash
git restore person/profile.md
```

To recover a file as it existed in an older commit, copy the id from `git log --oneline` and run:

```bash
git restore --source=abc1234 -- person/profile.md
```

(Use the real id, not `abc1234`.) You still need to `git add` and `git commit` if you want that restoration to become the latest snapshot.

You do not need more than this to treat git as an undo log for memory.

## Optional: a copy somewhere else

A **remote** is a name for another copy of the same repository. `origin` is the conventional name for "the main other copy."

Reasons to add one:

- Backup (disk failure should not delete your memory)
- A second computer
- Sharing with your future self, not with the internet at large

If the memory includes a profile, preferences, or anything you would not paste into a public page, create the remote as **private**.

On GitHub, for example: create a new **private** repository (empty, no README), then in your folder:

```bash
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git push -u origin main
```

If `git push` complains that your branch is called `master`, use `master` instead of `main`, or rename once with `git branch -M main`.

On another machine:

```bash
git clone https://github.com/YOUR_USER/YOUR_REPO.git
```

**Clone** downloads the files *and* the history. After that, the loop gains two commands:

```bash
git pull     # bring this machine up to date from the remote
git push     # send your new commits to the remote
```

Pull before you start, push when a batch of memory updates is done. If two machines (or two models) edit the same file without pulling, git will ask you to merge. That is the ordinary cost of two copies. It is still better than two invisible vendor memories you cannot compare. See [../use-cases/multi-llm.md](../use-cases/multi-llm.md).

You can skip remotes entirely and still get local history, diffs, and undo.

## Reviewing what a model wrote

This is the reason git belongs in an LLM memory system, not only in software projects.

1. Let the model edit Markdown (or propose a patch).
2. Run `git diff`.
3. Keep, edit, or `git restore` each file.
4. `git add` / `git commit` only the lines that should become long-term memory.

The commit is the acceptance step. An agent that writes files without a later diff-and-commit is writing unreviewed memory. [Memory rules](../structure/system/memory-rules.md) prefer a proposed diff over a silent rewrite of standing facts; git is how you see that diff.

## What not to commit

Git will happily snapshot anything you `git add`. Do not add:

- Secrets (API keys, passwords, tokens)
- Disposable indexes (`memory.db`, embedding vectors, chunk caches)
- Huge binary blobs that are not memory

A `.gitignore` file in the repository root lists names git should skip. Example:

```
.DS_Store
memory.db
*.sqlite
*.embeddings
.cache/
```

Files that match are still on disk. They are just not part of the repository's history. That matches the architecture: Markdown is durable; indexes are rebuildable.

If you accidentally commit a secret, changing the file in a later commit is **not** enough — the secret stays in history. Rotate the secret and, if the repo was ever pushed, treat it as leaked. Prevention is much easier than cleanup.

## You do not need the rest of git yet

Ignore these until a real problem requires them:

- **Branches** — parallel lines of history. One line of commits is enough for a personal memory tree.
- **Pull requests / merge requests** — a hosted way to review someone else's commits. Useful on a team; optional alone.
- **Rebase, cherry-pick, submodules, hooks** — later, if ever.

If `git status` ever says you are in the middle of a merge and you are lost, it is valid to copy your Markdown files somewhere safe, ask for help, or start from a known-good commit. The files are still the source of truth.

## If you would rather not use the terminal

The concepts are the same in [GitHub Desktop](https://desktop.github.com), VS Code's Source Control panel, and other git UIs:

1. See the changed files (status).
2. Open the diff and read it.
3. Commit with a message.
4. Optionally push to a private remote.

Use whichever interface you will actually run. The repository on disk is identical.

## How this page fits the rest of the tree

- [architecture.md](architecture.md) — files in git are durable; indexes are not
- [memory-lifecycle.md](memory-lifecycle.md) — commit after you store or update Markdown, not after every chat
- [consolidation.md](consolidation.md) — git history is not an excuse to promote every conversation; it only versions what you *did* keep
- [../use-cases/agents.md](../use-cases/agents.md) — commits record which run wrote what
- [../use-cases/long-running-projects.md](../use-cases/long-running-projects.md) — a remote is how two days and two machines share `state.md`
