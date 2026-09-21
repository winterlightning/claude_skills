# Icon workflow audit and migration (historical)

**Superseded on 2026-09-21.** The separate `.local` development build, the
publication staging folder and the untracked `icon_set/data/` datasets described
below were removed: an ignored build folder was wiped and the color, fill,
duotone and animation experiments were only recoverable from an old copy.
`published/` is now the single, tracked build root, datasets are tracked, and
runtime state lives in `icon_set/state/`. See
[the development workflow](development-workflow.md). The text below records
why the earlier boundary was introduced.


The code audit found these causes:

1. Git tracks 71,378 files in `icon_set/dist`, 9,320 PNG preview files and
   10,752 files in `icon_set/metadata` at the time of the audit. These counts are
   tracked inventory, not a claim that every file changes for each new icon.
2. `build._build_selected` stages entire selected family directories, publishes
   metadata for every carried-forward record, and rebuilds the combined gallery.
   `--icon` limits validation, but does not make publication a one-file operation.
3. `metadata.publish_metadata` previously called `load_metadata(create=True)`.
   A build could therefore seed missing JSON files throughout the source library.
   It also rewrote every output metadata sidecar whether its content changed or not.
4. The builder defaulted to the same `data/icon-artwork` store as the server.
   Generation acceptance explicitly passed that store to its rebuild command.
   Manual selections therefore entered the Python-generated baseline.
5. One server offered manual editing/uploading alongside generation acceptance,
   source deletion, catalog refresh and state replacement. `watch_deploy.py`
   pulled code into that same checkout, so server-side source mutations and
   generated tracked assets could obstruct deployment pulls.

The new default boundary is:

- Source: Python modules and optional curated metadata in Git.
- Development output: ignored `.local` build folders; no implicit manual choices.
- Production release: explicitly exported assets outside the checkout.
- Production state: external persistent SQLite database and sibling artwork,
  edit and reference stores, applied at request time.

Production mode blocks the routes that cross back into source development or
replace state. Existing manual upload/edit APIs remain available. Release export
never touches the production database, never overwrites a release, and rejects
manual selections baked into manifests. It must run when the source build is idle.
It copies the catalog as built, including failed-build review data; it is not an
additional quality approval or a full-library validation command.

The reconstruction now removes the 80,698 legacy exports/previews from Git
tracking while preserving every local file. Source metadata remains tracked.
The local runtime database is separate under `.local/state`. Active maintenance
scripts, generated skills and agent candidate workspaces follow the shared path
module. A single CLI exposes build, dev, release, production and doctor commands.

A real build revealed two additional side effects: catalog staging called the
role-export refresh routine (rewriting a shared JSON dataset and source assets),
and profile-report staging wrote its summary into a work directory. Both are now
read-only with respect to source inputs. Explicit maintenance commands retain
their intended writes. Missing optional historical experiment components no
longer prevent a clean development build.

Builds and release exports use a shared output lock. Release snapshots carry a
catalog fingerprint and cannot be reused as build destinations. Production
advertises its capabilities, hides development-only controls, and enforces the
same restrictions at the API. See [the development workflow](development-workflow.md)
for commands and migration.

Publication still stages aggregate catalogs; this reconstruction isolates that
cost rather than claiming an O(1) build. Live production rollout remains explicit.

Validation of the reconstruction: 70 focused workflow tests passed, covering
production restrictions, manual artwork persistence, candidate isolation,
metadata publication, source-read-only staging, output locks and generated skill
consistency. The gallery rollback regression also passed. A real check-mark build and release export succeeded, and the
release catalog matched its recorded fingerprint. Temporary smoke outputs were
removed afterwards. The workspace doctor reports zero tracked generated files.

The broader historical typeface snapshot tests still expect 95 samples where
the existing catalog has 97; those two assertions are outside this refactor.
The separate skill-creator frontmatter checker could not run because PyYAML is
absent; the repository's generated-skill tests and generator consistency check
passed. No live production migration or full-library geometry revalidation was
performed.
