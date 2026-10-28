"""Claude's side-pair review loop: claim a pair, render a compact sheet, render a layout, record.

Commands (run from the workspace root; every decision goes through review_claims' staged
verify/commit, and every pair touched is appended to the session log):

  next   --set pending_human|stale|pending [--n N]      list pairs still to review in that set
  prep   ID                                             claim ID and write STAGE/sheet.png
  layout ID --spec JSON [--spec JSON ...]              render staged pair-local layouts + sheet
  accept ID VARIANT --reason TEXT [--also VARIANT ...]  pin, verify and commit an accepted decision
  hold   ID --reason TEXT                               commit pending_human with the defect
  status                                                session counts

The rules for choosing are in fill-side-recheck/SKILL.md; this file only does the bookkeeping.
"""

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import json
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .adaptive_overlap import ROOT
from .ai_variant_review import DEFAULT_LAYOUT_OUTPUT, candidate_sources
from .pair_layout_review import (render_baseline_stress, render_one, repo_layout_svg,
                                 source_centerline_bounds, source_keyshape_name)
from . import review_claims as rc

SESSION = WORK / 'claude-review-20261027'
LOG = SESSION / 'log.jsonl'
REVIEWER = 'Claude visual review'
REPORT = WORK / 'recombined-all/report.json'
DECISIONS = DATA / 'data/ai-variant-decisions.json'


def now():
    return datetime.now(timezone.utc).isoformat()


def logged():
    return [json.loads(line) for line in LOG.open()] if LOG.exists() else []


def log(entry):
    SESSION.mkdir(parents=True, exist_ok=True)
    with LOG.open('a') as stream:
        stream.write(json.dumps({'at': now(), **entry}) + '\n')


def report_row(pair_id):
    return next((row for row in json.loads(REPORT.read_text())['rows'] if row['id'] == pair_id), None)


def claim(pair_id):
    """An active claim on exactly this pair (reopened when its earlier claim is done)."""
    with rc.locked_state() as state:
        record = state['claims'].get(pair_id)
        if record and record['status'] == 'active':
            if record.get('owner') != 'claude':
                raise ValueError(f'{pair_id} is actively claimed by {record.get("owner")}')
        else:
            current_decisions, current_proposals = rc.decisions(), rc.proposals()
            record = {'status': 'active', 'owner': 'claude', 'token': uuid.uuid4().hex[:12],
                      'claimed_at': rc.now(), 'queue_status': 'claude_review',
                      'decision_sha_before': rc.digest(current_decisions.get(pair_id)),
                      'proposal_sha_before': rc.digest(current_proposals.get(pair_id, []))}
            if state['claims'].get(pair_id):
                record['supersedes_token'] = state['claims'][pair_id]['token']
            state['claims'][pair_id] = record
        return rc.prepare_stage(pair_id, record, rc.decisions(), rc.proposals())


def png(svg, out, size):
    subprocess.run(['rsvg-convert', '-w', str(size), '-h', str(size), '-b', 'white', str(svg), '-o', str(out)],
                   check=True)


def sheet(pair_id, stage, layout_dir=None, name='sheet.png'):
    """One image: the four inputs, then every candidate at 160px, at actual 48px, and its 8px cut."""
    row = report_row(pair_id)
    sources = candidate_sources(row, REPORT.parent, layout_dir or DEFAULT_LAYOUT_OUTPUT)
    work = stage / 'tiles'
    work.mkdir(exist_ok=True)
    from .adaptive_overlap import fill_path, source_path
    item = next(i for i in json.loads(rc.DEFAULT_LAYOUTS.read_text())['items'] if i['reference_id'] == pair_id)
    parts = {p['role']: p for p in item['parts']}
    refs = []
    for label, path in (('main src', source_path(parts['main'], 'main')), ('main fill', fill_path(parts['main'], 'main')),
                        ('sub src', source_path(parts['sub'], 'sub')), ('sub fill', fill_path(parts['sub'], 'sub'))):
        out = work / f'ref-{label.replace(" ", "-")}.png'
        png(path, out, 96)
        refs += ['-label', label, str(out)]
    columns, table = [], []
    for variant, (candidate, path) in sources.items():
        if candidate.get('duplicate_of') or not path.is_file():
            continue
        big, small = work / f'{variant}-160.png', work / f'{variant}-48.png'
        png(path, big, 160)
        png(path, small, 48)
        stress = None
        if candidate.get('stress_svg'):
            stress = (layout_dir or DEFAULT_LAYOUT_OUTPUT) / candidate['stress_svg']
        elif variant != 'outline' and candidate.get('base_variant', variant) != 'outline':
            result = render_baseline_stress(pair_id, variant, work / f'{variant}--8px.svg')
            stress = Path(result['svg']) if result else None
        cell = [str(big), str(small)]
        if stress and stress.is_file():
            png(stress, work / f'{variant}-8px.png', 160)
            cell.append(str(work / f'{variant}-8px.png'))
        col = work / f'col-{variant}.png'
        subprocess.run(['magick', *cell, '-background', 'white', '-gravity', 'center', '-append',
                        '-gravity', 'north', '-splice', '0x14', '-pointsize', '12', '-annotate', '+0+1',
                        variant[:28], '-bordercolor', '#999', '-border', '1', str(col)], check=True)
        columns.append(str(col))
        table.append({'variant': variant, 'sha256': candidate.get('candidate_sha256'),
                      'status': candidate.get('semantic_status') or candidate.get('status'),
                      'safe': candidate.get('safe'), 'kind': 'layout' if variant.startswith('layout-') else 'normal'})
    top = work / 'refs.png'
    subprocess.run(['magick', 'montage', *refs, '-tile', 'x1', '-geometry', '96x96+4+2', '-pointsize', '11', str(top)],
                   check=True)
    body = work / 'cols.png'
    subprocess.run(['magick', *columns, '-background', 'white', '-gravity', 'north', '+append', str(body)], check=True)
    out = stage / name
    subprocess.run(['magick', str(top), str(body), '-background', 'white', '-gravity', 'west', '-append',
                    '-gravity', 'north', '-splice', '0x18', '-pointsize', '14', '-annotate', '+0+2',
                    f"{row['concept']} · {row['main'].split('/')[1]} + {row['sub'].split('/')[1]}", str(out)], check=True)
    return out, table


def locked_shapes(pair_id):
    """Each part's locked source keyshape, as the layout renderer requires it."""
    from .adaptive_overlap import source_path
    item = next(i for i in json.loads(rc.DEFAULT_LAYOUTS.read_text())['items'] if i['reference_id'] == pair_id)
    cls = repo_layout_svg()
    # A drawing matching no keyshape is locked to its own shape ('own' in a proposal).
    return {p['role']: source_keyshape_name(p['role'], source_centerline_bounds(cls, source_path(p, p['role']), p['role']))
            .replace('custom', 'own') for p in item['parts']}


def quick_spec(pair_id, text):
    """base,sub,position,main_size,sub_size[,main_dx,main_dy,sub_dx,sub_dy] -> a layout proposal."""
    base, sub, position, main_size, sub_size, *rest = text.split(',')
    rigid = 'rigid' in rest
    override = 'override' in rest
    moves = [value for value in rest if value not in ('rigid', 'override')]
    mdx, mdy, sdx, sdy = (list(map(int, moves)) + [0, 0, 0, 0])[:4]
    shapes = locked_shapes(pair_id)
    label = (f'claude-{base}-{sub}-{position}-{main_size}-{sub_size}' + (f'-m{mdx}x{mdy}-s{sdx}x{sdy}' if moves else '')
             + ('-rigid' if rigid else '') + ('-override' if override else ''))
    spec = {'id': label.lower().replace('_', '-'), 'base_variant': base, 'sub_variant': sub, 'position': position,
            'main': {'mode': 'preset', 'shape': shapes['main'], 'size': int(main_size), 'dx': mdx, 'dy': mdy},
            'sub': {'mode': 'preset', 'shape': shapes['sub'], 'size': int(sub_size), 'dx': sdx, 'dy': sdy},
            'reason': f'Claude pair-local layout: {base} main + {sub} sub at {position}, main {main_size}, sub {sub_size}.'}
    if override:
        # The locked source keyshape is wrong for this drawing (e.g. a square browser locked to CIRCLE);
        # the canvas limits still apply.
        spec['keyshape_override'] = True
        spec['reason'] += ' Keyshape override: the locked keyshape does not match the drawn shape.'
    if rigid:
        # The whole main as one unit on its keyshape box: every element moves together, undoing a
        # saved layout that rounds small elements (digits) into slightly different scales.
        from .pair_layout_review import keyshape_preset_box
        from .adaptive_overlap import source_path
        item = next(i for i in json.loads(rc.DEFAULT_LAYOUTS.read_text())['items'] if i['reference_id'] == pair_id)
        part = next(p for p in item['parts'] if p['role'] == 'main')
        bounds = source_centerline_bounds(repo_layout_svg(), source_path(part, 'main'), 'main')
        x0, y0, x1, y1 = keyshape_preset_box('main', position, bounds, int(main_size), shapes['main'])
        paths = sorted({i for unit in part['layout'] for i in unit.get('paths', [])})
        spec['main']['units'] = [{'paths': paths, 'x': x0 + mdx, 'y': y0 + mdy, 'w': x1 - x0, 'h': y1 - y0}]
        spec['reason'] += ' Main placed as one rigid unit.'
    return spec


STANDARD = ('current,fill,{p},40,28', 'current,fill,{p},40,28,rigid', 'outline,fill,{p},44,28', 'current,outline,{p},40,32')


def prepare_with_layouts(pair_id):
    """Claim a pair and render the standard trial layouts beside its candidates (one sheet)."""
    try:
        stage = claim(pair_id)
        from .pair_layout_review import ANCHORS
        item = next(i for i in json.loads(rc.DEFAULT_LAYOUTS.read_text())['items'] if i['reference_id'] == pair_id)
        saved = next((p.get('position') for p in item['parts'] if p['role'] == 'sub'), None)
        position = pair_id[-2:] if pair_id[-2:] in ANCHORS else saved if saved in ANCHORS else 'br'
        specs = json.loads((stage / 'layout-proposals.json').read_text())
        existing = specs['pairs'].get(pair_id, [])
        good = []
        for text in STANDARD:
            try:
                spec = quick_spec(pair_id, text.format(p=position))
            except ValueError:      # artwork with transforms: candidates only, no pair-local layouts
                break
            trial = stage / 'trial-specs.json'
            trial.write_text(json.dumps({'schema': 'side-ai-layout-proposals/v1', 'pairs': {pair_id: [*good, spec]}}))
            try:
                render_one(pair_id, specs_path=trial, out=stage / 'trial')
                good.append(spec)
            except Exception:
                continue
        specs['pairs'][pair_id] = [p for p in existing if p['id'] not in {g['id'] for g in good}] + good
        (stage / 'layout-proposals.json').write_text(json.dumps(specs, indent=2) + '\n')
        layout_dir = None
        if specs['pairs'][pair_id]:
            render_one(pair_id, specs_path=stage / 'layout-proposals.json', out=stage / 'layout')
            layout_dir = stage / 'layout'
        out, _table = sheet(pair_id, stage, layout_dir)
        return pair_id, str(out), None
    except Exception as error:
        return pair_id, None, repr(error)[:200]


def write_report():
    """claude-review-data.js for claude-review.html: every pair decided this session, newest first."""
    from urllib.parse import quote
    final = {}
    for entry in logged():
        if entry.get('action') in ('accept', 'hold'):
            final[entry['id']] = entry
    first_status = {}
    for entry in logged():
        if entry.get('action') == 'prep' and entry['id'] not in first_status and entry.get('before'):
            first_status[entry['id']] = entry['before']
    rows = {r['id']: r for r in json.loads(REPORT.read_text())['rows']}
    layouts = json.loads((DEFAULT_LAYOUT_OUTPUT / 'report.json').read_text())['pairs']
    out = []
    for pair_id, entry in sorted(final.items(), key=lambda kv: kv[1]['at'], reverse=True):
        row = rows.get(pair_id, {})
        images = []
        for variant in ([entry.get('variant')] + entry.get('also', [])) if entry['action'] == 'accept' else []:
            if variant.startswith('layout-'):
                candidate = next((c for c in layouts.get(pair_id, {}).get('candidates', []) if c['variant'] == variant), None)
                path = DEFAULT_LAYOUT_OUTPUT / candidate['svg'] if candidate else None
            else:
                candidate = next((c for c in row.get('candidates', []) if c['variant'] == variant), None)
                path = REPORT.parent / candidate['svg'] if candidate else None
            if path and path.is_file():
                images.append({'variant': variant, 'url': quote(str(path.relative_to(ROOT))) + f'?v={path.stat().st_mtime_ns:x}'})
        out.append({'id': pair_id, 'concept': row.get('concept', ''), 'main': row.get('main', ''), 'sub': row.get('sub', ''),
                    'action': entry['action'], 'before': first_status.get(pair_id), 'at': entry['at'],
                    'reason': entry.get('reason', ''), 'images': images})
    (WORK / 'claude-review-data.js').write_text('window.CLAUDE_REVIEW = ' + json.dumps(out) + ';\n')
    print(json.dumps({'pairs': len(out), 'accepted': sum(o['action'] == 'accept' for o in out),
                      'held': sum(o['action'] == 'hold' for o in out)}))


def write_decision(stage, pair_id, record):
    data = json.loads((stage / 'decisions.json').read_text())
    data['decisions'] = {pair_id: record}
    (stage / 'decisions.json').write_text(json.dumps(data, indent=2) + '\n')


def commit(pair_id):
    rc.staged_review(pair_id)
    rc.commit_stage(pair_id)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['next', 'batch', 'prep', 'layout', 'accept', 'hold', 'status', 'report'])
    parser.add_argument('id', nargs='?')
    parser.add_argument('variant', nargs='?')
    parser.add_argument('--set', default='pending_human')
    parser.add_argument('--n', type=int, default=5)
    parser.add_argument('--spec', action='append', default=[])
    parser.add_argument('--quick', action='append', default=[],
                        help='base,sub,position,main_size,sub_size[,mdx,mdy,sdx,sdy]')
    parser.add_argument('--also', action='append', default=[])
    parser.add_argument('--omit', type=int, action='append', default=[],
                        help='main element number to leave out of --quick layouts (user-authorised only)')
    parser.add_argument('--reason')
    args = parser.parse_args()

    if args.command == 'report':
        write_report()
        return
    if args.command == 'status':
        entries = logged()
        final = {}
        for e in entries:
            if e.get('action') in ('accept', 'hold'):
                final[e['id']] = e['action']
        from collections import Counter
        print(json.dumps({'pairs': len(final), 'by_action': Counter(final.values())}))
        return
    if args.command == 'next':
        done = {e['id'] for e in logged() if e.get('action') in ('accept', 'hold')}
        gallery = WORK / 'gallery-data.js'
        text = gallery.read_text()
        rows = json.loads(text[text.index('=') + 1:].rstrip().rstrip(';'))['rows']
        todo = [r['id'] for r in rows if r['selection_status'] == args.set and r['id'] not in done]
        print(json.dumps({'remaining': len(todo), 'next': todo[:args.n]}))
        return

    if args.command == 'batch':
        from concurrent.futures import ProcessPoolExecutor
        # Skip pairs already decided or already prepared (a prepared pair waits for its decision).
        # Also skip pairs whose prep already failed (no sheet can be rendered to review them).
        done = {e['id'] for e in logged() if e.get('action') in ('accept', 'hold') or
                e.get('action') == 'prep'}
        # Also skip pairs another reviewer holds an active claim on.
        with rc.locked_state() as state:
            done |= {pair_id for pair_id, record in state['claims'].items()
                     if record['status'] == 'active' and record.get('owner') != 'claude'}
        text = (WORK / 'gallery-data.js').read_text()
        rows = json.loads(text[text.index('=') + 1:].rstrip().rstrip(';'))['rows']
        todo = [r['id'] for r in rows if r['selection_status'] == args.set and r['id'] not in done][:args.n]
        with ProcessPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(prepare_with_layouts, todo))
        decisions = json.loads(DECISIONS.read_text())['decisions']
        for pair_id, out, error in results:
            log({'id': pair_id, 'action': 'prep', 'sheet': out, 'error': error,
                 'before': (decisions.get(pair_id) or {}).get('status', 'not reviewed')})
        rows_by_id = {r['id']: r for r in rows}
        # Two pairs per image (one Read each), numbered in order.
        good = [(pair_id, out) for pair_id, out, error in results if out]
        duos = []
        for k in range(0, len(good), 2):
            group = good[k:k + 2]
            duo = SESSION / 'duos' / f"{datetime.now().strftime('%H%M%S')}-{k // 2 + 1}.png"
            duo.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(['magick', *[out for _id, out in group], '-bordercolor', '#888888', '-border', '0x3',
                            '-background', 'white', '-gravity', 'west', '-append', str(duo)], check=True)
            duos.append({'image': str(duo), 'pairs': [pair_id for pair_id, _out in group]})
        print(json.dumps({'pairs': [{'id': pair_id, 'concept': rows_by_id[pair_id]['concept'], 'error': error}
                                    for pair_id, out, error in results], 'duos': duos}, indent=1))
        return

    pair_id = args.id
    stage = claim(pair_id)
    if args.command == 'prep':
        out, table = sheet(pair_id, stage)
        decision = json.loads(DECISIONS.read_text())['decisions'].get(pair_id, {})
        try:
            locked = locked_shapes(pair_id)
        except ValueError as error:   # artwork with transforms: no pair-local layouts possible
            locked = repr(error)
        print(json.dumps({'stage': str(stage), 'sheet': str(out), 'locked': locked,
                          'position': pair_id[-2:], 'candidates': table,
                          'before': decision.get('status'), 'ai_note': decision.get('reason', '')[:400]}, indent=1))
        log({'id': pair_id, 'action': 'prep', 'before': decision.get('status'), 'sheet': str(out)})
        return
    if args.command == 'layout':
        specs = json.loads((stage / 'layout-proposals.json').read_text())
        new = [json.loads(spec) for spec in args.spec] + [quick_spec(pair_id, q) for q in args.quick]
        if args.omit:
            for spec in new[len(args.spec):]:
                spec['omit_main_elements'] = args.omit
                spec['id'] += '-omit' + '-'.join(map(str, args.omit))
                spec['reason'] += f' Main element(s) {args.omit} left out at the user\'s request.'
        keep = [p for p in specs['pairs'].get(pair_id, []) if p['id'] not in {n['id'] for n in new}]
        # Try each new layout alone first; only those that render are kept, so one failure
        # (a keyshape or canvas refusal) never blocks the rest.
        dropped = {}
        for spec in new:
            trial = stage / 'trial-specs.json'
            trial.write_text(json.dumps({'schema': 'side-ai-layout-proposals/v1', 'pairs': {pair_id: [*keep, spec]}}))
            try:
                render_one(pair_id, specs_path=trial, out=stage / 'trial')
                keep.append(spec)
            except Exception as error:
                dropped[spec['id']] = str(error)[:160]
        specs['pairs'][pair_id] = keep
        (stage / 'layout-proposals.json').write_text(json.dumps(specs, indent=2) + '\n')
        if dropped:
            print(json.dumps({'dropped': dropped}), file=__import__('sys').stderr)
        rendered = render_one(pair_id, specs_path=stage / 'layout-proposals.json', out=stage / 'layout')
        n = len(list(stage.glob('sheet-layout-*.png'))) + 1
        out, table = sheet(pair_id, stage, stage / 'layout', name=f'sheet-layout-{n}.png')
        info = {c['variant']: {'sub_bounds': c['sub_bounds'], 'fits': {r: v.get('fits_keyshape') for r, v in
                                                                        c.get('keyshape_validation', {}).items()}}
                for c in rendered['candidates']}
        print(json.dumps({'sheet': str(out), 'candidates': table, 'layouts': info}, indent=1))
        log({'id': pair_id, 'action': 'layout', 'specs': new, 'sheet': str(out)})
        return

    if not args.reason or len(args.reason.strip()) < 25:
        raise SystemExit('a concrete visual reason (25+ characters) is required')
    evidence = sorted(str(p) for p in stage.glob('sheet*.png'))
    if args.command == 'hold':
        record = {'status': 'pending_human', 'reviewer': REVIEWER, 'reviewed_at': now(),
                  'review_protocol': rc.REVIEW_PROTOCOL, 'reason': args.reason, 'evidence': evidence}
        write_decision(stage, pair_id, record)
        commit(pair_id)
        log({'id': pair_id, 'action': 'hold', 'reason': args.reason, 'evidence': evidence})
        print(f'{pair_id} pending_human')
        return
    layout_dir = stage / 'layout' if (stage / 'layout' / 'report.json').exists() else DEFAULT_LAYOUT_OUTPUT
    sources = candidate_sources(report_row(pair_id), REPORT.parent, layout_dir)
    chosen = [args.variant, *args.also]
    record = {'status': 'accepted', 'reviewer': REVIEWER, 'reviewed_at': now(),
              'review_protocol': rc.REVIEW_PROTOCOL, 'reason': args.reason, 'evidence': evidence,
              'acceptable_candidate_sha256': {}, 'stress_candidate_sha256': {}}
    for variant in chosen:
        if variant not in sources:
            raise SystemExit(f'unknown variant {variant}; have {sorted(sources)}')
        candidate, path = sources[variant]
        digest = rc.sha(path)
        if variant == args.variant:
            record['variant'], record['candidate_sha256'] = variant, digest
        else:
            record['acceptable_candidate_sha256'][variant] = digest
        if variant.startswith('layout-') and candidate.get('stress_sha256'):
            record['stress_candidate_sha256'][variant] = candidate['stress_sha256']
    write_decision(stage, pair_id, record)
    commit(pair_id)
    log({'id': pair_id, 'action': 'accept', 'variant': args.variant, 'also': args.also,
         'reason': args.reason, 'evidence': evidence})
    print(f'{pair_id} accepted {args.variant}')


if __name__ == '__main__':
    main()
