#!/usr/bin/env python3
"""Push the built gallery catalog to the cloud: icon rows + drawings to D1, catalog JSON to R2.

    python3 cloud/migrate/push_catalog.py --base-url http://127.0.0.1:8787            # local rehearsal
    python3 cloud/migrate/push_catalog.py --base-url https://pictographic.<you>.workers.dev
    python3 cloud/migrate/push_catalog.py --sql cloud/exports/catalog.sql              # file for wrangler d1 execute

The effective catalog is what the gallery shows: ``published/gallery/icons.json`` by default,
or ``--from-server http://127.0.0.1:8000`` to take a running local deploy.py's /gallery/icons.json,
which applies saved artwork choices and shows workers' uploaded fixes (that overlay needs Python
rendering, so it is computed here). Uploaded icons are skipped; they already live in D1. The
"Side combination 64" family (``side-combination64.json``, kept outside icons.json) is pushed as
icons too, as deploy.py lists it.

Every current drawing is read from the build, checked against its svg_sha256, and stored inline
in D1 (authored SVGs are ~450 bytes). icons.json is rewritten with ``icons`` last so the Worker can
append uploads while streaming it. primitives.json and combinations.json are uploaded unchanged.

Each icon row also carries its full record and its review-facets.json entry: Icon review lists, filters and opens
icons from D1 (GET /api/icons, /api/icon). With --sql only the record is written; run POST /api/icons/reindex after
loading it to fill the list columns.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloudapi  # noqa: E402
from build_d1_import import inserts  # noqa: E402

ROOT = cloudapi.ROOT
DIST = ROOT / 'published'
CHUNK = 250
COLUMNS = ('key', 'icon_id', 'name', 'family', 'category', 'profile', 'canvas_size', 'svg_sha256', 'python_source',
           'preview_url', 'original_sources', 'variant_of', 'variant_root', 'variant_label', 'build_failed')
# The editable geometry of the generated drawing, as icon_artwork.baseline() and stroke_edits.GRAPH_FIELDS take it:
# the cloud graphics service edits, validates and renders from it (D1 icon_graphs, keyed by the generated sha).
GRAPH_FIELDS = ('icon_id', 'name', 'family', 'profile', 'canvas_size', 'keyshape',
                'keyshape_bounds', 'style', 'primitives', 'contours', 'anchors',
                'relationships', 'human_figures', 'composition_class', 'children',
                'semantic_role', 'semantic_kind', 'category', 'free_keyshape',
                'sizing_mode', 'canvas_width', 'canvas_height')


def graph(record: dict) -> dict | None:
    """The generated (baseline) graph of a record, or None when it has no stroke geometry."""
    source = dict(record, **(record.get('generated_graph') or {}))
    if not source.get('primitives'):
        return None
    result = {k: source[k] for k in GRAPH_FIELDS if k in source}
    result.update(key=record['key'], svg_sha256=record.get('generated_svg_sha256', record['svg_sha256']),
                  python_source=record.get('python_source'),
                  # approve_exception reads only the automatic status.
                  validation={'status': (record.get('validation') or {}).get('automatic_status',
                                         (record.get('validation') or {}).get('status', record.get('status')))})
    return result


def load_facets(dist: Path, server: str | None) -> dict:
    """review-facets.json: each drawing's measured mirror axes, by icon key."""
    try:
        if server:
            with urllib.request.urlopen(server.rstrip('/') + '/gallery/review-facets.json', timeout=300) as response:
                return json.loads(response.read())
        return json.loads((dist / 'gallery' / 'review-facets.json').read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return {}


def load_catalog(dist: Path, server: str | None) -> dict:
    if server:
        with urllib.request.urlopen(server.rstrip('/') + '/gallery/icons.json', timeout=300) as response:  # local server
            return json.loads(response.read())
    catalog = json.loads((dist / 'gallery' / 'icons.json').read_text(encoding='utf-8'))
    side = dist / 'gallery' / 'side-combination64.json'
    if side.is_file():
        catalog['icons'] = catalog['icons'] + json.loads(side.read_text(encoding='utf-8')).get('icons', [])
    return catalog


def drawing(dist: Path, server: str | None, record: dict) -> str | None:
    """The current SVG of a record, from the build or (for artwork choices) the local server."""
    url = record.get('preview_url') or ''
    if record.get('artwork_source') == 'work_fix':
        # The gallery shows a worker's uploaded fix; the revision itself is still the built Python drawing.
        profile = (record.get('profile') or '').lower()
        path = dist / ('failed' if record.get('build_failed') else '') / profile / f"{record.get('icon_id')}.svg"
        return path.read_text(encoding='utf-8') if path.is_file() else None
    if url.startswith('../api/') or url.startswith('/api/'):
        if not server:
            return None
        # preview URLs are relative to /gallery/, like the page that shows them.
        with urllib.request.urlopen(urllib.parse.urljoin(server.rstrip('/') + '/gallery/', url), timeout=60) as response:
            return response.read().decode('utf-8')
    path = (dist / 'gallery' / urllib.parse.unquote(url.split('?')[0])).resolve()
    if not path.is_relative_to(dist.resolve()) or path.suffix != '.svg' or not path.is_file():
        return None
    return path.read_text(encoding='utf-8')


def rows(dist: Path, server: str | None, catalog: dict, facets: dict | None = None) -> tuple[list[dict], dict]:
    result, report = [], {'icons': 0, 'failed_icons': 0, 'uploads_skipped': 0, 'missing_svg': [], 'sha_mismatch': []}
    for field in ('icons', 'failed_icons'):
        for record in catalog.get(field, []):
            if record.get('uploaded_icon'):
                report['uploads_skipped'] += 1
                continue
            svg = drawing(dist, server, record)
            if svg is None:
                report['missing_svg'].append(record['key'])
            else:
                # Store exactly the text the hash was taken of (text icons are hashed without the final newline).
                svg = next((text for text in (svg, svg.rstrip('\n'))
                            if hashlib.sha256(text.encode('utf-8')).hexdigest() == record.get('svg_sha256')), None)
                if svg is None:
                    report['sha_mismatch'].append(record['key'])
            row = {column: record.get(column) for column in COLUMNS}
            row['original_sources'] = record.get('original_sources') or []
            row['build_failed'] = field == 'failed_icons'
            row['svg'] = svg
            row['graph'] = graph(record)
            row['record'] = {k: v for k, v in record.items() if k != 'uploaded_svg'}
            row['facet'] = (facets or {}).get(record['key'])
            result.append(row)
            report[field] += 1
    return result, report


def extra_drawings(dist: Path, catalog: dict) -> list[dict]:
    """Drawings in the build's profile folders that the icon rows do not hold: failed-build leftovers
    the review pages still show, and the other sizes of icons drawn at several profiles (text icons
    exist at TEXT28 and TEXT32 under one key; the icon row keeps the last). Stored as drawings of
    the same icon, looked up by profile and icon id."""
    held = {}
    for field in ('icons', 'failed_icons'):
        for r in catalog.get(field, []):
            if not r.get('uploaded_icon'):
                held[r['key']] = (field == 'failed_icons', (r.get('profile') or '').lower(), r.get('icon_id'))
    known = set(held.values())
    extras = []
    for failed, base in ((False, dist), (True, dist / 'failed')):
        for folder in sorted(p for p in base.iterdir() if p.is_dir() and p.name[-1:].isdigit()) if base.is_dir() else []:
            for path in sorted(folder.glob('*.svg')):
                if (failed, folder.name, path.stem) in known:
                    continue
                svg = path.read_text(encoding='utf-8')
                extras.append({'profile': folder.name.upper(), 'icon_id': path.stem, 'failed': failed,
                               'svg_sha256': hashlib.sha256(svg.encode('utf-8')).hexdigest(), 'svg': svg})
    return extras


def icons_json(catalog: dict) -> tuple[bytes, dict]:
    """The catalog without uploads, `icons` last, compact: the file ends with `]}`."""
    icons = [{k: v for k, v in r.items() if k != 'uploaded_svg'} for r in catalog.get('icons', []) if not r.get('uploaded_icon')]
    dump = lambda value: json.dumps(value, ensure_ascii=False, separators=(',', ':'))  # noqa: E731
    parts = [f'{dump(k)}:{dump(v)}' for k, v in catalog.items() if k != 'icons']
    text = '{' + ''.join(p + ',' for p in parts) + '"icons":[' + ','.join(dump(r) for r in icons) + ']}'
    return text.encode('utf-8'), {'tail': 2, 'count': len(icons)}


def put_file(base_url: str, token: str, key: str, content: bytes, content_type: str) -> None:
    status, body = cloudapi.request(base_url, 'PUT', '/api/files/' + urllib.parse.quote(key), body=content,
                                    content_type=content_type, token=token, timeout=600)
    if status >= 400:
        raise RuntimeError(f'PUT {key} -> HTTP {status}: {body[:200]!r}')


def write_graph_sql(target: Path, graphs: list[dict], limit: int = 6 * 1024 * 1024) -> int:
    """icon_graphs INSERT OR IGNORE statements split into files under `limit` (a 90 MB execute rolls back)."""
    rows = {g['svg_sha256']: (g['svg_sha256'], g['key'], json.dumps(g, ensure_ascii=False, separators=(',', ':'))) for g in graphs}
    statements = [s.replace('INSERT INTO "icon_graphs"', 'INSERT OR IGNORE INTO "icon_graphs"', 1)
                  for s in inserts('icon_graphs', ['svg_sha256', 'icon', 'graph'], list(rows.values()))]
    files, part, size = [], [], 0
    for statement in statements + [None]:
        if part and (statement is None or size + len(statement) > limit):
            path = target.with_name(f'{target.stem}-{len(files) + 1:03d}.sql')
            path.write_text('\n'.join(part) + '\n')
            files.append(str(path))
            part, size = [], 0
        if statement is not None:
            part.append(statement)
            size += len(statement.encode('utf-8')) + 1
    print(json.dumps({'graphs': len(rows), 'files': files}, indent=2))
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument('--base-url', help='Worker URL to push to (D1 rows + R2 files)')
    target.add_argument('--sql', type=Path, help='write D1 SQL instead (R2 files are not uploaded)')
    parser.add_argument('--dist', type=Path, default=DIST)
    parser.add_argument('--from-server', help='running local deploy.py whose /gallery/icons.json has artwork choices applied')
    parser.add_argument('--user', default='catalog-push')
    parser.add_argument('--graphs-only', action='store_true',
                        help='with --sql: only the icon_graphs rows (the editor geometry), as SQL files of at most '
                             '6 MB each (<sql>-001.sql, ...) for `wrangler d1 execute --remote --file`; nothing else changes')
    args = parser.parse_args(argv)
    if args.graphs_only and not args.sql:
        parser.error('--graphs-only needs --sql')
    catalog = load_catalog(args.dist, args.from_server)
    if args.graphs_only:
        return write_graph_sql(args.sql, [row for row in (graph(r) for f in ('icons', 'failed_icons')
                                                           for r in catalog.get(f, []) if not r.get('uploaded_icon')) if row])
    facets = load_facets(args.dist, args.from_server)
    icon_rows, report = rows(args.dist, args.from_server, catalog, facets)
    content, layout = icons_json(catalog)
    push_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    details = {'icons_json': layout, 'report': {k: (len(v) if isinstance(v, list) else v) for k, v in report.items()},
               'source': args.from_server or str(args.dist)}
    if args.sql:
        now = datetime.now(timezone.utc).isoformat()
        statements = inserts('icons', list(COLUMNS) + ['uploaded', 'pushed_at', 'record'],
                             [tuple(json.dumps(r[c], ensure_ascii=False) if c == 'original_sources' else r[c] for c in COLUMNS)
                              + (0, push_id, json.dumps(r['record'], ensure_ascii=False, separators=(',', ':'))) for r in icon_rows])
        seen, revisions = set(), []
        for r in icon_rows:
            if r['svg'] and r['svg_sha256'] not in seen:
                seen.add(r['svg_sha256'])
                revisions.append((r['svg_sha256'], r['key'], r['svg'], 'build', now))
        statements += inserts('revisions', ['svg_sha256', 'icon', 'svg', 'origin', 'created_at'], revisions)
        graphs = {r['graph']['svg_sha256']: (r['graph']['svg_sha256'], r['key'], json.dumps(r['graph'], ensure_ascii=False, separators=(',', ':')))
                  for r in icon_rows if r['graph']}
        statements += inserts('icon_graphs', ['svg_sha256', 'icon', 'graph'], list(graphs.values()))
        statements += inserts('catalog_pushes', ['pushed_at', 'pushed_by', 'details'], [(now, args.user, json.dumps(details))])
        args.sql.write_text('\n'.join(s.replace('INSERT INTO "icons"', 'INSERT OR REPLACE INTO "icons"', 1)
                                      .replace('INSERT INTO "revisions"', 'INSERT OR IGNORE INTO "revisions"', 1)
                                      .replace('INSERT INTO "icon_graphs"', 'INSERT OR IGNORE INTO "icon_graphs"', 1) for s in statements) + '\n')
        (args.sql.parent / 'icons.json').write_bytes(content)
        print(json.dumps({'sql': str(args.sql), 'icons_json': str(args.sql.parent / 'icons.json'), **details}, indent=2))
        return 0
    token = cloudapi.push_token(args.base_url)
    # Measured symmetry of uploads (they are not pushed), a few hundred updates a request.
    pushed = {r['key'] for r in icon_rows}
    upload_facets = sorted((key, facet) for key, facet in facets.items() if key not in pushed)
    for start in range(0, len(upload_facets), 500):
        cloudapi.post_json(args.base_url, '/api/catalog/push', {'push_id': push_id, 'icons': [], 'final': False,
                                                                'upload_facets': dict(upload_facets[start:start + 500])}, token)
    for start in range(0, len(icon_rows), CHUNK):
        chunk = icon_rows[start:start + CHUNK]
        final = start + CHUNK >= len(icon_rows)
        payload = {'push_id': push_id, 'icons': chunk, 'final': final}
        if final:
            # Upload the catalog files before the final chunk makes the new layout current.
            put_file(args.base_url, token, 'site/gallery/icons.json', content, 'application/json')
            for name in ('primitives.json', 'combinations.json'):
                path = args.dist / 'gallery' / name
                if path.is_file():
                    put_file(args.base_url, token, f'site/gallery/{name}', path.read_bytes(), 'application/json')
            payload['details'] = details
            payload['extra_drawings'] = extra_drawings(args.dist, catalog)
        result = cloudapi.post_json(args.base_url, '/api/catalog/push', payload, token)
        print(f'pushed {start + len(chunk)}/{len(icon_rows)}' + (f' (removed {result.get("removed")})' if final else ''), flush=True)
    print(json.dumps(details, indent=2))
    if report['sha_mismatch'] or report['missing_svg']:
        print(f"warning: {len(report['missing_svg'])} icons without a readable SVG and {len(report['sha_mismatch'])} whose "
              'SVG does not match svg_sha256 were pushed without a drawing.', file=sys.stderr)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
