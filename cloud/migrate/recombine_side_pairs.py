#!/usr/bin/env python3
"""Combine every side pair on this machine with production's current drawings, then update production.

    /opt/homebrew/bin/python3 cloud/migrate/recombine_side_pairs.py --dry-run   # report + files, production unchanged
    /opt/homebrew/bin/python3 cloud/migrate/recombine_side_pairs.py             # combine everything, update production
    /opt/homebrew/bin/python3 cloud/migrate/recombine_side_pairs.py --only <pair id> ...   # just these pairs
    /opt/homebrew/bin/python3 cloud/migrate/recombine_side_pairs.py --force     # re-render pairs already up to date

Every pair with a main and a sub is combined from the drawings production shows now (a version picked in Icon
review wins over the catalog row, as the gallery shows it), keeping a layout saved on production. Each pair's combined
icon in Icon review's "Side combination 64" family then follows its main and sub:

* main and sub both approved in Icon review → combined from those, Ready (a new or changed drawing is a new revision;
  an approved combined icon whose drawing did not change stays approved);
* main or sub not approved → the combined icon shows "Failed check" with the reason, even if it was approved before
  (that approval stays stored and comes back once both parts are approved again with the same drawing), and it cannot
  be approved until they are (the Worker refuses it).

Results are written exactly as the side page's Recombine button writes them (cloud/worker/app/src/routes/side.rs
`save`): D1 store `side-layouts`, a `revisions` row and the pair's `side_combination64/<id>` icon row. A full run (no
--only, no --no-family) also rewrites the family itself: icon rows added / updated / removed, and `icons.json` /
`side-combination64.json` in R2 (what Icon review and the side page list).

Production is read and written with wrangler (the OAuth login, no push token); SQL goes through
`wrangler d1 execute --file` in ≤6 MB files (a 90 MB execute rolls back). Renders are cached in
icon_set/state/side-recombine/ so an interrupted run resumes.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import glob
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import threading
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_d1_import import literal  # noqa: E402
from icon_set.scripts.side_recombine import published_drawings  # noqa: E402

WORKER = ROOT / 'cloud' / 'worker'
STATE = ROOT / 'icon_set' / 'state' / 'side-recombine'
DATABASE = 'pictographic-review'
BUCKET = 'pictographic-review'
FAMILY = 'side_combination64'
SQL_LIMIT = 6 * 1024 * 1024
BATCH = 100  # keys per IN (...) query
SITE = 'https://pictographic-review.pictographic.workers.dev'
AGENT = 'Mozilla/5.0 (pictographic recombine_side_pairs)'  # Cloudflare refuses the Python-urllib agent (1010)
POSITION_LABELS = {'br': 'Bottom-right', 'bl': 'Bottom-left', 'tr': 'Top-right', 'tl': 'Top-left',
                   'ri': 'Right', 'le': 'Left', 'bo': 'Bottom', 'to': 'Top'}
STATUS_WORDS = {None: 'not reviewed', 'ready': 'not reviewed', 're-generated': 'not reviewed', 'pending': 'disapproved',
                'disapprove': 'disapproved', 'claimed': 'being fixed', 'rejected': 'rejected'}


def sha(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


# ---------------------------------------------------------------- production access (wrangler)

def npx() -> str:
    """The newest nvm Node's npx (wrangler needs Node 22+), else the one on PATH."""
    version = lambda path: tuple(int(n) for n in Path(path).parents[1].name.lstrip('v').split('.') if n.isdigit())  # noqa: E731
    candidates = sorted(glob.glob(os.path.expanduser('~/.nvm/versions/node/*/bin/npx')), key=version)
    if candidates and version(candidates[-1]) >= (22,):
        return candidates[-1]
    found = shutil.which('npx')
    if not found:
        raise SystemExit('npx (Node.js 22+) is required for wrangler.')
    return found


def wrangler(*args: str) -> str:
    env = {**os.environ, 'PATH': str(Path(npx()).parent) + os.pathsep + os.environ.get('PATH', '')}
    done = subprocess.run([npx(), 'wrangler', *args], cwd=WORKER, capture_output=True, text=True, env=env)
    if done.returncode:
        raise SystemExit(f'wrangler {" ".join(args[:3])} failed:\n{done.stdout[-2000:]}\n{done.stderr[-2000:]}')
    return done.stdout


def query(sql: str) -> list[dict]:
    out = wrangler('d1', 'execute', DATABASE, '--remote', '--json', '--command', sql)
    return json.loads(out[out.index('['):])[0]['results']


def query_in(sql: str, values: list[str]) -> list[dict]:
    """`sql` with one `{}` for an IN list, run in batches."""
    rows = []
    for start in range(0, len(values), BATCH):
        rows += query(sql.format(','.join(literal(v) for v in values[start:start + BATCH])))
    return rows


def r2_get(name: str) -> Path:
    wrangler('r2', 'object', 'get', f'{BUCKET}/site/gallery/{name}', '--remote', '--file', str(STATE / name))
    return STATE / name


# ---------------------------------------------------------------- pairs and their drawings

def item_key(item: dict) -> str | None:
    """side.rs item_key (the page's sideSubKey): native text has no catalog drawing."""
    if item.get('native_text'):
        return None
    return item.get('model_key') or f"{item.get('family', '')}/{item['icon']}"


def chosen_items(row: dict, saved: dict | None) -> tuple[dict, dict]:
    """The main and sub the side page shows (a saved pair keeps the ones it was made with)."""
    def pick(items, name):
        return next((i for i in items if i['icon'] == name), None)
    main = (saved and pick(row['mains'], saved['main']['icon'])) or \
        next((m for m in row['mains'] if m.get('family') in ('solo', 'combination_main')), row['mains'][0])
    sub = (saved and pick(row['subs'], saved['sub']['icon'])) or row['subs'][0]
    return main, sub


def active(row: dict, entry: dict | None) -> bool:
    """combination_layouts.active: the saved pair still pins the published row's drawings."""
    if not entry:
        return False
    pinned = lambda items, pin: any(i['icon'] == pin.get('icon') and (i.get('sha256') or '') == (pin.get('sha256') or '')  # noqa: E731
                                    for i in items)
    return pinned(row['mains'], entry.get('main') or {}) and pinned(row['subs'], entry.get('sub') or {})


def load_production(only: set[str]) -> dict:
    STATE.mkdir(parents=True, exist_ok=True)
    print('Reading the published side pairs from R2…', flush=True)
    rows = [r for r in json.loads(r2_get('experiment-combination.json').read_text())['rows']
            if r.get('mains') and r.get('subs') and (not only or r['id'] in only)]
    published = json.loads(r2_get('experiment-combination-results.json').read_text()).get('results', {})
    # A published pair given another main / sub on the side page (store side-pairs, routes/side_pairs.rs) is
    # combined there from its own row: recombining the published row here would put the old main / sub back.
    changed = {r['key'] for r in query("SELECT key FROM store_documents WHERE store = 'side-pairs'")}
    rows = [r for r in rows if r['id'] not in changed]
    print(f'{len(rows)} pairs with a main and a sub ({len(changed)} changed on the side page left out).', flush=True)

    print('Reading review statuses, saved pairs and icon rows…', flush=True)
    with urllib.request.urlopen(urllib.request.Request(SITE + '/api/reviews', headers={'User-Agent': AGENT}), timeout=120) as response:
        reviews = json.loads(response.read())
    saved = {r['key']: json.loads(r['document']) for r in query(
        "SELECT key, json_remove(document, '$.result.elements') AS document FROM store_documents WHERE store = 'side-layouts'")}
    keys = sorted({k for row in rows for group in ('mains', 'subs') for item in row[group] if (k := item_key(item))})
    icon_rows = query_in("SELECT key, svg_sha256, build_failed FROM icons WHERE uploaded = 0 AND key IN ({})", keys)
    current = {r['key']: r['svg_sha256'] for r in icon_rows}
    failed = {r['key'] for r in icon_rows if r['build_failed']}
    # edits.rs current_drawing: a picked artwork wins over the icon row. Choices made on a local gallery before
    # the cloud editor never moved the row (an uploaded SVG lives only in its choice).
    picked, svgs, edited = set(), {}, {}
    for r in query_in(
            "SELECT s.key, json_extract(s.document, '$.source_mode') AS mode, json_extract(s.document, '$.source_svg_sha256') AS source, "
            "json_extract(s.document, '$.selected_svg_sha256') AS selected, "
            "CASE WHEN json_type(s.document, '$.selected_upload') = 'object' THEN json_extract(s.document, '$.selected_upload.svg_sha256') "
            "ELSE json_extract(s.document, '$.uploaded.svg_sha256') END AS upload_sha, "
            "CASE WHEN json_type(s.document, '$.selected_upload') = 'object' THEN json_extract(s.document, '$.selected_upload.svg') "
            "ELSE json_extract(s.document, '$.uploaded.svg') END AS upload_svg, "
            "i.svg_sha256 AS icon_sha, EXISTS (SELECT 1 FROM icon_graphs g WHERE g.svg_sha256 = i.svg_sha256) AS built "
            "FROM store_documents s JOIN icons i ON i.key = s.key WHERE s.store = 'icon-artwork' AND i.uploaded = 0 AND s.key IN ({})", keys):
        baseline = r['icon_sha'] if r['built'] else r['source']
        if r['source'] != baseline:
            continue  # made for an older generated drawing
        picked.add(r['key'])
        if r['mode'] == 'use_upload' and r['upload_sha'] and r['upload_svg']:
            current[r['key']] = r['upload_sha']
            svgs[r['upload_sha']] = r['upload_svg']
        elif r['mode'] == 'use_edited' and r['selected']:
            edited[r['key']] = r['selected']
    # The family as it is: every Side combination 64 icon, its drawing and that drawing's review. Pairs made on
    # the cloud from a primitive (store side-pairs, routes/side_pairs.rs) are not in the published rows: left out,
    # so a full run neither removes nor rewrites them.
    family = {r['key']: r for r in query(
        "SELECT i.key, i.svg_sha256, i.build_failed, (SELECT status FROM reviews v WHERE v.icon = i.key "
        f"AND v.svg_sha256 = i.svg_sha256) AS review FROM icons i WHERE i.family = '{FAMILY}' "
        "AND COALESCE(i.icon_id, '') NOT IN (SELECT key FROM store_documents WHERE store = 'side-pairs')")}

    # Only the drawings that differ from the published rows are fetched.
    items_of = {}
    for row in rows:
        for group in ('mains', 'subs'):
            for item in row[group]:
                if key := item_key(item):
                    items_of.setdefault(key, []).append(item)
    changed = lambda key: any(current[key] not in published_drawings(item) for item in items_of.get(key, ()))  # noqa: E731
    wanted = {current[key] for key in current if key in keys and changed(key)} - set(svgs)
    stored = {r['svg_sha256']: r['svg'] for r in query_in(
        'SELECT svg_sha256, svg FROM revisions WHERE svg_sha256 IN ({})', sorted(wanted | set(edited.values())))}
    for key, selected in edited.items():  # an edited pick counts only when its drawing is stored
        if selected in stored:
            current[key] = selected
    svgs.update(stored)
    print(f'{sum(1 for key in keys if key in current and changed(key))} main / sub drawings changed since the pairs were published.', flush=True)
    return {'rows': rows, 'published': published, 'saved': saved, 'current': current, 'svgs': svgs, 'family': family,
            'reviews': reviews, 'failed': failed, 'picked': picked}


# ---------------------------------------------------------------- approval (side_combination_approval.approved_pairs)

def not_approved(prod: dict, item: dict) -> str | None:
    """Why a main / sub is not approved, or None: approved in Icon review, on a drawing that builds or was picked
    (a failed build a reviewer approved as an exception is pushed as built)."""
    key = item_key(item)
    if not key:
        return None  # native text: no catalog drawing to review
    if key not in prod['current']:
        return 'has no drawing on production'
    status = prod['reviews'].get(key)
    if status != 'approve':
        return 'not approved in Icon review (' + STATUS_WORDS.get(status, status) + ')'
    if key in prod['failed'] and key not in prod['picked']:
        return 'fails the build check'
    return None


def pair_items(row: dict, entry: dict | None, prod: dict) -> tuple[dict, dict, list[str]]:
    """The main and sub to combine and why the pair is not approved (empty when it is): the saved pair's if both
    are approved, else the first approved main and sub, else the ones the side page shows."""
    ok = lambda item: not_approved(prod, item) is None  # noqa: E731
    if entry:
        main, sub = chosen_items(row, entry)
        if main['icon'] == entry['main']['icon'] and sub['icon'] == entry['sub']['icon'] and ok(main) and ok(sub):
            return main, sub, []
    main = next((m for m in row['mains'] if ok(m)), None)
    sub = next((s for s in row['subs'] if ok(s)), None)
    if main and sub:
        return main, sub, []
    shown_main, shown_sub = chosen_items(row, entry)
    main, sub = main or shown_main, sub or shown_sub
    reasons = [f"{role.capitalize()} {item['icon']} {why}" for role, item in (('main', main), ('sub', sub))
               if (why := not_approved(prod, item))]
    return main, sub, reasons


def plan(prod: dict, force: bool) -> tuple[list[dict], list[dict], list[str]]:
    """(jobs to render, pairs already up to date, pair ids whose drawing is not stored on production)."""
    jobs, kept, missing = [], [], []
    for row in prod['rows']:
        entry = prod['saved'].get(row['id'])
        entry = entry if active(row, entry) else None
        main, sub, reasons = pair_items(row, entry, prod)
        documents, drawings = {}, {}
        for role, item in (('main', main), ('sub', sub)):
            key = item_key(item)
            drawing = prod['current'].get(key) if key else None
            # side.rs parts(): the drawing production shows, else the published item's.
            drawings[role] = drawing or item.get('sha256') or ''
            if drawing and drawing not in published_drawings(item):
                if drawing not in prod['svgs']:
                    print(f"Skipped {row['id']}: drawing {drawing[:12]} of {key} is not stored.", flush=True)
                    missing.append(row['id'])
                    break
                documents[role] = prod['svgs'][drawing]
        else:
            layout = entry.get('layout') if entry else None
            published = prod['published'].get(row['id']) or {}
            placed = {p.get('role'): p.get('icon') for p in (published.get('result') or {}).get('placements') or []}
            if entry:
                shown_svg = (entry.get('result') or {}).get('svg')
                up_to_date = entry.get('drawings') == drawings and entry['main']['icon'] == main['icon'] and entry['sub']['icon'] == sub['icon']
            else:
                shown_svg = (published.get('result') or {}).get('svg')
                up_to_date = bool(shown_svg) and not documents and placed == {'main': main['icon'], 'sub': sub['icon']}
            job = {'row': row, 'main': main['icon'], 'sub': sub['icon'], 'documents': documents, 'drawings': drawings,
                   'layout': layout, 'shown_svg': shown_svg, 'shown': sha(shown_svg) if shown_svg else None,
                   'main_key': item_key(main), 'sub_key': item_key(sub), 'reasons': reasons}
            (kept if up_to_date and not force else jobs).append(job)
    return jobs, kept, missing


# ---------------------------------------------------------------- rendering

class Cache:
    def __init__(self, path: Path):
        self.path, self.lock, self.pending = path, threading.Lock(), 0
        self.data = json.loads(path.read_text()) if path.is_file() else {}

    @staticmethod
    def key(job: dict) -> str:
        return '|'.join([job['row']['id'], job['main'], job['sub'], job['drawings']['main'], job['drawings']['sub'],
                         sha(json.dumps(job['layout'], sort_keys=True))])

    def get(self, job):
        return self.data.get(self.key(job))

    def put(self, job, result):
        with self.lock:
            self.data[self.key(job)] = result
            self.pending += 1
            if self.pending >= 50:
                self.flush()

    def flush(self):
        if self.pending or not self.path.exists():
            temp = self.path.with_suffix('.tmp')
            temp.write_text(json.dumps(self.data))
            os.replace(temp, self.path)
            self.pending = 0


def render_all(jobs: list[dict], workers: int) -> tuple[list[tuple[dict, dict]], list[tuple[dict, str]]]:
    from icon_set.scripts.combination_experiment import render
    from icon_set.scripts.side_recombine import pair_with_documents
    cache = Cache(STATE / 'cache.json')
    done, failed, count = [], [], [0]
    lock = threading.Lock()

    def one(job):
        result = cache.get(job)
        if result is None:
            row, chosen = pair_with_documents(job['row'], job['main'], job['sub'], job['documents'])
            request = {'id': row['id'], **chosen}
            if job['layout']:
                request['layout'] = job['layout']
            result = {k: v for k, v in render(request, row=row).items() if k != 'elements'}
            cache.put(job, result)
        return result

    def run(job):
        try:
            result = one(job)
            with lock:
                done.append((job, result))
        except Exception as error:  # noqa: BLE001 - one failing pair never stops the run
            with lock:
                failed.append((job, str(error) or type(error).__name__))
        with lock:
            count[0] += 1
            if count[0] % 25 == 0 or count[0] == len(jobs):
                print(f'Rendered {count[0]} of {len(jobs)}', flush=True)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(run, jobs))
    with cache.lock:
        cache.flush()
    return done, failed


# ---------------------------------------------------------------- SQL

def chunked(statements: list[str], name: str) -> list[Path]:
    """Statements in ≤6 MB files icon_set/state/side-recombine/sql/<name>-NNN.sql (old ones of that name removed)."""
    folder = STATE / 'sql'
    folder.mkdir(parents=True, exist_ok=True)
    for stale in folder.glob(f'{name}-*.sql'):
        stale.unlink()
    files, buffer, size = [], [], 0

    def flush():
        nonlocal buffer, size
        if buffer:
            files.append(folder / f'{name}-{len(files) + 1:03d}.sql')
            files[-1].write_text('\n'.join(buffer) + '\n')
            buffer, size = [], 0

    for statement in statements:
        n = len(statement.encode('utf-8')) + 1
        if buffer and size + n > SQL_LIMIT:
            flush()
        buffer.append(statement)
        size += n
    flush()
    return files


def pair_statements(job: dict, result: dict, user: str, now: str) -> list[str]:
    """side.rs save(): the saved pair and its drawing (the family icon row is written by family_statements)."""
    row, svg = job['row'], result['svg']
    pin = lambda group, name: {'icon': name, 'sha256': next((i.get('sha256', '') for i in row[group] if i['icon'] == name), '')}  # noqa: E731
    entry = {'main': pin('mains', job['main']), 'sub': pin('subs', job['sub']), 'layout': job['layout'], 'result': result,
             'drawings': job['drawings'], 'svg_sha256': sha(svg), 'user': user, 'updated_at': now}
    document = json.dumps(entry, ensure_ascii=False, separators=(',', ':'))
    return [
        'INSERT INTO store_documents(store, key, document, updated_at, updated_by) VALUES '
        f"('side-layouts', {literal(row['id'])}, {literal(document)}, {literal(now)}, {literal(user)}) "
        'ON CONFLICT(store, key) DO UPDATE SET document = excluded.document, updated_at = excluded.updated_at, '
        'updated_by = excluded.updated_by;',
        f"INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES "
        f"({literal(sha(svg))}, {literal(FAMILY + '/' + row['id'])}, {literal(svg)}, 'side-layout', {literal(now)});",
    ]


# ---------------------------------------------------------------- the Side combination 64 family

def family_record(job: dict, svg: str, result: dict | None, previous: dict, reference: str | None, now: str) -> dict:
    """experiment_gallery.stage_side_combination64's record; a pair that is not approved fails its check."""
    row, digest = job['row'], sha(svg)
    errors = job['reasons']
    return {
        'key': f"{FAMILY}/{row['id']}", 'icon_id': row['id'], 'name': row['concept'], 'family': FAMILY,
        'profile': 'SIDE_COMBINATION64', 'canvas_size': int((result or {}).get('canvas') or previous.get('canvas_size') or 64),
        'category': POSITION_LABELS.get(row.get('position'), row.get('position') or 'Side'),
        'position': row.get('position'), 'native_text': bool(row.get('native_text')),
        'main_icon': job['main'], 'sub_icon': job['sub'], 'main_key': job['main_key'], 'sub_key': job['sub_key'],
        'tags': [], 'keywords': [], 'aliases': [], 'description': '',
        'svg_sha256': digest, 'preview_url': f"combination-previews/{row['id']}.svg?v={digest[:12]}",
        'build_failed': bool(errors), 'errors': errors,
        'validation': {'status': 'fail', 'automatic_status': 'fail', 'errors': errors} if errors
        else {'status': 'valid', 'automatic_status': 'pass', 'errors': []},
        'original_sources': [{'url': reference, 'format': 'SVG', 'source_path': reference}] if reference else [],
        'python_source': None,
        'created_at': previous['created_at'] if previous.get('svg_sha256') == digest and previous.get('created_at') else now,
        'created_at_source': 'side-combination-run',
    }


def family_statements(records: list[dict], svgs: dict[str, str], leaving: list[str], now: str, push_id: str) -> list[str]:
    out = []
    for r in records:
        record = json.dumps({'main_key': r['main_key'], 'sub_key': r['sub_key'], 'errors': r['errors']}, ensure_ascii=False)
        values = [r['key'], r['icon_id'], r['name'], FAMILY, r['category'], r['profile'], r['canvas_size'], r['svg_sha256'],
                  None, r['preview_url'], json.dumps(r['original_sources'], ensure_ascii=False), None, None, None,
                  int(r['build_failed']), 0, record, push_id]
        out.append('INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, python_source, '
                   'preview_url, original_sources, variant_of, variant_root, variant_label, build_failed, uploaded, record, pushed_at) '
                   'VALUES (' + ', '.join(literal(v) for v in values) + ') ON CONFLICT(key) DO UPDATE SET name = excluded.name, '
                   'category = excluded.category, canvas_size = excluded.canvas_size, svg_sha256 = excluded.svg_sha256, '
                   'preview_url = excluded.preview_url, original_sources = excluded.original_sources, '
                   'build_failed = excluded.build_failed, record = excluded.record, pushed_at = excluded.pushed_at '
                   'WHERE icons.uploaded = 0;')
        out.append('INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES '
                   f"({literal(r['svg_sha256'])}, {literal(r['key'])}, {literal(svgs[r['svg_sha256']])}, 'side-layout', {literal(now)});")
    for start in range(0, len(leaving), BATCH):
        out.append(f"DELETE FROM icons WHERE family = '{FAMILY}' AND key IN ({', '.join(literal(k) for k in leaving[start:start + BATCH])});")
    return out


def prepare_family(prod: dict, finals: list[tuple[dict, str, dict | None]], missing: list[str], now: str) -> dict:
    """Records, SQL files and R2 files that make the family one icon per combined pair."""
    from push_catalog import icons_json
    print('Reading icons.json and the combination catalog from R2…', flush=True)
    catalog = json.loads(r2_get('icons.json').read_text())
    references = json.loads(r2_get('combinations.json').read_text()).get('references', {})
    old = {r['key']: r for r in catalog.get('icons', []) if r.get('family') == FAMILY}
    records, svgs = [], {}
    for job, svg, result in finals:
        key = f"{FAMILY}/{job['row']['id']}"
        records.append(family_record(job, svg, result, old.get(key, {}), references.get(job['row']['id'], {}).get('reference_url'), now))
        svgs[sha(svg)] = svg
    keys = {r['key'] for r in records}
    # A pair skipped for a missing drawing keeps its icon as it is; only pairs that are gone leave the family.
    keep = keys | {f'{FAMILY}/{pair_id}' for pair_id in missing}
    leaving = sorted(set(prod['family']) - keep)
    kept_records = [r for r in catalog.get('icons', []) if r.get('family') == FAMILY and r['key'] in keep - keys]
    push_id = 'recombine-' + now.replace(':', '').replace('-', '')
    files = chunked(family_statements(records, svgs, leaving, now, push_id), 'family')
    catalog['icons'] = [r for r in catalog.get('icons', []) if r.get('family') != FAMILY] + kept_records + records
    content, layout = icons_json(catalog)
    (STATE / 'icons.new.json').write_bytes(content)
    family_json = {'generated_at': now, 'count': len(records) + len(kept_records), 'icons': kept_records + records}
    (STATE / 'side-combination64.new.json').write_text(json.dumps(family_json, ensure_ascii=False, separators=(',', ':')) + '\n')
    previous = query('SELECT details FROM catalog_pushes ORDER BY id DESC LIMIT 1')
    details = json.loads(previous[0]['details']) if previous else {}
    details.update(icons_json=layout, side_family={'count': family_json['count'], 'removed': len(leaving),
                                                   'by': 'recombine_side_pairs', 'at': now})
    push = chunked([f"INSERT INTO catalog_pushes(pushed_at, pushed_by, details) VALUES ({literal(now)}, 'recombine-all', "
                    f"{literal(json.dumps(details))});"], 'catalog-push')
    return {'records': records, 'leaving': leaving, 'files': files, 'push': push}


def outcome(prod: dict, records: list[dict]) -> dict:
    """How each combined icon lands in Icon review, from its drawing before and after and that drawing's review."""
    counts = {'ready_new': 0, 'ready_changed': 0, 'approved_kept': 0, 'unchanged_other': 0, 'failed_check': 0,
              'approvals_reset': 0, 'approvals_held_by_failed_check': 0}
    for r in records:
        before = prod['family'].get(r['key'])
        same = bool(before) and before['svg_sha256'] == r['svg_sha256']
        approved_before = bool(before) and before['review'] == 'approve'
        if r['build_failed']:
            counts['failed_check'] += 1
            counts['approvals_held_by_failed_check'] += same and approved_before
        elif not before:
            counts['ready_new'] += 1
        elif not same:
            counts['ready_changed'] += 1
            counts['approvals_reset'] += approved_before
        elif approved_before:
            counts['approved_kept'] += 1
        else:
            counts['unchanged_other'] += 1
    return counts


# ---------------------------------------------------------------- main

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--only', nargs='+', default=[], metavar='PAIR_ID', help='combine only these pairs (the family is not rewritten)')
    parser.add_argument('--jobs', type=int, default=4, help='parallel renders (default 4)')
    parser.add_argument('--force', action='store_true', help='re-render pairs that are already up to date')
    parser.add_argument('--dry-run', action='store_true', help='render and write the files, but change nothing on production')
    parser.add_argument('--no-family', action='store_true', help="leave Icon review's Side combination 64 family as it is")
    parser.add_argument('--user', default='recombine-all', help='recorded as the author of the saved pairs')
    args = parser.parse_args(argv)

    prod = load_production(set(args.only))
    jobs, kept, missing = plan(prod, args.force)
    print(f'{len(jobs)} pairs to render, {len(kept)} already up to date.', flush=True)
    done, failed = render_all(jobs, args.jobs)
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')

    # Each pair's final drawing: the new render, else (up to date, or its render failed) the drawing it shows now.
    finals = [(job, result['svg'], result) for job, result in done]
    finals += [(job, job['shown_svg'], None) for job in kept + [job for job, _error in failed] if job['shown_svg']]
    saved = [(job, result) for job, result in done if sha(result['svg']) != job['shown']]
    statements = [s for job, result in saved for s in pair_statements(job, result, args.user, now)]

    sync = not (args.only or args.no_family)
    family = prepare_family(prod, finals, missing, now) if sync else None
    if family:
        records = family['records']
    else:  # only the icon rows of these pairs: drawing and check follow the same rules
        records = [family_record(job, svg, result, {}, None, now) for job, svg, result in finals
                   if f"{FAMILY}/{job['row']['id']}" in prod['family']]
        for r in records:
            statements.append(f"UPDATE icons SET svg_sha256 = {literal(r['svg_sha256'])}, build_failed = {int(r['build_failed'])}, "
                              f"record = {literal(json.dumps({'main_key': r['main_key'], 'sub_key': r['sub_key'], 'errors': r['errors']}))} "
                              f"WHERE key = {literal(r['key'])} AND family = '{FAMILY}';")
    counts = outcome(prod, records)
    summary = {'pairs': len(prod['rows']), 'rendered': len(done), 'saved': len(saved), 'render_failed': len(failed),
               'skipped_missing_drawing': len(missing), 'icon_review': counts}
    if family:
        summary['icon_review']['family_size'] = len(records)
        summary['icon_review']['removed'] = len(family['leaving'])
    statements.append('INSERT INTO activity_log(username, action, icon, details, created_at) VALUES '
                      f"({literal(args.user)}, 'side_recombine_all', NULL, {literal(json.dumps(summary))}, {literal(now)});")
    files = chunked(statements, 'pairs')

    for job, error in failed[:20]:
        print(f"Failed {job['row']['id']} ({job['row'].get('concept', '')}): {error}", file=sys.stderr)
    if len(failed) > 20:
        print(f'… and {len(failed) - 20} more failures.', file=sys.stderr)
    print(json.dumps(summary, indent=2))
    if args.dry_run:
        print(f'Dry run: SQL and files are in {STATE}; production is unchanged.')
        return 0
    for path in files + (family['files'] if family else []):
        print(f'Applying {path.name} ({path.stat().st_size / 1e6:.1f} MB)…', flush=True)
        wrangler('d1', 'execute', DATABASE, '--remote', '--yes', '--file', str(path))
    if family:
        print('Uploading side-combination64.json and icons.json…', flush=True)
        wrangler('r2', 'object', 'put', f'{BUCKET}/site/gallery/side-combination64.json', '--remote',
                 '--file', str(STATE / 'side-combination64.new.json'), '--content-type', 'application/json')
        wrangler('r2', 'object', 'put', f'{BUCKET}/site/gallery/icons.json', '--remote',
                 '--file', str(STATE / 'icons.new.json'), '--content-type', 'application/json')
        for path in family['push']:
            wrangler('d1', 'execute', DATABASE, '--remote', '--yes', '--file', str(path))
    c = counts
    print(f"Production updated. Icon review: {c['ready_new']} new + {c['ready_changed']} changed combined icons are Ready "
          f"({c['approvals_reset']} of them were approved), {c['approved_kept']} stay approved, "
          f"{c['failed_check']} show Failed check" + (f", {len(family['leaving'])} removed" if family else '') + '.')
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
