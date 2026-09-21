# Production updates: pull prebuilt assets

Build and publish on the development machine. Commit the resulting `published/`
assets to `icon-lib` with the intended source changes. Production serves those
files directly and never needs to build icons.

## Prepare an update locally

```sh
python3 -m icon_set publish
python3 -m icon_set doctor
git add published
# Stage the intended Python, metadata, template and documentation changes too.
git diff --cached --stat
git commit -m "Publish updated icon catalog"
git push origin icon-lib
```

Finish the build before committing. Include new files and deletions under
`published/`, so production receives the complete catalog, SVGs and gallery.
Uncommitted local changes are not delivered by a production pull.

## One-time production setup

Stop the old `watch_deploy.py` process if it is still running. It builds releases
and serves a different directory. From the production repository, start this
server instead, using the existing production database:

```sh
python3 -u icon_set/scripts/deploy.py \
  --production --dist published \
  --database "$HOME/pictographic-production/state/feedback.sqlite3" \
  --host 0.0.0.0 --port 8000
```

Keep this process running through the existing service supervisor or terminal.
If it already serves `published/` with this database, no setup change is needed.

## Every subsequent icon update on production

From the production repository:

```sh
git pull --ff-only origin icon-lib
```

Refresh the browser after the pull completes. The running server detects changed
catalog files. No build, database import or server restart is needed for icon
assets and gallery HTML/CSS/JavaScript updates. A pull is not an atomic directory
swap; requests during the pull can briefly see a partially updated catalog.

Restart the same server command when Python server code changes. Pulling Python
files does not replace code already loaded by a running process.

## Data ownership

- Git delivers built icons, catalog metadata and gallery files in `published/`.
- Production retains its own reviews, approvals, comments, uploads and edits in
  `$HOME/pictographic-production/state/`. Keep the database and sibling stores
  together. They are not committed or replaced by a pull.
- Development progression and local reviews do not overwrite production state.
- Active counts can differ when the two installations have different rejection
  decisions or uploads, even with identical published assets.

Do not run `build`, `publish` or the build watcher on production. If a fast-forward
pull fails, resolve the checkout divergence; do not replace it with a hard reset
that could discard local work.
