#!/usr/bin/env python3
"""Compare the Worker with the Python server it replaces, route by route.

    # Old server on a COPY of the database (never the live file), new Worker on the imported copy:
    python3 icon_set/scripts/deploy.py --production --dist published --database /tmp/parity/feedback.sqlite3 --port 8799
    python3 cloud/migrate/verify.py --old http://127.0.0.1:8799 --new http://127.0.0.1:8787

Only GET routes are compared (reads never change data). JSON is compared structurally: object
key order is ignored, list order is not. Per-icon routes are checked for a sample of icons that
have feedback, claims, flags and types. Exits 1 when any route differs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import urllib.parse
import urllib.request

ROUTES = [
    '/api/reviews', '/api/reviews?include_approvers=1', '/api/feedback-feed',
    '/api/reviewer-stats', '/api/reviewer-stats?period=all', '/api/reviewer-stats?start=2026-09-01&end=2026-09-25&family=solo',
    '/api/work', '/api/work/queue', '/api/work/queue?limit=500&offset=10', '/api/work/disapproved?limit=500',
    '/api/work/review', '/api/work/review?state=done', '/api/icon-types', '/api/icon-types?type=uploaded&status=ready',
    '/api/pending-briefs', '/api/icon-families', '/api/icon-categories',
    '/api/primitives/summary', '/api/primitives/status', '/api/primitives/briefs', '/api/primitives/symbol-links',
    '/api/primitives?category=accessories', '/api/primitives?status=skip', '/api/primitives/prompt?format=json&category=computers',
    '/api/primitives/prompt?category=computers&count=3&offset=2', '/api/auth/session',
]
PER_ICON = ['/api/review-detail?icon={}', '/api/feedback?icon={}', '/api/icon-type?icon={}', '/api/icon-flag?icon={}',
            '/api/work/history?icon={}', '/api/work?icon={}']
# Fields the old server computes from local files the cloud does not have (documented differences).
IGNORED = {'/api/runtime'}


def fetch(base: str, path: str) -> tuple[int, bytes, str]:
    request = urllib.request.Request(base.rstrip('/') + path, headers={'Accept': 'application/json', 'User-Agent': 'pictographic-verify/1.0'})
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            return response.status, response.read(), response.headers.get('Content-Type', '')
    except urllib.error.HTTPError as error:
        return error.code, error.read(), error.headers.get('Content-Type', '')


def normalize(value):
    """Floats that are whole numbers compare equal to ints (SQLite vs D1 number handling)."""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, list):
        return [normalize(v) for v in value]
    if isinstance(value, dict):
        return {k: normalize(v) for k, v in value.items()}
    return value


def first_difference(old, new, where='$'):
    if type(old) is not type(new):
        return f'{where}: {type(old).__name__} {json.dumps(old)[:120]} != {type(new).__name__} {json.dumps(new)[:120]}'
    if isinstance(old, dict):
        for key in sorted(set(old) | set(new)):
            if key not in old or key not in new:
                return f'{where}.{key}: only in {"old" if key in old else "new"}'
            found = first_difference(old[key], new[key], f'{where}.{key}')
            if found:
                return found
        return None
    if isinstance(old, list):
        if len(old) != len(new):
            return f'{where}: {len(old)} items != {len(new)} items'
        for index, (a, b) in enumerate(zip(old, new)):
            found = first_difference(a, b, f'{where}[{index}]')
            if found:
                return found
        return None
    return None if old == new else f'{where}: {json.dumps(old)[:120]} != {json.dumps(new)[:120]}'


def compare(old_base: str, new_base: str, path: str) -> str | None:
    old_status, old_body, old_type = fetch(old_base, path)
    new_status, new_body, new_type = fetch(new_base, path)
    if old_status != new_status:
        return f'status {old_status} != {new_status}: {new_body[:160]!r}'
    if 'json' not in old_type:
        return None if old_body == new_body else f'body differs ({len(old_body)} vs {len(new_body)} bytes)'
    return first_difference(normalize(json.loads(old_body)), normalize(json.loads(new_body)))


def sample_icons(old_base: str, count: int) -> list[str]:
    """Icons with the most workflow history: feedback, claims, types and flags."""
    picked = []
    _, body, _ = fetch(old_base, '/api/feedback-feed')
    picked += [row['icon'] for row in json.loads(body)[:count]]
    _, body, _ = fetch(old_base, '/api/work/review')
    picked += [item['key'] for item in json.loads(body).get('items', [])[:count]]
    _, body, _ = fetch(old_base, '/api/icon-types')
    picked += [item['icon'] for item in json.loads(body).get('icons', [])[:count]]
    _, body, _ = fetch(old_base, '/api/reviews?include_approvers=1')
    data = json.loads(body)
    picked += list(data.get('rejected_by', {}))[:count] + list(data.get('approved_by', {}))[:count]
    picked.append('solo/does-not-exist')
    return list(dict.fromkeys(picked))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--old', required=True, help='the Python deploy.py base URL (on a database copy)')
    parser.add_argument('--new', required=True, help='the Worker base URL')
    parser.add_argument('--sample', type=int, default=8, help='icons per category for per-icon routes')
    parser.add_argument('--catalog', action='store_true', help='also compare /gallery/icons.json (67 MB)')
    args = parser.parse_args(argv)
    paths = list(ROUTES)
    for key in sample_icons(args.old, args.sample):
        paths += [route.format(urllib.parse.quote(key, safe='')) for route in PER_ICON]
    if args.catalog:
        paths.append('/gallery/icons.json')
    failures = 0
    for path in paths:
        difference = compare(args.old, args.new, path)
        print(('DIFF ' if difference else 'same ') + path + (f'\n     {difference}' if difference else ''), flush=True)
        failures += bool(difference)
    print(f'\n{len(paths) - failures}/{len(paths)} routes identical')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
