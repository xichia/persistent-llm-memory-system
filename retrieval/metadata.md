# Metadata

Small, regular frontmatter on each **memory** file — the files under [../structure/](../structure/), not the documentation in `concepts/`, `retrieval/`, `use-cases/`, or the README. Enough to filter without parsing the whole page.

Suggested fields:

```yaml
---
type: overview | state | decisions | research | tasks | log | profile | preferences | communication | knowledge | rules | index
status: active | draft | archived | template | superseded
updated: YYYY-MM-DD
tags: [project-name, domain, …]
---
```

## type

What kind of memory the file *is*, independent of where it sits.

Use `type` when a search returns mixed files and you only want decisions, or only current state. Paths often imply type (`decisions.md`); the field makes that queryable and survives a rename.

Keep the vocabulary small. A new `type` should correspond to a retrieval behavior ("never load logs by default"), not to a one-off label.

## status

Lifecycle, not quality.

| Value | Meaning | Retrieval |
| --- | --- | --- |
| `active` | Current memory | Default include |
| `draft` | Not settled | Include only when editing it |
| `template` | Example / blank | Skip unless scaffolding |
| `archived` | Finished or abandoned | Skip unless explicitly researching history |
| `superseded` | Replaced by another file | Skip; follow the replacement |

Archiving a project is often a `status` change plus a folder move. Either is fine if retrieval respects it.

`status: superseded` is for replacing a **whole file**. An individual decision that was reversed stays in `decisions.md` and is marked superseded in the entry — the file itself stays `active`. See [../use-cases/decision-history.md](../use-cases/decision-history.md).

## updated

Date of the last real edit to the content (not a whitespace touch).

Use it to:

- Prefer a newer `state.md` over an older log
- Find stale files (`updated` older than some threshold)
- Show a human what has changed recently

Bump it whenever you change the file. Retrieval may treat a missing `updated` as oldest.

## tags

Optional, flat, lowercase. Tags are for cross-cutting queries the folder tree cannot express: `health`, `tax-2026`, `oncall`, a shared theme across projects.

Do not duplicate the path in tags. If the file is already in `projects/example-project/`, an `example-project` tag adds noise unless you need to mark related files *outside* that folder.

## Rules

- Frontmatter is metadata, not a second copy of the note. Do not put the decision itself in YAML.
- Unknown fields are allowed; retrieval should ignore what it does not understand.
- Indexes may copy these fields. The file remains the source of truth. See [../concepts/architecture.md](../concepts/architecture.md).

If a filter needs a field you do not have, add it when the need is real. Four fields are enough to start.
