# Icon workspace ownership

Use `python3 -m icon_set` as the common entry point. The original script entry
points remain supported. Read `docs/development-workflow.md` for the workflow.

- Author Python originals under `icon_set/model/icons/`. Curated search metadata
  under `icon_set/metadata/` is source data: preserve editorial changes.
- Default build output is `icon_set/.local/dist/`; PNG previews are under
  `icon_set/.local/previews-png/`. Both are disposable and ignored by Git.
  Read paths from `icon_set/scripts/workspace.py` in application code.
- `icon_set/dist/` and `icon_set/assets/previews-png/` are preserved legacy output,
  not active publication targets. Do not restore them to Git tracking.
- For one icon: `python3 -m icon_set build --icon PATH --no-png --no-report`.
  Do not seed metadata for the full library as a side effect of creating an icon.
- Agent builds use Python originals. Manual artwork choices and browser edits
  belong to the server's persistent state; do not overwrite them from a build.
- `published/` is the one committed production asset directory. Refresh it using
  `python3 -m icon_set publish`, which builds Python originals in
  `icon_set/.local/publish-dist/` before replacing the complete publication.
  Commit source changes and `published/` together; production pulls this branch
  and serves `published/` without building. Never build directly into it.
- Production keeps its own database, uploads, edits and reviews outside the
  checkout. Never import local progression snapshots into production.
- Keep experiments and reference SVGs. Remove only temporary execution output
  from tracking, retaining local copies when cleaning up existing files.
- Do not commit other build output, runtime databases, candidate workspaces, or previews.
  `python3 -m icon_set doctor` checks generated-file tracking.
- Edit skill generator/source instructions, then run `generate_skills.py`.
  Do not hand-edit generated `.agents/skills` or portable `skills` copies.
- Preserve unrelated working changes. Test workflow boundaries using
  `test_workflow_isolation`, `test_generation`, `test_metadata`, and relevant
  upload/edit tests; use temporary output directories for tests.
