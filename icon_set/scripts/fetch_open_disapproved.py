"""Download every open (unclaimed, not yet fixed) disapproved icon from production, without claiming.

    python3 icon_set/scripts/fetch_open_disapproved.py [--family solo] [--reason meaning] [--out DIR] [--jobs 8]

Each icon gets ``<out>/<family>__<name>/`` with ``item.json`` (the queue row: reason, feedback,
disapproved_by, svg_sha256, ...), ``before/<icon_id>.svg`` (the drawing production shows),
``before/<module>.py`` (the registered module when it exists locally) and
``reference/<concept>_<uuid>.svg`` (the original reference, the input /primitive-make-ray takes).
``<out>/index.json`` lists every icon and ``<out>/references.txt`` the reference paths, one per line.

Nothing is claimed: other machines can still take these icons. Claim with
``primitive_fix.py --worker NAME start`` (or ``work_queue.py next``) before fixing one.
"""
import argparse
import json
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts import work_queue  # noqa: E402
from icon_set.scripts.primitive_fix import fetch_svg, key_folder, stage_reference  # noqa: E402


def open_items(base_url, family=None, reason=None):
    """Every claimable disapproved row (work state none), oldest disapproval first."""
    items, offset = [], 0
    while True:
        page = work_queue.call(base_url, 'GET', '/api/work/queue',
                               query={'family': family, 'reason': reason, 'limit': work_queue.MAX_PAGE, 'offset': offset})
        items += page['items']
        if page.get('next_offset') is None:
            return items
        offset = page['next_offset']


def save(base_url, item, out):
    target = out / key_folder(item['key'])
    before = target / 'before'
    before.mkdir(parents=True, exist_ok=True)
    (target / 'item.json').write_text(json.dumps(item, indent=2) + '\n')
    problems = []
    try:
        (before / f"{item.get('icon_id') or item['key'].split('/')[-1]}.svg").write_text(fetch_svg(base_url, item))
    except RuntimeError as error:
        problems.append(str(error))
    source = (item.get('python_source') or {}).get('path') if isinstance(item.get('python_source'), dict) else None
    if source and (REPO_ROOT / source).is_file():
        shutil.copyfile(REPO_ROOT / source, before / Path(source).name)
    elif source:
        problems.append(f'module not in this checkout: {source}')
    reference = stage_reference(base_url, item, target / 'reference')
    if reference is None:
        problems.append('no UUID-named original reference')
    return {'key': item['key'], 'family': item.get('family'), 'reason': item.get('reason'), 'feedback': item.get('feedback'),
            'svg_sha256': item.get('svg_sha256'), 'dir': str(target.relative_to(REPO_ROOT)) if target.is_relative_to(REPO_ROOT) else str(target),
            'reference': str(reference.relative_to(REPO_ROOT)) if reference and reference.is_relative_to(REPO_ROOT) else (str(reference) if reference else None),
            'problems': problems}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--base-url', default=None, help='production gallery (default: $PICTOGRAPHIC_API or the recorded tunnel)')
    parser.add_argument('--family', help='solo, icon-72, container (default: all)')
    parser.add_argument('--reason', choices=work_queue.REASONS, help='only this disapproval reason')
    parser.add_argument('--out', type=Path, help='default: icon_set/work/disapproved-open/<UTC stamp>')
    parser.add_argument('--jobs', type=int, default=8, help='parallel downloads (keep it low; production is one process)')
    args = parser.parse_args(argv)
    base_url = args.base_url or work_queue.default_base_url()
    out = args.out or REPO_ROOT / 'icon_set/work/disapproved-open' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    out.mkdir(parents=True, exist_ok=True)
    items = open_items(base_url, args.family, args.reason)
    print(f'{len(items)} open disapproved icons -> {out}', file=sys.stderr)
    with ThreadPoolExecutor(max(1, args.jobs)) as pool:
        saved = list(pool.map(lambda item: save(base_url, item, out), items))
    (out / 'index.json').write_text(json.dumps({'base_url': base_url, 'fetched_at': datetime.now(timezone.utc).isoformat(),
                                                'family': args.family, 'reason': args.reason, 'icons': saved}, indent=2) + '\n')
    (out / 'references.txt').write_text(''.join(entry['reference'] + '\n' for entry in saved if entry['reference']))
    missing = sum(1 for entry in saved if entry['problems'])
    print(f'saved {len(saved)}; {sum(1 for e in saved if e["reference"])} with a reference; {missing} with problems (see index.json)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
