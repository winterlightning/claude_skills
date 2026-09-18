#!/usr/bin/env python3
"""Build the container SVG-unit audit: python3 -m icon_set.scripts.build_container_vector_report."""
from pathlib import Path
from collections import Counter
import hashlib
import html
import json
import xml.etree.ElementTree as ET
from icon_set.scripts.container_placement import artwork_group
from icon_set.scripts.container_vector_geometry import (
    TOLERANCE, GUARD, QUAD_SEGS, VectorInk, read_art, vector_zone, check_pair, pair_groups)

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist


BASE = Path(__file__).resolve().parents[1]
OUT = BASE / 'work/container-vector-report'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def preview(art, zone, center, pair=None, check=None):
    root = ET.Element('{http://www.w3.org/2000/svg}svg', {'viewBox': '0 0 64 64', 'width': '640', 'height': '640'})
    ET.SubElement(root, 'rect', {'width': '64', 'height': '64', 'fill': 'white'})
    if zone is not None:
        root.append(ET.fromstring(zone.svg(fill_color='#bde8cb', opacity=1)))
        # Shapely's default polygon stroke is decorative; suppress it.
        for n in root[-1].iter():
            n.set('stroke', 'none')
    root.append(artwork_group(art, 'exclusion', stroke=8, color='#f3bf66', opacity=.6))
    root.append(artwork_group(art, 'container', color='#202630'))
    if pair:
        sub, transform = pair
        root.append(artwork_group(sub, 'content', *transform, color='#425b83'))
    if center:
        x, y = center
        ET.SubElement(root, 'path', {'d': f'M{x-1} {y}H{x+1}M{x} {y-1}V{y+1}', 'stroke': '#2563eb', 'stroke-width': '.35'})
    if check:
        a, b = check['nearest_edge_points_units']
        ET.SubElement(root, 'path', {'d': f'M{a[0]} {a[1]}L{b[0]} {b[1]}', 'stroke': '#e11d48', 'stroke-width': '.3'})
        for x, y in (a,b):
            ET.SubElement(root, 'circle', {'cx': str(x), 'cy': str(y), 'r': '.3', 'fill': '#e11d48'})
    return ET.tostring(root, encoding='unicode')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    areas = json.loads((BASE/'data/container-content-areas.json').read_text())['areas']
    trials = json.loads((BASE/'data/container-solo-trials.json').read_text())['results']
    grouped = {}
    for r in trials.values():
        grouped.setdefault(r['main_key'].split('/',1)[1], {})[r['svg_file']] = r
    cards, results = [], []
    for source in sorted((development_dist(BASE.parent) / 'container64').glob('*.svg')):
        ident = source.stem
        result = {'container': ident, 'source_sha256': digest(source), 'pairs': []}
        try:
            area = areas.get(ident)
            if not area or area['source_sha256'] != digest(source):
                raise ValueError('Missing or stale semantic selection; select an interior for this source version.')
            art = read_art(source.read_text())
            ink = VectorInk.from_art(art)
            summary, inner, outer = vector_zone(ink, area)
            result.update(summary)
            center = summary.get('center_units')
            result['preview'] = f'{ident}.svg'
            (OUT/result['preview']).write_text(preview(art, inner, center))
            if inner is not None:
                from shapely.geometry import mapping
                result['safe_zone_inner'] = mapping(inner)
                result['safe_zone_outer'] = mapping(outer)
            details = []
            for file, trial in grouped.get(ident, {}).items():
                pair_result = {'sub_key': trial['sub_key'], 'asset': file}
                try:
                    asset = BASE/'assets/container-solo-trials'/file
                    sub_source = development_dist(BASE.parent) / 'solo48'/f"{trial['sub_key'].split('/',1)[1]}.svg"
                    if (trial['main_sha256'] != digest(source) or not sub_source.exists()
                        or digest(sub_source) != trial['sub_sha256'] or not asset.exists() or digest(asset) != trial['svg_sha256']):
                        raise ValueError('Stale source or pair asset; rebuild before measuring.')
                    groups = pair_groups(asset.read_text())
                    host_art, host_transform = groups['container']
                    if host_transform != (1.,0.,0.) or [p[1] for p in host_art.paths] != [p[1] for p in art.paths]:
                        raise ValueError('Saved pair host does not match current container paths.')
                    sub_art, transform = groups['content']
                    sub_ink = VectorInk.from_art(sub_art, transform)
                    measured = check_pair(ink, sub_ink, inner, outer)
                    pair_result.update(measured)
                    pair_result['preview'] = Path(file).stem+'.svg'
                    pair_result['source_sha256'] = digest(asset)
                    pair_result['transform'] = transform
                    (OUT/pair_result['preview']).write_text(preview(art, inner, center, (sub_art,transform), measured))
                    lo, hi = measured['ink_gap_lower_units'], measured['ink_gap_upper_units']
                    details.append(f'<figure><a href="{pair_result["preview"]}"><img loading="lazy" src="{pair_result["preview"]}" alt="Vector pair and nearest gap"></a><figcaption>{html.escape(trial["sub_key"].split("/",1)[1])}<br><b>{measured["status"].upper()}</b> · gap {lo:.5f}–{hi:.5f} u<br>Spacing: {measured["gap_status"]} · interior: {measured["containment_status"]} · canvas: {measured["canvas_status"]}</figcaption></figure>')
                except (ValueError, KeyError, OSError) as e:
                    pair_result.update(status='blocked', reason=str(e))
                    details.append(f'<p>{html.escape(trial["sub_key"])}: {html.escape(str(e))}</p>')
                result['pairs'].append(pair_result)
            metrics = ''
            if inner is not None:
                x0,y0,x1,y1 = inner.bounds
                metrics = (f'<dl><dt>Usable area</dt><dd>{inner.area:.4f}–{outer.area:.4f} u²</dd>'
                           f'<dt>Width × height (bounds)</dt><dd>{x1-x0:.4f} × {y1-y0:.4f} u</dd>'
                           f'<dt>Center</dt><dd>({center[0]:.5f}, {center[1]:.5f}) u</dd></dl>')
            cards.append(f'<article data-name="{ident}" data-status="{summary["status"]}"><h2>{html.escape(ident)}</h2><span class="badge">{summary["status"].upper()}</span><a href="{result["preview"]}"><img class="host" loading="lazy" src="{result["preview"]}" alt="Vector container interior"></a>{metrics}<p>{html.escape(summary["reason"])}</p><p class="muted">{html.escape(area.get("reason", ""))}</p><details><summary>{len(details)} existing pairs</summary>{"".join(details)}</details></article>')
        except (ValueError, KeyError, OSError) as e:
            result.update(status='blocked', reason=str(e))
            cards.append(f'<article data-name="{ident}" data-status="blocked"><h2>{html.escape(ident)}</h2><b>BLOCKED</b><p>{html.escape(str(e))}</p></article>')
        results.append(result)
    counts = dict(Counter(r['status'] for r in results))
    pair_counts = dict(Counter(p['status'] for r in results for p in r['pairs']))
    payload = {'units': 'SVG viewBox units', 'canvas': [0,0,64,64], 'stroke_width_units':4,
               'required_ink_clearance_units': 2, 'curve_tolerance_units': TOLERANCE,
               'distance_interval_width_max_units': 2*(2*TOLERANCE+GUARD),
               'round_buffer_quadrant_segments':QUAD_SEGS, 'numerical_guard_units': GUARD,
               'method': 'Bounded adaptive vector curves, continuous segment distance, vector offset envelopes. No raster measurements. GEOS floating-point operations are not formal interval proofs.',
               'containers_by_status':counts, 'pairs_by_status':pair_counts, 'containers':results}
    (OUT/'results.json').write_text(json.dumps(payload, indent=2)+'\n')
    (OUT/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Container vector measurements</title><style>
body{font:15px system-ui;background:#f5f7fa;color:#202630;margin:32px}header{max-width:980px}h1{font-size:30px}h2{font-size:16px;overflow-wrap:anywhere}p{line-height:1.55}.muted{color:#657184}a{color:#235da6}nav{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:26px 0;position:sticky;top:0;background:#f5f7fa;padding:12px 0;z-index:1}input,select,button{font:inherit;padding:10px;border:1px solid #c9d0da;border-radius:8px;background:white}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}article{background:white;border:1px solid #dde2ea;border-radius:12px;padding:22px}article[hidden]{display:none}.host{display:block;width:100%;max-width:300px;margin:12px auto}dl{display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:13px}dd{margin:0;font-variant-numeric:tabular-nums}.badge{background:#e9eef5;padding:4px 8px;border-radius:4px;font-size:12px}summary{cursor:pointer;color:#235da6;padding:12px 0}figure{margin:12px 0;border-top:1px solid #edf0f4;padding-top:12px}figure img{width:180px;max-width:100%}figcaption{font-size:13px;line-height:1.6;overflow-wrap:anywhere}code{font-size:13px}</style>
<header><h1>Container vector measurements</h1><p><a href="../container-size-report/index.html"><b>Check 32 × 32 and 48 × 48 icon fit</b></a></p>'''
        +f'<p><b>{len(results)} containers · {counts.get("vector",0)} vector interiors · {counts.get("review",0)} need a boundary decision · {counts.get("overlay",0)} overlays · {counts.get("blocked",0)} blocked</b></p>'
        +'''<p>All measurements use <b>SVG units</b> on the 64 × 64 viewBox. Green is the conservative usable interior. Orange extends <b>2 units beyond the visible 4-unit stroke</b>. Blue marks the area center. Click any preview to open its SVG and zoom without losing vector detail.</p>
<p>The interior boundary is rebuilt from vector paths. The old pixel-derived polygon only identifies which enclosed face is intended; its edges do not define the new area. Open or specially bounded faces remain under review until an explicit vector boundary is supplied.</p>
<details><summary>Precision and pass/fail rules</summary><p>Curves are adaptively subdivided with a maximum 0.0005-unit geometric deviation per source. Distances are continuous segment-to-segment minima, not distances between sampled points. Each displayed gap is an uncertainty interval (at most about 0.00201 units wide). A spacing PASS requires its lower bound to be at least 2 units; FAIL requires its upper bound to be below 2; an interval crossing the threshold requires REVIEW.</p><p>Round vector offsets use conservative inner and outer envelopes, accounting for curve error and circular tessellation. Area values are shown as lower–upper estimates in square units. GEOS uses floating-point arithmetic with a 0.00000001-unit allowance; these are engineering bounds, not symbolic exact solutions or formally certified interval arithmetic. Width, height and center describe the conservative inner zone; the bounds rectangle is not a guaranteed fitting rectangle.</p><p>A full pair PASS also requires its entire stroked geometry inside the selected interior and the 64-unit canvas. REVIEW is used for borderline geometry or unresolved interior selection. Existing pairs keep their saved placements. Their results may differ from the old raster report. The red segment marks the nearest stroke-edge gap on the bounded vector approximation. Intentional overlays have no containment pass.</p></details>
<p><a href="results.json">Download measurements and vector polygons (JSON)</a> · <a href="../container-buffer-preview/index.html">Previous pixel report</a></p>'''
        +f'<p>Existing pair results: {html.escape(str(pair_counts))}</p></header>'
        +'''<nav><input id="search" aria-label="Find container" placeholder="Find container…"><select id="status" aria-label="Status"><option value="all">All containers</option><option value="vector">Vector interiors</option><option value="review">Boundary review</option><option value="overlay">Overlays</option><option value="blocked">Blocked</option></select><button id="expand">Expand pairs</button><span id="count"></span></nav><main>'''
        +''.join(cards)+'''</main><script>const cards=[...document.querySelectorAll('article')],q=document.querySelector('#search'),s=document.querySelector('#status');function filter(){let n=0;for(const c of cards){c.hidden=!(c.dataset.name.includes(q.value.toLowerCase())&&(s.value==='all'||c.dataset.status===s.value));if(!c.hidden)n++}document.querySelector('#count').textContent=n+' shown'}q.oninput=filter;s.onchange=filter;document.querySelector('#expand').onclick=()=>{let d=[...document.querySelectorAll('article:not([hidden]) details')],v=d.some(x=>!x.open);d.forEach(x=>x.open=v)};filter()</script></html>''')
    print(json.dumps({'containers':counts,'pairs':pair_counts,'report':str(OUT/'index.html')},indent=2))

if __name__ == '__main__':
    main()
