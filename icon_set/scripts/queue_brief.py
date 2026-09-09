#!/usr/bin/env python3
"""Queue two component briefs after visually rejecting a combined reference.

python3 icon_set/scripts/queue_brief.py --file work/pending-brief/split.json
The JSON must contain reference_path, combination_type, reason and two components.
Each component gets a source copy, brief.md and brief.json under work/pending-brief/<family>/.
Use --files-only to save handoffs without adding records to the review database.
"""
import argparse
from contextlib import closing
import hashlib
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from icon_set.scripts.brief_queue import init_brief_queue, enqueue_split
from icon_set.scripts.split_handoff import save_split_handoffs


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file', required=True, type=Path)
    parser.add_argument('--database', type=Path, default=ROOT/'icon_set/data/feedback.sqlite3')
    parser.add_argument('--out', type=Path, default=ROOT/'work/pending-brief')
    parser.add_argument('--files-only', action='store_true', help='Save source/brief bundles without writing the review database')
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.file.read_text(encoding='utf-8'))
        if not isinstance(data, dict):
            raise ValueError('Expected one split JSON object.')
        reference = (ROOT / data['reference_path']).resolve()
        if not reference.is_relative_to(ROOT) or reference.suffix.lower() not in ('.svg', '.png') or not reference.is_file():
            raise ValueError('reference_path must be an existing SVG or PNG inside this repository.')
        key = 'reference:' + reference.relative_to(ROOT).as_posix()
        sha = hashlib.sha256(reference.read_bytes()).hexdigest()
        # If supplied, target the reviewed generated icon and its current revision.
        if data.get('icon'):
            catalog = json.loads((ROOT/'icon_set/dist/gallery/icons.json').read_text())['icons']
            icon = next((item for item in catalog if item['key'] == data['icon']), None)
            if not icon:
                raise ValueError('Unknown icon key in current gallery.')
            if not any(item['source_path'] == reference.relative_to(ROOT).as_posix() for item in icon.get('original_sources', [])):
                raise ValueError('Reference is not linked to the supplied icon.')
            key, sha = icon['key'], icon['svg_sha256']
        for folder in save_split_handoffs(reference, data, args.out.resolve()):
            print(f'Saved component handoff: {folder}')
        if args.files_only:
            return 0
        args.database.parent.mkdir(parents=True, exist_ok=True)
        with closing(sqlite3.connect(args.database)) as connection, connection:
            init_brief_queue(connection)
            split_id = enqueue_split(connection, key, sha, reference.relative_to(ROOT).as_posix(), data)
        print(f'Queued split {split_id}: two component icons in Pending briefs.')
    except (OSError, ValueError, KeyError, TypeError, sqlite3.Error) as error:
        parser.exit(1, f'error: {error}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
