# Register reviewed container combinations

`cloud/migrate/migrate_container_review.py` converts the reviewed data into migration
input and registers container/symbol reference relationships in an explicit local
D1 SQLite snapshot. It preserves artwork, feedback, review status and icon family.
It does not call the cloud API or run against production.

Prepare the 90 container cases from the complete handoff:

```sh
python3 cloud/migrate/migrate_container_review.py prepare \
  --review data/rejected-correction-input-379.json \
  --out data/container-reference-migration-90
```

The bundle contains `input.json`, the byte-for-byte `source-review.json`, and
`component-check.json` with a reason for every held record. Preparation accepts the
original visual-review format and the `pictographic-correction-handoff/v1` format.
Side combinations and all other recommendations are excluded. The default count
check requires 90; `--expect-count` supports explicitly scoped batches.

The supplied 379-record handoff (SHA-256
`47f4f365c56d7b230d916dacb4b1100cdf97e1f894268bd5a6ae8029be119446`)
yields 5 records ready for a database check and 85 held for component decisions.
These are source-data checks, not confirmation that any pair is missing from the
current database. Multiple hold reasons may apply to one record.

Rehearse against a separately obtained local snapshot:

```sh
python3 cloud/migrate/migrate_container_review.py migrate \
  --input data/container-reference-migration-90/input.json \
  --db /absolute/path/to/local-d1-snapshot.sqlite3 \
  --actor reviewer-name > /tmp/container-migration-report.json
```

The default runs in memory and leaves the snapshot untouched. `--apply` explicitly
applies to that local file after making a consistent SQLite backup. All writes are
one transaction, with rollback on error. This is not a production deployment
procedure; do not replace production with the modified snapshot.

For each record the migration checks the source drawing hash, current-revision
rejection (or active split), source-reference link, and existence of both component
references. It compares ordered `container` and `symbol` reference IDs across the
database, including relationships registered earlier in the same batch:

- One exact pair: reuse its combination reference; create nothing.
- No exact pair: classify the original source reference as a combination and add
  its two parts, or create that reference under its supplied ID if absent.
- Multiple exact pairs, a conflicting source mapping, missing references or stale
  source state: hold and report the reason.

Side pairs, reversed roles and composites with extra parts do not count as exact
container pairs. Newly registered parts have no chosen drawing or layout. Existing
reference metadata is retained. Registration adds migration and activity records;
repeat runs reuse the registered pair without creating additional records.

Unresolved, nested, approximate or role-adapted components require an explicit
review decision. The migration never invents a primitive ID or infers absence
from a failed lookup. Pass a JSON decision file with `--decisions` when resolved:

```json
{
  "decisions": {
    "solo/example": {
      "container_reference_id": "verified-container-id",
      "symbol_reference_id": "verified-symbol-id",
      "reason": "Reviewed both independent references for this relationship.",
      "reviewed_by": "reviewer-name"
    }
  }
}
```

These decisions resolve component identity only. Database existence, revision,
source linkage, pair conflicts and combination-type checks still apply. This
script does not approve artwork or create the missing component drawings.

Validation:

```sh
python3 -m unittest icon_set.tests.test_container_review_migration \
  icon_set.tests.test_import_rejected_review
```

Tests use the repository's D1 schema in temporary databases. The initial container-only tests did not include a live snapshot. The subsequent
[all-record rehearsal](rejected-review-migration.md) used a read-only copy of the
current data and records its exact results. Database snapshots are not committed.
