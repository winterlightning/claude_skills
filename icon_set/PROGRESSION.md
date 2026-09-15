# Publishing primitive review progress

`progression.sqlite3` is the committed publication snapshot. It contains primitive
SKIP decisions, explicit TODO restores, separate component briefs and positions,
and archived category review records (including uncertain and deferred cases).
It excludes authentication, sessions, and unrelated gallery feedback.

After a local review, refresh the snapshot:

```sh
python3 -m icon_set.scripts.progression
```

Commit `icon_set/progression.sqlite3` and push. Deploy the repository with
`icon_set/scripts/progression.py` and restart the gallery server. At startup,
`deploy.py` merges the snapshot into its persistent feedback database. Newer
production decisions and explicit TODO restores take precedence; equal timestamps
retain the production record. Repeated startup imports are safe.

The server continues using its existing writable database. The committed snapshot
is not modified by web requests. Back up the production database separately.
A push publishes repository data; your hosting system must still deploy the new
revision and restart the server. Static hosting alone cannot serve the status API.

SQLite snapshots have binary Git diffs. Regenerate from the authoritative local
review database rather than attempting to merge binary conflict markers.
