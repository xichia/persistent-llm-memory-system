# Memory rules

Save only information that will help future work: confirmed facts, explicit decisions, current project state, useful findings, and stated preferences. Do not save every conversation.

## Choose the file

| Information | File, relative to this folder |
| --- | --- |
| Standing personal facts | `person/profile.md` |
| Recurring choices | `person/preferences.md` |
| Tone and format | `person/communication.md` |
| Project purpose and scope | `projects/<name>/overview.md` |
| Current position and blockers | `projects/<name>/state.md` |
| Explicit choices and reasons | `projects/<name>/decisions.md` |
| Sources, findings, and open questions | `projects/<name>/research.md` |
| Next actions | `projects/<name>/tasks.md` |
| Optional chronology | `projects/<name>/log/YYYY-MM-DD.md` |
| Reusable topic knowledge | `knowledge/<topic>/overview.md` |

Keep facts separate from decisions. Label uncertainties as open questions or hypotheses in research notes; do not present them as facts. Logs describe what happened, while state describes what is true now.

## Review an update

1. Propose the affected files and exact changes before editing memory.
2. Review accuracy and remove anything unnecessary or private.
3. Before substantial changes, make a backup copy of the folder.
4. Apply the approved edits and review the changed files.

Prefer existing files. Update overview and state in place. Add dated decisions with reasons; mark superseded decisions rather than silently replacing them. Remove completed tasks. Add index links for new projects or topics.

When filling a template, replace its prompts and set `status: active`. If you use an `updated` field, set it to the actual date of the change. Never infer missing personal details.

Do not store secrets, copy entire chats into state, or duplicate material already maintained elsewhere. Never automatically publish or share memory files. Version history can be added later; reviewing files and keeping backups is enough to begin.
