#!/usr/bin/env python3
"""Query main and sub icons that still need generation for side combinations."""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from contextlib import closing
from pathlib import Path


def positive_limit(value):
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError('limit must be an integer from 1 to 500') from None
    if not 1 <= number <= 500:
        raise argparse.ArgumentTypeError('limit must be an integer from 1 to 500')
    return number


def nonnegative_offset(value):
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError('offset must be a nonnegative integer') from None
    if number < 0:
        raise argparse.ArgumentTypeError('offset must be a nonnegative integer')
    return number


def load_queue(limit=10, offset=0, *, role='all', q='', dist=None, database=None):
    if not __package__:
        sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from icon_set.scripts.workspace import DEFAULT_DIST, DEFAULT_DATABASE
    from icon_set.scripts.primitive_status import load_status
    from icon_set.scripts.side_component_queue import generation_queue

    root = Path(dist or DEFAULT_DIST)
    combinations = json.loads((root / 'gallery/combinations.json').read_text(encoding='utf-8'))
    primitives = json.loads((root / 'gallery/primitives.json').read_text(encoding='utf-8'))
    uri = Path(database or DEFAULT_DATABASE).resolve().as_uri() + '?mode=ro'
    with closing(sqlite3.connect(uri, uri=True, timeout=10)) as connection:
        statuses = load_status(connection)
    return generation_queue(combinations, primitives, statuses,
                            role=role, limit=limit, offset=offset, q=q)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('limit_number', nargs='?', type=positive_limit, default=10,
                        help='number of queue items to return (default: 10)')
    parser.add_argument('offset_number', nargs='?', type=nonnegative_offset, default=0,
                        help='starting queue offset (default: 0)')
    parser.add_argument('--role', choices=['all', 'main', 'sub'], default='all')
    parser.add_argument('--q', help='optional concept, UUID or combination search')
    parser.add_argument('--dist', type=Path, help='gallery build directory (default: workspace build)')
    parser.add_argument('--database', type=Path, help='review database (default: workspace state)')
    parser.add_argument('--all', action='store_true', help='return every item from the starting offset')
    args = parser.parse_args(argv)
    try:
        data = load_queue(args.limit_number, args.offset_number, role=args.role, q=args.q or '',
                          dist=args.dist, database=args.database)
        if args.all:
            data = load_queue(500, args.offset_number, role=args.role, q=args.q or '',
                              dist=args.dist, database=args.database)
            briefs = list(data['briefs'])
            while data['next_offset'] is not None:
                data = load_queue(500, data['next_offset'], role=args.role, q=args.q or '',
                                  dist=args.dist, database=args.database)
                briefs.extend(data['briefs'])
            data = {**data, 'offset': args.offset_number, 'limit': len(briefs),
                    'next_offset': None, 'briefs': briefs}
    except (OSError, sqlite3.Error, ValueError, KeyError) as error:
        print(f'Could not read side generation queue: {error}', file=sys.stderr)
        return 1
    json.dump(data, sys.stdout, indent=2)
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
