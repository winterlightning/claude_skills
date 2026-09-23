#!/usr/bin/env python3
"""Take, report and release disapproved-icon fixes against the production gallery.

Every machine and agent talks to the same production database over HTTP, so no
two of them fix the same icon. ``next`` claims the oldest claimable disapproved
icon and prints its brief; ``done`` reports the fix (the revision returns to
Ready for the reviewer); ``cannot-fix`` and ``abandon`` release it.

    python3 icon_set/scripts/work_queue.py next --worker "$WORKER" [--family sub] [--out fix-input.txt]
    python3 icon_set/scripts/work_queue.py done --icon sub/plus --worker "$WORKER" --note "sub/plus-v3"
    python3 icon_set/scripts/work_queue.py cannot-fix --icon sub/plus --worker "$WORKER" --note "why"
    python3 icon_set/scripts/work_queue.py abandon --icon sub/plus --worker "$WORKER"
    python3 icon_set/scripts/work_queue.py heartbeat --icon sub/plus --worker "$WORKER"
    python3 icon_set/scripts/work_queue.py status [--icon sub/plus]
    python3 icon_set/scripts/work_queue.py queue [--family sub] [--limit 20]

The base URL defaults to $PICTOGRAPHIC_API, then $PICTOGRAPHIC_SYNC_SOURCE, then
the production tunnel recorded in deploy.py. The worker name defaults to
$PICTOGRAPHIC_WORKER, then "<hostname>/<user>". See docs/work-claims.md.
"""
from __future__ import annotations

import argparse
import getpass
import json
import os
from pathlib import Path
import socket
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[2]
TIMEOUT = 30
CLAIM_ATTEMPTS = 5


class ApiError(RuntimeError):
    def __init__(self, status, payload):
        super().__init__(payload.get('error') if isinstance(payload, dict) else str(payload))
        self.status, self.payload = status, payload


def default_base_url():
    for name in ('PICTOGRAPHIC_API', 'PICTOGRAPHIC_SYNC_SOURCE'):
        if os.environ.get(name):
            return os.environ[name]
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from icon_set.scripts.deploy import DEFAULT_SYNC_SOURCE
    return DEFAULT_SYNC_SOURCE


def default_worker():
    if os.environ.get('PICTOGRAPHIC_WORKER'):
        return os.environ['PICTOGRAPHIC_WORKER']
    try:
        user = getpass.getuser()
    except (KeyError, OSError):
        user = 'agent'
    return f'{socket.gethostname().split(".")[0]}/{user}'


def call(base_url, method, path, body=None, query=None):
    url = base_url.rstrip('/') + path
    if query:
        url += '?' + urlencode({k: v for k, v in query.items() if v is not None})
    request = Request(url, method=method, data=json.dumps(body).encode('utf-8') if body is not None else None,
                      headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            return json.loads(response.read().decode('utf-8'))
    except HTTPError as error:
        try:
            payload = json.loads(error.read().decode('utf-8'))
        except ValueError:
            payload = {'error': f'HTTP {error.code}'}
        raise ApiError(error.code, payload) from None
    except (URLError, TimeoutError, OSError) as error:
        raise ApiError(0, {'error': f'Could not reach {base_url}: {getattr(error, "reason", error)}'}) from None


def brief(item, work=None):
    """The fix input an agent reads, in the style of next_icon.py."""
    work = work or item.get('work') or {}
    source = item.get('python_source') or {}
    lines = [f"icon: {item['key']}",
             f"name: {item.get('name') or item.get('icon_id') or ''}",
             f"family: {item.get('family') or ''}",
             f"category: {item.get('category') or ''}",
             f"svg_sha256: {item.get('svg_sha256') or ''}",
             f"python source: {source.get('path') if isinstance(source, dict) else source or 'none'}",
             f"reason: {item.get('reason') or 'none recorded'}",
             f"disapproved by: {item.get('disapproved_by') or 'unknown'} · {item.get('disapproved_at') or ''}"]
    references = [ref.get('source_path') for ref in item.get('original_sources') or [] if isinstance(ref, dict) and ref.get('source_path')]
    if references:
        lines.append('reference: ' + ', '.join(references))
    lines.append('feedback:')
    lines.append(item.get('feedback') or '(no feedback text)')
    lines.append(f"worker: {work.get('worker') or ''}")
    lines.append(f"lease expires: {work.get('expires_at') or ''}")
    lines.append(f"report with: python3 icon_set/scripts/work_queue.py done --icon {item['key']} --worker \"{work.get('worker') or ''}\" --note \"<variant or commit>\"")
    return '\n'.join(lines) + '\n'


def take_next(base_url, worker, family=None, category=None, icon_type=None, lease_hours=None):
    """Claim the first claimable queue item; retry a few rows when another machine wins the race."""
    page = call(base_url, 'GET', '/api/work/queue',
                query={'family': family, 'category': category, 'type': icon_type, 'limit': CLAIM_ATTEMPTS})
    if not page['items']:
        return None, page
    last = None
    for item in page['items']:
        body = {'icon': item['key'], 'svg_sha256': item['svg_sha256'], 'worker': worker}
        if lease_hours:
            body['lease_hours'] = lease_hours
        try:
            result = call(base_url, 'POST', '/api/work/claim', body)
        except ApiError as error:
            if error.status != 409:
                raise
            last = error
            continue
        return result, page
    raise last


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='\n'.join(__doc__.splitlines()[2:]))
    parser.add_argument('--base-url', default=None, help='production gallery (default: $PICTOGRAPHIC_API or the recorded tunnel)')
    parser.add_argument('--worker', default=None, help='who is working (default: $PICTOGRAPHIC_WORKER or hostname/user)')
    parser.add_argument('--json', action='store_true', help='print the raw API response')
    commands = parser.add_subparsers(dest='command', required=True)
    take = commands.add_parser('next', help='claim the next disapproved icon and print its brief')
    take.add_argument('--family')
    take.add_argument('--category')
    take.add_argument('--type', dest='icon_type')
    take.add_argument('--lease-hours', type=int)
    take.add_argument('--out', type=Path, help='write the brief here instead of printing it')
    listing = commands.add_parser('queue', help='list claimable disapproved icons without claiming')
    listing.add_argument('--family')
    listing.add_argument('--category')
    listing.add_argument('--type', dest='icon_type')
    listing.add_argument('--limit', type=int, default=20)
    listing.add_argument('--offset', type=int, default=0)
    for name, help_text, note in (('done', 'report the fix; the revision returns to Ready', False),
                                  ('cannot-fix', 'give up with a required note', True),
                                  ('abandon', 'release your claim so another machine can take it', False),
                                  ('heartbeat', 'extend your lease', False)):
        sub = commands.add_parser(name, help=help_text)
        sub.add_argument('--icon', required=True)
        sub.add_argument('--svg-sha256', help='revision to report (default: the current production revision)')
        sub.add_argument('--note', required=note, default='')
        if name == 'heartbeat':
            sub.add_argument('--lease-hours', type=int)
    status = commands.add_parser('status', help='show claims (all, or one icon)')
    status.add_argument('--icon')
    args = parser.parse_args(argv)
    base_url = args.base_url or default_base_url()
    worker = args.worker or default_worker()
    try:
        if args.command == 'next':
            result, page = take_next(base_url, worker, args.family, args.category, args.icon_type, args.lease_hours)
            if result is None:
                print(f'No claimable disapproved icons on {base_url}'
                      + (f' for family {args.family}' if args.family else '') + '.', file=sys.stderr)
                return 3
            if args.json:
                json.dump(result, sys.stdout, indent=2)
                print()
                return 0
            text = brief(result['item'], result['work'])
            if args.out:
                args.out.write_text(text, encoding='utf-8')
                print(f'wrote {args.out}')
            else:
                print(text, end='')
            return 0
        if args.command == 'queue':
            data = call(base_url, 'GET', '/api/work/queue', query={'family': args.family, 'category': args.category,
                                                                   'type': args.icon_type, 'limit': args.limit, 'offset': args.offset})
            if args.json:
                json.dump(data, sys.stdout, indent=2)
                print()
                return 0
            print(f"{data['total']} claimable disapproved icons (showing {len(data['items'])} from {data['offset']})")
            for item in data['items']:
                print(f"  {item['key']}  {item.get('reason') or '-'}  by {item.get('disapproved_by') or '?'}  {item.get('disapproved_at') or ''}  work={item['work']['state']}")
            return 0
        if args.command == 'status':
            data = call(base_url, 'GET', '/api/work', query={'icon': args.icon} if args.icon else None)
            json.dump(data, sys.stdout, indent=2)
            print()
            return 0
        sha = args.svg_sha256
        if not sha:
            sha = call(base_url, 'GET', '/api/work', query={'icon': args.icon})['svg_sha256']
        body = {'icon': args.icon, 'svg_sha256': sha, 'worker': worker}
        if args.note:
            body['note'] = args.note
        if getattr(args, 'lease_hours', None):
            body['lease_hours'] = args.lease_hours
        data = call(base_url, 'POST', '/api/work/' + args.command, body)
        if args.json:
            json.dump(data, sys.stdout, indent=2)
            print()
        else:
            state = data['work']['state']
            extra = ' · review status ready (feedback kept for the reviewer)' if data.get('status') == 'ready' else ''
            print(f"{args.icon}: work={state}{extra}")
        return 0
    except ApiError as error:
        print(f'Error ({error.status or "network"}): {error}', file=sys.stderr)
        work = error.payload.get('work') if isinstance(error.payload, dict) else None
        if work:
            print('current work state: ' + json.dumps(work), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
