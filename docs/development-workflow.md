# Development and production workflow

## Ownership

| Area | Location | What belongs here |
| --- | --- | --- |
| Authoring | `icon_set/model/icons/` | Python originals created or revised by agents |
| Editorial source | `icon_set/metadata/` | Optional curated names, tags and descriptions |
| Build implementation | `icon_set/scripts/` | Validation, rendering, gallery and release tools |
| Development output | `icon_set/.local/dist/` | Generated SVGs, manifests and gallery |
| Development previews | `icon_set/.local/previews-png/` | Generated PNG previews |
| Development state | `icon_set/.local/state/` | Local reviews, uploads, edits, candidate jobs |
| Legacy state / supporting datasets | `icon_set/data/` | Preserved old state and existing combination datasets; never a default runtime database |
| Production releases | An external directory per release | Explicitly exported Python baseline |
| Production state | A separate external directory | Persistent production database and manual artwork |

The shared paths live in `icon_set/scripts/workspace.py`. Use those definitions
when adding tools. Model contracts still name family subfolders, independently
of which root contains a build. Original references and reviewed supporting
assets remain inputs; a normal gallery build must not regenerate them in place.

## Daily work

```sh
# Check paths and confirm generated output is not tracked.
python3 -m icon_set doctor

# Initial complete catalog; failures remain available in the Failed build view.
python3 -m icon_set build --no-png

# For subsequent edits, validate the actual module you changed.
python3 -m icon_set build --icon icon_set/model/icons/solo/example.py --no-png --no-report

# Local app and its own local database.
python3 -m icon_set dev --open
```

Replace `example.py` with the real module. A targeted build keeps previously
built icons and does not invent a complete catalog on a fresh checkout. Use
`--all` when a full revalidation is required. Builds do not create source
metadata; `python3 -m icon_set.scripts.sync_metadata` is an explicit library-wide
editorial seeding operation, not part of creating one icon.

Agent candidates get private workspaces and build folders, with the same CLI
and authoring instructions. Accepting a candidate affects development only.
No build imports saved manual artwork unless `--artwork-dir` explicitly requests
a manual export. Such an export is not accepted as a production baseline.

Build and release-export commands share an output lock. If the folder is busy,
the second operation fails without publishing a partial release. Retry after the
first operation completes. Do not run historical maintenance scripts concurrently
with a build: they remain explicit operations on supporting datasets.

## Release and rollback

```sh
python3 -m icon_set release /srv/pictographic/releases/release-001
python3 -m icon_set production \
  --dist /srv/pictographic/releases/release-001 \
  --database /srv/pictographic/state/feedback.sqlite3 \
  --host 0.0.0.0 --port 8000
```

Choose paths on the deployment machine. Export takes a snapshot, refuses to
replace an existing release, rejects baked-in manual choices, and records a
catalog fingerprint and icon counts in `release.json`. A build refuses to write
into a marked release. Export includes failed-build review data and does not
imply that all icons passed QA. Review the build result before promotion.

For updates, export a new directory, stop the server, and restart with the new
`--dist` and the **same state directory**. To roll back assets, restart with the
previous release and that same state directory. No database is copied from the
developer machine as part of release export. Keep icon identities stable so
manual choices and reviews remain associated with their icons.

Production enables manual uploads, editing, source selection, and reviews. It
has no agent manager, and rejects generation, source deletion, catalog regeneration,
and replacement of its database through the sync endpoint. Development-only
controls are hidden based on `/api/runtime`; the API enforces the boundary too.

`watch_deploy.py` is a code-update watcher, not an icon publisher. Use a dedicated
clean checkout if using it, and pass the production arguments after `--`.
It must not run against the agent authoring checkout. A new code version does not
automatically select a new asset release.

## Existing installation migration

1. Stop the existing production server and back up its persistent state directory.
2. Copy its `feedback.sqlite3` and the sibling `icon-artwork`, `stroke-edits`, and
   `reference-images` stores to the external production state directory. Preserve
   any other state folders in the backup. Copy after shutdown so database and
   artwork revisions agree.
3. Build the Python baseline, export a release, and start production with explicit
   external release and database paths.
4. Verify selected manual artwork, uploaded icons, reviews, and references before
   retiring the old installation. Pending agent jobs stay in development.

Nothing in this reconstruction moves a live server or deletes legacy state.
The local dev server now starts with its own `.local/state` database. To inspect
an old installation, use explicit `--dist` and `--database` arguments; do not
make it the default again.

The repository migration removes **80,698** legacy exports/previews from Git's
index while keeping them on disk. This is a one-time staged deletion in the next
commit. The ignore rules prevent them returning. Curated metadata and original
Python sources remain tracked. The retained files are listed in the ignored
`icon_set/.local/migrations/generated-files-retired.json` audit.

## Regression checks

```sh
python3 -m unittest \
  icon_set.tests.test_workflow_isolation \
  icon_set.tests.test_generation \
  icon_set.tests.test_metadata \
  icon_set.tests.test_icon_artwork \
  icon_set.tests.test_sub_usage_categories \
  icon_set.tests.test_generated_skills
python3 -m icon_set doctor
```

Tests use temporary directories and loopback HTTP servers. Do not test by editing
production data. Regenerate authoring skills with
`python3 icon_set/scripts/generate_skills.py` after changing their generator or
source instructions. Build output still contains aggregate catalogs; the boundary
prevents those catalogs becoming source-control churn or production state.
