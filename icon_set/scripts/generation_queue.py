#!/usr/bin/env python3
"""Fetch the primitives generation queue from the local icon_set deploy server."""
import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


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

    try:
        data = fetch_generation_queue(args.base_url, args.family, args.limit, offset,
                                      category=args.category, brief=args.brief, q=args.q)
        if args.all:
            briefs = list(data['briefs'])
            while data.get('next_offset') is not None and len(briefs) < data['total']:
                data = fetch_generation_queue(args.base_url, args.family, args.limit, data['next_offset'],
                                              category=args.category, brief=args.brief, q=args.q)
                briefs.extend(data['briefs'])
            data = {'total': data['total'], 'briefs': briefs}
    except HTTPError as error:
        body = error.read().decode('utf-8', 'replace')
        print(f'HTTP {error.code}: {body}', file=sys.stderr)
        return 1
    except URLError as error:
        print(f'Could not reach {args.base_url}: {error.reason}', file=sys.stderr)
        return 1

    json.dump(data, sys.stdout, indent=2)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
