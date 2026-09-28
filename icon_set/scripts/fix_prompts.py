#!/usr/bin/env python3
"""Export icons that need fixing as ready-to-paste /primitive-make-ray prompts, 10 per prompt.

Two sources, one template:

  disapproved  every claimable Disapproved icon on the production work queue (/api/work/queue):
               the reviewer, reason and feedback text, the current drawing and its original reference.
  side-mains   the gallery side-mains page's "Needs fix" bucket: mains whose drawings all fail
               validation or were disapproved / rejected. Validation errors are listed with a fix hint.

    python3 icon_set/scripts/fix_prompts.py                                    # disapproved, all families
    python3 icon_set/scripts/fix_prompts.py --family solo --reason bad-stroke
    python3 icon_set/scripts/fix_prompts.py --source side-mains --base-url http://localhost:8000
    python3 icon_set/scripts/fix_prompts.py --exclude icon_set/work/side-mains-needs-fix/icons.json

Writes prompts.md and icons.json to --out (default icon_set/work/fix-prompts/<source>-<date>/).
Pass an earlier icons.json to --exclude (repeatable) to skip references already exported.
Exporting does not claim anything: other workers can still take these icons from the queue.
To claim while fixing, use /primitive-fix-thuan instead. primitive-make-ray runs are folder-only;
promote them afterwards with promote_work_icons.py --build.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from icon_set.scripts.work_queue import MAX_PAGE, REASONS, ApiError, call, default_base_url  # noqa: E402

UUID = re.compile(r'_([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\.svg$', re.I)
HINTS = {'internal-spacing': 'parts sit too close, keep 4u ink clearance (8u between centerlines)',
         'mic': 'a gap or opening is too narrow, widen it to 4u ink clearance (8u centerlines)',
         'holes/pinches': 'enlarge the undersized holes and remove pinched joins'}
REASON_TEXT = {'bad-stroke': 'bad stroke', 'meaning': 'does not convey the intended meaning',
               'manual-fix-request': 'manual fix request', 'other': 'other'}
NO_FEEDBACK = ('no written feedback: likely a bad stroke or it does not look like the reference. '
               'Compare it with the reference, find what is off and redraw it faithfully.')
INSTRUCTION = ('Each of these references already has a drawing that needs fixing. Author a FRESH run for every file, '
               'even if an earlier result.json exists under icon_set/work/primitive-make-ray/<uuid>/. Do not skip any file. '
               'Open the current drawing and read why it failed, then redraw from the reference so the new icon resolves '
               'every note below, stays faithful to the reference and passes SOLO48 validation.')


def review_note(verb, reviewer, reason, feedback):
    """One line saying who flagged the drawing and what they asked for."""
    head = f"{verb} by {(reviewer or 'a reviewer').capitalize()}"
    if reason and reason != 'manual-fix-request':
        head += f" (reason: {REASON_TEXT.get(reason, reason)})"
    text = (feedback or '').strip()
    if text and text.lower() != 'manual fix request':
        return f'{head}. Reviewer feedback: "{text}"'
    return f'{head}, {NO_FEEDBACK}'


def validation_notes(errors):
    notes, kinds = [], []
    for error in errors:
        notes.append(f'Validation error: {error}')
        kind = error.split(':')[0].split(' [')[0]
        if kind not in kinds:
            kinds.append(kind)
    return notes + [f'Fix: {kind}: {HINTS[kind]}' for kind in kinds if kind in HINTS]


def queue_items(base_url, family=None, reason=None, category=None):
    items, offset = [], 0
    while True:
        page = call(base_url, 'GET', '/api/work/queue', query={'family': family, 'reason': reason, 'category': category,
                                                               'limit': MAX_PAGE, 'offset': offset})
        items += page['items']
        if not page['items'] or page.get('next_offset') is None or len(items) >= page['total']:
            return items
        offset = page['next_offset']


def from_disapproved(base_url, family, reason, category):
    """Rows keyed by reference: several disapproved icons drawn from one reference share a row."""
    rows, orphans = {}, []
    for item in queue_items(base_url, family, reason, category):
        source = item.get('python_source') or {}
        path = source.get('path') if isinstance(source, dict) else source
        refs = [r['source_path'] for r in item.get('original_sources') or [] if isinstance(r, dict) and r.get('source_path')]
        drawing = {'icon': item['key'], 'python_source': path,
                   'notes': [review_note('Disapproved (Needs fix)', item.get('disapproved_by'), item.get('reason'), item.get('feedback'))]}
        match = next((m for m in map(UUID.search, refs) if m), None)
        if not match:
            orphans.append({'icon': item['key'], 'name': item.get('name'), 'python_source': path, 'references': refs})
            continue
        uuid = match.group(1).lower()
        row = rows.setdefault(uuid, {'uuid': uuid, 'concept': item.get('name') or item.get('icon_id'), 'reference': match.string,
                                     'kind': 'review', 'drawings': []})
        row['drawings'].append(drawing)
    return list(rows.values()), orphans


def from_side_mains(base_url):
    """The side-mains.html Needs fix bucket, same rule as side-components.js restatus()."""
    try:
        data = call(base_url, 'GET', '/api/side-components')
    except ApiError:
        data = call(base_url, 'GET', '/gallery/side-components.json')
    reviews = call(base_url, 'GET', '/api/reviews')
    try:
        queue = {item['key']: item for item in queue_items(base_url)}
    except ApiError as error:
        print(f'warning: work queue unavailable ({error}); reviewer names and feedback omitted', file=sys.stderr)
        queue = {}
    usable = lambda d: d['status'] == 'pass' and reviews.get(d['key']) not in ('pending', 'rejected')
    rows = []
    for main in data['mains']:
        if not main['drawings'] or any(usable(d) for d in main['drawings']):
            continue
        kinds, drawings = set(), []
        for d in main['drawings']:
            state = reviews.get(d['key'])
            notes = []
            if d['status'] != 'pass':
                kinds.add('validation')
                notes += validation_notes(d.get('errors') or [])
            if state in ('pending', 'rejected'):
                kinds.add('review')
                q = queue.get(d['key'], {})
                notes.append(review_note('Rejected' if state == 'rejected' else 'Disapproved (Needs fix)',
                                         q.get('disapproved_by'), q.get('reason'), q.get('feedback')))
            if notes:
                drawings.append({'icon': d['key'], 'python_source': d.get('python_source'), 'notes': notes})
        rows.append({'uuid': main['id'], 'concept': main['concept'], 'reference': main['source_path'], 'uses': main.get('uses', 0),
                     'kind': 'validation' if kinds == {'validation'} else 'review' if kinds == {'review'} else 'mixed',
                     'drawings': drawings})
    order = {'validation': 0, 'mixed': 1, 'review': 2}
    rows.sort(key=lambda r: (order[r['kind']], -r['uses']))
    return rows, []


def render(rows, orphans, batch, title, summary):
    count = -(-len(rows) // batch)
    out = [f'# {title}', '', summary, f'{len(rows)} references in {count} prompt{"s" if count != 1 else ""} of up to {batch}.',
           'Run each prompt in its own session. The runs stay in icon_set/work/primitive-make-ray/. '
           'Afterwards, promote them with `promote_work_icons.py --build`.', '']
    for start in range(0, len(rows), batch):
        chunk = rows[start:start + batch]
        out += [f'## Prompt {start // batch + 1:02d}', '', '```text',
                '/primitive-make-ray ' + ' '.join(f'"{r["reference"]}"' for r in chunk), '', INSTRUCTION, '']
        for n, row in enumerate(chunk, 1):
            out.append(f"{n}. {row['concept']} ({row['uuid']})")
            for d in row['drawings']:
                out.append(f"   - Current drawing {d['icon']} ({d['python_source'] or 'no python source'})")
                out += [f'     - {note}' for note in d['notes']]
        out += ['```', '']
    if orphans:
        out += ['## No reference: fix by hand', '', 'These icons have no original reference with a UUID, so primitive-make-ray cannot redraw them.', '']
        out += [f"- {o['icon']} ({o['python_source'] or 'no python source'})" for o in orphans]
        out.append('')
    return '\n'.join(out), count


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='\n'.join(__doc__.splitlines()[2:]))
    parser.add_argument('--source', choices=('disapproved', 'side-mains'), default='disapproved')
    parser.add_argument('--base-url', help='gallery server (default: $PICTOGRAPHIC_API or the production tunnel)')
    parser.add_argument('--family', help='disapproved only: e.g. solo')
    parser.add_argument('--category', help='disapproved only')
    parser.add_argument('--reason', '--disapprove-status', dest='reason', choices=REASONS, help='disapproved only')
    parser.add_argument('--batch', type=int, default=10, help='references per prompt (default 10)')
    parser.add_argument('--exclude', type=Path, action='append', default=[], help='earlier icons.json whose references to skip')
    parser.add_argument('--out', type=Path, help='output folder (default icon_set/work/fix-prompts/<source>-<date>)')
    args = parser.parse_args(argv)
    if args.batch < 1:
        parser.error('--batch must be at least 1')
    base_url = args.base_url or default_base_url()
    try:
        rows, orphans = from_side_mains(base_url) if args.source == 'side-mains' else \
            from_disapproved(base_url, args.family, args.reason, args.category)
    except ApiError as error:
        print(f'Error ({error.status}): {error}', file=sys.stderr)
        return 1
    skip = {row['uuid'] for path in args.exclude for row in json.loads(path.read_text(encoding='utf-8'))}
    before = len(rows)
    rows = [row for row in rows if row['uuid'] not in skip]
    missing = [row for row in rows if not (REPO_ROOT / row['reference']).exists()]
    today = dt.date.today().isoformat()
    out_dir = args.out or REPO_ROOT / 'icon_set/work/fix-prompts' / f'{args.source}-{today}'
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.source == 'side-mains':
        title = 'Side mains needing fix: primitive-make-ray prompts'
        summary = (f'Exported {today} from gallery/side-mains.html?status=failing. Validation-only: '
                   f"{sum(r['kind'] == 'validation' for r in rows)} · reviewer-flagged: {sum(r['kind'] == 'review' for r in rows)}"
                   f" · both: {sum(r['kind'] == 'mixed' for r in rows)}.")
    else:
        filters = ', '.join(f'{k} {v}' for k, v in (('family', args.family), ('category', args.category), ('reason', args.reason)) if v)
        title = 'Disapproved icons: primitive-make-ray prompts'
        summary = f'Exported {today} from the production work queue ({base_url})' + (f', {filters}' if filters else '') + '.'
    text, count = render(rows, orphans, args.batch, title, summary)
    (out_dir / 'prompts.md').write_text(text, encoding='utf-8')
    (out_dir / 'icons.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding='utf-8')
    print(f'{len(rows)} references ({before - len(rows)} excluded) in {count} prompts; {len(orphans)} icons without a reference.')
    if missing:
        print(f'warning: {len(missing)} reference files are not on disk, e.g. {missing[0]["reference"]}', file=sys.stderr)
    print(f'wrote {out_dir / "prompts.md"}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
