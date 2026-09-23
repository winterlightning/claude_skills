#!/usr/bin/env python3
"""Take, report and release disapproved-icon fixes against the production gallery.

Every machine and agent talks to the same production database over HTTP, so no
two of them fix the same icon. A claim is a review status: ``next`` turns the
oldest Disapproved icon into Claimed under your worker name and prints its
brief; ``done`` reports the fix (the revision returns to Ready for the
reviewer); ``cannot-fix`` and ``abandon`` release it. A claim older than the
lease (six hours) is claimable again; there is no heartbeat.

    python3 icon_set/scripts/work_queue.py next --limit 1 --offset 0 --disapprove-status bad-stroke [--family sub] [--out fix-input.txt]
    python3 icon_set/scripts/work_queue.py done --icon sub/plus --worker "$WORKER" --note "sub/plus-v3"
    python3 icon_set/scripts/work_queue.py cannot-fix --icon sub/plus --worker "$WORKER" --note "why"
    python3 icon_set/scripts/work_queue.py abandon --icon sub/plus --worker "$WORKER"
    python3 icon_set/scripts/work_queue.py upload --icon sub/plus --stage after --svg fixed.svg --python icon_set/model/icons/sub/plus.py
    python3 icon_set/scripts/work_queue.py status [--icon sub/plus]
    python3 icon_set/scripts/work_queue.py queue [--family sub] [--limit 20]

The base URL defaults to $PICTOGRAPHIC_API, then $PICTOGRAPHIC_SYNC_SOURCE, then
the production tunnel recorded in deploy.py. The worker name has no default: pass
--worker or export PICTOGRAPHIC_WORKER (for example thuan-mac). See docs/work-claims.md.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[2]
TIMEOUT = 30
CLAIM_ATTEMPTS = 5
MAX_PAGE = 500
REASONS = ('bad-stroke', 'meaning', 'manual-fix-request', 'other')


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


WORKER_HELP = ('Set your worker name so production knows which machine holds the claim: '
               'pass --worker thuan-mac or export PICTOGRAPHIC_WORKER=thuan-mac. There is no default.')


def default_worker():
    """The worker name must be chosen deliberately; never derive one from the machine."""
    worker = os.environ.get('PICTOGRAPHIC_WORKER', '').strip()
    if not worker:
        raise SystemExit('error: ' + WORKER_HELP)
    return worker


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
    lines.append(f"claim expires: {work.get('expires_at') or ''}")
    lines.append(f"report with: python3 icon_set/scripts/work_queue.py done --icon {item['key']} --worker \"{work.get('worker') or ''}\" --note \"<variant or commit>\"")
    return '\n'.join(lines) + '\n'


def upload_result(base_url, worker, key, sha, stage, svg_path, python_path=None, validation_path=None, note=''):
    """POST one stage of a fix result; file contents are read here, paths are reported relative to the repo."""
    body = {'icon': key, 'svg_sha256': sha, 'worker': worker, 'stage': stage,
            'svg': Path(svg_path).read_text(encoding='utf-8'), 'note': note or ''}
    if python_path:
        python_path = Path(python_path)
        body['python_source'] = python_path.read_text(encoding='utf-8')
        resolved = python_path.resolve()
        body['python_path'] = resolved.relative_to(REPO_ROOT).as_posix() if resolved.is_relative_to(REPO_ROOT) else python_path.as_posix()
    if validation_path:
        body['validation'] = Path(validation_path).read_text(encoding='utf-8')
    return call(base_url, 'POST', '/api/work/result', body)


def take_next(base_url, worker, family=None, category=None, icon_type=None, *, limit=1, offset=0, reason=None):
    """Claim up to ``limit`` claimable icons starting at ``offset``; skip rows another machine wins."""
    query = {'family': family, 'category': category, 'type': icon_type, 'reason': reason,
             'limit': min(MAX_PAGE, max(limit + CLAIM_ATTEMPTS, 1)), 'offset': offset}
    page = call(base_url, 'GET', '/api/work/queue', query=query)
    if not page['items']:
        return [], page, None
    claimed, last = [], None
    for item in page['items']:
        if len(claimed) >= limit:
            break
        body = {'icon': item['key'], 'svg_sha256': item['svg_sha256'], 'worker': worker}
        try:
            claimed.append(call(base_url, 'POST', '/api/work/claim', body))
        except ApiError as error:
            if error.status != 409:
                raise
            last = error
    return claimed, page, last


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='\n'.join(__doc__.splitlines()[2:]))
    # --base-url, --worker and --json are accepted before or after the subcommand.
    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument('--base-url', default=argparse.SUPPRESS, help='production gallery (default: $PICTOGRAPHIC_API or the recorded tunnel)')
    shared.add_argument('--worker', default=argparse.SUPPRESS, help='your worker name, e.g. thuan-mac (or export PICTOGRAPHIC_WORKER); required for claims and reports')
    shared.add_argument('--json', action='store_true', default=argparse.SUPPRESS, help='print the raw API response')
    parser.set_defaults(base_url=None, worker=None, json=False)
    for action in shared._actions:
        parser._add_action(action)
    commands = parser.add_subparsers(dest='command', required=True)
    take = commands.add_parser('next', help='claim the next disapproved icon(s) and print the brief(s)', parents=[shared])
    take.add_argument('--limit', type=int, default=1, help='how many icons to claim (default 1)')
    take.add_argument('--offset', type=int, default=0, help='skip this many claimable icons first')
    take.add_argument('--disapprove-status', '--reason', dest='reason', choices=REASONS,
                      help='only icons disapproved for this reason')
    take.add_argument('--family')
    take.add_argument('--category')
    take.add_argument('--type', dest='icon_type')
    take.add_argument('--out', type=Path, help='write the brief(s) here instead of printing')
    listing = commands.add_parser('queue', help='list claimable disapproved icons without claiming', parents=[shared])
    listing.add_argument('--disapprove-status', '--reason', dest='reason', choices=REASONS)
    listing.add_argument('--family')
    listing.add_argument('--category')
    listing.add_argument('--type', dest='icon_type')
    listing.add_argument('--limit', type=int, default=20)
    listing.add_argument('--offset', type=int, default=0)
    for name, help_text, note in (('done', 'report the fix; the revision returns to Ready', False),
                                  ('cannot-fix', 'give up with a required note', True),
                                  ('abandon', 'release a claim (or a cannot-fix) so the icon is disapproved again', False)):
        sub = commands.add_parser(name, help=help_text, parents=[shared])
        sub.add_argument('--icon', required=True)
        sub.add_argument('--svg-sha256', help='revision to report (default: the current production revision)')
        sub.add_argument('--note', required=note, default='')
    upload = commands.add_parser('upload', help='upload the before or after result of a fix to production', parents=[shared])
    upload.add_argument('--icon', required=True)
    upload.add_argument('--svg-sha256', help='revision (default: the current production revision)')
    upload.add_argument('--stage', required=True, choices=('before', 'after'))
    upload.add_argument('--svg', required=True, type=Path, help='SVG file to upload')
    upload.add_argument('--python', type=Path, help='the icon\'s Python module')
    upload.add_argument('--validation', type=Path, help='validation report text')
    upload.add_argument('--note', default='')
    status = commands.add_parser('status', help='show claims (all, or one icon)', parents=[shared])
    status.add_argument('--icon')
    args = parser.parse_args(argv)
    base_url = args.base_url or default_base_url()
    worker = (args.worker or '').strip() or (default_worker() if args.command not in ('queue', 'status') else '')
    try:
        if args.command == 'next':
            if args.limit < 1 or args.offset < 0:
                parser.error('--limit must be at least 1 and --offset nonnegative')
            results, page, last = take_next(base_url, worker, args.family, args.category, args.icon_type,
                                            limit=args.limit, offset=args.offset, reason=args.reason)
            if not results:
                if last is not None:
                    print(f'Error (409): {last}', file=sys.stderr)
                    return 1
                print(f'No claimable disapproved icons on {base_url}'
                      + (f' for family {args.family}' if args.family else '')
                      + (f' with reason {args.reason}' if args.reason else '') + '.', file=sys.stderr)
                return 3
            if args.json:
                json.dump(results if args.limit > 1 else results[0], sys.stdout, indent=2)
                print()
                return 0
            text = '\n'.join(brief(result['item'], result['work']) for result in results)
            if args.out:
                args.out.write_text(text, encoding='utf-8')
                print(f'wrote {args.out} ({len(results)} icon' + ('s' if len(results) != 1 else '') + ')')
            else:
                print(text, end='')
            return 0
        if args.command == 'queue':
            data = call(base_url, 'GET', '/api/work/queue', query={'family': args.family, 'category': args.category, 'reason': args.reason,
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
        if args.command == 'upload':
            data = upload_result(base_url, worker, args.icon, sha, args.stage, args.svg, args.python, args.validation, args.note)
            if args.json:
                json.dump(data, sys.stdout, indent=2)
                print()
            else:
                print(f"{args.icon}: {args.stage} result uploaded ({data['result']['saved_at']}); work={data['work']['state']}")
            return 0
        body = {'icon': args.icon, 'svg_sha256': sha, 'worker': worker}
        if args.note:
            body['note'] = args.note
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
