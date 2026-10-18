# Maintain this repository

Read [README.md](README.md) and [guide.md](guide.md) first.

- Concise and elegant is the North Star. Prefer removing duplication to adding explanations.
- `guide.md` is the source for [the PDF](output/pdf/course-guide.pdf). Rebuild it with `python3 tools/build_pdf.py` after guide changes; render and inspect every page.
- Keep the PDF's teal, muted gold, serif headings, fine rules, and landscape cover.
- Both PDF title pages share the cover in `tools/build_pdf.py`. After cover changes, run `python3 tools/build_pdf.py --extended-cover` (also requires `pypdf`); preserve the extended guide's remaining pages.
- `my-ai-workspace/` and `example/` each contain a map, Codex instructions, and project state, decisions, and tasks. Starter links must work after copying the folder.
- Teach the Codex app with ordinary local Markdown files. No Git lessons, editor installation, or timed assessments.
- Keep facts, unknowns, decisions, and actions distinct. Use fictional example details.
- Review changes and check links before committing. Do not publish personal learner files.

This checkout has a separate Git directory. Do not initialise a nested repository.
