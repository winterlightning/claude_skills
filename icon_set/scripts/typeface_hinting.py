"""Grid-hint typeface v2 centerlines to other even ink heights.

The stroke stays 4; only the centerline skeleton moves. Curves are split at
their x/y extrema, so every extremum, corner and stroke end becomes a key
node. Key coordinates are scaled and rounded to integers, symmetrically about
the glyph centre, and every other point (Bezier handles, smooth joins) is
interpolated between the snapped keys (TrueType-style IUP).
"""
import math
from svgpathtools import Arc, CubicBezier, Line, Path as SVGPath, QuadraticBezier

STROKE = 4
CLUSTER = 0.35      # source coordinates closer than this are one key
CORNER_DEG = 12     # tangent turn that makes a node a corner
FLAT = math.sin(math.radians(6))  # near-axis tangent: exporter noise on extrema


def _cubics(path):
    out = []
    for seg in path:
        if isinstance(seg, Arc):
            # One cubic per <=90 degrees; a single cubic undershoots a half circle.
            out.extend(seg.as_cubic_curves(max(1, math.ceil(abs(seg.delta)/90-1e-9))))
        elif isinstance(seg, QuadraticBezier):
            p0, p1, p2 = seg.bpoints()
            out.append(CubicBezier(p0, p0+2/3*(p1-p0), p2+2/3*(p1-p2), p2))
        elif isinstance(seg, Line):
            out.append(seg)
        else:
            out.append(seg)
    return out


def _extrema(seg, axis):
    """Parameters in (0, 1) where the cubic's derivative on axis is zero."""
    if isinstance(seg, Line):
        return []
    p = [getattr(z, axis) for z in seg.bpoints()]
    a = -p[0]+3*p[1]-3*p[2]+p[3]
    b = 2*(p[0]-2*p[1]+p[2])
    c = p[1]-p[0]
    roots = []
    if abs(a) < 1e-12:
        if abs(b) > 1e-12:
            roots = [-c/b]
    else:
        disc = b*b-4*a*c
        if disc >= 0:
            r = math.sqrt(disc)
            roots = [(-b+r)/(2*a), (-b-r)/(2*a)]
    return [t for t in roots if 1e-4 < t < 1-1e-4]


def split_at_extrema(segments):
    out = []
    for seg in segments:
        ts = sorted({round(t, 9) for axis in ('real', 'imag') for t in _extrema(seg, axis)})
        rest, start = seg, 0.0
        for t in ts:
            local = (t-start)/(1-start)
            first, rest = rest.split(local)
            out.append(first)
            start = t
        out.append(rest)
    return [s for s in out if s.length() > 1e-6]


def _unit(z):
    return z/abs(z) if abs(z) > 1e-12 else 0


def _tangent_out(seg):
    pts = seg.bpoints()
    for q in pts[1:]:
        if abs(q-pts[0]) > 1e-9:
            return _unit(q-pts[0])
    return 0


def _tangent_in(seg):
    pts = seg.bpoints()
    for q in reversed(pts[:-1]):
        if abs(pts[-1]-q) > 1e-9:
            return _unit(pts[-1]-q)
    return 0


def key_coords(runs):
    """Source x and y values that must land on the grid."""
    keys = {'real': [], 'imag': []}
    for segs in runs:
        closed = abs(segs[0].start-segs[-1].end) < 1e-6
        for i, seg in enumerate(segs):
            if i == 0 and not closed:
                for axis in keys:
                    keys[axis].append(getattr(seg.start, axis))
            nxt = segs[i+1] if i+1 < len(segs) else (segs[0] if closed else None)
            node = seg.end
            if nxt is None:
                for axis in keys:
                    keys[axis].append(getattr(node, axis))
                continue
            tin, tout = _tangent_in(seg), _tangent_out(nxt)
            corner = not tin or not tout or math.degrees(abs(math.atan2((tout/tin).imag, (tout/tin).real))) > CORNER_DEG
            for axis in keys:
                flat = [abs(getattr(t, axis)) < FLAT for t in (tin, tout) if t]
                if corner or any(flat):
                    keys[axis].append(getattr(node, axis))
    return {axis: _cluster(values) for axis, values in keys.items()}


def _cluster(values):
    groups = []
    for v in sorted(values):
        if groups and v-groups[-1][-1] <= CLUSTER:
            groups[-1].append(v)
        else:
            groups.append([v])
    return [(min(g), max(g), sum(g)/len(g)) for g in groups]


def _round_from(center, value):
    d = value-center
    return center+math.copysign(math.floor(abs(d)+0.5), d)


def snap_axis(clusters, center_src, center_dst, scale):
    """Map each key cluster to an integer; symmetric about an integer centre."""
    table = []
    for lo, hi, mean in clusters:
        target = _round_from(center_dst, center_dst+(mean-center_src)*scale)
        if table and target < table[-1][3]:
            target = table[-1][3]
        table.append((lo, hi, mean, target))
    return table


def interpolator(table, center_src, center_dst, scale):
    """Monotone piecewise-linear source -> target map built on the snapped keys."""
    anchors = []
    for lo, hi, mean, target in table:
        anchors.append((lo, target))
        if hi > lo:
            anchors.append((hi, target))

    def f(v):
        if not anchors:
            return center_dst+(v-center_src)*scale
        if v <= anchors[0][0]:
            return anchors[0][1]+(v-anchors[0][0])*scale
        if v >= anchors[-1][0]:
            return anchors[-1][1]+(v-anchors[-1][0])*scale
        for (a, ta), (b, tb) in zip(anchors, anchors[1:]):
            if a <= v <= b:
                return ta if b == a else ta+(v-a)*(tb-ta)/(b-a)
        return center_dst+(v-center_src)*scale
    return f


def _round_even(value):
    return 2*math.floor(value/2+0.5)


def hint_glyph(paths, master_band, height):
    """Return (paths, report) for one glyph at ink height `height` (even)."""
    if height % 2 or height < 8:
        raise ValueError(f'Ink height must be an even integer >= 8, got {height}')
    top, bottom = master_band
    body = bottom-top
    cl_height = height-STROKE
    sy = cl_height/body
    runs = [split_at_extrema(_cubics(p)) for p in paths]
    xs = [getattr(z, 'real') for p in paths for z in (p.bbox()[0], p.bbox()[1])]
    left, right = min(xs), max(xs)
    width = right-left
    new_width = _round_even(width*sy) if width > 0.5 else 0
    sx = new_width/width if width > 0.5 else sy
    keys = key_coords(runs)
    center_x_src, center_y_src = (left+right)/2, (top+bottom)/2
    center_x_dst, center_y_dst = height/2, height/2
    ytab = snap_axis(keys['imag'], center_y_src, center_y_dst, sy)
    xtab = snap_axis(keys['real'], center_x_src, center_x_dst, sx)
    fy = interpolator(ytab, center_y_src, center_y_dst, sy)
    fx = interpolator(xtab, center_x_src, center_x_dst, sx)
    out = []
    for segs in runs:
        moved = []
        for seg in segs:
            pts = [complex(fx(z.real), fy(z.imag)) for z in seg.bpoints()]
            moved.append(Line(*pts) if isinstance(seg, Line) else CubicBezier(*pts))
        out.append(SVGPath(*moved))
    shift = max(abs(t-(c+(m-cs)*s)) for tab, c, cs, s in ((xtab, center_x_dst, center_x_src, sx), (ytab, center_y_dst, center_y_src, sy)) for _, _, m, t in tab)
    # Source keys at least half a stroke apart that snap onto one grid line
    # lose a feature; closer keys are sub-stroke drawing noise and may merge.
    merged = sum(a[3] == b[3] and b[2]-a[2] >= STROKE/2 for tab in (xtab, ytab) for a, b in zip(tab, tab[1:]))
    report = dict(x_keys=[float(t) for *_, t in xtab], y_keys=[float(t) for *_, t in ytab],
                  scale_x=round(sx, 6), scale_y=round(sy, 6), max_snap=round(float(shift), 4),
                  merged_keys=merged)
    return out, report


def fmt(v):
    v = round(v, 3)
    if abs(v-round(v)) < 1e-9:
        return str(int(round(v)))
    return f'{v:.3f}'.rstrip('0').rstrip('.')


def path_d(path):
    parts, pen = [], None
    for seg in path:
        pts = seg.bpoints()
        if pen is None or abs(pen-pts[0]) > 1e-9:
            parts.append(f'M{fmt(pts[0].real)} {fmt(pts[0].imag)}')
        if isinstance(seg, Line):
            parts.append(f'L{fmt(pts[1].real)} {fmt(pts[1].imag)}')
        else:
            parts.append('C'+' '.join(f'{fmt(z.real)} {fmt(z.imag)}' for z in pts[1:]))
        pen = pts[-1]
    if abs(path[0].start-path[-1].end) < 1e-6 and len(path) > 1:
        parts.append('Z')
    return ''.join(parts)
