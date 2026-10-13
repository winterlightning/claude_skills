"""Fill, duotone and twotone variants of a Pictographic line icon, plus a preview sheet.

    python3 icon_set/scripts/icon_variant.py faces SOURCE.svg [--png FACES.png]
    python3 icon_set/scripts/icon_variant.py strokes SOURCE.svg [--png STROKES.png] [--split ID@X,Y]
    python3 icon_set/scripts/icon_variant.py fill SOURCE.svg OUT.svg [--open F,..] [--keep ID,..] [--region D]
    python3 icon_set/scripts/icon_variant.py duotone SOURCE.svg OUT.svg --face F,.. [--region D] [--closure D] [--color HEX]
    python3 icon_set/scripts/icon_variant.py twotone SOURCE.svg OUT.svg --secondary ID,.. [--split ID@X,Y] [--dim 0.4 | --color HEX]
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

``strokes`` lists every path (id, open or closed, bounding box, length, the faces it bounds) and with
``--png`` draws the icon with each path labelled by id, so the two tone groups can be chosen by eye.

``twotone`` writes the Twotone variant: the source strokes unchanged, sorted into two groups. The
``--secondary`` strokes go first in a group drawn in the line colour at 40 % opacity (``--dim``, the
hugeicons pattern; ``--color`` gives them a second colour instead); every other stroke follows in the
primary group in full ``currentColor``, so the line colour owns each junction. ``--split ID@X,Y`` cuts
a stroke at a point first (round caps make the cut invisible) so a path shared by two parts can carry
two tones. Nothing is filled.

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


DRAWN = ('path', 'circle', 'ellipse', 'line', 'polyline', 'polygon', 'rect')


def element_d(el):
    """The path data of a drawable element (circles and the like become arcs and lines)."""
    tag = el.tag.split('}')[-1]
    g = lambda k, default=0: float(el.get(k, default))
    if tag == 'path':
        return el.get('d')
    if tag in ('circle', 'ellipse'):
        cx, cy = g('cx'), g('cy')
        rx = ry = g('r') if tag == 'circle' else None
        if rx is None:
            rx, ry = g('rx'), g('ry')
        return f'M{cx - rx:g} {cy:g}A{rx:g} {ry:g} 0 1 0 {cx + rx:g} {cy:g}A{rx:g} {ry:g} 0 1 0 {cx - rx:g} {cy:g}Z'
    if tag == 'line':
        return f"M{g('x1'):g} {g('y1'):g}L{g('x2'):g} {g('y2'):g}"
    if tag in ('polyline', 'polygon'):
        nums = re.findall(r'-?\d*\.?\d+', el.get('points', ''))
        pts = list(zip(nums[::2], nums[1::2]))
        return 'M' + 'L'.join(f'{x} {y}' for x, y in pts) + ('Z' if tag == 'polygon' else '')
    if tag == 'rect':
        x, y, w, h = g('x'), g('y'), g('width'), g('height')
        return f'M{x:g} {y:g}L{x + w:g} {y:g}L{x + w:g} {y + h:g}L{x:g} {y + h:g}Z'
    return None


def transform_matrix(text):
    """A 3x3 matrix for an SVG transform list (matrix, translate, scale, rotate)."""
    import math
    import numpy as np
    m = np.identity(3)
    for name, args in re.findall(r'(\w+)\s*\(([^)]*)\)', text or ''):
        v = [float(x) for x in re.findall(r'-?\d*\.?\d+(?:e-?\d+)?', args)]
        if name == 'matrix' and len(v) == 6:
            step = np.array([[v[0], v[2], v[4]], [v[1], v[3], v[5]], [0, 0, 1]])
        elif name == 'translate':
            step = np.array([[1, 0, v[0]], [0, 1, v[1] if len(v) > 1 else 0], [0, 0, 1]])
        elif name == 'scale':
            step = np.array([[v[0], 0, 0], [0, v[1] if len(v) > 1 else v[0], 0], [0, 0, 1]])
        elif name == 'rotate':
            a = math.radians(v[0]); c, s = math.cos(a), math.sin(a)
            cx, cy = (v[1], v[2]) if len(v) > 2 else (0, 0)
            step = (np.array([[1, 0, cx], [0, 1, cy], [0, 0, 1]]) @ np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
                    @ np.array([[1, 0, -cx], [0, 1, -cy], [0, 0, 1]]))
        else:
            continue
        m = m @ step
    return m


def apply_transform(d, m):
    import numpy as np
    if np.allclose(m, np.identity(3)):
        return d
    from svgpathtools.path import transform
    return transform(svgpathtools.parse_path(d), m).d()


def tidy_d(d):
    """Path data with short numbers."""
    d = re.sub(r'-?\d+\.\d+', lambda m: f'{float(m.group()):.3f}'.rstrip('0').rstrip('.'), d).replace(',', ' ')
    return re.sub(r'\s*([MLHVCSQTAZ])\s*', r'\1', d)


def split_d(d, points):
    """Cut one path at the given (x, y) points: a list of path data pieces, in path order. A point snaps
    to the nearest vertex within half a unit, else to the nearest point on the path. A closed path needs
    two cuts to fall into two pieces (one cut only opens it)."""
    path = svgpathtools.parse_path(d)
    cuts = []
    for x, y in points:
        target = complex(x, y)
        best = None
        for i, seg in enumerate(path):
            for k in range(0, 201):
                u = k / 200
                dist = abs(seg.point(u) - target)
                if best is None or dist < best[0]:
                    best = (dist, i, u)
        dist, i, u = best
        if dist > 2:
            sys.exit(f'--split: ({x:g},{y:g}) is {dist:.1f} units from the path')
        if abs(path[i].start - target) <= 0.5:
            u = 0.0
        elif abs(path[i].end - target) <= 0.5:
            u = 1.0
        cuts.append((i, u))
    cuts = sorted(set(cuts))
    closed = path.isclosed()

    def between(a, b):
        (i, u), (j, v) = a, b
        segs = []
        n = len(path)
        k = i
        while True:
            seg = path[k % n]
            lo = u if k == i else 0.0
            hi = v if (k % n == j and (k != i or v > u or not closed)) else 1.0
            if k == i and k % n == j and v > u:
                hi = v
            if hi > lo:
                segs.append(seg.cropped(lo, hi))
            if k % n == j and (k != i or not closed or v > u):
                break
            k += 1
            if k - i > n:
                break
        return svgpathtools.Path(*segs)

    pieces = []
    if closed:
        if len(cuts) < 2:
            sys.exit('--split: a closed path needs two cut points')
        for a, b in zip(cuts, cuts[1:] + cuts[:1]):
            pieces.append(between(a, b))
    else:
        edges = [(0, 0.0)] + cuts + [(len(path) - 1, 1.0)]
        for a, b in zip(edges, edges[1:]):
            if a != b:
                pieces.append(between(a, b))
    return [tidy_d(p.d()) for p in pieces if len(p)]


def load(source, cuts=None):
    """The drawing as a flat list of strokes. A ``<g id>`` is a named part: its children are listed as
    ``id.1``, ``id.2`` ... unless they carry their own id. A shape with a fill and no stroke is a filled
    dot (``filled``), whose ink is its area rather than a stroked line. ``cuts`` maps a stroke id to the
    points it is cut at; the pieces replace it as ``id`` + ``a``, ``b`` ..."""
    cuts = cuts or {}
    root = ET.parse(source).getroot()
    view = [float(v) for v in root.get('viewBox', '0 0 48 48').split()]
    width = float(root.get('stroke-width', 4))
    title = root.find(SVG + 'title')
    paths = []

    def walk(parent, prefix, inherited, matrix):
        n = 0
        for el in parent:
            tag = el.tag.split('}')[-1]
            fill = el.get('fill', inherited.get('fill'))
            stroke = el.get('stroke', inherited.get('stroke'))
            m = matrix @ transform_matrix(el.get('transform'))
            if tag == 'g':
                gid = el.get('id') or (f'{prefix}.{n + 1}' if prefix else f'g{len(paths)}')
                n += 1
                walk(el, gid, {'fill': fill, 'stroke': stroke}, m)
            elif tag in DRAWN:
                d = element_d(el)
                if not d:
                    continue
                d = apply_transform(d, m)
                n += 1
                pid = el.get('id') or (f'{prefix}.{n}' if prefix else f'p{len(paths)}')
                filled = fill not in (None, 'none') and stroke == 'none'
                base = {'width': float(el.get('stroke-width', width)), 'filled': filled, 'el': el, 'group': prefix,
                        'part': pid, 'piece': None}
                if pid in cuts:
                    for letter, piece in zip('abcdefgh', split_d(d, cuts[pid])):
                        paths.append({**base, 'id': pid + letter, 'd': piece, 'piece': letter})
                else:
                    paths.append({**base, 'id': pid, 'd': d})

    import numpy as np
    walk(root, '', {'fill': root.get('fill'), 'stroke': root.get('stroke')}, np.identity(3))
    return {'view': view, 'width': width, 'title': title.text.strip() if title is not None and title.text else Path(source).stem,
            'paths': paths, 'root': root}


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
    """The painted area of a stroke: round caps and joins (a filled dot: its own area)."""
    if path.get('filled'):
        return region(path['d'])
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


def parse_cuts(values):
    cuts = {}
    for v in values or []:
        pid, _, point = v.partition('@')
        xy = re.findall(r'-?\d*\.?\d+', point)
        if not pid or len(xy) != 2:
            sys.exit(f'--split: expected ID@X,Y, got {v!r}')
        cuts.setdefault(pid, []).append((float(xy[0]), float(xy[1])))
    return cuts


def vertices(d):
    """The corner points of a path: every segment end (arcs and curves contribute their ends only)."""
    pts = []
    for seg in svgpathtools.parse_path(d):
        for z in (seg.start, seg.end):
            xy = (round(z.real, 2), round(z.imag, 2))
            if not pts or pts[-1] != xy:
                pts.append(xy)
    return pts


def cmd_strokes(args):
    icon = load(args.source, parse_cuts(args.split))
    found = faces(icon)
    print(f"{icon['title']}  viewBox {' '.join(f'{v:g}' for v in icon['view'])}  stroke {icon['width']:g}  "
          f"{len(icon['paths'])} path(s)")
    for p in icon['paths']:
        lines = centerlines(p)
        kind = 'filled' if p['filled'] else 'closed' if any(c for _, c in subpaths(p['d'])) else 'open'
        x0, y0, x1, y1 = ink(p).bounds
        length = sum(l.length for l in lines)
        bounds = [n for n, f in found.items() if any(l.buffer(0.05).intersects(f.exterior) for l in lines)]
        print(f"  {p['id']:<22} {kind:<6} bbox {x0:5.1f},{y0:5.1f} -> {x1:5.1f},{y1:5.1f}  length {length:5.1f}"
              + (f"  bounds {', '.join(bounds)}" if bounds else ''))
        if not p['filled']:
            print('      points ' + ' '.join(f'({x:g},{y:g})' for x, y in vertices(p['d'])))
    if args.png:
        draw_strokes(icon, args.png)


def draw_strokes(icon, out):
    import cairosvg
    x, y, w, h = icon['view']
    scale = 512 / w
    tints = ['#E76F51', '#2A9D8F', '#3A86FF', '#8338EC', '#FB8500', '#06A77D', '#D62828', '#4361EE', '#B5179E', '#588157']
    body = []
    labels = []
    for n, p in enumerate(icon['paths']):
        colour = tints[n % len(tints)]
        if p['filled']:
            body.append(f'<path d="{p["d"]}" fill="{colour}" stroke="none"/>')
        else:
            body.append(f'<path d="{p["d"]}" fill="none" stroke="{colour}" stroke-width="{p["width"]:g}" '
                        'stroke-linecap="round" stroke-linejoin="round"/>')
        c = ink(p).representative_point()
        labels.append(f'<text x="{c.x:.2f}" y="{c.y:.2f}" font-size="{max(2.2, w / 20):.1f}" font-family="Helvetica" '
                      f'font-weight="bold" fill="#000" stroke="#fff" stroke-width="0.6" paint-order="stroke" '
                      f'text-anchor="middle" dominant-baseline="central">{p["id"]}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w * scale:g}" height="{h * scale:g}" '
           f'viewBox="{x:g} {y:g} {w:g} {h:g}"><rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="#fff"/>'
           + ''.join(body) + ''.join(labels) + '</svg>')
    cairosvg.svg2png(bytestring=svg.encode(), write_to=out)
    print(f'wrote {out}')


GEOMETRY = {'d', 'cx', 'cy', 'r', 'rx', 'ry', 'x', 'y', 'x1', 'y1', 'x2', 'y2', 'width', 'height', 'points', 'transform'}


def cmd_twotone(args):
    import copy
    icon = load(args.source, parse_cuts(args.split))
    root = icon['root']
    ids = [p['id'] for p in icon['paths']]
    groups = {p['group'] for p in icon['paths'] if p['group']}
    wanted = names(args.secondary)
    unknown = [w for w in wanted if w not in ids and w not in groups]
    if unknown:
        sys.exit(f'--secondary: unknown {", ".join(unknown)} (run the strokes command)')
    secondary = [p['id'] for p in icon['paths'] if p['id'] in wanted or p['group'] in wanted]
    primary = [i for i in ids if i not in secondary]
    if not secondary or not primary:
        sys.exit('a twotone needs both a secondary and a primary group')
    ET.register_namespace('', SVG.strip('{}'))
    out = ET.Element(root.tag, dict(root.attrib))
    for k, v in (('fill', 'none'), ('stroke', 'currentColor'), ('stroke-width', f'{icon["width"]:g}'),
                 ('stroke-linecap', 'round'), ('stroke-linejoin', 'round')):
        out.attrib.setdefault(k, v)
    title = ET.SubElement(out, SVG + 'title'); title.text = icon['title'] + ' — twotone'
    tone_attrs = {'stroke-opacity': f'{args.dim:g}'} if args.color is None else {'stroke': args.color}
    # One group per tone, secondary first so the line colour owns every junction. Group opacity keeps
    # crossings between secondary strokes from doubling up.
    weak = ET.SubElement(out, SVG + 'g', {'data-tone': 'secondary', **({'opacity': f'{args.dim:g}'} if args.color is None else {'stroke': args.color})})
    strong = ET.SubElement(out, SVG + 'g', {'data-tone': 'primary'})
    for p in icon['paths']:
        tone = 'secondary' if p['id'] in secondary else 'primary'
        if p['piece']:
            el = ET.Element(SVG + 'path', {k: v for k, v in p['el'].attrib.items() if k not in GEOMETRY and k != 'id'})
            el.set('d', p['d'])
        else:
            el = copy.deepcopy(p['el'])
        el.set('id', p['id'])
        if p['piece']:
            el.set('data-part', p['part'])
        if p['filled'] and tone == 'secondary' and args.color is not None:
            el.set('fill', args.color)
        el.tail = '\n'
        (weak if tone == 'secondary' else strong).append(el)
    for g in (weak, strong):
        g.text = '\n'; g.tail = '\n'
    out.text = '\n'; title.tail = '\n'
    Path(args.out).write_text(ET.tostring(out, encoding='unicode') + '\n')
    print(f"wrote {args.out}  (secondary: {', '.join(secondary)}; primary: {', '.join(primary)}; "
          + (f'accent {args.color}' if args.color is not None else f'dim {args.dim:g}') + ')')


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
    p = sub.add_parser('strokes')
    p.add_argument('source'); p.add_argument('--png', help='draw the icon with each path labelled by id')
    p.add_argument('--split', action='append', help='ID@X,Y: cut that stroke at the point (repeatable); pieces are listed as IDa, IDb ...')
    p.set_defaults(run=cmd_strokes)
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
    p = sub.add_parser('twotone')
    p.add_argument('source'); p.add_argument('out')
    p.add_argument('--secondary', required=True, help='stroke or group ids in the second tone (every other stroke stays primary)')
    p.add_argument('--split', action='append', help='ID@X,Y: cut that stroke at the point first (repeatable); pieces are IDa, IDb ...')
    p.add_argument('--dim', type=float, default=0.4, help='second tone = the line colour at this opacity (default 0.4, the hugeicons pattern)')
    p.add_argument('--color', help='instead of the opacity: a second stroke colour (hex), e.g. SKY_BLUE #7EC8E3')
    p.set_defaults(run=cmd_twotone)
    p = sub.add_parser('preview')
    p.add_argument('out'); p.add_argument('source'); p.add_argument('results', nargs='+')
    p.add_argument('--size', type=int, default=192)
    p.set_defaults(run=cmd_preview)
    args = parser.parse_args(argv)
    args.run(args)


if __name__ == '__main__':
    main()
