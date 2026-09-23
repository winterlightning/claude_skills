#!/usr/bin/env python3
"""Gallery reads and writes for the solo queue: check an item, save a combination split.

Run against the same gallery server that served the queue page.

    python3 icon_set/scripts/solo_queue_util.py check <uuid>
    python3 icon_set/scripts/solo_queue_util.py save split.json
    python3 icon_set/scripts/solo_queue_util.py save - < split.json

`check` prints the canonical UUID, current status, SKIP decision and saved
reference brief. Exit 0 when the item is still TODO, 2 when it is no longer
eligible (skipped, generated or unknown), and 1 when state cannot be read.
Read-only.

`save` takes one JSON file (or stdin with `-`) holding both payloads:

    {
      "status": {"uuids": ["<uuid>"], "status": "skip", "reason": "container",
                 "note": "...", "main_brief": {...}, "sub_brief": {...}},
      "brief":  {"uuid": "<uuid>", "family": "container", "brief": "..."}
    }

It POSTs /api/primitives/status and /api/primitives/briefs, reads both back and
compares them with the intended payloads. Exit 0 only when every field
verified; otherwise exit 1 with the payloads for retry. `--dry-run` checks the
payload shape without saving.
"""
import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_BASE_URL = 'http://localhost:8000'
SESSION_ENV = 'PICTOGRAPHIC_SESSION'
COMPONENT_KEYS = ('name', 'family', 'description')


def request_json(base_url, path, payload=None, session=None):
    """GET, or POST when a payload is given; the session cookie is optional."""
    headers = {'Accept': 'application/json'}
    data = None
    if payload is not None:
        data = json.dumps(payload).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    if session:
        headers['Cookie'] = f'pictographic_session={session}'
    request = Request(base_url.rstrip('/') + path, data=data, headers=headers,
                      method='POST' if payload is not None else 'GET')
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def describe_error(error, base_url):
    if isinstance(error, HTTPError):
        return f"HTTP {error.code}: {error.read().decode('utf-8', 'replace')}"
    if isinstance(error, URLError):
        return f'Could not reach {base_url}: {error.reason}'
    return f'Could not read gallery state: {error}'


def find_row(rows, uid):
    """The catalog row for a UUID; the server folds alias UUIDs onto their canonical primitive."""
    return next((r for r in rows if r['uuid'] == uid or
                 any(alias.get('uuid') == uid for alias in r.get('aliases', []))), None)


# --- check -----------------------------------------------------------------

def item_state(base_url, uid, session=None):
    uid = uid.strip().lower()
    row = find_row(request_json(base_url, '/api/primitives?status=all', session=session), uid)
    if row is None:
        return {'uuid': uid, 'eligible': False, 'reason': 'unknown primitive'}
    canonical = row['uuid']
    statuses = request_json(base_url, '/api/primitives/status', session=session)
    briefs = request_json(base_url, '/api/primitives/briefs', session=session)
    result = {'uuid': canonical, 'requested_uuid': uid, 'status': row['status'],
              'decision': statuses.get(canonical), 'saved_brief': briefs.get(canonical),
              'concept': row.get('concept') or row.get('old_concept'), 'path': row.get('path'),
              'eligible': row['status'] == 'todo'}
    if not result['eligible']:
        reason = (result['decision'] or {}).get('reason')
        result['reason'] = f"status is {row['status']}" + (f' ({reason})' if reason else '')
    return result


def run_check(args):
    try:
        result = item_state(args.base_url, args.uuid, args.session)
    except (HTTPError, URLError, OSError, ValueError, KeyError) as error:
        print(describe_error(error, args.base_url), file=sys.stderr)
        return 1
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0 if result['eligible'] else 2


# --- save ------------------------------------------------------------------

def check_payloads(status, brief):
    """Local shape checks mirroring the skill rules; the server still validates."""
    problems = []
    uuids = status.get('uuids')
    if not (isinstance(uuids, list) and len(uuids) == 1):
        problems.append('status.uuids must list exactly one source UUID')
    elif brief.get('uuid', '').strip().lower() != uuids[0].strip().lower():
        problems.append('status.uuids and brief.uuid must name the same source')
    if status.get('status') != 'skip':
        problems.append('status.status must be "skip"')
    reason = status.get('reason')
    if reason not in ('container', 'combination'):
        problems.append('status.reason must be "container" or "combination"')
    for field in ('main_brief', 'sub_brief'):
        component = status.get(field)
        if not isinstance(component, dict) or any(not str(component.get(k, '')).strip() for k in COMPONENT_KEYS):
            problems.append(f'status.{field} needs name, family and description')
    main_family = (status.get('main_brief') or {}).get('family')
    if (status.get('sub_brief') or {}).get('family') != 'sub':
        problems.append('sub_brief.family must be "sub"')
    if reason == 'container':
        if main_family != 'container':
            problems.append('container main_brief.family must be "container"')
        if 'sub_position' in status:
            problems.append('containers must not send sub_position')
    elif reason == 'combination':
        if main_family not in ('solo', 'container'):
            problems.append('side main_brief.family must be "solo" or "container"')
        if not status.get('sub_position'):
            problems.append('side combinations need the observed sub_position')
    if brief.get('family') != main_family:
        problems.append("brief.family must match the main component's family")
    if not str(brief.get('brief', '')).strip():
        problems.append('brief.brief must be nonempty')
    return problems


def component(value):
    return {k: value[k].strip() for k in COMPONENT_KEYS} if value else None


def verify(uid, status, brief, saved_status, saved_brief):
    """Field -> ok/expected/actual for everything the split must persist."""
    decision = saved_status.get(uid) or {}
    record = saved_brief.get(uid) or {}
    expected = {
        'status': ('skip', decision.get('status')),
        'reason': (status['reason'], decision.get('reason')),
        'note': ((status.get('note') or '').strip(), decision.get('note')),
        'main_brief': (component(status['main_brief']), component(decision.get('main_brief'))),
        'sub_brief': (component(status['sub_brief']), component(decision.get('sub_brief'))),
        'brief_family': (brief['family'], record.get('family')),
        'brief': (brief['brief'].strip(), record.get('brief')),
    }
    if status['reason'] == 'combination':
        expected['sub_position'] = (status['sub_position'], decision.get('sub_position'))
    return {field: {'ok': want == got, 'expected': want, 'actual': got}
            for field, (want, got) in expected.items()}


def save_split(base_url, status, brief, session=None):
    report = {'uuid': status['uuids'][0].strip().lower()}
    errors = {}
    for name, path, body in (('status', '/api/primitives/status', status),
                             ('brief', '/api/primitives/briefs', brief)):
        try:
            request_json(base_url, path, body, session)
        except (HTTPError, URLError, OSError, ValueError) as error:
            errors[name] = describe_error(error, base_url)
    try:
        saved_status = request_json(base_url, '/api/primitives/status', session=session)
        saved_brief = request_json(base_url, '/api/primitives/briefs', session=session)
        row = find_row(request_json(base_url, '/api/primitives?status=all', session=session), report['uuid'])
        if row:
            report['uuid'] = row['uuid']
        fields = verify(report['uuid'], status, brief, saved_status, saved_brief)
    except (HTTPError, URLError, OSError, ValueError, KeyError) as error:
        errors['readback'] = describe_error(error, base_url)
        fields = {}
    report.update(errors=errors, fields=fields,
                  unverified=sorted(f for f, v in fields.items() if not v['ok']) if fields else ['all'])
    report['saved'] = not errors and not report['unverified']
    return report


def run_save(args):
    try:
        text = sys.stdin.read() if args.payload == '-' else Path(args.payload).read_text(encoding='utf-8')
        payload = json.loads(text)
        status, brief = payload['status'], payload['brief']
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Could not read payload: {error}', file=sys.stderr)
        return 1
    problems = check_payloads(status, brief)
    if problems:
        report = {'uuid': (status.get('uuids') or [None])[0], 'saved': False, 'problems': problems}
    elif args.dry_run:
        report = {'uuid': status['uuids'][0], 'saved': False, 'dry_run': True, 'problems': []}
    else:
        report = save_split(args.base_url, status, brief, args.session)
    if not report['saved']:
        report['retry_payload'] = payload
    json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0 if report['saved'] or report.get('dry_run') else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--base-url', default=DEFAULT_BASE_URL)
    common.add_argument('--session', default=os.environ.get(SESSION_ENV),
                        help=f'gallery session token (default: ${SESSION_ENV})')
    commands = parser.add_subparsers(dest='command', required=True)
    check = commands.add_parser('check', parents=[common], help="read a queued item's current state")
    check.add_argument('uuid', help='source UUID from the frozen queue page')
    check.set_defaults(run=run_check)
    save = commands.add_parser('save', parents=[common], help='save a combination split and verify it')
    save.add_argument('payload', help='JSON file with "status" and "brief" payloads, or - for stdin')
    save.add_argument('--dry-run', action='store_true', help='check the payloads without saving')
    save.set_defaults(run=run_save)
    args = parser.parse_args(argv)
    return args.run(args)


if __name__ == '__main__':
    sys.exit(main())
