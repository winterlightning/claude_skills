#!/usr/bin/env python3
"""Container combinations as local processing: fetch production, fix locally, push the fixes back.

    python3 icon_set/scripts/combination_sync.py fetch
    python3 icon_set/scripts/combination_sync.py status [--family container] [ICON_ID ...]
    python3 icon_set/scripts/combination_sync.py push   [--family container] (--changed | ICON_ID ...) [--send]
    python3 icon_set/scripts/combination_sync.py approve --reviewer NAME [--family container] (--pushed | ICON_ID ...) [--send]
    python3 icon_set/scripts/combination_sync.py builds  --builder NAME [REFERENCE_ID ...] [--send]

fetch   Reads production (no writes): review statuses, every container pair with its parts, the current drawing of
        every part and of every local module of the family, and the placement defaults. Writes the snapshot the
        local tools work from into the work folder (default icon_set/work/container-combination64): reviews.json,
        items.json, drawings.json, container-centers.json, approved-pairs.json (pairs whose container and SYMBOL32
        symbol are both approved) and text-pairs.json (pairs whose symbol is text, from container-text-v2.json).

status  Builds the family's local modules into a scratch dist (build.py --dist; published/ is not touched) and
        compares each drawing with production's: unchanged, changed (the local fix differs) or new. Writes
        sync-status.json. Run fetch first so production's side is current.

push    Pushes local drawings to production's catalog: each selected icon's row, drawing, editor graph and record,
        by POST /api/catalog/push with `final` false, so only those icons are written and nothing else in the
        catalog changes (a final push deletes every icon it does not carry; this tool never sends one). A changed
        drawing is a new revision: its review status starts again on production. Without --send it only prints
        what would be pushed. Needs PICTOGRAPHIC_PUSH_TOKEN in cloud/.env (or the environment).

builds  Stores combo.py's combined container icons (out/pairs/<reference_id>.svg) on production as the
        container_combination64 icons, as POST /api/combinations/build would for BUILDER: the drawing as a
        'combination-build' revision, the icon row and its list columns, the pair's parts with the drawing each was
        built from (production's current sha) and its boxes, and the activity entry. A part not approved in Icon
        review makes the combined icon fail its check with the server's own message, as the route does. Text pairs
        send their symbol part without an icon (native text). Run fetch first. Without --send it writes the SQL only.

approve Records an approval by REVIEWER on each icon's current production drawing, as POST /api/reviews would for
        that reviewer: the activity entry, the review row (icon, svg_sha256) and the list counts again (the core
        UNCOUNT_ICON / REFRESH_KEY / RECOUNT_ICON statements). The API takes the reviewer from a login, so this goes
        to D1 with `wrangler d1 execute --remote` (the wrangler OAuth login on this machine). Only icons whose current
        production drawing is the one built locally are approved. Without --send it writes the SQL file only.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'cloud' / 'migrate'))
import cloudapi  # noqa: E402
import push_catalog  # noqa: E402

DEFAULT_API = 'https://pictographic-review.pictographic.workers.dev'
DEFAULT_WORK = ROOT / 'icon_set' / 'work' / 'container-combination64'
MODULES = ROOT / 'icon_set' / 'model' / 'icons'
TEXT_DATA = ROOT / 'icon_set' / 'data' / 'container-text-v2.json'
PUSH_CHUNK = 100
D1_DATABASE = 'pictographic-review-next'  # cloud/worker/wrangler.toml: both Workers use it
# wrangler 4 needs Node 22+; the shell's default nvm Node may be older.
NODE22 = sorted(Path.home().glob('.nvm/versions/node/v2[2-9]*/bin'))
WRANGLER = [str(NODE22[-1] / 'npx') if NODE22 else 'npx', '--yes', 'wrangler@4']
UNCOUNT_ICON = [
    "UPDATE icon_counts SET n = n - 1 WHERE (family, side_role, style, state, category, built_failed) = ("
    "SELECT COALESCE(family, ''), COALESCE(side_role, ''), style, COALESCE(state, ''), COALESCE(category, ''), "
    "build_failed FROM icons WHERE key = ?1)",
    "UPDATE icon_facet_counts SET n = n - 1 WHERE (kind, value) IN ("
    "SELECT 'author' AS kind, COALESCE(author, 'unknown') AS value FROM icons WHERE key = ?1 "
    "UNION ALL SELECT 'family', COALESCE(family, '') FROM icons WHERE key = ?1 "
    "UNION ALL SELECT 'keyshape', keyshape FROM icons WHERE key = ?1 AND NOT build_failed AND keyshape IS NOT NULL "
    "UNION ALL SELECT 'category', category FROM icons WHERE key = ?1 AND NOT build_failed AND COALESCE(category, '') != '' "
    "UNION ALL SELECT 'total', 'built' FROM icons WHERE key = ?1 AND NOT build_failed)"]
REFRESH_KEY = ("UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, "
               "cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, "
               "v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = ?1")
RECOUNT_ICON = [
    "INSERT INTO icon_counts(family, side_role, style, state, category, built_failed, n) "
    "SELECT COALESCE(family, ''), COALESCE(side_role, ''), style, COALESCE(state, ''), COALESCE(category, ''), build_failed, 1 "
    "FROM icons WHERE key = ?1 ON CONFLICT(family, side_role, style, state, category, built_failed) DO UPDATE SET n = n + 1",
    "INSERT INTO icon_facet_counts(kind, value, n) SELECT kind, value, 1 FROM ("
    "SELECT 'author' AS kind, COALESCE(author, 'unknown') AS value FROM icons WHERE key = ?1 "
    "UNION ALL SELECT 'family', COALESCE(family, '') FROM icons WHERE key = ?1 "
    "UNION ALL SELECT 'keyshape', keyshape FROM icons WHERE key = ?1 AND NOT build_failed AND keyshape IS NOT NULL "
    "UNION ALL SELECT 'category', category FROM icons WHERE key = ?1 AND NOT build_failed AND COALESCE(category, '') != '' "
    "UNION ALL SELECT 'total', 'built' FROM icons WHERE key = ?1 AND NOT build_failed"
    ") WHERE 1 ON CONFLICT(kind, value) DO UPDATE SET n = n + 1"]


def get_json(api: str, path: str):
    status, body = cloudapi.request(api, 'GET', path, timeout=300)
    if status >= 400:
        raise SystemExit(f'GET {path} -> HTTP {status}: {body[:200]!r}')
    return json.loads(body)


def module_files(family: str) -> dict[str, Path]:
    """icon_id -> module file for every module of the family."""
    out = {}
    for f in sorted((MODULES / family).glob('*.py')):
        if f.name.startswith('_'):
            continue
        for icon_id in re.findall(r"icon_id = ['\"]([^'\"]+)['\"]", f.read_text()):  # a file may hold several
            out[icon_id] = f
    return out


def write(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')


# ---- fetch

def fetch(args) -> None:
    api, work = args.api, args.work
    work.mkdir(parents=True, exist_ok=True)
    reviews = get_json(api, '/api/reviews')
    items, offset = [], 0
    while offset is not None:
        page = get_json(api, '/api/combinations?' + urllib.parse.urlencode({'kind': 'container', 'limit': 500, 'offset': offset}))
        items += page['items']
        offset = page.get('next_offset')
    keys = {p['icon'] for i in items for p in i['parts'] if p.get('icon')}
    keys |= {f'container/{i}' for i in module_files('container')}
    if (work / 'symbol-assignments.json').exists():
        keys |= {v['symbol'] for v in json.loads((work / 'symbol-assignments.json').read_text())['pairs'].values()}
    drawings, ordered = {}, sorted(keys)
    for n in range(0, len(ordered), 100):
        drawings.update(get_json(api, '/api/combinations/drawings?keys=' + urllib.parse.quote(','.join(ordered[n:n + 100]))))
    centers = get_json(api, '/gallery/container-centers.json')

    approved = []
    for i in items:
        parts = {p['role']: p for p in i['parts']}
        c, s = parts.get('container', {}), parts.get('symbol', {})
        # The symbol must be approved; the container may still be under review (a pushed redraw): such a pair is
        # combined for review and its combined icon fails its check until the container is approved.
        if (c.get('icon') or '').startswith('container/') and s.get('review') == 'approve' and (s.get('icon') or '').startswith('symbol/'):
            approved.append({'reference_id': i['reference_id'], 'concept': i['concept'], 'state': i['state'],
                             'container': c['icon'], 'symbol': s['icon'], 'container_review': c.get('review')})
    # Pairs with no symbol on production get one from symbol-assignments.json (drawn or reused symbols).
    assigned = json.loads((work / 'symbol-assignments.json').read_text())['pairs'] if (work / 'symbol-assignments.json').exists() else {}
    review = reviews if isinstance(reviews, dict) else {}
    for i in items:
        parts = {p['role']: p for p in i['parts']}
        c, s = parts.get('container', {}), parts.get('symbol', {})
        got = assigned.get(i['reference_id'])
        if got and not s.get('icon') and (c.get('icon') or '').startswith('container/'):
            approved.append({'reference_id': i['reference_id'], 'concept': i['concept'], 'state': i['state'],
                             'container': c['icon'], 'symbol': got['symbol'], 'container_review': c.get('review'),
                             'assigned': True})
    text_of = {}
    data = json.loads(TEXT_DATA.read_text())
    for group in ('icons', 'lowercase_later'):
        for e in data[group]:
            for c in e['combinations']:
                text_of[c['combination_id']] = (group, e['text'], bool(e.get('underline')))
    texts = []
    for i in items:
        parts = {p['role']: p for p in i['parts']}
        if i['reference_id'] in text_of and parts.get('container', {}).get('icon'):
            group, text, underline = text_of[i['reference_id']]
            texts.append({'reference_id': i['reference_id'], 'concept': i['concept'], 'container': parts['container']['icon'],
                          'container_review': parts['container'].get('review'), 'group': group, 'text': text,
                          'underline': underline})
    write(work / 'reviews.json', reviews)
    write(work / 'items.json', items)
    write(work / 'drawings.json', drawings)
    write(work / 'container-centers.json', centers)
    write(work / 'approved-pairs.json', {'fetched': now(), 'source': api, 'pairs': approved})
    write(work / 'text-pairs.json', texts)
    summary = {'fetched': now(), 'api': api, 'pairs': len(items), 'drawings': len(drawings),
               'approved_symbol_pairs': len(approved), 'text_pairs': len(texts)}
    write(work / 'fetch.json', summary)
    print(json.dumps(summary, indent=2))


# ---- status

def scratch_build(family: str, files: list[Path], dist: Path) -> dict:
    """Build the given modules into `dist` and return the build's catalog (gallery/icons.json)."""
    cmd = [sys.executable, str(ROOT / 'icon_set' / 'scripts' / 'build.py'), '--dist', str(dist),
           '--png-dir', str(dist / '_png'), '--allow-validation-failures']
    for f in dict.fromkeys(files):
        cmd += ['--icon', str(f)]
    run = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if run.returncode != 0:
        raise SystemExit(f'build failed:\n{run.stdout[-2000:]}\n{run.stderr[-2000:]}')
    catalog = json.loads((dist / 'gallery' / 'icons.json').read_text())
    # review-facets.json (measured mirror axes) from the build's QA report, as the gallery stages it; the push
    # stores it with each icon (an icon pushed without one has its symmetry cleared).
    sys.path.insert(0, str(ROOT / 'icon_set' / 'scripts'))
    import gallery
    gallery.stage_review_facets(catalog['icons'] + catalog.get('failed_icons', []), dist, dist, dist / 'gallery')
    return catalog


def status(args) -> dict:
    work, family = args.work, args.family
    drawings = json.loads((work / 'drawings.json').read_text())
    reviews = json.loads((work / 'reviews.json').read_text())
    modules = module_files(family)
    ids = args.ids or sorted(modules)
    unknown = [i for i in ids if i not in modules]
    if unknown:
        raise SystemExit(f'no {family} module for: {", ".join(unknown)}')
    dist = work / 'build' / family
    catalog = scratch_build(family, [modules[i] for i in ids], dist)
    records = {r['key']: (r, field) for field in ('icons', 'failed_icons') for r in catalog.get(field, [])}
    rows = []
    for i in ids:
        key = f'{family}/{i}'
        record, field = records.get(key, (None, None))
        local = record.get('svg_sha256') if record else None
        remote = (drawings.get(key) or {}).get('svg_sha256')
        state = 'missing-build' if not local else 'new' if not remote else 'unchanged' if local == remote else 'changed'
        rows.append({'key': key, 'state': state, 'build_failed': field == 'failed_icons',
                     'validation': ((record or {}).get('validation') or {}).get('status'),
                     'production_review': reviews.get(key), 'local_sha': local, 'production_sha': remote})
    report = {'checked': now(), 'family': family, 'dist': str(dist), 'icons': rows}
    write(work / 'sync-status.json', report)
    counts = {}
    for r in rows:
        counts[r['state']] = counts.get(r['state'], 0) + 1
    print(f'{family}: ' + ', '.join(f'{v} {k}' for k, v in sorted(counts.items())))
    failed = [r['key'] for r in rows if r['build_failed']]
    if failed:
        print(f'{len(failed)} fail validation (not pushable): ' + ', '.join(failed[:20]))
    return report


# ---- push

def push(args) -> None:
    work, family = args.work, args.family
    report = status(args) if args.ids else json.loads((work / 'sync-status.json').read_text())
    if report['family'] != family:
        raise SystemExit(f'sync-status.json is for {report["family"]}; run status --family {family}')
    rows = {r['key']: r for r in report['icons']}
    if args.ids:
        wanted = [f'{family}/{i}' for i in args.ids]
    elif args.changed:
        wanted = [k for k, r in rows.items() if r['state'] in ('changed', 'new')]
    else:
        raise SystemExit('name the icons to push, or --changed for every icon whose local drawing differs')
    blocked = [k for k in wanted if rows[k]['build_failed'] or rows[k]['state'] == 'missing-build']
    wanted = [k for k in wanted if k not in blocked and rows[k]['state'] != 'unchanged']
    dist = Path(report['dist'])
    catalog = json.loads((dist / 'gallery' / 'icons.json').read_text())
    icon_rows, built = push_catalog.rows(dist, None, catalog, push_catalog.load_facets(dist, None))
    icon_rows = [r for r in icon_rows if r['key'] in wanted]
    missing = [r['key'] for r in icon_rows if not r['svg']]
    if missing or built['sha_mismatch']:
        raise SystemExit(f'drawings missing or not matching their hash: {missing + built["sha_mismatch"]}')
    print(f'{len(icon_rows)} {family} icons to push' + (f'; skipped (failing validation): {", ".join(blocked)}' if blocked else ''))
    for r in icon_rows:
        state = rows[r['key']]
        print(f"  {r['key']:60} {state['state']:9} production review: {state['production_review']}")
    if args.via == 'wrangler':
        return push_sql(args, icon_rows)
    if not args.send:
        print('dry run: nothing sent. Add --send to push these to', args.api)
        return
    token = cloudapi.push_token(args.api)
    push_id = 'sync-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    for start in range(0, len(icon_rows), PUSH_CHUNK):
        chunk = [{k: v for k, v in r.items()} for r in icon_rows[start:start + PUSH_CHUNK]]
        cloudapi.post_json(args.api, '/api/catalog/push', {'push_id': push_id, 'icons': chunk, 'final': False}, token)
        print(f'pushed {start + len(chunk)}/{len(icon_rows)}', flush=True)
    write(work / f'push-{push_id}.json', {'push_id': push_id, 'api': args.api, 'keys': [r['key'] for r in icon_rows]})
    print('done; run fetch to refresh the local snapshot')


def wrangler(args_list: list[str]) -> subprocess.CompletedProcess:
    import os
    env = dict(os.environ, PATH=f"{Path(WRANGLER[0]).parent}{os.pathsep}{os.environ.get('PATH', '')}")
    return subprocess.run(WRANGLER + args_list, cwd=ROOT / 'cloud' / 'worker', capture_output=True, text=True, env=env)


def rehearse(sql_files: list[Path]) -> None:
    """Run the SQL on an empty SQLite database built from the Worker's migrations; raises on any error."""
    import sqlite3
    db = sqlite3.connect(':memory:')
    for migration in sorted((ROOT / 'cloud' / 'worker' / 'migrations').glob('*.sql')):
        db.executescript(migration.read_text())
    for f in sql_files:
        db.executescript(f.read_text())
    n = db.execute('SELECT COUNT(*) FROM icons').fetchone()[0]
    print(f'rehearsal on the migrations schema: ok ({n} icon rows written)')


def push_sql(args, icon_rows: list[dict]) -> None:
    """The non-final catalog push as SQL (push_sql, the Worker's own statements), run with wrangler d1 execute."""
    work = args.work
    push_id = 'sync-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    stamp = datetime.now(timezone.utc).isoformat()
    helper = work / 'push_sql'
    build = subprocess.run(['cargo', 'build', '--release', '--quiet'], cwd=helper, capture_output=True, text=True,
                           env=dict(__import__('os').environ, PATH=str(Path.home() / '.cargo/bin') + ':' + __import__('os').environ['PATH']))
    if build.returncode != 0:
        raise SystemExit(build.stderr[-2000:])
    out_dir = work / 'pushes' / push_id
    out_dir.mkdir(parents=True)
    files, chunk, size, part = [], [], 0, 1
    def flush():
        nonlocal chunk, size, part
        if not chunk:
            return
        rows_file = out_dir / f'rows-{part:03}.json'
        rows_file.write_text(json.dumps(chunk, ensure_ascii=False))
        sql = subprocess.run([str(helper / 'target/release/push_sql'), str(rows_file), push_id, stamp],
                             capture_output=True, text=True, check=True).stdout
        target = out_dir / f'push-{part:03}.sql'
        target.write_text(sql)
        files.append(target)
        chunk, size, part = [], 0, part + 1
    for row in icon_rows:  # files under ~4 MB: D1 rolls a very large execute back
        weight = len(json.dumps(row, ensure_ascii=False)) * 3
        if size + weight > 4_000_000:
            flush()
        chunk.append(row)
        size += weight
    flush()
    print(f'{len(files)} SQL file(s) in {out_dir}: ' + ', '.join(f'{f.name} {f.stat().st_size // 1024} KB' for f in files))
    rehearse(files)
    if not args.send:
        print('dry run: nothing sent. Add --send to run them on D1', D1_DATABASE)
        return
    info = wrangler(['d1', 'time-travel', 'info', D1_DATABASE, '--json'])
    (out_dir / 'bookmark-before.json').write_text(info.stdout)
    print('time-travel bookmark before the push saved:', (out_dir / 'bookmark-before.json'))
    for f in files:
        run = wrangler(['d1', 'execute', D1_DATABASE, '--remote', '--yes', '--file', str(f.resolve())])
        print(f.name, 'exit', run.returncode, run.stdout[-600:].strip(), run.stderr[-600:].strip())
        if run.returncode != 0:
            raise SystemExit(f'stopped at {f.name}; restore with: wrangler d1 time-travel restore {D1_DATABASE} --bookmark <bookmark-before>')
    write(work / f'push-{push_id}.json', {'push_id': push_id, 'via': 'wrangler', 'database': D1_DATABASE,
                                          'keys': [r['key'] for r in icon_rows]})
    print('done; run fetch to refresh the local snapshot')


# ---- builds

def group_box(svg: str, gid: str) -> dict:
    """The centreline box {x, y, w, h} of the <g id=gid> group: its rendered ink box (1/8 unit) less half a stroke."""
    import io
    import numpy as np, cairosvg
    from PIL import Image
    g = re.search(r'<g id="%s".*?</g>' % gid, svg, re.S).group(0)
    head = '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">'
    png = cairosvg.svg2png(bytestring=(head + g + '</svg>').encode(), output_width=512, output_height=512)
    ys, xs = np.where(np.array(Image.open(io.BytesIO(png)).split()[-1]) > 127)
    r = lambda v: round(float(v), 2)
    x0, y0, x1, y1 = xs.min() / 8 + 2, ys.min() / 8 + 2, (xs.max() + 1) / 8 - 2, (ys.max() + 1) / 8 - 2
    return {'x': r(x0), 'y': r(y0), 'w': r(max(0, x1 - x0)), 'h': r(max(0, y1 - y0))}


def built_on_production(api: str, want: dict) -> int:
    """How many of {reference_id: sha} production shows built with exactly that drawing."""
    got, offset = {}, 0
    while offset is not None:
        page = get_json(api, '/api/combinations?' + urllib.parse.urlencode({'kind': 'container', 'state': 'built', 'limit': 500, 'offset': offset}))
        got.update({i['reference_id']: (i.get('icon') or {}).get('svg_sha256') for i in page['items']})
        offset = page.get('next_offset')
    return sum(got.get(k) == v for k, v in want.items())


def builds(args) -> None:
    work = args.work
    results = json.loads((work / 'combos-result.json').read_text())
    items = {i['reference_id']: i for i in json.loads((work / 'items.json').read_text())}
    drawings = json.loads((work / 'drawings.json').read_text())
    reviews = json.loads((work / 'reviews.json').read_text())
    refs = args.ids or sorted(results)
    assigned = json.loads((work / 'symbol-assignments.json').read_text())['pairs'] if (work / 'symbol-assignments.json').exists() else {}
    rows, skipped = [], []
    for ref in refs:
        r = results.get(ref)
        if not r or r.get('error') or ref not in items:
            skipped.append((ref, 'no combined icon' if not r or r.get('error') else 'not a production pair')); continue
        own = {p['role']: p.get('icon') for p in items[ref]['parts']}
        if set(own) != {'container', 'symbol'}:
            skipped.append((ref, 'parts are not container + symbol')); continue
        want = {'container': f"container/{r['container']}",
                'symbol': f"symbol/{r['symbol']}" if r['kind'] == 'symbol' else None}
        # A pair with no symbol on production may take its assigned one (symbol-assignments.json).
        assigned_ok = own['symbol'] is None and assigned.get(ref, {}).get('symbol') == want['symbol']
        if own['container'] != want['container'] or (r['kind'] == 'text' and own['symbol']) or \
                (r['kind'] == 'symbol' and own['symbol'] != want['symbol'] and not assigned_ok):
            skipped.append((ref, 'production pair has other parts')); continue
        svg = (work / 'out' / 'pairs' / f'{ref}.svg').read_text()
        parts, errors = {}, []
        for role in ('container', 'symbol'):
            key = want[role]
            box = group_box(svg, role)
            if key is None:
                parts[role] = {'icon': None, 'svg_sha256': None, 'layout': [box]}
                continue
            if key not in drawings:
                break
            parts[role] = {'icon': key, 'svg_sha256': drawings[key]['svg_sha256'], 'layout': [box]}
            if reviews.get(key) != 'approve':
                errors.append(f"{role.capitalize()} {key.split('/', 1)[1]} is not approved in Icon review")
        else:
            rows.append({'reference_id': ref, 'svg': svg, 'parts': parts, 'errors': errors})
            continue
        skipped.append((ref, 'a part has no production drawing'))
    failing = sum(1 for r in rows if r['errors'])
    print(f'{len(rows)} combined icons to store ({failing} with a part not approved: they show as failing their check); '
          f'{len(skipped)} skipped')
    for ref, why in skipped[:10]:
        print('  skipped', ref, why)
    helper = work / 'push_sql'
    subprocess.run(['cargo', 'build', '--release', '--quiet'], cwd=helper, check=True,
                   env=dict(__import__('os').environ, PATH=str(Path.home() / '.cargo/bin') + ':' + __import__('os').environ['PATH']))
    stamp = datetime.now(timezone.utc).isoformat()
    run_id = 'build-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out_dir = work / 'pushes' / run_id
    out_dir.mkdir(parents=True)
    files, chunk, size = [], [], 0
    def flush():
        nonlocal chunk, size
        if not chunk:
            return
        n = len(files) + 1
        rows_file = out_dir / f'builds-{n:03}.json'
        rows_file.write_text(json.dumps(chunk, ensure_ascii=False))
        run = subprocess.run([str(helper / 'target/release/push_sql'), 'build', str(rows_file), stamp, args.builder],
                             capture_output=True, text=True, check=True)
        if run.stderr.strip():
            print(run.stderr.strip())
        target = out_dir / f'build-{n:03}.sql'
        target.write_text(run.stdout)
        files.append(target)
        chunk, size = [], 0
    for row in rows:
        weight = len(row['svg']) * 3 + 6000
        if size + weight > 3_500_000:
            flush()
        chunk.append(row); size += weight
    flush()
    print(f'{len(files)} SQL file(s) in {out_dir}')
    rehearse(files)
    if not args.send:
        print('dry run: nothing sent. Add --send to run them on D1', D1_DATABASE)
        return
    info = wrangler(['d1', 'time-travel', 'info', D1_DATABASE, '--json'])
    (out_dir / 'bookmark-before.json').write_text(info.stdout)
    print('time-travel bookmark before the builds saved:', out_dir / 'bookmark-before.json')
    for f in files:
        run = wrangler(['d1', 'execute', D1_DATABASE, '--remote', '--yes', '--file', str(f.resolve())])
        rows = json.loads((out_dir / f.name.replace('build-', 'builds-').replace('.sql', '.json')).read_text())
        stored = built_on_production(args.api, {r['reference_id']: hashlib.sha256(r['svg'].encode()).hexdigest() for r in rows})
        # wrangler can report "Not currently importing anything" after an import that finished: judge by the result.
        print(f'{f.name}: exit {run.returncode}, {stored}/{len(rows)} stored as built')
        if stored != len(rows):
            print(run.stdout[-800:], run.stderr[-800:])
            raise SystemExit(f'stopped at {f.name}; restore with the bookmark in {out_dir}')
    write(work / f'{run_id}.json', {'run': run_id, 'builder': args.builder, 'database': D1_DATABASE,
                                    'references': [r['reference_id'] for r in rows]})
    print('done; run fetch to refresh the local snapshot')


# ---- approve

def sql_text(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def approve(args) -> None:
    work, family, reviewer = args.work, args.family, args.reviewer
    report = json.loads((work / 'sync-status.json').read_text())
    local = {r['key']: r['local_sha'] for r in report['icons'] if r['local_sha']}
    keys = [f'{family}/{i}' for i in args.ids] if args.ids else sorted(local) if args.pushed else None
    if not keys:
        raise SystemExit('name the icons to approve, or --pushed for every icon in sync-status.json')
    current = {}
    for n in range(0, len(keys), 100):
        current.update(get_json(args.api, '/api/combinations/drawings?keys=' + urllib.parse.quote(','.join(keys[n:n + 100]))))
    ready = [k for k in keys if (current.get(k) or {}).get('svg_sha256') == local.get(k)]
    waiting = [k for k in keys if k not in ready]
    stamp = datetime.now(timezone.utc).isoformat()
    lines = []
    for key in ready:
        sha, q = local[key], sql_text(key)
        details = json.dumps({'status': 'approve', 'svg_sha256': sha})  # python_json: ", " and ": " separators
        lines += [s.replace('?1', q) + ';' for s in UNCOUNT_ICON]
        lines.append(f"INSERT INTO activity_log(username, action, icon, details, created_at) VALUES "
                     f"({sql_text(reviewer)}, 'review', {q}, {sql_text(details)}, {sql_text(stamp)});")
        lines.append(f"INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES "
                     f"({q}, {sql_text(sha)}, 'approve', {sql_text(stamp)}, {sql_text(reviewer)}) "
                     f"ON CONFLICT(icon, svg_sha256) DO UPDATE SET status = excluded.status, updated_at = excluded.updated_at, "
                     f"updated_by = excluded.updated_by, worker = NULL, claimed_at = NULL, note = '';")
        lines.append(REFRESH_KEY.replace('?1', q) + ';')
        lines += [s.replace('?1', q) + ';' for s in RECOUNT_ICON]
    path = work / f"approve-{reviewer}-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.sql"
    path.write_text('\n'.join(lines) + '\n')
    print(f'{len(ready)} icons to approve as {reviewer}; SQL in {path}')
    if waiting:
        print(f'{len(waiting)} skipped: production does not show the local drawing yet (push first): ' + ', '.join(waiting[:10]))
    if not args.send or not ready:
        print('dry run: nothing sent. Add --send to run it on D1', D1_DATABASE)
        return
    import os
    env = dict(os.environ, PATH=f"{Path(WRANGLER[0]).parent}{os.pathsep}{os.environ.get('PATH', '')}")
    run = subprocess.run(WRANGLER + ['d1', 'execute', D1_DATABASE, '--remote', '--yes', '--file', str(path)],
                         cwd=ROOT / 'cloud' / 'worker', capture_output=True, text=True, env=env)
    print(run.stdout[-1500:], run.stderr[-1500:])
    if run.returncode != 0:
        raise SystemExit('wrangler failed; nothing is approved if the batch rolled back -- check the output above')


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--api', default=DEFAULT_API, help='production Worker URL')
    parser.add_argument('--work', type=Path, default=DEFAULT_WORK, help='local work folder')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('fetch', help='read production into the local snapshot')
    b = sub.add_parser('builds', help="store combo.py's combined icons on production")
    b.add_argument('ids', nargs='*', help='reference ids (default: every combined pair)')
    b.add_argument('--builder', required=True, help='who the builds are recorded for')
    b.add_argument('--send', action='store_true', help='run the SQL on D1 (default: write it only)')
    for name in ('status', 'push', 'approve'):
        p = sub.add_parser(name)
        p.add_argument('--family', default='container', choices=['container', 'symbol'])
        p.add_argument('ids', nargs='*', help='icon ids (default for status: every module of the family)')
        if name == 'push':
            p.add_argument('--changed', action='store_true', help='every icon whose local drawing differs from production')
            p.add_argument('--send', action='store_true', help='actually push (default: dry run)')
            p.add_argument('--via', choices=['api', 'wrangler'], default='api',
                           help='api: POST /api/catalog/push with the push token; wrangler: the same statements as SQL '
                                'through wrangler d1 execute (the OAuth login), rehearsed locally first')
        if name == 'approve':
            p.add_argument('--reviewer', required=True, help='the reviewer the approvals are recorded for')
            p.add_argument('--pushed', action='store_true', help='every icon in sync-status.json')
            p.add_argument('--send', action='store_true', help='run the SQL on D1 (default: write it only)')
    args = parser.parse_args(argv)
    {'fetch': fetch, 'status': status, 'push': push, 'approve': approve, 'builds': builds}[args.command](args)


if __name__ == '__main__':
    main()
