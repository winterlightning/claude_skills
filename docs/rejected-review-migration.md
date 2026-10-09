# Rejected review migration and local rehearsal

The migration processes every record in the supplied 379-record handoff. It
registers verified combination relationships and applies explicit text routing.
It preserves drawings and review decisions. Records requiring new geometry,
uncertain component identity or a reviewer decision remain visible in the report;
they are not marked fixed or approved.

## Actual-data rehearsal

On 2026-10-09, the relevant complete tables were exported read-only from D1
`pictographic-review-next` (the database shared by both current review URLs).
The local copy contained 84,066 icons, 24,042 references, 90,187 reviews and 94,817
drawing revisions. Routing/count tables were exported separately, so the overall
copy is not an atomic production snapshot. No production tables were changed.

Applied to a disposable SQLite copy:

| Result | Records |
| --- | ---: |
| Text routing updated | 105 |
| Combination references registered | 7 |
| Already routed | 1 |
| Drawing repair required | 60 |
| Human re-verification, rejection preserved | 64 |
| Held with specific reasons | 142 |
| Total | 379 |

The 105 routing updates comprise 78 single-character assets assigned to **Font 48**
and 27 multi-character assets assigned to the **Sub-icon** section. Seventeen of
those routed assets still have separate artwork repairs. The already-routed record
is native C5. One source drawing changed after the review and is held.

A second apply reused all seven combinations and found all 106 routing targets
already satisfied. It added no routing changes, reference registrations or audit
rows. SQLite integrity passed. All non-routing icon columns, revision SVGs, reviews,
feedback, flags, types, splits, briefs and original icon-reference links were
compared with the untouched snapshot. The gallery counts match all copied icons.

The 31 Python tests pass, including rollback and duplicate handling. An additional
Rust integration test runs the actual Worker list SQL on the applied copy and
confirms the Font 48 and Sub-icon cards and counts. Run it from `cloud/worker`:

```sh
REJECTED_REHEARSAL_DB=/absolute/path/to/rehearsal.sqlite3 \
  cargo test -p pictographic-core --test rejected_review_rehearsal -- --ignored
```

See [the complete rehearsal report](../data/rejected-correction-rehearsal.json) for
every record and its exact reason or required fix. This is evidence from a local
copy, not a production completion report or visual approval.

## Run locally

Use Python 3.10+ and an existing SQLite export of the current D1 schema. Keep an
untouched snapshot, then copy it to a disposable rehearsal database. Never use the
`-next` URL as an isolated test environment: it shares production data.

```sh
python3 -m unittest icon_set.tests.test_rejected_review_migration \
  icon_set.tests.test_container_review_migration \
  icon_set.tests.test_import_rejected_review

python3 cloud/migrate/migrate_rejected_review.py \
  --review data/rejected-correction-input-379.json \
  --db /path/to/rehearsal.sqlite3 --actor thuan \
  --report /tmp/rejected-dry-run.json

# Explicitly apply only to the disposable local file. A backup is made first.
python3 cloud/migrate/migrate_rejected_review.py \
  --review data/rejected-correction-input-379.json \
  --db /path/to/rehearsal.sqlite3 --actor thuan --apply \
  --report /tmp/rejected-applied.json

# Repeat with a new report path; expect reused/already_routed, no new writes.
python3 cloud/migrate/migrate_rejected_review.py \
  --review data/rejected-correction-input-379.json \
  --db /path/to/rehearsal.sqlite3 --actor thuan --apply \
  --report /tmp/rejected-rerun.json
```

The migration requires the full tables `icons`, `references`, `reference_parts`,
`icon_references`, `reviews`, `split_requests`, `activity_log`,
`review_data_migrations`, `upload_families`, `icon_counts`, and `icon_facet_counts`.
Include revisions, feedback, flags, types and briefs when checking preservation.
Use the repository's Wrangler configuration and existing authentication to export
these tables read-only; keep exports and SQLite files outside Git. Retain all rows,
not only the 379 reviewed icons, because deduplication checks the whole reference
catalog and counts cover the whole icon catalog. Import exported SQL inside one
local transaction and run `PRAGMA integrity_check` before migration.

Default mode rehearses in an in-memory copy. `--apply` backs up and transactionally
changes only the explicitly named local file. No HTTP calls occur in the migration.
Existing report files are refused. The report includes input SHA-256 and each
record's outcome. Database/validation failures roll back the transaction.

## Rules and review decisions

Container pairs compare ordered `container`/`symbol` IDs; side pairs compare
ordered `main`/`sub` IDs. They never deduplicate across types. One existing exact
pair is reused. Multiple matches are held. A missing pair registers the original
reference as a combination, retaining its metadata. A missing source ID may be
resolved from exactly one actual icon-reference link; ambiguous or absent links
remain held. Source revision, current approval/claim, rejection and component
existence are checked before writing. Unknown or approximate component matches
and required role adaptations remain held. No new primitive identity is invented.

Font 48 uses the existing custom-family registry, reusing an exact matching family
or creating `font-48` with canvas size 48. Only reviewed single-character assets
already on a 48px canvas are eligible. Multi-character text uses the existing
Sub-icon list's `side_role='sub'` routing. Its original family, canvas and profile
are retained: routing is not a conversion into a 32px drawing. Stable icon keys,
assets and source links are retained. Record/card metadata, version groups and
stored family/section counts are updated consistently.

Thuan should verify these routing semantics and the seven registered pairs before
any production procedure is considered. The report carries drawing briefs and
review questions for the remaining records. This PR does not supply new geometry,
resolve approximate candidates by guessing, clear rejections, or deploy changes.
The previously requested container-only preparer remains available; see
[container migration](container-reference-migration.md).
