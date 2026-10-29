"""Find closed-fill variants for outline-only subs: add ONE straight edge between two native open path
endpoints, then run the normal region fill. Writes output/sub32-closure-candidates/ (previews only;
nothing is applied until a closure is accepted into the sub32 review decisions)."""
from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import json, math, sys, tempfile, itertools
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from .build_sub32_region_fill_review import DEFAULT_SOURCE, process_svg, geometry_to_svg, stroke_to_polygon
from shapely.geometry import LineString, Point
from shapely.ops import unary_union

ROOT = WORK
OUT = WORK / 'sub32-closure-candidates'
REVIEW = WORK / 'sub32-region-fill-review/manifest.json'

def ends(shape):
    c = shape['coords']
    if len(c) < 2 or math.dist(c[0], c[-1]) < 1e-6: return []
    return [(shape['source_id'], 'first', tuple(c[0])), (shape['source_id'], 'last', tuple(c[-1]))]

def fill_with(source, a, b):
    root = ET.fromstring(source.read_bytes())
    ns = root.tag.split('}')[0] + '}' if root.tag.startswith('{') else ''
    ET.SubElement(root, f'{ns}path', {'id': 'closure', 'd': f'M{a[0]:.6g} {a[1]:.6g}L{b[0]:.6g} {b[1]:.6g}'})
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / source.name; p.write_bytes(ET.tostring(root, encoding='utf-8'))
        row, filled, regions, _ = process_svg(str(p), algo='smart_fill', edge_close=False)
    return row, filled

def cut_inner_details(row, filled):
    """Native strokes and filled marks lying wholly inside the new solid (eyes, mouth, $) are cut out as white,
    so the closed fill does not swallow them. Outline strokes touching the outside edge are kept."""
    vb = [float(v) for v in str(row['viewbox']).strip('()').replace(',', ' ').split()]
    outer = unary_union([g.exterior for g in getattr(filled, 'geoms', [filled])])
    cut = []
    for shape in row['shapes']:
        if shape['source_id'] == 'closure': continue
        poly = stroke_to_polygon([shape], vb)
        if poly.is_empty or poly.buffer(.5).difference(filled).area > .5 or poly.distance(outer) < 1: continue
        cut.append((shape['source_id'], poly))
    for item in row.get('filled_shapes', []):
        g = item['geometry']
        if g.buffer(.5).difference(filled).area <= .5 and g.distance(outer) >= 1: cut.append((item.get('source_id'), g))
    if not cut: return filled, []
    return filled.difference(unary_union([g for _, g in cut])), [i for i, _ in cut]

def search(name):
    source = DEFAULT_SOURCE / f'{name}.svg'
    try:
        row, filled0, _, _ = process_svg(str(source), algo='smart_fill', edge_close=False)
    except Exception as e:
        return {'name': name, 'error': str(e)[:160]}
    ink = row['polygon']
    pts = [e for s in row['shapes'] for e in ends(s)]
    cands = []
    for (ia, ea, a), (ib, eb, b) in itertools.combinations(pts, 2):
        length = math.dist(a, b)
        if not 2 <= length <= 28: continue
        seg = LineString([a, b])
        # the new edge must run through empty space, not across existing strokes
        crossing = seg.difference(Point(a).buffer(3)).difference(Point(b).buffer(3))
        if not crossing.is_empty and crossing.buffer(.4).intersection(ink.buffer(-.3)).area > .3: continue
        try: r, f = fill_with(source, a, b)
        except Exception: continue
        if f is None or f.is_empty: continue
        f, cuts = cut_inner_details(r, f)
        if f.is_empty: continue
        gain = f.difference(ink.union(seg.buffer(2, cap_style=1))).area
        if gain < 20: continue
        cands.append({'from': [ia, ea], 'to': [ib, eb], 'a': a, 'b': b, 'length': round(length, 2), 'gain': round(gain, 1), 'cut_details': cuts,
                      'svg': geometry_to_svg(f, r['viewbox'], r['width'], r['height'])})
    cands.sort(key=lambda c: -c['gain'] / (c['length'] + 4))
    return {'name': name, 'candidates': cands[:3]}

# Claude's visual pick per sub (candidate index); everything else is only a mechanical closure, not a body.
RECOMMENDED = {'upward-hand-pointer-batch-024-07-sub32-v2': 0, 'hand-down-1-sub32-v2': 1,
               'dog-head-profile-sub32': 0, 'dog-sub32': 0, 'roof-sub': 0, 'roof-sub32-v3': 0}

def page(results):
    def section(r, pick=None):
        tiles = [f'<figure><img src="{r["name"]}--source.svg"><figcaption>original (outline)</figcaption></figure>']
        for i, c in enumerate(r['candidates']):
            mark = ' class="pick"' if i == pick else ''
            tiles.append(f'<figure{mark}><img src="{r["name"]}--close-{i}.svg"><figcaption>{"★ pick · " if i == pick else ""}option {i} · edge {c["length"]}px</figcaption></figure>')
        small = ''.join(f'<img class="s" src="{r["name"]}--close-{i}.svg">' for i in range(len(r['candidates'])))
        return f'<section><h2>{r["name"]}</h2><div class="t">{"".join(tiles)}<div class="sm">32px: <img class="s" src="{r["name"]}--source.svg">{small}</div></div></section>'
    good = [r for r in results if r['name'] in RECOMMENDED and r.get('candidates')]
    rest = [r for r in results if r['name'] not in RECOMMENDED and r.get('candidates')]
    rows = [f'<h3>Recommended ({len(good)})</h3>', *[section(r, RECOMMENDED[r['name']]) for r in good],
            f'<details><summary>Other mechanical closures ({len(rest)}) · arrows, letters, signs: closing them makes a blob, not recommended</summary>',
            *[section(r) for r in rest], '</details>']
    return ('<!doctype html><meta charset="utf-8"><title>Sub closed-fill candidates</title><style>'
            ':root{--bg:#f5f6f8;--card:#fff;--ink:#18212e;--muted:#667385;--line:#dce2e9}'
            '@media (prefers-color-scheme:dark){:root{--bg:#101722;--card:#192333;--ink:#edf2fb;--muted:#a9b8cb;--line:#34445a}}'
            'body{margin:0;padding:20px 16px;font:14px system-ui;background:var(--bg);color:var(--ink)}h1{margin:0 0 4px}'
            'section{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px;margin:10px 0}'
            'h2{font-size:13px;margin:0 0 8px}.t{display:flex;flex-wrap:wrap;gap:12px;align-items:end}'
            'figure{margin:0;text-align:center}figure img{width:128px;height:128px;background:#fff;border:1px solid var(--line);border-radius:8px}'
            'figure.pick img{outline:3px solid #16a34a;outline-offset:2px}h3{margin:18px 0 4px}summary{cursor:pointer;margin:16px 0 6px;color:var(--muted)}'
            'figcaption{font-size:11px;color:var(--muted)}.sm{font-size:11px;color:var(--muted)}.s{width:32px;height:32px;background:#fff;margin-left:6px;border:1px solid var(--line)}'
            f'</style><h1>Sub closed-fill candidates</h1><p style="color:var(--muted)">One straight edge added between two native open endpoints, then the normal region fill. Outline-only subs checked: {len(results)}. Nothing is applied yet.</p>'
            + ''.join(rows))

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    names = [r['name'] for r in json.loads(REVIEW.read_text())['records'] if r['status'] == 'unchanged']
    with ProcessPoolExecutor(8) as ex: results = list(ex.map(search, names))
    for r in results:
        src = (DEFAULT_SOURCE / f'{r["name"]}.svg').read_text()
        (OUT / f'{r["name"]}--source.svg').write_text(src.replace('currentColor', 'black'))
        for i, c in enumerate(r.get('candidates', [])):
            (OUT / f'{r["name"]}--close-{i}.svg').write_text(c.pop('svg'))
    (OUT / 'candidates.json').write_text(json.dumps(results, indent=1))
    (OUT / 'index.html').write_text(page(results))
    print(len(names), 'outline-only subs;', sum(1 for r in results if r.get('candidates')), 'with closures;',
          sum(1 for r in results if r.get('error')), 'errors')
