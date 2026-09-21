# Development and production workflow

## Current workflow: build locally, commit, pull on production

Python files under `icon_set/model/icons/` remain the drawing source. Experiments,
reference SVGs, metadata, contracts, tests and gallery templates remain tracked.
Only temporary execution logs, process IDs, runtime databases and build caches
are ignored. Existing temporary files removed from Git tracking remain locally.

`published/` is the **only committed build output**. Prepare it locally:

```sh
python3 -m icon_set publish
python3 -m icon_set doctor
git add published icon_set/model/icons
# Include any intended code, metadata and documentation changes in the same commit.
git commit -m "Publish updated icon catalog"
git push origin icon-lib
```

The publisher builds into `icon_set/.local/publish-dist/`, reuses unchanged
Python outputs, refreshes the gallery, rejects embedded local manual artwork,
and replaces the complete `published/` directory. It omits temporary QA output
and compacts JSON catalogs for Git. Validation failures remain available in
Failed build; their artwork is excluded from the passing family manifests.
Managed review drafts may also appear in the management gallery; they retain
`release_eligible: false` and are counted separately in `release.json`.
Do not run `build --dist published`: that path is protected against direct builds.

On production, keep the **existing production database and all sibling state
folders** outside the checkout. Pull the same branch, then serve the assets:

```sh
git pull --ff-only origin icon-lib
python3 -m icon_set production \
  --database /srv/pictographic/state/feedback.sqlite3 \
  --host 0.0.0.0 --port 8000
```

Replace the example database path with the existing production path; do not
create a fresh database or copy the developer database. `production` defaults
to `published/`. Production does not build, generate icons, modify source files,
or import the local progression snapshot. Reviews, approvals, comments, uploads
and selected manual edits stay in its own persistent state. Stable icon IDs
retain their associations; approval of a specific SVG is version-specific.

For this first update, restart the server with the command above so it switches
from its old asset path. Future asset-only pulls are picked up by the running
server; restart when Python server code changes. A Git pull updates many files
individually, so use a brief maintenance window if readers must never see a
partially updated catalog. The external immutable-release workflow below remains
available when atomic asset switching is needed, but is not required for this
committed-assets setup. Disable any old watcher that builds on production.

No production migration or state copy is performed by a local publish or push.


## Ownership

| Area | Location | What belongs here |
| --- | --- | --- |
| Authoring | `icon_set/model/icons/` | Python originals created or revised by agents |
| Editorial source | `icon_set/metadata/` | Optional curated names, tags and descriptions |
| Build implementation | `icon_set/scripts/` | Validation, rendering, gallery and release tools |
| Committed production assets | `published/` | Built Python baseline and gallery; production pulls this |
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

# Export all standalone typeface heights 12–32, without building the icon library.
python3 -m icon_set typeface-sizes

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

## Optional legacy workflow: production builds after a push

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
checkout. Committed sources are synchronized into `releases/workspace/source`;
unchanged files are preserved and deleted sources are removed. The build cache
at `workspace/source/icon_set/.local/dist` persists across updates and restarts.
The current build log is always `releases/workspace/build.log`, with unbuffered
output. It is overwritten each run rather than accumulated.

On first use, the watcher seeds that cache from the active release, or an existing
`icon_set/.local/dist` or legacy `icon_set/dist` gallery in its checkout. You may
choose another existing baseline with `--seed-dist /absolute/path/to/dist`.
This copies built assets only; the original baseline is not modified or deleted.
If no baseline exists, the watcher stops with an explanation instead of silently
starting a full-library build. No migration of production state is needed again
if the previous steps have already copied it successfully.

Automatic builds use `--changed-only --no-report --no-png`. They compare current
SVG content against saved manifests and actual exported files. Unchanged passing
and failing drawings reuse their existing validation and exports; new, changed,
or missing drawings are validated and regenerated. Merely changing timestamps,
build scripts or validation rules no longer triggers a library-wide revalidation.
This intentionally keeps old validation results for unchanged drawings. To audit
the whole library under new rules, run an explicit `build --all` separately.
Shared geometry changes still rebuild affected drawings whose SVG content changes.
Gallery indexes and editorial metadata are refreshed each run. This still scans
the library and computes drawing hashes; it is not an instantaneous operation.

The server starts from the existing gallery **before** fetching commits or building.
On first startup the existing assets are frozen in a serving slot before the
working cache is changed. The watcher prints `Server is online on port ...` as
soon as it is available. Builds run in a background worker; the watcher also
monitors and restarts the server if it exits during a build.

Production alternates between **two fixed slots**, `releases/slot-a` and
`releases/slot-b`. Only the inactive slot is updated. After preparation, the
watcher atomically updates `active.json`. The same running server selects the
completed gallery at the start of each request. It does not restart or close its
listening socket for icon updates. A failed HTTP check restores the previous
pointer without stopping the server. Artwork, stroke-edit validation and QA
requests use the selected gallery and the same persistent state directory.

One prior catalog is retained for rollback, plus one persistent build cache.
The log says `Gallery updated to ... Server stayed running.` after publication.
Refresh the browser to load the updated gallery. This live switch updates assets
and frontend files; changes to Python server behavior require pulling the installed
checkout and restarting the watcher intentionally. It does not hot-reload Python
server code. Keep the watcher running (or run it under your existing service
supervisor); closing it or shutting down the machine still stops the application.

Drawing-validation failures remain in the Failed build gallery and do not block
deployment. Build/export crashes or empty catalogs keep the current version;
the latest failed log is `releases/last-failed.log`. A failed revision is attempted
once per watcher run; fix and push, or restart after resolving an environment issue.
Production state stays in the same external database and sibling storage folders.
Two watchers cannot use the same state directory concurrently.

After a successful switch the watcher removes recognisable retired releases and
abandoned preparation folders from the older deployment implementation, except
any active or rollback release. Unknown folders, state directories, migration
backups and the original seed gallery are preserved. This bounds future storage;
new icons naturally add files to the active catalog.

To manually roll back, stop the watcher and run the installed `icon_set/scripts/deploy.py`,
pointing `--dist` at the slot recorded by `active.json` as `previous` and its
`assets` and using the same production database. Restarting the watcher follows
the watched branch again, so revert the bad commit before resuming updates.
The watcher itself stays at its installed version; pull and restart it when
changing deployment orchestration code.
