"""The 72 fill side pairs (migration 0026): the 72 set's main-54 + sub-36 pairs on the 72 canvas, as fill-remake made
and reviewed them, brought into this app beside the 64 ones.

    python3 -m icon_set side-fill import72 --from ~/Downloads/fill-remake [--write]
                    copy fill-remake's export (side_combinations/output/fill72-app, written by its
                    `python3 -m side_combinations.export_fill72_app`) into icon_set/data/side-fill-72; report only
                    without --write. Every file is checked against the export's sha256.
    python3 -m icon_set side-fill icons72      the fill variant icons + manifest for upload_fill_parts.py --size 72
    python3 -m icon_set side-fill d1-import72  side-fill-72-import.sql (pairs, parts, totals) and side-fill-72-picks.sql
    python3 -m icon_set side-fill goldens72 [--count N]   fixtures for icon_set/tests/js/side-fill.test.mjs at 72

The snapshot (icon_set/data/side-fill-72, data: not in git):
  export.json                   pairs (picks, the pair's own placement, state, note), parts (status, variants), excluded
  parts/<role>/<name>/source.svg            the part's main-54 / sub-36 drawing (its icon on the site)
  parts/<role>/<name>/<variant>.svg         a fill variant as fill-remake made it (stroke-fill/v1 regions tucked 0.5 px)
  renders/<pair>.svg            the pick fill-remake rendered and reviewed (its rank 1): the goldens' expected drawing

Pairs fill-remake could only make from a part that is not a main-54 / sub-36 icon (drawn from 64 or a 48 drawing, a
text label, or none) are not here: export.json `excluded` lists them (the user's decision, 2026-11-11).

A pick names icons as at 64: a fill variant is <part>--fill (the main's current, the sub's fill) or
<part>--fill-<variant>, the outline is the part's own icon. Layout boxes are on the 72 grid.
"""
import argparse
import gzip
import hashlib
import json
import random
import shutil
from datetime import datetime, timezone
from pathlib import Path

from . import d1_import as D
from .fill_icons import compact, fill_key, on_canvas, portable
from .paths import ICON_SET

DATA72 = ICON_SET / 'data' / 'side-fill-72'
WORK72 = ICON_SET / 'state' / 'side-fill-72'
GOLDENS72 = ICON_SET / 'tests/js/fixtures/side-fill-72'
EXPORT = 'side_combinations/output/fill72-app/export.json'
SIZE = 72


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def text_sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def snapshot():
    return json.loads((DATA72 / 'export.json').read_text())


# ======== import72 ========

def import_export(source, write):
    """Copy fill-remake's 72 export into the snapshot, every file checked against its sha256."""
    export = json.loads((Path(source).expanduser() / EXPORT).read_text())
    if export.get('schema') != 'fill72-app-export/v1':
        raise SystemExit(f'not a fill72 app export: {export.get("schema")}')
    copies, problems = [], []

    def plan(src, digest, dest):
        src = Path(src)
        if not src.is_file():
            problems.append(f'missing {src}')
        elif sha(src) != digest:
            problems.append(f'changed since the export: {src}')
        copies.append((src, dest))
        return str(dest)
    parts = {}
    for key, part in export['parts'].items():
        role, name = part['role'], part['name']
        folder = Path('parts') / role / name
        out = {**part, 'source': plan(part['source'], part['source_sha256'], folder / 'source.svg'), 'variants': []}
        for v in part['variants']:
            out['variants'].append({**v, 'file': plan(v['file'], v['svg_sha256'], folder / f"{v['variant']}.svg")})
        parts[key] = out
    pairs = []
    for pair in export['pairs']:
        picks = [{**p, 'render': plan(p['render'], p['render_sha256'], Path('renders') / f"{pair['id']}--{p['rank']}.svg")}
                 for p in pair['picks']]
        pairs.append({**pair, 'picks': picks})
    snap = {**export, 'parts': parts, 'pairs': pairs, 'imported_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'imported_from': str(Path(source).expanduser())}
    report = {'pairs': len(pairs), 'parts': len(parts), 'files': len(copies), 'excluded': len(export['excluded']),
              'problems': problems[:20], 'problem_count': len(problems)}
    if write and not problems:
        for path in DATA72.iterdir() if DATA72.exists() else []:
            if path.name != '.gitignore':
                shutil.rmtree(path) if path.is_dir() else path.unlink()
        for src, dest in copies:
            target = DATA72 / dest
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, target)
        (DATA72 / 'export.json').write_text(json.dumps(snap, indent=1) + '\n')
        report['written'] = str(DATA72)
    return report


# ======== icons72 ========

def variant_svg(part, variant):
    """A variant as the upload route stores it (fill_icons.portable at 5 decimals), on its source drawing's canvas."""
    text = portable(compact((DATA72 / variant['file']).read_text()), variant.get('reverse', False))
    return on_canvas(text, (DATA72 / part['source']).read_text())


def export_icons():
    """icon_set/state/side-fill-72/fill-icons/<role>/<name>/<variant>.svg and manifest.json, as fill_icons.export
    writes them at 64: [{key, source_key, variant, name, svg, svg_sha256, source_sha256}]."""
    snap = snapshot()
    out = WORK72 / 'fill-icons'
    manifest, off_canvas = [], []
    for key, part in sorted(snap['parts'].items()):
        for variant in part['variants']:
            svg = variant_svg(part, variant)
            if svg is None:
                off_canvas.append(f"{key} {variant['variant']}")
                continue
            path = out / part['role'] / part['name'] / f"{variant['variant']}.svg"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(svg)
            manifest.append({'key': fill_key(key, variant['variant']), 'source_key': key, 'variant': variant['variant'],
                             'name': f"{part['name']} {variant['variant']}", 'svg': str(path.relative_to(WORK72)),
                             'svg_sha256': text_sha(svg), 'source_sha256': part['source_sha256']})
    out.mkdir(parents=True, exist_ok=True)
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=1) + '\n')
    families = {}
    for m in manifest:
        families[m['source_key'].split('/')[0]] = families.get(m['source_key'].split('/')[0], 0) + 1
    return {'icons': len(manifest), 'by_family': families, 'off_canvas': off_canvas, 'manifest': str(out / 'manifest.json')}


# ======== d1-import72 ========

def pick_icon(pair, role, variant):
    source = pair[role]
    return source if variant == 'outline' else fill_key(source, variant)


def d1_statements(now=None):
    """(import statements, pick statements) of the 72 pairs, as d1_import.build writes the 64 ones: upserts that keep
    what people did on the site (an edited pair's picks and state, a part filled there), and every delete and total
    limited to size 72."""
    snap = snapshot()
    now = now or datetime.now(timezone.utc).isoformat(timespec='seconds')
    pairs_sql, parts_sql, picks_sql = [], [], []
    for pair in snap['pairs']:
        layouts = [D.q(json.dumps(pair['layout'][r])) if pair['layout'].get(r) else 'NULL' for r in ('main', 'sub')]
        pairs_sql.append(D.pair_statement(pair['id'], D.sort_key(pair['concept'], pair['id']), pair['state'], pair['main'], pair['sub'],
                                          layouts, pair['note'], now, size=SIZE))
        for pick in pair['picks']:
            for role in ('main', 'sub'):
                chosen = pick[role]
                icon = pick_icon(pair, role, chosen['variant'])
                layout = json.dumps(chosen['layout']) if chosen.get('layout') else None
                picks_sql.append(D.pick_statement(pair['id'], role, pick['rank'], icon, layout, None, now,
                                                  exists=chosen['variant'] != 'outline', size=SIZE))
    pairs_sql.append(f"DELETE FROM fill_pairs WHERE size = {SIZE} AND updated_at != {D.q(now)};")
    for key, part in sorted(snap['parts'].items()):
        parts_sql.append(D.part_statement(key, part['role'], D.sort_key(part['name'], key), part['status'], part['note'], None,
                                          part['pairs'], now, size=SIZE))
    parts_sql.append(f"DELETE FROM fill_parts WHERE size = {SIZE} AND updated_at != {D.q(now)};")
    counts = D.counts_sql(SIZE)
    imports = pairs_sql + parts_sql + counts
    picks = picks_sql + [D.picks_tail(now, size=SIZE)] + counts + [
        f"UPDATE fill_pairs SET version = version + 1 WHERE size = {SIZE} AND edited_at IS NULL;"]
    return imports, picks


def d1_import():
    imports, picks = d1_statements()
    WORK72.mkdir(parents=True, exist_ok=True)
    (WORK72 / 'side-fill-72-import.sql').write_text('\n'.join(imports) + '\n')
    (WORK72 / 'side-fill-72-picks.sql').write_text('\n'.join(picks) + '\n')
    snap = snapshot()
    states = {}
    for pair in snap['pairs']:
        states[pair['state']] = states.get(pair['state'], 0) + 1
    return {'pairs': len(snap['pairs']), 'states': states, 'parts': len(snap['parts']),
            'pick_rows': sum(len(p['picks']) * 2 for p in snap['pairs']),
            'import_sql': str(WORK72 / 'side-fill-72-import.sql'), 'picks_sql': str(WORK72 / 'side-fill-72-picks.sql')}


# ======== goldens72 ========

def golden_cases(count=300, seed=72):
    """Real 72 picks of every kind, with the drawing fill-remake rendered for each: the outline / stroke-fill / flat /
    reverse kinds of main and sub, the pair's own placement or a moved one, and every flat fallback."""
    snap = snapshot()
    by_kind = {}
    for pair in snap['pairs']:
        for pick in pair['picks']:
            kind = []
            for role in ('main', 'sub'):
                v = pick[role]['variant']
                if v == 'outline':
                    kind.append('outline')
                    continue
                entry = next(x for x in snap['parts'][pair[role]]['variants'] if x['variant'] == v)
                kind.append('flat-fallback' if v.endswith('-flat') else 'reverse' if entry.get('reverse')
                            else 'stroke-fill' if entry['file'].endswith('.svg') and 'stroke-fill' in (DATA72 / entry['file']).read_text()[:400]
                            else 'flat')
            kind.append('moved' if pick['main']['layout'] != pair['layout']['main'] or pick['sub']['layout'] != pair['layout']['sub'] else 'placed')
            by_kind.setdefault(tuple(kind), []).append((pair, pick))
    rng = random.Random(seed)
    chosen = []
    for kind, items in sorted(by_kind.items()):
        rng.shuffle(items)
        take = len(items) if 'flat-fallback' in kind else max(1, round(count * len(items) / sum(map(len, by_kind.values()))))
        chosen += [(kind, *item) for item in items[:take]]
    return chosen


def at_72():
    """The Python combine set to 72 for this process: the 72 canvas and stroke-fill regions tucked 0.5 px (as
    side-fill-combine.js does for a size 72 pick)."""
    from . import combine_fill_side as cfs, combine_fill_side_layouts as cfl, stroke_fill_format as sf
    cfs.CANVAS = cfl.CANVAS = SIZE
    sf.TUCK = 0.5


def write_goldens(count=300):
    """Fixtures of real 72 picks combined by pick_combine at 72 (the reference side-fill-combine.js is held to). Each
    also says how far fill-remake's reviewed render is from it (reviewed_differs_px2): fill-remake's reader painted a
    whole stroke white where a dashed white cut of a closed path was meant (stroke_fill_format._chained), so those
    reviewed renders lack that outline; the app draws it."""
    from .combine_fill_side import geometry_to_svg, load_fill
    from .pick_combine import combine
    at_72()
    snap = snapshot()
    shutil.rmtree(GOLDENS72, ignore_errors=True)
    GOLDENS72.mkdir(parents=True)
    (GOLDENS72 / '.gitignore').write_text('# Made from the 72 snapshot by `python3 -m icon_set side-fill goldens72`; not in git.\n*\n!.gitignore\n')
    written = 0
    for kind, pair, pick in golden_cases(count):
        roles = {}
        for role in ('main', 'sub'):
            part = snap['parts'][pair[role]]
            source = (DATA72 / part['source']).read_text()
            v = pick[role]['variant']
            if v == 'outline':
                svg = source
            else:
                svg = variant_svg(part, next(x for x in part['variants'] if x['variant'] == v))
            roles[role] = {'svg': svg, 'source': source, 'layout': pick[role]['layout'], 'outline': v == 'outline'}
        combined, cut, sub, _details = combine({**roles, 'options': {}})
        reviewed, _ = load_fill(DATA72 / pick['render'])
        case = {'id': pair['id'], 'rank': pick['rank'], 'variant': f"{pick['main']['variant']} + {pick['sub']['variant']}",
                'kind': list(kind), 'size': SIZE,
                'pick': {**roles, 'options': {}, 'size': SIZE},
                'expected': {'svg': geometry_to_svg(combined, f'0 0 {SIZE} {SIZE}'), 'area': round(combined.area, 3),
                             'main_area': round(cut.area, 3), 'sub_area': round(sub.area, 3)},
                'reviewed_differs_px2': round(combined.symmetric_difference(reviewed).area, 2)}
        with gzip.open(GOLDENS72 / f"{pair['id']}--{pick['rank']}.json.gz", 'wt') as handle:
            json.dump(case, handle)
        written += 1
    return {'goldens': written, 'folder': str(GOLDENS72)}


# ======== commands ========

def main(command, argv):
    parser = argparse.ArgumentParser(prog=f'side-fill {command}', description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    if command == 'import72':
        parser.add_argument('--from', dest='source', required=True, help='a fill-remake checkout')
        parser.add_argument('--write', action='store_true')
    if command == 'goldens72':
        parser.add_argument('--count', type=int, default=300)
    args = parser.parse_args(argv)
    if command == 'import72':
        result = import_export(args.source, args.write)
    elif command == 'icons72':
        result = export_icons()
    elif command == 'd1-import72':
        result = d1_import()
    else:
        result = write_goldens(args.count)
    print(json.dumps(result, indent=1))
    return 1 if result.get('problem_count') else 0
