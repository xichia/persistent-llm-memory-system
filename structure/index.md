---
type: index
status: active
updated: 2026-08-25
tags: [map, navigation]
---

# Memory index

Compact map of this tree. Load this file first when you need to know what exists without listing everything.

In this repository the memory layout lives under `structure/`. In a live memory tree, this file sits at the root and paths look like `person/profile.md`, not `structure/person/profile.md`.

## Person

Who the memory is about, how they work, how to talk to them.

- [person/profile.md](person/profile.md) — identity, context, constraints
- [person/preferences.md](person/preferences.md) — tastes, defaults, non-negotiables
- [person/communication.md](person/communication.md) — tone, format, what to skip

## Projects

One folder per project. Copy `example-project/` to start another.

- [projects/example-project/overview.md](projects/example-project/overview.md) — what it is
- [projects/example-project/state.md](projects/example-project/state.md) — where it stands
- [projects/example-project/decisions.md](projects/example-project/decisions.md) — what was chosen and why
- [projects/example-project/research.md](projects/example-project/research.md) — sources and findings
- [projects/example-project/tasks.md](projects/example-project/tasks.md) — open work
- [projects/example-project/log/](projects/example-project/log/) — chronology (`YYYY-MM-DD.md`)

## Knowledge

Topics that outlive a single project. One folder per topic.

- [knowledge/topic/overview.md](knowledge/topic/overview.md) — template for a topic area (duplicate the folder, do not pile topics into one file)

## System

Rules for writing and reading this tree. Load these when creating, updating, or retrieving memory.

- [system/memory-rules.md](system/memory-rules.md) — what to store, where, and how to update
- [system/retrieval-rules.md](system/retrieval-rules.md) — what to load for a given task

## How to use this map

- For a personal question, start with `person/`.
- For continuing a project, start with that project's `state.md` and `overview.md`.
- For "why did we do it this way?", start with `decisions.md`.
- For "what do we know about X?", start with `knowledge/` then project `research.md`.
- Do not load logs unless you need chronology.

Keep this index short. When a new durable area appears, add one line here — not a summary of the files it points to.
