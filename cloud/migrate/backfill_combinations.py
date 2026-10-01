#!/usr/bin/env python3
"""Fill the combination columns of reference_parts (migration 0009) from the old stores.

    python3 cloud/migrate/backfill_combinations.py --db snapshot.sqlite --pairs experiment-combination.json \
        --combinations combinations.json --out fill.sql
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
4. container / symbol parts with a single icon of their family;
5. the icons the old Container pairs page showed (``site/gallery/combinations.json``, ``--combinations``): the
   container's generated container drawing and the symbol source's symbol drawing (a source drawn only as a sub
   gets none: the Worker takes symbol icons only);
6. ``reference_uploads`` (dropped by 0010): an upload for a part's source fills a part still without an icon,
   an upload for the combination itself (a pair's own symbol, e.g. its typeface text) wins;
7. ``container_centers`` (dropped by 0010): symbol placements saved for a pair or for a whole container.

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
# What the side engine reads of a pair item (combine-side.js); the rest of the published item is left out.
FORM_FIELDS = ('icon', 'family', 'model_key', 'document', 'engine_document', 'bounds', 'canvas', 'canvas_width',
               'canvas_height', 'sizing_mode', 'sizing_kind', 'ink32', 'native_text', 'sha256', 'source_sha256')


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
    parser.add_argument('--combinations', type=Path, help='site/gallery/combinations.json (the old Container pairs catalog)')
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
    pair_rows = {row['id']: row for row in rows}
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
            # The item the layout pinned (its name in the pair row) says which icon it is; `revisions` only
            # remembers the first icon a drawing belonged to, and identical drawings are shared.
            pinned = (entry.get(role) or {}).get('icon')
            row = pair_rows.get(key)
            item = next((i for i in (row or {}).get('mains' if role == 'main' else 'subs', []) if i['icon'] == pinned), None) if row else None
            if item is not None:
                fields['icon'] = item_key(item)          # None for a native text sub
            elif sha in by_sha:
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

    # 4. Container / symbol parts with exactly one icon of their family.
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

    # 5. What the old Container pairs page showed (progression-combinations.js containerMain / containerSymbol).
    if args.combinations:
        catalog = json.loads(args.combinations.read_text())
        sources = catalog.get('references', {})
        for row in catalog.get('rows', []):
            if row.get('kind') != 'container' or row['id'] not in references:
                continue
            main = row['main_generated'] if row.get('main_generated') is not None else sources.get(row['main_id'], {}).get('generated') or []
            container = next((g.get('key') or f"container/{g['icon_id']}" for g in main if (g.get('key') or '').startswith('container/')), None)
            generated = row.get('sub_generated') or sources.get(row['sub_id'], {}).get('generated') or []
            symbol = next((g['key'] for g in generated if (g.get('key') or '').startswith('symbol/')), None)
            for role, icon in (('container', container), ('symbol', symbol)):
                if not icon:
                    continue
                if icon not in icons:
                    notes[f'catalog {role} icon not in icons'] += 1
                elif (row['id'], role) in existing:
                    parts.set(row['id'], role, f'catalog {role}', icon=icon)

    # 6. Uploads for a part's source or for the combination itself (reference_uploads, dropped by 0010).
    if 'reference_uploads' in tables:
        uploads = list(db.execute('SELECT reference, role, icon_key FROM reference_uploads'))
        for reference, role, icon in uploads:
            if icon not in icons:
                notes['upload not in icons'] += 1
                continue
            for (ref, part_role), part in existing.items():
                if part_role == role and part['part_reference_id'] == reference and not parts.values.get((ref, role), {}).get('icon'):
                    parts.set(ref, role, 'source upload', icon=icon)
        for reference, role, icon in uploads:
            if icon in icons and (reference, role) in existing:
                parts.set(reference, role, 'pair upload', icon=icon)

    # 7. Symbol placements saved on the old Container pairs page (container_centers, 0006 / 0008, dropped by 0010),
    #    in the layout fields container-placement.js reads: a row for a container and a symbol is that pair's own
    #    placement, one with sub '' the container's. A pair keeps the box it was built with; one without a box gets
    #    a 0 x 0 placeholder (the page places it from the centre). Container and symbol are icon ids.
    if 'container_centers' in tables:
        centers = {(main_id, sub_id): {'center': [x, y], 'size': [width or 32, height or 32] if width or height else None}
                   for main_id, sub_id, x, y, width, height in
                   db.execute('SELECT main, sub, x, y, width, height FROM container_centers')}

        def value(ref: str, role: str, name: str):
            if name in parts.values.get((ref, role), {}):
                return parts.values[(ref, role)][name]
            row = existing.get((ref, role))
            return row[name] if row is not None and name in row.keys() else None

        for ref, role in list(existing):
            container, symbol = value(ref, 'container', 'icon'), value(ref, 'symbol', 'icon')
            if role != 'symbol' or not container or not symbol:
                continue
            ids = container.split('/')[-1], symbol.split('/')[-1]
            own, whole = centers.get(ids), centers.get((ids[0], ''))
            if not own and not whole:
                continue
            layout = value(ref, 'symbol', 'layout')
            layout = json.loads(layout) if isinstance(layout, str) else layout
            box = layout[0] if isinstance(layout, list) and len(layout) == 1 else {}
            built = all(isinstance(box.get(k), int) for k in 'xywh') and bool(box['w'] or box['h'])
            entry = {k: box[k] for k in ('paths', 'x', 'y', 'w', 'h') if k in box} if built else {'x': 0, 'y': 0, 'w': 0, 'h': 0}
            entry['scope'] = 'pair' if own else 'container'
            if own and not built:
                entry.update(own)
            if whole:
                entry['container'] = whole
            parts.set(ref, 'symbol', 'pair center' if own else 'container center', layout=[entry])

    # Positions the seed left empty: the side position is the reference id's suffix.
    for (ref, role), part in existing.items():
        if role == 'sub' and part['position'] is None and ref[-2:] in POSITIONS \
                and 'position' not in parts.values.get((ref, role), {}):
            parts.set(ref, role, 'position from id', position=ref[-2:])

    # Each side part's form: the published item for the icon it uses (or, for a native text sub, the one
    # the pair shows). A part given an icon the pair never listed gets none: the browser measures it.
    for row in rows:
        ref = row['id']
        for role, group in (('main', 'mains'), ('sub', 'subs')):
            key = (ref, role)
            if key not in existing and key not in parts.values:
                continue
            icon = parts.values.get(key, {}).get('icon')
            items = row.get(group) or []
            if icon:
                item = next((i for i in items if item_key(i) == icon), None)
            else:
                shown = shown_main(row) if role == 'main' else (items[0] if items else None)
                item = shown if shown and shown.get('native_text') else None
            parts.values.setdefault(key, {})['form'] = {k: item[k] for k in FORM_FIELDS if item and k in item} or None
            notes[f'side {role} form' if item else f'side {role} without a form'] += 1

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
