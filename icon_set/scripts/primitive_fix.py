#!/usr/bin/env python3
"""Claim disapproved solo icons, keep their first version, and report in-place fixes.

The two commands behind the /primitive-fix-thuan skill. Every run is recorded in
a standalone folder and mirrored to production so the Fix queue page can show
the drawing before and after the fix:

    python3 icon_set/scripts/primitive_fix.py start --worker thuan-mac --limit 5 [--offset 0] [--disapprove-status bad-stroke]
    python3 icon_set/scripts/primitive_fix.py finish --icon solo/plus --outcome done --note "equalised the arms"
    python3 icon_set/scripts/primitive_fix.py finish --icon solo/plus --outcome cannot-fix --note "MIC 8 impossible with three bars"

``start`` claims up to ``--limit`` claimable disapproved solo icons on production,
creates ``icon_set/work/primitive-fix-thuan/<key>/<run>/`` per icon with the
brief, the claim record and a ``before/`` copy of the registered module and the
displayed SVG, and uploads that first version to production. Exit 3 when nothing
was claimable.

``finish`` validates the edited registered module through the icon registry,
writes ``after/`` (module, SVG, previews, validation.txt) and ``result.json``,
uploads the after result, then reports ``done`` (only when the model is valid
with zero warnings; otherwise exit 2 and nothing is uploaded or reported) or
``cannot-fix`` (note required).
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import sys
import traceback
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from icon_set.scripts import work_queue  # noqa: E402
from icon_set.scripts.workspace import primitive_fix_results_dir  # noqa: E402

FAMILY = 'solo'
PREVIEW_SIZES = (48, 384)
THEMES = (('light', '#141413', '#ffffff'), ('dark', '#f5f4ef', '#1c1c19'))


def slug(value):
    return re.sub(r'[^a-z0-9]+', '-', str(value).lower()).strip('-') or 'run'


def key_folder(key):
    return key.replace('/', '__')


def fetch_svg(base_url, item):
    """The drawing production displays: the artwork route first, then the published preview file."""
    base = base_url.rstrip('/')
    urls = [base + '/api/icon-artwork/svg?icon=' + quote(item['key'], safe='')]
    if item.get('preview_url'):
        urls.append(urljoin(base + '/gallery/', item['preview_url']))
    failure = None
    for url in urls:
        try:
            with urlopen(Request(url, headers={'Accept': 'image/svg+xml'}), timeout=work_queue.TIMEOUT) as response:
                return response.read().decode('utf-8')
        except (HTTPError, URLError, OSError) as error:
            failure = error
    raise RuntimeError(f'could not download the current SVG for {item["key"]}: {failure}')


def load_icon(icon_id):
    """The registered icon instance; errors here mean the registry does not import cleanly."""
    from icon_set.model.icons.registry import create
    return create(icon_id)


def describe_block(item, result_dir, module_path):
    work = item.get('work') or {}
    lines = [f"icon: {item['key']}",
             f"icon_id: {item.get('icon_id') or ''}",
             f"module: {module_path or 'unknown (no python_source on production)'}",
             f"result dir: {result_dir}",
             f"svg_sha256: {item.get('svg_sha256') or ''}",
             f"reason: {item.get('reason') or 'none recorded'}",
             f"disapproved by: {item.get('disapproved_by') or 'unknown'} · {item.get('disapproved_at') or ''}",
             'feedback:',
             item.get('feedback') or '(no feedback text)',
             f"claim expires: {work.get('expires_at') or ''}",
             f"finish with: python3 icon_set/scripts/primitive_fix.py finish --icon {item['key']} --outcome done --note \"<what changed>\""]
    return '\n'.join(lines) + '\n'


def start(base_url, worker, limit, offset=0, reason=None, results_root=None):
    root = Path(results_root) if results_root else primitive_fix_results_dir()
    claimed, page, last = work_queue.take_next(base_url, worker, family=FAMILY, limit=limit, offset=offset, reason=reason)
    if not claimed:
        if last is not None:
            raise work_queue.ApiError(last.status, last.payload)
        return []
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    started = []
    for result in claimed:
        item = result['item']
        key = item['key']
        result_dir = root / key_folder(key) / f'{stamp}-{slug(worker)}'
        before = result_dir / 'before'
        before.mkdir(parents=True, exist_ok=False)
        (result_dir / 'brief.txt').write_text(work_queue.brief(item, result['work']), encoding='utf-8')
        (result_dir / 'claim.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        source = item.get('python_source') or {}
        module_path = source.get('path') if isinstance(source, dict) else None
        module_copy = None
        if module_path and (REPO_ROOT / module_path).is_file():
            module_copy = before / Path(module_path).name
            shutil.copyfile(REPO_ROOT / module_path, module_copy)
        svg_path = before / f"{item.get('icon_id') or key_folder(key)}.svg"
        upload_error = None
        try:
            svg_path.write_text(fetch_svg(base_url, item), encoding='utf-8')
            work_queue.upload_result(base_url, worker, key, item['svg_sha256'], 'before', svg_path, module_copy,
                                     note='first version, before the fix')
        except Exception as error:  # the claim stands; the agent still has the local copy
            upload_error = f'{type(error).__name__}: {error}'
            (result_dir / 'before-upload-error.txt').write_text(upload_error + '\n', encoding='utf-8')
        started.append({'key': key, 'result_dir': result_dir, 'module': module_path, 'item': item, 'upload_error': upload_error})
    return started


def latest_run(key, results_root=None):
    root = Path(results_root) if results_root else primitive_fix_results_dir()
    folder = root / key_folder(key)
    runs = sorted((run for run in folder.iterdir() if run.is_dir() and (run / 'claim.json').is_file()),
                  key=lambda run: run.name) if folder.is_dir() else []
    open_runs = [run for run in runs if not (run / 'result.json').is_file()]
    if not open_runs:
        raise SystemExit(f'error: no unfinished run for {key} under {folder}; run start first')
    return open_runs[-1]


def render_previews(svg, icon_id, canvas, target):
    import cairosvg
    files = []
    for name, ink, background in THEMES:
        themed = svg.replace('currentColor', ink)
        for size in PREVIEW_SIZES:
            path = target / f'preview-{name}-{size}.png'
            cairosvg.svg2png(bytestring=themed.encode('utf-8'), write_to=str(path),
                             output_width=size, output_height=size, background_color=background)
            files.append(path.name)
    return files


def finish(base_url, worker, key, outcome, note='', results_root=None, icon_loader=None):
    if outcome not in ('done', 'cannot-fix'):
        raise SystemExit('error: --outcome must be done or cannot-fix')
    if outcome == 'cannot-fix' and not note.strip():
        raise SystemExit('error: --note is required for cannot-fix')
    run = latest_run(key, results_root)
    claim = json.loads((run / 'claim.json').read_text(encoding='utf-8'))
    item = claim['item']
    icon_id, sha = item.get('icon_id'), item['svg_sha256']
    source = item.get('python_source') or {}
    module_path = source.get('path') if isinstance(source, dict) else None
    after = run / 'after'
    after.mkdir(exist_ok=True)
    findings = {'source_key': key, 'icon_id': icon_id, 'svg_sha256': sha, 'worker': worker, 'outcome': outcome,
                'note': note, 'module': module_path, 'validation_status': None, 'validation_errors': [],
                'validation_warnings': [], 'artifacts': [], 'finished_at': None}
    module_copy = None
    if module_path and (REPO_ROOT / module_path).is_file():
        module_copy = after / Path(module_path).name
        shutil.copyfile(REPO_ROOT / module_path, module_copy)
        findings['artifacts'].append(f'after/{module_copy.name}')
    svg_path = validation_path = None
    try:
        icon = (icon_loader or load_icon)(icon_id)
        report = icon.validate_icon()
        findings['validation_status'] = report.status
        findings['validation_errors'] = list(getattr(report, 'errors', []) or [])
        findings['validation_warnings'] = list(getattr(report, 'warnings', []) or [])
        validation_path = run / 'validation.txt'
        validation_path.write_text(report.describe() + '\n', encoding='utf-8')
        findings['artifacts'].append('validation.txt')
        svg = icon.to_svg()
        svg_path = after / f'{icon_id}.svg'
        svg_path.write_text(svg, encoding='utf-8')
        findings['artifacts'].append(f'after/{svg_path.name}')
        try:
            canvas = icon.profile.spec.canvas_size
        except AttributeError:
            canvas = 48
        try:
            findings['artifacts'] += [f'after/{name}' for name in render_previews(svg, icon_id, canvas, after)]
        except Exception as error:  # previews are evidence, not a gate
            findings['preview_error'] = f'{type(error).__name__}: {error}'
    except Exception as error:
        findings['error'] = f'{type(error).__name__}: {error}'
        (run / 'finish-error.txt').write_text(traceback.format_exc(), encoding='utf-8')
    clean = (findings['validation_status'] == 'valid' and not findings['validation_warnings'] and 'error' not in findings)
    if outcome == 'done' and not clean:
        findings['outcome'] = 'refused'
        (run / 'result.json.refused').write_text(json.dumps(findings, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        problem = findings.get('error') or f"validation {findings['validation_status']} with {len(findings['validation_warnings'])} warning(s)"
        print(f'refused: {key} is not clean ({problem}); nothing uploaded or reported. Fix the model or finish with --outcome cannot-fix.',
              file=sys.stderr)
        return 2
    if svg_path is not None:
        uploaded = work_queue.upload_result(base_url, worker, key, sha, 'after', svg_path, module_copy, validation_path, note=note)
        findings['uploaded'] = uploaded['result']
    reported = work_queue.call(base_url, 'POST', '/api/work/' + outcome,
                               {'icon': key, 'svg_sha256': sha, 'worker': worker, 'note': note})
    findings['reported'] = reported.get('work')
    findings['review_status'] = reported.get('status')
    findings['finished_at'] = datetime.now(timezone.utc).isoformat()
    (run / 'result.json').write_text(json.dumps(findings, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f"{key}: {outcome}" + (f" · review status {reported['status']}" if reported.get('status') else '')
          + f" · result {run}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='\n'.join(__doc__.splitlines()[2:]))
    parser.add_argument('--base-url', default=None, help='production gallery (default: $PICTOGRAPHIC_API or the recorded tunnel)')
    parser.add_argument('--worker', default=None, help='your worker name, e.g. thuan-mac (or export PICTOGRAPHIC_WORKER); required')
    parser.add_argument('--results-root', type=Path, default=None, help=argparse.SUPPRESS)
    commands = parser.add_subparsers(dest='command', required=True)
    begin = commands.add_parser('start', help='claim disapproved solo icons and record their first version')
    begin.add_argument('--limit', type=int, required=True, help='how many icons to claim')
    begin.add_argument('--offset', type=int, default=0, help='skip this many claimable icons first')
    begin.add_argument('--disapprove-status', '--reason', dest='reason', choices=work_queue.REASONS,
                       help='only icons disapproved for this reason')
    end = commands.add_parser('finish', help='validate, record and report one fixed icon')
    end.add_argument('--icon', required=True)
    end.add_argument('--outcome', required=True, choices=('done', 'cannot-fix'))
    end.add_argument('--note', default='')
    args = parser.parse_args(argv)
    base_url = args.base_url or work_queue.default_base_url()
    worker = (args.worker or '').strip() or work_queue.default_worker()  # exits with guidance when unset
    try:
        if args.command == 'start':
            if args.limit < 1 or args.offset < 0:
                parser.error('--limit must be at least 1 and --offset nonnegative')
            started = start(base_url, worker, args.limit, args.offset, args.reason, args.results_root)
            if not started:
                print(f'No claimable disapproved {FAMILY} icons on {base_url}'
                      + (f' with reason {args.reason}' if args.reason else '') + '.', file=sys.stderr)
                return 3
            for entry in started:
                print(describe_block(entry['item'], entry['result_dir'], entry['module']))
                if entry['upload_error']:
                    print(f"warning: the before result was not uploaded: {entry['upload_error']}\n", file=sys.stderr)
            print(f'claimed {len(started)} icon' + ('s' if len(started) != 1 else '') + f' for {worker}')
            return 0
        return finish(base_url, worker, args.icon, args.outcome, args.note, args.results_root)
    except work_queue.ApiError as error:
        print(f'Error ({error.status or "network"}): {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
