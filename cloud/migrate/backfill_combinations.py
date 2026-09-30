#!/usr/bin/env python3
"""Fill the combination columns of reference_parts (migration 0009) from the old stores.

    python3 cloud/migrate/backfill_combinations.py --db snapshot.sqlite --pairs experiment-combination.json --out fill.sql
    wrangler d1 execute <database> --remote --file fill.sql            # from cloud/worker

Reads a D1 snapshot (``wrangler d1 export`` loaded into sqlite, opened read-only) and the published
``site/gallery/experiment-combination.json``; writes idempotent SQL. Rerun it on a fresh export before
moving over: every statement sets values, none depends on an earlier run.

In order, later sources winning:

1. published side pairs (the pairs file, keyed by combination reference id): the icon each part shows on
   the side page, and the drawing the published combined icon was built from; a part the seed skipped
   (no id in combination_data.json) is added from the pairs file's main_id / sub_id;
2. ``side-layouts`` store: the drawings a saved pair was rendered from (their icons via ``revisions``),
   and each part's box: the hand-adjusted layout, else the automatic placement the engine chose;
3. ``side-pairs`` store: a pair given another main / sub; a primitive classified as a combination
   becomes a combination reference with its two parts;
4. ``container_centers`` (when the snapshot has it): the symbol's box;
5. container / symbol parts with a single icon of their family.

Also sets the side position of subs seeded without one (the id's suffix) and links every combined icon
(side_combination64/<id>, container_combination64/<id>) to its reference in icon_references.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sqlite3

POSITIONS = ('tl', 'tr', 'bl', 'br', 'ri', 'le', 'bo', 'to')


def q(value) -> str:
    if value is None:
        return 'NULL'
    if isinstance(value, (dict, list)):
        value = json.dumps(value, separators=(',', ':'))
    return "'" + str(value).replace("'", "''") + "'"


def item_key(item: dict) -> str | None:
    """side.rs item_key: the catalog key of a pair item; native text has none."""
    if item.get('native_text'):
        return None
    return item.get('model_key') or f"{item.get('family', '')}/{item['icon']}"


def shown_main(row: dict) -> dict | None:
    """The main the side page shows: the first solo / combination_main one, else the first."""
    mains = row.get('mains') or []
    return next((m for m in mains if m.get('family') in ('solo', 'combination_main')), mains[0] if mains else None)


def centreline_box(painted: dict | None) -> list | None:
    """The engine's painted box as a layout box: stroke centrelines, 2 in from each side for the 4-unit stroke."""
    if not painted:
        return None
    return [{'x': painted['x'] + 2, 'y': painted['y'] + 2, 'w': painted['w'] - 4, 'h': painted['h'] - 4}]


class Parts:
    """reference_parts values by (reference_id, role), merged across sources."""

    def __init__(self):
        self.values: dict[tuple[str, str], dict] = {}
        self.sources = Counter()

    def set(self, ref: str, role: str, source: str, **fields):
        self.values.setdefault((ref, role), {}).update(fields)
        self.sources[source] += 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--db', required=True, type=Path)
    parser.add_argument('--pairs', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()

    db = sqlite3.connect(f'file:{args.db}?mode=ro', uri=True)
    db.row_factory = sqlite3.Row
    references = {r['reference_id']: r['kind'] for r in db.execute('SELECT reference_id, kind FROM "references"')}
    existing = {(r['reference_id'], r['role']): r for r in db.execute('SELECT * FROM reference_parts')}
    icons = {r['key']: r for r in db.execute('SELECT key, family, svg_sha256 FROM icons')}
    by_sha = dict(db.execute('SELECT svg_sha256, icon FROM revisions'))
    tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    parts = Parts()
    notes = Counter()
    statements: list[str] = []

    # 1. Published side pairs.
    rows = json.loads(args.pairs.read_text())['rows']
    for row in rows:
        ref = row['id']
        if ref not in references:
            notes['published pair without reference'] += 1
            continue
        built = icons.get(f'side_combination64/{ref}')
        for role, item in (('main', shown_main(row)), ('sub', (row.get('subs') or [None])[0])):
            if item is None:
                continue
            key = item_key(item)
            if key is None:
                notes['native text sub (no icon)'] += 1
            fields = {'icon': key}
            if (ref, role) not in existing:
                # combination_data.json had no id for this part (the seed skips those); the pairs file has it.
                if row.get(f'{role}_id'):
                    fields['part_reference_id'] = row[f'{role}_id']
                fields['position'] = row.get('position') if role == 'sub' else None
                notes[f'published pair {role} part added'] += 1
            if built is not None and built['svg_sha256']:
                fields['built_sha'] = item.get('source_sha256') or item.get('sha256')
            parts.set(ref, role, 'published pair', **fields)

    # 2. Saved side layouts (a recombined or hand-adjusted pair).
    for key, text in db.execute("SELECT key, document FROM store_documents WHERE store = 'side-layouts'"):
        entry = json.loads(text)
        if key not in references:
            notes['layout without reference'] += 1
            continue
        layout = entry.get('layout') or {}
        placed = {p.get('role'): p.get('painted_box') for p in (entry.get('result') or {}).get('placements') or []}
        for role in ('main', 'sub'):
            sha = (entry.get('drawings') or {}).get(role)
            fields = {'built_sha': sha, 'layout': layout.get(role) or centreline_box(placed.get(role)),
                      'updated_at': entry.get('updated_at'), 'updated_by': entry.get('user')}
            if sha in by_sha:
                fields['icon'] = by_sha[sha]
            else:
                notes[f'layout {role} drawing not in revisions'] += 1
            parts.set(key, role, 'side layout', **fields)

    # 3. Side pairs saved on the cloud.
    for key, text in db.execute("SELECT key, document FROM store_documents WHERE store = 'side-pairs'"):
        pair = json.loads(text)
        when = {'updated_at': pair.get('updated_at'), 'updated_by': pair.get('updated_by')}
        if references.get(key) == 'single':
            # A primitive classified as a combination: it becomes one, its parts are the picked icons.
            statements.append(f'UPDATE "references" SET kind = \'combination\' WHERE reference_id = {q(key)};')
            notes['primitive made a combination'] += 1
        for role in ('main', 'sub'):
            icon = pair.get(f'{role}_id') or ''
            if icon.startswith('draw:') or icon not in icons:
                notes[f'side pair {role} still to draw'] += 1
                icon = None
            fields = {'icon': icon, **when}
            if role == 'sub':
                fields['position'] = pair.get('position') or None
            parts.set(key, role, 'side pair', **fields)

    # 4. Container centers (migration 0006; absent until it runs).
    if 'container_centers' in tables:
        columns = {r[1] for r in db.execute('PRAGMA table_info(container_centers)')}
        for c in db.execute('SELECT * FROM container_centers'):
            c = dict(c)
            if c['sub']:
                notes['container center for one pair (not mapped)'] += 1
                continue
            w, h = (c.get('width') or 32, c.get('height') or 32) if 'width' in columns else (32, 32)
            box = [{'x': c['x'] - w / 2, 'y': c['y'] - h / 2, 'w': w, 'h': h}]
            for (ref, role), part in existing.items():
                if role == 'container' and parts.values.get((ref, role), {}).get('icon', part['icon'] if 'icon' in part.keys() else None) == c['main']:
                    parts.set(ref, 'symbol', 'container center', layout=box,
                              updated_at=c['updated_at'], updated_by=c['updated_by'])

    # 5. Container / symbol parts with exactly one icon of their family.
    links: dict[str, list[str]] = {}
    for icon, ref in db.execute('SELECT icon, reference_id FROM icon_references'):
        links.setdefault(ref, []).append(icon)
    for (ref, role), part in existing.items():
        if role not in ('container', 'symbol') or 'icon' in parts.values.get((ref, role), {}):
            continue
        candidates = [i for i in links.get(part['part_reference_id'], []) if i.split('/', 1)[0] == role]
        if len(candidates) == 1:
            parts.set(ref, role, f'single {role} icon', icon=candidates[0])
        else:
            notes[f'{role} part with {"no" if not candidates else "several"} {role} icons'] += 1

    # Positions the seed left empty: the side position is the reference id's suffix.
    for (ref, role), part in existing.items():
        if role == 'sub' and part['position'] is None and ref[-2:] in POSITIONS \
                and 'position' not in parts.values.get((ref, role), {}):
            parts.set(ref, role, 'position from id', position=ref[-2:])

    # A new part the sources gave no reference for (native text pairs, mains without an id): its icon's.
    for (ref, role), fields in parts.values.items():
        if (ref, role) in existing or fields.get('part_reference_id'):
            continue
        linked = db.execute('SELECT reference_id FROM icon_references WHERE icon = ? ORDER BY reference_id LIMIT 1',
                            (fields.get('icon'),)).fetchone() if fields.get('icon') else None
        fields['part_reference_id'] = linked[0] if linked else f"icon:{fields.get('icon') or ''}"
        notes['new part: reference from its icon' if linked else 'new part: no reference (icon: placeholder)'] += 1

    for (ref, role), fields in sorted(parts.values.items()):
        if (ref, role) in existing:
            sets = ', '.join(f'{name} = {q(value)}' for name, value in fields.items())
            statements.append(f'UPDATE reference_parts SET {sets} WHERE reference_id = {q(ref)} AND role = {q(role)};')
        else:
            names = ['reference_id', 'role', *fields]
            values = [ref, role, *fields.values()]
            statements.append(f'INSERT OR REPLACE INTO reference_parts({", ".join(names)}) VALUES ({", ".join(map(q, values))});')

    # Combined icons → their reference.
    linked = 0
    for key in icons:
        family, _, ref = key.partition('/')
        if family in ('side_combination64', 'container_combination64') and ref in references:
            statements.append(f'INSERT OR IGNORE INTO icon_references(icon, reference_id) VALUES ({q(key)}, {q(ref)});')
            linked += 1

    args.out.write_text('\n'.join(statements) + '\n')
    print(f'{len(statements)} statements → {args.out}')
    for source, n in parts.sources.items():
        print(f'  {n:6d} part values from {source}')
    print(f'  {linked:6d} combined icons linked to their reference')
    for note, n in sorted(notes.items()):
        print(f'  {n:6d} {note}')


if __name__ == '__main__':
    main()
