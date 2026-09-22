#!/usr/bin/env python3
"""Fetch the primitives generation queue from the local icon_set deploy server."""
import argparse
import json
import sys
import sqlite3
from contextlib import closing
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


def load_local_generation_queue(family='solo', limit=10, offset=0, *,
                                dist=None, database=None, **extra):
    """Read the gallery's queue locally without HTTP or modifying runtime state.

    Paths must refer to the same build and database as the intended gallery.
    Missing files or schemas raise errors; they never become an empty queue.
    """
    if not __package__:
        sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from icon_set.scripts.workspace import DEFAULT_DIST, DEFAULT_DATABASE
    from icon_set.scripts.deploy import ADMIN_USERS
    from icon_set.scripts.primitive_briefs import generation_queue, load_primitive_briefs
    from icon_set.scripts.primitive_status import load_status
    from icon_set.scripts.primitive_decision_history import load_history

    catalog = json.loads((Path(dist or DEFAULT_DIST) / 'gallery/primitives.json').read_text(encoding='utf-8'))
    uri = Path(database or DEFAULT_DATABASE).resolve().as_uri() + '?mode=ro'
    with closing(sqlite3.connect(uri, uri=True, timeout=10)) as connection:
        connection.execute('BEGIN')
        statuses = load_status(connection)
        briefs = load_primitive_briefs(connection)
        history = load_history(connection, ADMIN_USERS)
    params = dict(family=family, limit=limit, offset=offset, **extra)
    query = {key: [str(value)] for key, value in params.items() if value is not None}
    return generation_queue(catalog, statuses, briefs, query, history)


def fetch_generation_queue(base_url, family='solo', limit=10, offset=0, **extra):
    params = {'family': family, 'limit': limit, 'offset': offset}
    params.update({k: v for k, v in extra.items() if v is not None})
    url = f'{base_url.rstrip("/")}/api/primitives/generation-queue?{urlencode(params)}'
    with urlopen(url, timeout=30) as response:
        return json.load(response)


def nonnegative_offset(value):
    try:
        offset = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError('offset must be a nonnegative integer') from None
    if offset < 0:
        raise argparse.ArgumentTypeError('offset must be a nonnegative integer')
    return offset


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('offset_number', nargs='?', type=nonnegative_offset,
                        help='starting queue offset (default: 0); for example: generation_queue.py 10')
    parser.add_argument('--base-url', default='http://localhost:8000')
    parser.add_argument('--offline', action='store_true', help='read the local catalog and database without HTTP')
    parser.add_argument('--dist', type=Path, help='offline gallery build directory (default: workspace build)')
    parser.add_argument('--database', type=Path, help='offline review database (default: workspace state)')
    parser.add_argument('--family', default='solo', choices=['solo', 'sub'])
    parser.add_argument('--limit', type=int, default=10, help='1-500')
    parser.add_argument('--offset', type=nonnegative_offset,
                        help='starting queue offset; alternative to the positional number')
    parser.add_argument('--category', help='optional category filter')
    parser.add_argument('--brief', choices=['ready', 'missing'], help='optional brief-state filter')
    parser.add_argument('--q', help='optional text search')
    parser.add_argument('--all', action='store_true', help='follow next_offset until the queue is exhausted')
    args = parser.parse_args(argv)
    if args.offset_number is not None and args.offset is not None:
        parser.error('pass the offset either as a positional number or with --offset, not both')
    offset = args.offset if args.offset is not None else (args.offset_number or 0)
    if (args.dist or args.database) and not args.offline:
        parser.error('--dist and --database require --offline')

    def fetch(offset):
        filters = dict(category=args.category, brief=args.brief, q=args.q)
        if args.offline:
            return load_local_generation_queue(args.family, args.limit, offset,
                                               dist=args.dist, database=args.database, **filters)
        return fetch_generation_queue(args.base_url, args.family, args.limit, offset, **filters)

    try:
        data = fetch(offset)
        if args.all:
            briefs = list(data['briefs'])
            while data.get('next_offset') is not None and len(briefs) < data['total']:
                data = fetch(data['next_offset'])
                briefs.extend(data['briefs'])
            data = {'total': data['total'], 'briefs': briefs}
    except HTTPError as error:
        body = error.read().decode('utf-8', 'replace')
        print(f'HTTP {error.code}: {body}', file=sys.stderr)
        return 1
    except URLError as error:
        print(f'Could not reach {args.base_url}: {error.reason}', file=sys.stderr)
        return 1
    except (OSError, sqlite3.Error, ValueError, KeyError) as error:
        print(f'Could not read generation queue: {error}', file=sys.stderr)
        return 1

    json.dump(data, sys.stdout, indent=2)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
