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

`watch_deploy.py --release-root ...` builds and promotes automatic production
releases as described below. The legacy mode with arguments after `--` only
updates server code and keeps the same asset directory; it requires a dedicated
clean checkout and does not publish new icons.

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

## Automatic production releases after a push

Use the new automatic release mode instead of the old code-only watcher:

```sh
python3 watch_deploy.py \
  --branch icon-lib \
  --release-root /srv/pictographic/releases \
  --database /srv/pictographic/state/feedback.sqlite3 \
  --host 0.0.0.0 --port 8000
```

Paths are examples; set them to the server's actual persistent directories. The
server needs the same Python/build dependencies as local development, access to
`origin`, and sufficient disk space for the current, previous and staged release.
Run this under the existing service supervisor using the intended Python interpreter.
Do not leave a separate service also starting `deploy.py` on the same port.

The watcher fetches the named branch without pulling into or modifying its own
checkout. It extracts the exact committed source into an isolated directory,
seeds the build from the last successful release, and builds with normal validation.
Identical source files retain their timestamps so cached validation and exports
remain reusable. Shared build/schema/dependency changes force full revalidation;
geometry and validation dependencies also invalidate the normal build cache.
Gallery indexes are regenerated. Builds use Python originals and never read the
production artwork store. Uncommitted local work is never deployed.

A failed build keeps the current server running and saves
`releases/failed-COMMIT.log`. Drawing-validation failures do not block deployment: passing icons and the
Failed build review gallery are published together, even when only failed
drawings exist. Empty catalogs and build/export crashes still stop promotion. A failed revision is attempted once per watcher run; fix and push a
new commit, or restart the watcher after correcting an environment problem.
The first successful release needs a full baseline build.

After preparing the assets, the watcher briefly stops the old server, starts the
new server from that release's own source directory, and checks its production
mode, gallery and unique release ID over local HTTP. Only then does it atomically
update `releases/active.json`. A failed startup stops the candidate and restarts
the previous server. Uploads, artwork, edits and reviews continue using the same
external database and sibling storage directories. Two watchers cannot use the
same state directory concurrently. This is a short restart, not zero-downtime
traffic switching.

Code and assets are retained together in `releases/COMMIT-SUFFIX/{source,assets}`.
`active.json` records the current and previous release; `build.log` records the
successful build. Releases are not automatically deleted. To manually roll back,
stop the watcher and run the previous release's
`source/icon_set/scripts/deploy.py --production --dist PREVIOUS/assets
--database /srv/pictographic/state/feedback.sqlite3 --host 0.0.0.0 --port 8000`.
Keep the same state path. Restarting the watcher will follow the watched branch
again, so revert the bad commit there before resuming automatic updates.

For an existing installation, complete the state migration described above and
stop its old launcher before starting this watcher. The initial build may take
longer; after initialization, subsequent builds run while the active server stays
available. Installing this code alone does not change the live service command.
The watcher itself stays at its installed version; restart/update its checkout
explicitly when changing deployment orchestration code.
