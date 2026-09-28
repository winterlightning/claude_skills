#!/usr/bin/env python3
"""Copy the fixes workers uploaded to production into the local Python models.

A worker who fixes a disapproved icon (/primitive-fix-thuan, /fix-icon-queue)
uploads the fixed module to production as the revision's ``after`` result and
reports ``done``. The gallery then shows the uploaded drawing, but the model in
``icon_set/model/icons/<family>/`` still draws the disapproved revision. This
script closes that gap. Run it any time; it only touches icons whose fix has
not landed yet.

For every uploaded fix (``GET /api/work/fixes``) it:

1. keeps only fixes whose revision is Ready from a worker's ``done`` report or
   was approved afterwards (``--status`` changes that). Icons disapproved or
   rejected again are left alone;
2. loads the local module named in the catalog and renders it. The fix is
   applied only when the SVG hash still equals the fixed revision's
   ``svg_sha256``, meaning the local model still draws the disapproved icon.
   After a rebuild the hash changes, so a fix is applied once and a later
   local edit is never overwritten;
3. downloads the fixed Python (``/api/work/result?stage=after&part=python``) and
   keeps the local module's ``icon_id``, ``SOURCE_PATH``, ``SOURCE_ICON_ID`` and
   ``category``. It rewrites the imports to the relative form the model tree
   uses and writes the result over the local module;
4. imports the new module and restores the old text if it no longer loads or
   defines that icon_id, then runs the build gate on it (build_gate.py: holes,
   pinches, internal spacing, symmetry). A fix that fails the gate is still
   applied and lands in the Failed build bucket, and it is listed in the
   report; ``--strict`` holds it back instead.

Each applied fix is appended to ``icon_set/state/applied-work-fixes.jsonl``.

    /opt/homebrew/bin/python3 icon_set/scripts/apply_work_fixes.py --dry-run     # list what would change
    /opt/homebrew/bin/python3 icon_set/scripts/apply_work_fixes.py               # override the models
    /opt/homebrew/bin/python3 icon_set/scripts/apply_work_fixes.py --build       # ... then build --changed-only
    /opt/homebrew/bin/python3 icon_set/scripts/apply_work_fixes.py --icon solo/adaptive-headlight

The base URL defaults to $PICTOGRAPHIC_API, then $PICTOGRAPHIC_SYNC_SOURCE, then
the production tunnel recorded in deploy.py (the same as work_queue.py).
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts import work_queue  # noqa: E402

CATALOG = REPO_ROOT / 'published' / 'gallery' / 'icons.json'
LEDGER = REPO_ROOT / 'icon_set' / 'state' / 'applied-work-fixes.jsonl'
TIMEOUT = 60
PAGE = 500
STATUSES = ('done', 'approve')  # done = Ready from a worker's report; approve = the reviewer accepted it
KEPT = ('SOURCE_PATH', 'SOURCE_ICON_ID')  # module-level lines the local model keeps


def fetch_text(base_url, path, query):
    request = Request(base_url.rstrip('/') + path + '?' + urlencode(query), headers={'Accept': 'text/plain'})
    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            return response.read().decode('utf-8')
    except HTTPError as error:
        raise work_queue.ApiError(error.code, {'error': f'HTTP {error.code} for {path}'}) from None
    except (URLError, TimeoutError, OSError) as error:
        raise work_queue.ApiError(0, {'error': f'Could not reach {base_url}: {getattr(error, "reason", error)}'}) from None


def _status(row):
    state = (row.get('work') or {}).get('state')
    return state if state and state != 'none' else row.get('status')


def fix_status(base_url, fixes):
    """(icon, sha) -> 'done' | 'approve' | 'disapprove' | 'rejected' | 'cannot-fix' | ... for every fix."""
    statuses, offset = {}, 0
    while offset is not None:
        page = work_queue.call(base_url, 'GET', '/api/work/review', query={'limit': PAGE, 'offset': offset})
        for item in page['items']:
            statuses[(item['key'], item.get('svg_sha256'))] = _status(item)
        offset = page.get('next_offset')
    # The review listing only holds disapproved, claimed and fixed-awaiting-review icons; ask for the rest.
    missing = sorted({key for key, sha in fixes if (key, sha) not in statuses})

    def current(key):
        try:
            return key, work_queue.call(base_url, 'GET', '/api/work', query={'icon': key})
        except work_queue.ApiError as error:
            return key, {'error': str(error)}

    with ThreadPoolExecutor(8) as pool:
        for key, row in pool.map(current, missing):
            if 'error' in row:
                continue
            for fix_key, sha in fixes:
                if fix_key == key:  # a different current hash means production already builds a newer model
                    statuses[(key, sha)] = _status(row) if row.get('svg_sha256') == sha else 'revision replaced on production'
    return statuses


def load_class(path: Path, icon_id: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for value in vars(module).values():
        if isinstance(value, type) and value.__module__ == name and getattr(value, 'icon_id', None) == icon_id:
            return value
    raise LookupError(f'{path.name} defines no class with icon_id {icon_id!r}')


def local_icon(path: Path, icon_id: str):
    package = '.'.join(path.relative_to(REPO_ROOT).with_suffix('').parts)
    return load_class(path, icon_id, package)()


def local_sha(path: Path, icon_id: str) -> str:
    """Hash of the local model's SVG, as the build computes svg_sha256."""
    return hashlib.sha256(local_icon(path, icon_id).to_svg().encode('utf-8')).hexdigest()


def gate(path: Path, icon_id: str) -> dict:
    """The build's own QA (holes/pinches, internal spacing, symmetry) on the applied module, as build_gate.py runs it."""
    from icon_set.validation.library_qa import inspect_icon
    qa = inspect_icon(local_icon(path, icon_id))
    return {'status': qa['status'], 'errors': list(qa['errors']), 'warnings': list(qa['warnings'])}


def _assignment(name, text, *, indented=False):
    pattern = (r'^(\s+)' if indented else r'^()') + name + r'''\s*=\s*(['"])(.*?)\2[ \t]*$'''
    return re.search(pattern, text, re.MULTILINE)


def merge(fixed: str, local: str, family: str) -> str:
    """The fixed module with the local icon identity and tree-relative imports."""
    for name in KEPT:
        old, new = _assignment(name, local), _assignment(name, fixed)
        if old and new:
            fixed = fixed[:new.start()] + old.group(0) + fixed[new.end():]
    for name in ('icon_id', 'category'):
        old, new = _assignment(name, local, indented=True), _assignment(name, fixed, indented=True)
        if old and new:
            fixed = fixed[:new.start(3)] + old[3] + fixed[new.end(3):]
    fixed = re.sub(r'^from icon_set\.model\.keyshapes import', 'from ...keyshapes import', fixed, flags=re.MULTILINE)
    fixed = re.sub(rf'^from icon_set\.model\.icons\.{family}\._base import', 'from ._base import', fixed, flags=re.MULTILINE)
    return fixed if fixed.endswith('\n') else fixed + '\n'


def apply(base_url, *, statuses_wanted, only=None, dry_run=False, strict=False, jobs=8):
    fixes = work_queue.call(base_url, 'GET', '/api/work/fixes')['fixes']
    if only:
        fixes = [fix for fix in fixes if fix['icon'] in only]
    statuses = fix_status(base_url, {(fix['icon'], fix['svg_sha256']) for fix in fixes})
    catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
    rows = {row['key']: row for row in catalog['icons'] + catalog.get('failed_icons', [])}
    report = {'applied': [], 'already': [], 'skipped': [], 'failed': [], 'gate_failed': [], 'held': []}

    candidates = []
    for fix in fixes:
        key, sha = fix['icon'], fix['svg_sha256']
        status = statuses.get((key, sha), 'unknown')
        row = rows.get(key)
        if status not in statuses_wanted:
            report['skipped'].append((key, f'status {status}'))
        elif row is None or not (row.get('python_source') or {}).get('path'):
            report['skipped'].append((key, 'not in the local catalog'))
        else:
            candidates.append((fix, row))

    def download(candidate):
        fix, row = candidate
        try:
            return candidate, fetch_text(base_url, '/api/work/result', {
                'icon': fix['icon'], 'svg_sha256': fix['svg_sha256'], 'stage': 'after', 'part': 'python'}), None
        except work_queue.ApiError as error:
            return candidate, None, str(error)

    # Check the local drawing first so only pending fixes are downloaded.
    pending = []
    for fix, row in candidates:
        key, path = fix['icon'], REPO_ROOT / row['python_source']['path']
        if not path.is_file():
            report['skipped'].append((key, f'{path.relative_to(REPO_ROOT)} is missing'))
            continue
        try:
            drawn = local_sha(path, row['icon_id'])
        except Exception as error:  # a broken local module is reported, never overwritten blindly
            report['failed'].append((key, f'local module does not load: {type(error).__name__}: {error}'))
            continue
        if drawn != fix['svg_sha256']:
            report['already'].append((key, 'local model no longer draws the fixed revision (already applied or edited)'))
            continue
        pending.append((fix, row))

    with ThreadPoolExecutor(jobs) as pool:
        downloads = list(pool.map(download, pending))

    ledger = []
    for (fix, row), source, error in downloads:
        key, path = fix['icon'], REPO_ROOT / row['python_source']['path']
        rel = path.relative_to(REPO_ROOT).as_posix()
        if error or not source or not source.strip():
            report['failed'].append((key, error or 'the fix has no Python upload'))
            continue
        local = path.read_text(encoding='utf-8')
        text = merge(source, local, row.get('family') or key.split('/', 1)[0])
        if text == local:
            report['already'].append((key, 'module already matches the fix'))
            continue
        path.write_text(text, encoding='utf-8')
        try:
            checked = gate(path, row['icon_id'])
        except Exception as error:
            path.write_text(local, encoding='utf-8')
            report['failed'].append((key, f'fixed module does not load, kept the old one: {type(error).__name__}: {error}'))
            continue
        if checked['status'] != 'pass':
            finding = (checked['errors'] + checked['warnings'] or [checked['status']])[0]
            if strict:
                path.write_text(local, encoding='utf-8')
                report['held'].append((key, f"build gate {checked['status']}: {finding}"))
                continue
            report['gate_failed'].append((key, f"build gate {checked['status']}: {finding}"))
        if dry_run:
            path.write_text(local, encoding='utf-8')
            report['applied'].append((key, rel))
            continue
        report['applied'].append((key, rel))
        ledger.append({'icon': key, 'svg_sha256': fix['svg_sha256'], 'worker': fix.get('worker'),
                       'saved_at': fix.get('saved_at'), 'module': rel, 'build_gate': checked['status'],
                       'applied_at': datetime.now(timezone.utc).isoformat()})
    if ledger:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        with LEDGER.open('a', encoding='utf-8') as handle:
            handle.writelines(json.dumps(entry, ensure_ascii=False) + '\n' for entry in ledger)
    report['families'] = sorted({key.split('/', 1)[0] for key, _ in report['applied']})
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--base-url', default=None, help='production gallery (default: as work_queue.py)')
    parser.add_argument('--status', action='append', metavar='STATUS',
                        help=f'apply fixes whose revision has this work state or review status (repeatable; '
                             f'default: {", ".join(STATUSES)})')
    parser.add_argument('--icon', action='append', metavar='KEY', help='only this icon key, e.g. solo/adaptive-headlight')
    parser.add_argument('--dry-run', action='store_true', help='report only; write nothing')
    parser.add_argument('--strict', action='store_true',
                        help='hold back fixes that fail the build gate (holes/pinches, internal spacing, symmetry); '
                             'by default they are applied and land in the Failed build bucket')
    parser.add_argument('--build', action='store_true', help='after applying, run build.py --changed-only for the touched families')
    parser.add_argument('--verbose', '-v', action='store_true', help='list every skipped or already-applied icon')
    args = parser.parse_args(argv)
    base_url = args.base_url or work_queue.default_base_url()

    try:
        report = apply(base_url, statuses_wanted=set(args.status or STATUSES), only=set(args.icon or ()),
                       dry_run=args.dry_run, strict=args.strict)
    except work_queue.ApiError as error:
        print(f'error: {error}', file=sys.stderr)
        return 1
    verb = 'would apply' if args.dry_run else 'applied'
    print(f"{verb} {len(report['applied'])} fix(es) from {base_url}")
    for key, rel in report['applied']:
        print(f'  {key}  -> {rel}')
    print(f"{len(report['already'])} already in the local model; {len(report['skipped'])} skipped; "
          f"{len(report['failed'])} failed")
    if args.verbose:
        for key, reason in report['already'] + report['skipped']:
            print(f'  - {key}: {reason}')
    if report['gate_failed']:
        print(f"{len(report['gate_failed'])} applied fix(es) fail the build gate and will build into the Failed bucket:")
        for key, reason in report['gate_failed']:
            print(f'  x {key}: {reason}')
    if report['held']:
        print(f"held back {len(report['held'])} fix(es) that fail the build gate (--strict):")
        for key, reason in report['held']:
            print(f'  - {key}: {reason}')
    for key, reason in report['failed']:
        print(f'  ! {key}: {reason}')

    if report['applied'] and not args.dry_run:
        command = [sys.executable, str(REPO_ROOT / 'icon_set' / 'scripts' / 'build.py'), '--changed-only']
        for family in report['families']:
            command += ['--family', family]
        if args.build:
            print('$', ' '.join(command[1:]), flush=True)
            return subprocess.call(command, cwd=REPO_ROOT) or (1 if report['failed'] else 0)
        print('now run: ' + ' '.join(['/opt/homebrew/bin/python3', *command[1:]]).replace(str(REPO_ROOT) + '/', ''))
    return 1 if report['failed'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
