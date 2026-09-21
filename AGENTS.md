# Icon workspace ownership

Use `python3 -m icon_set` as the common entry point. The original script entry
points remain supported. Read `docs/development-workflow.md` for the workflow.

- Author Python originals under `icon_set/model/icons/`. Curated search metadata
  under `icon_set/metadata/` is source data: preserve editorial changes.
- There is one build output, `published/`, and Git tracks it: family SVG
  exports and manifests, the gallery, failed builds, reports and PNG previews.
  `build`, `dev`, `publish` and `release` all read and write it. Read paths from
  `icon_set/scripts/workspace.py` in application code; never hard-code them.
- Supporting datasets in `icon_set/data/`, experiments in `icon_set/work/` and
  the experiment snapshots in `icon_set/assets/experiments/` are tracked source
  data. A build must not regenerate, seed or delete them as a side effect.
- Runtime state lives only in the ignored `icon_set/state/`: the review database
  and its backups, uploads, stroke edits, agent jobs and API keys. The only
  other ignored build output is `published/qa/`, the per-icon validation
  evidence, which every build regenerates.
- For one icon: `python3 -m icon_set build --icon PATH --no-png --no-report`.
  Do not seed metadata for the full library as a side effect of creating an icon.
- Agent builds use Python originals. Manual artwork choices and browser edits
  belong to the server's persistent state; do not overwrite them from a build.
- Before committing icons run `python3 -m icon_set publish`. It builds the
  changed originals into `published/`, rejects embedded manual artwork, compacts
  the JSON catalogs for Git and writes `release.json`. Commit source changes and
  `published/` together; production pulls this branch and serves `published/`
  without building.
- Production keeps its own database, uploads, edits and reviews outside the
  checkout. Never import local progression snapshots into production.
- `icon_set/.local/`, `icon_set/dist/` and `icon_set/assets/previews-png/` are
  retired folders kept on disk only. Nothing reads or writes them any more; do
  not restore them to Git tracking.
- Edit skill sources in `.claude/skills/` or the generator, then run
  `generate_skills.py`. Do not hand-edit generated `.agents/skills` or portable
  `skills` copies.
- Preserve unrelated working changes. Test workflow boundaries using
  `test_workflow_isolation`, `test_publish`, `test_generation`, `test_metadata`,
  and relevant upload/edit tests; use temporary output directories for tests.
  `python3 -m icon_set doctor` confirms no runtime state is tracked and no
  build output or dataset is left uncommitted.
