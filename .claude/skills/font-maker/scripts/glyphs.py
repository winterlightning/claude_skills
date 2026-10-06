"""Shared loading for stroke glyph SVGs: centreline paths, canvas, stroke and bounds.

A glyph is an SVG whose strokes are its centrelines (fill none, one stroke width,
round caps and joins). path, rect, circle, ellipse and line elements are read;
transforms are not (keep glyph sources flat)."""
import math, os, re, xml.etree.ElementTree as ET
from svgpathtools import parse_path

NS = '{http://www.w3.org/2000/svg}'

def _rect(x, y, w, h, r):
    r = min(r, w / 2, h / 2)
    if r <= 0:
        return parse_path(f"M{x},{y} H{x+w} V{y+h} H{x} Z")
    return parse_path(f"M{x+r},{y} H{x+w-r} A{r},{r} 0 0 1 {x+w},{y+r} V{y+h-r} A{r},{r} 0 0 1 {x+w-r},{y+h} "
                      f"H{x+r} A{r},{r} 0 0 1 {x},{y+h-r} V{y+r} A{r},{r} 0 0 1 {x+r},{y} Z")

def load(path):
    """Return a dict: paths (svgpathtools Paths), dots (zero-length points), canvas (w, h), stroke."""
    root = ET.parse(path).getroot()
    vb = [float(v) for v in re.split(r'[\s,]+', root.get('viewBox', '0 0 0 0').strip())]
    paths, dots, stroke = [], [], None
    for el in root.iter():
        t = el.tag.replace(NS, '')
        g = lambda k, d=0: float(el.get(k, d))
        if el.get('stroke-width'):
            stroke = stroke or float(el.get('stroke-width'))
        if t == 'path':
            p = parse_path(el.get('d'))
            if p.length() < 1e-9:
                dots.append(p.start)
            else:
                paths.append(p)
        elif t == 'rect':
            paths.append(_rect(g('x'), g('y'), g('width'), g('height'), g('rx', el.get('ry', 0))))
        elif t == 'circle':
            cx, cy, r = g('cx'), g('cy'), g('r')
            paths.append(parse_path(f"M{cx-r},{cy} A{r},{r} 0 1 0 {cx+r},{cy} A{r},{r} 0 1 0 {cx-r},{cy} Z"))
        elif t == 'ellipse':
            cx, cy, rx, ry = g('cx'), g('cy'), g('rx'), g('ry')
            paths.append(parse_path(f"M{cx-rx},{cy} A{rx},{ry} 0 1 0 {cx+rx},{cy} A{rx},{ry} 0 1 0 {cx-rx},{cy} Z"))
        elif t == 'line':
            paths.append(parse_path(f"M{g('x1')},{g('y1')} L{g('x2')},{g('y2')}"))
    return {'paths': paths, 'dots': dots, 'canvas': (vb[2], vb[3]), 'stroke': stroke or 4.0, 'file': path}

def bounds(glyph):
    """Centreline bounds (x0, y0, x1, y1) including dots."""
    xs, ys = [], []
    for p in glyph['paths']:
        x0, x1, y0, y1 = p.bbox(); xs += [x0, x1]; ys += [y0, y1]
    for d in glyph['dots']:
        xs.append(d.real); ys.append(d.imag)
    return min(xs), min(ys), max(xs), max(ys)

def ink_bounds(glyph):
    s = glyph['stroke'] / 2; x0, y0, x1, y1 = bounds(glyph)
    return x0 - s, y0 - s, x1 + s, y1 + s

def char_of(path):
    """File stem to character: 'A.svg' -> 'A', 'a.svg' -> 'a', '0.svg' -> '0'."""
    return os.path.splitext(os.path.basename(path))[0]

def collect(folder_or_files):
    """Every .svg under the given folders/files, sorted by character."""
    out = []
    for f in folder_or_files:
        if os.path.isdir(f):
            for root, _, files in os.walk(f):
                out += [os.path.join(root, x) for x in files if x.endswith('.svg')]
        elif f.endswith('.svg'):
            out.append(f)
    return sorted(out, key=lambda p: (char_of(p).isdigit(), char_of(p).lower(), char_of(p).islower()))
