"""Fill and duotone variants of a Pictographic line icon, plus a preview sheet.

    python3 icon_set/scripts/icon_variant.py faces SOURCE.svg [--png FACES.png]
    python3 icon_set/scripts/icon_variant.py fill SOURCE.svg OUT.svg [--open F,..] [--keep ID,..] [--region D]
    python3 icon_set/scripts/icon_variant.py duotone SOURCE.svg OUT.svg --face F,.. [--region D] [--closure D] [--color HEX]
    python3 icon_set/scripts/icon_variant.py preview OUT.png SOURCE.svg RESULT.svg [MORE.svg ...]

``faces`` lists the source paths (id, open or closed) and the faces: every area the stroke centrelines
enclose, numbered F1, F2 ... largest first, with its bounding box and the paths lying inside it.
``--png`` draws the numbered faces over the icon so you can pick them by eye.

``fill`` writes the solid (Fill) variant: one ``fill="currentColor"`` evenodd path. Each stroke is
outlined at the source stroke width with round caps and joins and every face is filled solid, except the
``--open`` faces, which stay open inside their stroke (handle loops, gaps between legs, see-through
windows). Every stroke drawn inside the silhouette would vanish into the solid, so it becomes a
knockout: a negative line one stroke wide, stopped a rim one stroke wide short of the edge so the
silhouette never breaks. ``--keep`` names paths that merge into the solid instead (a seam that means
nothing filled). ``--region`` adds solid geometry (a closure for an open silhouette). It warns about openings thinner than ``--min-gap`` units.

``duotone`` writes the Duotone variant: the chosen faces (and any ``--region`` geometry) painted in one
accent colour behind the unchanged black source strokes; ``--closure`` adds a black stroke that closes
an open silhouette.

``preview`` renders the source and each result at native size and 4x on a light and a dark background.
"""
import argparse
import io
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import svgpathtools
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import polygonize, unary_union

SVG = '{http://www.w3.org/2000/svg}'
ACCENT = '#7EC8E3'  # SKY_BLUE in icon_set/skills/icon-design/color-theme.json: the duotone accent
STEP = 0.25         # curve sampling, in canvas units
MIN_FACE = 2.0      # faces smaller than this (square units) are slivers between touching strokes


def load(source):
    root = ET.parse(source).getroot()
    view = [float(v) for v in root.get('viewBox', '0 0 48 48').split()]
    width = float(root.get('stroke-width', 4))
    title = root.find(SVG + 'title')
    paths = []
    for n, el in enumerate(root.iter(SVG + 'path')):
        if el.get('d'):
            paths.append({'id': el.get('id') or f'p{n}', 'd': el.get('d'), 'width': float(el.get('stroke-width', width))})
    return {'view': view, 'width': width, 'title': title.text.strip() if title is not None and title.text else Path(source).stem,
            'paths': paths}


def subpaths(d):
    """Each subpath as a list of points and whether it is closed."""
    out = []
    for sub in svgpathtools.parse_path(d).continuous_subpaths():
        points = []
        for seg in sub:
            if isinstance(seg, svgpathtools.Line):
                pts = [seg.start, seg.end]
            else:
                count = max(2, int(seg.length() / STEP) + 1)
                pts = [seg.point(i / (count - 1)) for i in range(count)]
            points += pts if not points else pts[1:]
        xy = [(p.real, p.imag) for p in points]
        closed = len(xy) > 2 and (abs(sub.start - sub.end) < 1e-6 or re.search(r'[zZ]\s*$', d) is not None)
        out.append((xy, closed))
    return out


def centerlines(path):
    lines = []
    for xy, closed in subpaths(path['d']):
        if len(set(xy)) > 1:
            lines.append(LineString(xy + ([xy[0]] if closed and xy[0] != xy[-1] else [])))
    return lines


def ink(path, width=None):
    """The painted area of a stroke: round caps and joins."""
    r = (width or path['width']) / 2
    parts = []
    for xy, closed in subpaths(path['d']):
        if len(set(xy)) == 1:
            parts.append(Point(xy[0]).buffer(r, quad_segs=16))
        else:
            line = LineString(xy + ([xy[0]] if closed else []))
            parts.append(line.buffer(r, cap_style='round', join_style='round', quad_segs=16))
    return unary_union(parts)


def faces(icon):
    """Every area the centrelines enclose, largest first, as F1, F2 ..."""
    lines = unary_union([line for p in icon['paths'] for line in centerlines(p)])
    found = sorted((f for f in polygonize(lines) if f.area >= MIN_FACE), key=lambda f: -f.area)
    return {f'F{n + 1}': f for n, f in enumerate(found)}


def polys(shape):
    if isinstance(shape, Polygon):
        return [] if shape.is_empty else [shape]
    return [g for g in getattr(shape, 'geoms', []) if isinstance(g, Polygon) and not g.is_empty]


def names(value):
    return [v for v in (value or '').split(',') if v]


def pick(known, wanted, flag):
    missing = [n for n in wanted if n not in known]
    if missing:
        sys.exit(f'{flag}: unknown {", ".join(missing)} (run the faces command)')
    return wanted


def ring_d(coords, digits=3):
    pts = list(coords)[:-1]
    return 'M' + 'L'.join(f'{x:.{digits}f} {y:.{digits}f}' for x, y in pts) + 'Z'


def shape_d(shape, digits=3):
    return ''.join(ring_d(p.exterior.coords, digits) + ''.join(ring_d(i.coords, digits) for i in p.interiors)
                   for p in polys(shape))


def region(d):
    shape = Polygon()
    for xy, closed in subpaths(d):
        if len(xy) > 2:
            shape = shape.symmetric_difference(Polygon(xy).buffer(0))
    return shape


def cmd_faces(args):
    icon = load(args.source)
    found = faces(icon)
    print(f"{icon['title']}  viewBox {' '.join(f'{v:g}' for v in icon['view'])}  stroke {icon['width']:g}")
    print('paths:')
    for p in icon['paths']:
        kind = 'closed' if any(c for _, c in subpaths(p['d'])) else 'open'
        x0, y0, x1, y1 = ink(p).bounds
        print(f"  {p['id']:<22} {kind:<6} bbox {x0:5.1f},{y0:5.1f} -> {x1:5.1f},{y1:5.1f}")
    print('faces:')
    for name, f in found.items():
        x0, y0, x1, y1 = f.bounds
        inner = [p['id'] for p in icon['paths'] if (s := ink(p)).intersection(f).area >= 0.9 * s.area]
        print(f"  {name:<4} area {f.area:6.1f}  bbox {x0:5.1f},{y0:5.1f} -> {x1:5.1f},{y1:5.1f}"
              + (f"  contains {', '.join(inner)}" if inner else ''))
    if not found:
        print('  none: no stroke encloses an area (an open silhouette needs a --region or --closure)')
    if args.png:
        draw_faces(icon, found, args.png)


def draw_faces(icon, found, out):
    import cairosvg
    x, y, w, h = icon['view']
    scale = 512 / w
    tints = ['#F4A261', '#2A9D8F', '#E9C46A', '#8AB17D', '#E76F51', '#7EC8E3', '#B392AC', '#C9955B']
    body = []
    for n, (name, f) in enumerate(found.items()):
        body.append(f'<path d="{shape_d(f)}" fill="{tints[n % len(tints)]}" fill-opacity="0.75"/>')
    for p in icon['paths']:
        body.append(f'<path d="{p["d"]}" fill="none" stroke="#000" stroke-opacity="0.35" stroke-width="{p["width"]:g}" '
                    'stroke-linecap="round" stroke-linejoin="round"/>')
    for name, f in found.items():
        c = f.representative_point()
        body.append(f'<text x="{c.x:.2f}" y="{c.y:.2f}" font-size="{max(2.5, w / 16):.1f}" font-family="Helvetica" '
                    f'font-weight="bold" text-anchor="middle" dominant-baseline="central">{name}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w * scale:g}" height="{h * scale:g}" '
           f'viewBox="{x:g} {y:g} {w:g} {h:g}"><rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="#fff"/>'
           + ''.join(body) + '</svg>')
    cairosvg.svg2png(bytestring=svg.encode(), write_to=out)
    print(f'wrote {out}')


def cmd_fill(args):
    icon = load(args.source)
    paths, sw = icon['paths'], icon['width']
    found = faces(icon)
    opened = pick(found, names(args.open), '--open')
    keep = set(pick({p['id'] for p in paths}, names(args.keep), '--keep'))
    filled = unary_union([f for n, f in found.items() if n not in opened] + [region(d) for d in args.region or []])
    solid = unary_union([ink(p) for p in paths] + [filled])
    for n in opened:
        solid = solid.difference(found[n].buffer(-sw / 2, join_style='round'))
    # Every stroke drawn inside the silhouette becomes a negative line; the rim keeps the edge whole.
    rim = args.rim if args.rim is not None else sw
    inside = solid.buffer(-rim, join_style='round')
    knock = []
    for p in paths:
        if p['id'] in keep:
            continue
        cut = ink(p, args.gap or sw).intersection(inside)
        if cut.area >= args.speck:
            knock.append(p['id'])
            solid = solid.difference(cut)
    solid = clean(solid.buffer(0), args.speck)
    x, y, w, h = icon['view']
    Path(args.out).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}" height="{h:g}" viewBox="{x:g} {y:g} {w:g} {h:g}" '
        f'fill="currentColor"><title>{icon["title"]} fill</title><path fill-rule="evenodd" d="{shape_d(solid)}"/></svg>\n')
    print(f'wrote {args.out}')
    print(f"  filled faces: {', '.join(n for n in found if n not in opened) or '-'}; open: {', '.join(opened) or '-'}; "
          f"knockouts: {', '.join(knock) or '-'}" + (f"; regions: {len(args.region)}" if args.region else ''))
    report(solid, icon['view'], args.min_gap)


def clean(shape, speck):
    """Drop islands and holes smaller than ``speck`` square units."""
    kept = [Polygon(p.exterior, [i for i in p.interiors if Polygon(i).area >= speck]) for p in polys(shape) if p.area >= speck]
    return unary_union(kept)


def report(solid, view, min_gap):
    x, y, w, h = view
    thin = 0
    for p in polys(solid):
        for hole in p.interiors:
            hp = Polygon(hole)
            if hp.difference(hp.buffer(-min_gap / 2).buffer(min_gap / 2)).area > 0.25 * hp.area:
                thin += 1
    if thin:
        print(f'  WARNING: {thin} opening(s) or knockout(s) thinner than {min_gap:g} units close up at native size')
    print(f'  {len(polys(solid))} solid piece(s), ink {solid.area / (w * h):.0%} of the canvas')


def cmd_duotone(args):
    icon = load(args.source)
    found = faces(icon)
    chosen = pick(found, names(args.face), '--face')
    x, y, w, h = icon['view']
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}" height="{h:g}" viewBox="{x:g} {y:g} {w:g} {h:g}" '
           f'stroke-width="{icon["width"]:g}" stroke-linecap="round" stroke-linejoin="round">'
           f'<title>{icon["title"]} — duotone</title>']
    for n in chosen:
        out.append(f'<path data-face="{n}" d="{shape_d(found[n])}" fill="{args.color}" stroke="none" />')
    for d in args.region or []:
        out.append(f'<path data-color-addition="region" d="{d}" fill="{args.color}" stroke="none" />')
    for p in icon['paths']:
        width = '' if p['width'] == icon['width'] else f' stroke-width="{p["width"]:g}"'
        out.append(f'<path id="{p["id"]}" d="{p["d"]}" fill="none" stroke="#000000"{width} />')
    for d in args.closure or []:
        out.append(f'<path data-color-addition="closure" d="{d}" fill="none" stroke="#000000" />')
    Path(args.out).write_text(''.join(out) + '</svg>\n')
    print(f"wrote {args.out}  (faces {', '.join(chosen)}; {len(args.region or [])} region(s); {len(args.closure or [])} closure(s))")


def cmd_preview(args):
    import cairosvg
    from PIL import Image
    size, pad = args.size, 8
    files = [args.source] + args.results
    backgrounds = [('#FFFFFF', '#000000'), ('#2B2B2B', '#FFFFFF')]
    cell = size + 48 + pad * 3
    sheet = Image.new('RGB', (cell * len(files), (size + pad * 2) * len(backgrounds)), '#CCCCCC')
    for col, f in enumerate(files):
        text = Path(f).read_text()
        for row, (bg, fg) in enumerate(backgrounds):
            colored = text.replace('currentColor', fg)
            ox, oy = col * cell + pad, row * (size + pad * 2) + pad
            for px, dx in ((48, 0), (size, 48 + pad)):
                png = cairosvg.svg2png(bytestring=colored.encode(), output_width=px, output_height=px, background_color=bg)
                sheet.paste(Image.open(io.BytesIO(png)).convert('RGB'), (ox + dx, oy))
    sheet.save(args.out)
    print(f'wrote {args.out}  (columns: {", ".join(Path(f).name for f in files)}; rows: light, dark)')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('faces')
    p.add_argument('source'); p.add_argument('--png', help='draw the numbered faces to this PNG')
    p.set_defaults(run=cmd_faces)
    p = sub.add_parser('fill')
    p.add_argument('source'); p.add_argument('out')
    p.add_argument('--open', help='faces that stay open inside their stroke')
    p.add_argument('--keep', help='path ids inside the solid that must not become knockouts')
    p.add_argument('--region', action='append', help='extra solid geometry (path d), repeatable')
    p.add_argument('--gap', type=float, help='knockout line width (default: the stroke width)')
    p.add_argument('--rim', type=float, help='solid kept between a knockout and the silhouette edge (default: the stroke width)')
    p.add_argument('--speck', type=float, default=1.0, help='drop islands and holes smaller than this many square units')
    p.add_argument('--min-gap', type=float, default=3.0, help='warn about openings thinner than this')
    p.set_defaults(run=cmd_fill)
    p = sub.add_parser('duotone')
    p.add_argument('source'); p.add_argument('out')
    p.add_argument('--face', required=True, help='faces painted in the accent colour')
    p.add_argument('--region', action='append', help='extra accent-only geometry (path d), repeatable')
    p.add_argument('--closure', action='append', help='extra black stroke closing an open silhouette (path d), repeatable')
    p.add_argument('--color', default=ACCENT, help=f'accent colour (default {ACCENT}, SKY_BLUE)')
    p.set_defaults(run=cmd_duotone)
    p = sub.add_parser('preview')
    p.add_argument('out'); p.add_argument('source'); p.add_argument('results', nargs='+')
    p.add_argument('--size', type=int, default=192)
    p.set_defaults(run=cmd_preview)
    args = parser.parse_args(argv)
    args.run(args)


if __name__ == '__main__':
    main()
