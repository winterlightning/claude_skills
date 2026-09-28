#!/usr/bin/env python3
"""Discard published icons that are pixel-identical re-generations of one primitive.

python3 icon_set/scripts/find_duplicates.py --within-folder --exclude gallery/ --exclude qa/ \\
    --exclude failed/ --same-source same.csv -q
python3 icon_set/scripts/apply_same_source_dedupe.py --list same.csv            # dry run
python3 icon_set/scripts/apply_same_source_dedupe.py --list same.csv --apply

Rows whose ``blocked`` column is set are reported and skipped. Each applied drop
goes through discard_icon.discard_many, the same path as the gallery's Discard
action: the model and its record are archived beside the database, the model
file (or class) is removed, the published SVG, metadata sidecar and preview PNG
are deleted, review rows go, the family manifest and gallery/icons.json are
rewritten, and the activity log records the discard. Afterwards the primitives
catalog is refreshed so the review page keeps every primitive generated through
the kept icon. Nothing is committed.

A build that started before the discard republishes its own snapshot, files
included, when it finishes; the script refuses to apply while a ``.icon-build-*``
staging folder is active. The next full build after the discard prunes the
outputs anyway, because it only keeps records for models still in the registry.
"""
from __future__ import annotations

import argparse
import collections
from contextlib import closing
import csv
import json
from pathlib import Path
import sqlite3
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.discard_icon import discard_many, plan_source_removal  # noqa: E402


def active_stages(dist: Path, seconds: int = 120) -> list[Path]:
    """build.py staging folders touched recently: a build in flight will republish its own snapshot."""
    import time
    cutoff = time.time() - seconds
    return sorted(stage for stage in dist.glob(".icon-build-*") if stage.is_dir() and stage.stat().st_mtime >= cutoff)


def load_rows(path: Path) -> tuple[list[dict], list[dict]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    applicable = [row for row in rows if not row.get("blocked")]
    return applicable, [row for row in rows if row.get("blocked")]


def main(argv=None) -> int:
    from icon_set.scripts.deploy import DEFAULT_DB, init_database, record_activity

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--list", type=Path, required=True, help="CSV from find_duplicates.py --same-source")
    parser.add_argument("--apply", action="store_true", help="Discard the icons (default: dry run)")
    parser.add_argument("--database", type=Path, default=DEFAULT_DB)
    parser.add_argument("--dist", type=Path, default=REPO_ROOT / "published")
    parser.add_argument("--user", default="dedupe", help="Recorded as the actor in the activity log")
    parser.add_argument("--force", action="store_true", help="Apply even while a build is staging into --dist")
    args = parser.parse_args(argv)

    applicable, blocked = load_rows(args.list)
    catalog = json.loads((args.dist / "gallery" / "icons.json").read_text(encoding="utf-8"))
    by_key = {row["key"]: row for row in catalog["icons"] + catalog.get("failed_icons", []) if row.get("key")}

    icons, missing = [], []
    for row in applicable:
        record = by_key.get(row["drop_key"])
        (icons if record else missing).append(record or row)
    print(f"{len(applicable)} drops listed, {len(blocked)} blocked, {len(missing)} not in gallery/icons.json")
    for row in blocked:
        print(f"  blocked  {row['drop']}  ({row['blocked']})")
    for row in missing:
        print(f"  missing  {row['drop']}  {row['drop_key']}")

    if not args.apply:
        indexes: dict = {}
        errors = 0
        for row, icon in zip([r for r in applicable if by_key.get(r["drop_key"])], icons):
            try:
                plan = plan_source_removal(REPO_ROOT, icon, indexes)
                print(f"  drop     {row['drop']}  <- keep {row['keep']}  ({plan['path'].relative_to(REPO_ROOT)})")
            except (ValueError, SyntaxError) as error:
                errors += 1
                print(f"  ERROR    {row['drop']}: {error}")
        print(f"\ndry run: {len(icons) - errors} would be discarded, {errors} errors; pass --apply to proceed")
        return 1 if errors else 0

    staging = active_stages(args.dist)
    if staging and not args.force:
        print(f"a build is staging in {staging[0].name}; it would write its pre-discard snapshot back over "
              f"{args.dist}. Wait for it to finish, or pass --force.", file=sys.stderr)
        return 2

    init_database(args.database)
    with closing(sqlite3.connect(args.database, timeout=10)) as connection, connection:
        result = discard_many(icons, source_root=REPO_ROOT, dist=args.dist,
                              connection=connection, user=args.user)
        for row in result["discarded"]:
            record_activity(connection, args.user, "discard", row["icon"], svg_sha256=by_key[row["icon"]].get("svg_sha256"),
                            source=row["source"], archive=row["archive"], reason="same-source duplicate")
    print(f"discarded {len(result['discarded'])}, failed {len(result['failed'])}")
    for row in result["failed"]:
        print(f"  failed   {row['icon']}: {row['error']}")
    removed = collections.Counter(row["removed_rows"].get("reviews", 0) for row in result["discarded"])
    print(f"  review rows removed: {sum(k * v for k, v in removed.items())}")

    from icon_set.scripts.primitives_catalog import main as refresh_catalog
    refresh_catalog(["--dist", str(args.dist)])
    return 1 if result["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
