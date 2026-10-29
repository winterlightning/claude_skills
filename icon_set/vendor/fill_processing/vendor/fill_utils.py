"""Shared utilities for fill processing pipeline.

- load / load_one: Parse raw SVGs from assets dir → stroke-to-polygon → DataFrame
- build_region_dataframe: Walk polygon nesting → one row per region (DataFrame)
- geometry_to_svg: Convert Shapely geometry to SVG string
- close_open_edges: Connect open shapes near viewbox edges

Usage:
    from fill_utils import load, build_region_dataframe, geometry_to_svg
    df = load("assets_todo_svg_1024_60")
    df = load("assets_todo_svg_1024_60/some_icon.svg")
    regions_df = build_region_dataframe(polygon, buffer_dist=70)
"""

import glob
import copy
import json
import math
import os
import re
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd
from shapely.geometry import LineString, LinearRing, MultiPolygon, Polygon, Point
from shapely.geometry import box as shapely_box
from shapely.ops import unary_union, polygonize
from shapely.affinity import affine_transform
from svgpathtools import parse_path, Line
import pathops
from fontTools.svgLib.path import SVGPath
from fontTools.pens.basePen import BasePen
from fontTools.pens.svgPathPen import SVGPathPen

DEFAULT_INPUT_DIR = "assets_todo_svg_1024_60"
CIRCLE_SAMPLES = 64
CURVE_SAMPLES = 20

# SVG cap/join → Shapely equivalents
SHAPELY_CAP = {'butt': 'flat', 'round': 'round', 'square': 'square'}
SHAPELY_JOIN = {'miter': 'mitre', 'round': 'round', 'bevel': 'bevel'}


# ---------------------------------------------------------------------------
# SVG path → LineString conversion (from stroke_to_fill.py)
# ---------------------------------------------------------------------------

def _sample_segment(seg, num_samples=CURVE_SAMPLES):
    """Sample points from a path segment."""
    if isinstance(seg, Line):
        return [(seg.start.real, seg.start.imag), (seg.end.real, seg.end.imag)]
    else:
        points = []
        for i in range(num_samples + 1):
            t = i / num_samples
            pt = seg.point(t)
            points.append((pt.real, pt.imag))
        return points


def _points_close(p1, p2, tol=1e-4):
    """Check if two points are close enough to be considered connected."""
    return abs(p1[0] - p2[0]) < tol and abs(p1[1] - p2[1]) < tol


def _replace_zero_length_arcs(d):
    """SVG ignores arcs with equal endpoints; svgpathtools rejects them."""
    tokens = re.findall(r'[AaCcHhLlMmQqSsTtVvZz]|[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?', d)
    sizes = {'M': 2, 'L': 2, 'H': 1, 'V': 1, 'C': 6, 'S': 4, 'Q': 4, 'T': 2, 'A': 7}
    out, i, command = [], 0, None
    current = start = complex(0, 0)
    while i < len(tokens):
        if tokens[i].isalpha():
            command = tokens[i]
            i += 1
            if command.upper() == 'Z':
                out.append(command)
                current = start
                command = None
                continue
        kind = command.upper()
        n = sizes[kind]
        raw = tokens[i:i+n]
        values = list(map(float, raw))
        if len(values) != n:
            raise ValueError('Incomplete path command')
        i += n
        relative = command.islower()
        if kind == 'H':
            end = complex(values[0] + (current.real if relative else 0), current.imag)
        elif kind == 'V':
            end = complex(current.real, values[0] + (current.imag if relative else 0))
        else:
            end = complex(*values[-2:]) + (current if relative else 0)
        if kind == 'A' and abs(end-current) < 1e-12:
            out.extend(['L', str(end.real), str(end.imag)])
        else:
            out.extend([command, *raw])
        current = end
        if kind == 'M':
            start = current
            command = 'l' if relative else 'L'
    return ' '.join(out)


def path_to_linestrings(d_attr):
    """Convert an SVG path d attribute to a list of Shapely LineStrings.

    Splits at discontinuities (M commands) to form connected chains,
    then converts each chain to a LineString.
    """
    try:
        parsed = parse_path(d_attr)
    except Exception:
        try:
            parsed = parse_path(_replace_zero_length_arcs(d_attr))
        except Exception:
            return []

    if not parsed:
        return []

    chains = []
    current_points = []

    for seg in parsed:
        seg_points = _sample_segment(seg)
        if not seg_points:
            continue

        if current_points:
            last_point = current_points[-1]
            first_seg_point = seg_points[0]
            if not _points_close(last_point, first_seg_point):
                if len(current_points) >= 2:
                    chains.append(current_points)
                current_points = []

        if current_points and seg_points and _points_close(current_points[-1], seg_points[0]):
            current_points.extend(seg_points[1:])
        else:
            current_points.extend(seg_points)

    if len(current_points) >= 2:
        chains.append(current_points)

    linestrings = []
    for chain in chains:
        deduped = [chain[0]]
        for pt in chain[1:]:
            if not _points_close(deduped[-1], pt):
                deduped.append(pt)
        if len(deduped) >= 2:
            linestrings.append(LineString(deduped))
        elif deduped:
            # A zero-length subpath can render as a dot with round caps.
            linestrings.append(LineString([deduped[0], deduped[0]]))

    return linestrings


# ---------------------------------------------------------------------------
# SVG parsing helpers (from step_1_visualize_stroke_svg.py)
# ---------------------------------------------------------------------------

def _local_tag(tag):
    return tag.split('}')[-1] if '}' in tag else tag


def _get_ns(tag):
    if '}' in tag:
        return tag.split('}')[0] + '}'
    return ''


def _build_parent_map(root):
    parent_map = {}
    for parent in root.iter():
        for child in parent:
            parent_map[child] = parent
    return parent_map


def _resolve_attr(elem, attr, parent_map, default=None):
    current = elem
    while current is not None:
        val = current.get(attr)
        if val is not None:
            return val
        current = parent_map.get(current)
    return default


def _get_float(elem, attr, default=0.0):
    try:
        return _svg_length(elem.get(attr, default))
    except (ValueError, TypeError):
        return default


def _svg_length(value, percentage_base=None):
    value = str(value).strip()
    if value.endswith('%'):
        if percentage_base is None:
            raise ValueError('Percentage length needs a viewport')
        return float(value[:-1]) * percentage_base / 100
    value = re.sub(r'px$', '', value, flags=re.I)
    number = float(value)
    if not math.isfinite(number):
        raise ValueError('Non-finite SVG length')
    return number


def _inline_svg_styles(root):
    """Resolve stylesheet selectors and inline declarations before inheritance."""
    styles = list(root.iter('{http://www.w3.org/2000/svg}style'))
    if not styles and not any('style' in e.attrib for e in root.iter()):
        return
    import tinycss2
    import cssselect2
    matcher = cssselect2.Matcher()
    for style in styles:
        for rule in tinycss2.parse_stylesheet(style.text or '', skip_comments=True, skip_whitespace=True):
            if rule.type != 'qualified-rule':
                continue
            declarations = tinycss2.parse_declaration_list(rule.content, skip_comments=True, skip_whitespace=True)
            for selector in cssselect2.compile_selector_list(rule.prelude):
                matcher.add_selector(selector, declarations)
    for wrapped in cssselect2.ElementWrapper.from_xml_root(root).iter_subtree():
        element = wrapped.etree_element
        winners = {}
        for specificity, order, pseudo, declarations in matcher.match(wrapped):
            if pseudo is not None:
                continue
            for declaration in declarations:
                if declaration.type == 'declaration':
                    rank = (declaration.important, 0, specificity, order)
                    if declaration.lower_name not in winners or rank >= winners[declaration.lower_name][0]:
                        winners[declaration.lower_name] = (rank, tinycss2.serialize(declaration.value).strip())
        for declaration in tinycss2.parse_declaration_list(element.get('style', ''), skip_comments=True, skip_whitespace=True):
            if declaration.type == 'declaration':
                rank = (declaration.important, 1, (0, 0, 0), 0)
                if declaration.lower_name not in winners or rank >= winners[declaration.lower_name][0]:
                    winners[declaration.lower_name] = (rank, tinycss2.serialize(declaration.value).strip())
        for name, (_, value) in winners.items():
            element.set(name, value)


def _circle_to_coords(cx, cy, r, n=CIRCLE_SAMPLES):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=True)
    return list(zip(cx + r * np.cos(angles), cy + r * np.sin(angles)))


def _ellipse_to_coords(cx, cy, rx, ry, n=CIRCLE_SAMPLES):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=True)
    return list(zip(cx + rx * np.cos(angles), cy + ry * np.sin(angles)))


def _rect_to_coords(x, y, w, h):
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]


def _parse_points(points_str):
    coords = []
    parts = points_str.replace(',', ' ').split()
    for i in range(0, len(parts) - 1, 2):
        try:
            coords.append((float(parts[i]), float(parts[i + 1])))
        except ValueError:
            continue
    return coords


# ---------------------------------------------------------------------------
# Affine transforms, <use> resolution, rounded rect sampling
# ---------------------------------------------------------------------------

_IDENTITY = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
_XLINK_HREF = '{http://www.w3.org/1999/xlink}href'
_TRANSFORM_RE = re.compile(r'(matrix|translate|scale|rotate|skewX|skewY)\s*\(([^)]*)\)')
_NUM_RE = re.compile(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?')


def _compose(m1, m2):
    a1, b1, c1, d1, e1, f1 = m1
    a2, b2, c2, d2, e2, f2 = m2
    return (
        a1 * a2 + c1 * b2,
        b1 * a2 + d1 * b2,
        a1 * c2 + c1 * d2,
        b1 * c2 + d1 * d2,
        a1 * e2 + c1 * f2 + e1,
        b1 * e2 + d1 * f2 + f1,
    )


def _parse_transform(attr_str):
    if not attr_str:
        return _IDENTITY
    m = _IDENTITY
    for name, body in _TRANSFORM_RE.findall(attr_str):
        nums = [float(n) for n in _NUM_RE.findall(body)]
        if name == 'matrix' and len(nums) == 6:
            t = tuple(nums)
        elif name == 'translate':
            tx = nums[0] if nums else 0.0
            ty = nums[1] if len(nums) > 1 else 0.0
            t = (1.0, 0.0, 0.0, 1.0, tx, ty)
        elif name == 'scale':
            sx = nums[0] if nums else 1.0
            sy = nums[1] if len(nums) > 1 else sx
            t = (sx, 0.0, 0.0, sy, 0.0, 0.0)
        elif name == 'rotate':
            angle = math.radians(nums[0]) if nums else 0.0
            cos_a, sin_a = math.cos(angle), math.sin(angle)
            if len(nums) >= 3:
                cx, cy = nums[1], nums[2]
                tx = cx - cos_a * cx + sin_a * cy
                ty = cy - sin_a * cx - cos_a * cy
                t = (cos_a, sin_a, -sin_a, cos_a, tx, ty)
            else:
                t = (cos_a, sin_a, -sin_a, cos_a, 0.0, 0.0)
        elif name == 'skewX':
            angle = math.radians(nums[0]) if nums else 0.0
            t = (1.0, 0.0, math.tan(angle), 1.0, 0.0, 0.0)
        elif name == 'skewY':
            angle = math.radians(nums[0]) if nums else 0.0
            t = (1.0, math.tan(angle), 0.0, 1.0, 0.0, 0.0)
        else:
            continue
        m = _compose(m, t)
    return m


def _apply_xform(coords, m):
    if m == _IDENTITY:
        return coords
    a, b, c, d, e, f = m
    return [(a * x + c * y + e, b * x + d * y + f) for x, y in coords]


def _rounded_rect_to_coords(x, y, w, h, rx, ry, n=CIRCLE_SAMPLES):
    rx = min(max(rx, 0.0), w / 2.0)
    ry = min(max(ry, 0.0), h / 2.0)
    if rx <= 0 or ry <= 0:
        return _rect_to_coords(x, y, w, h)
    per_corner = max(4, n // 4)
    angles = np.linspace(0, np.pi / 2, per_corner, endpoint=True)
    coords = []
    # CW traversal (SVG y-down): top-right → bottom-right → bottom-left → top-left
    cx_tr, cy_tr = x + w - rx, y + ry
    for a in angles:
        ang = -np.pi / 2 + a
        coords.append((cx_tr + rx * math.cos(ang), cy_tr + ry * math.sin(ang)))
    cx_br, cy_br = x + w - rx, y + h - ry
    for a in angles:
        coords.append((cx_br + rx * math.cos(a), cy_br + ry * math.sin(a)))
    cx_bl, cy_bl = x + rx, y + h - ry
    for a in angles:
        ang = np.pi / 2 + a
        coords.append((cx_bl + rx * math.cos(ang), cy_bl + ry * math.sin(ang)))
    cx_tl, cy_tl = x + rx, y + ry
    for a in angles:
        ang = np.pi + a
        coords.append((cx_tl + rx * math.cos(ang), cy_tl + ry * math.sin(ang)))
    deduped = [coords[0]]
    for c in coords[1:]:
        if abs(c[0] - deduped[-1][0]) > 1e-9 or abs(c[1] - deduped[-1][1]) > 1e-9:
            deduped.append(c)
    if deduped[0] != deduped[-1]:
        deduped.append(deduped[0])
    return deduped


def _build_id_map(root):
    id_map = {}
    for elem in root.iter():
        eid = elem.get('id')
        if eid:
            id_map[eid] = elem
    return id_map


def _resolve_href(elem):
    href = elem.get('href') or elem.get(_XLINK_HREF)
    if not href:
        return None
    href = href.strip()
    if not href.startswith('#'):
        return None
    return href[1:]


# ---------------------------------------------------------------------------
# Parse all shapes from SVG
# ---------------------------------------------------------------------------

def _filled_path_geometry(chains, fill_rule='nonzero'):
    """Build already-filled SVG geometry without filling its intentional holes."""
    rings = []
    for coords, _ in chains:
        if len(set(coords)) < 3:
            continue
        ring = list(coords)
        if ring[-1] != ring[0]:
            ring.append(ring[0])
        rings.append(ring)
    if not rings:
        return Polygon()
    faces = polygonize(unary_union([LineString(ring) for ring in rings]))
    def winding(point, ring):
        count = 0
        for (x0, y0), (x1, y1) in zip(ring, ring[1:]):
            side = (x1-x0)*(point.y-y0) - (point.x-x0)*(y1-y0)
            if y0 <= point.y < y1 and side > 0:
                count += 1
            elif y1 <= point.y < y0 and side < 0:
                count -= 1
        return count
    filled = []
    for face in faces:
        point = face.representative_point()
        count = sum(winding(point, ring) for ring in rings)
        inside = (count % 2 != 0) if fill_rule == 'evenodd' else (count != 0)
        if inside:
            filled.append(face)
    return unary_union(filled) if filled else Polygon()


def _native_path(elem):
    """Read original curves before applying transforms or expanding strokes."""
    leaf = copy.deepcopy(elem)
    leaf.attrib.pop('transform', None)
    if _local_tag(leaf.tag) == 'path':
        leaf.set('d', _replace_zero_length_arcs(leaf.get('d', '')))
    if _local_tag(leaf.tag) == 'rect':
        rx = float(leaf.get('rx', leaf.get('ry', '0')))
        ry = float(leaf.get('ry', leaf.get('rx', '0')))
        leaf.set('rx', str(min(max(rx, 0), float(leaf.get('width', '0')) / 2)))
        leaf.set('ry', str(min(max(ry, 0), float(leaf.get('height', '0')) / 2)))
    path = pathops.Path()
    SVGPath.fromstring(ET.tostring(leaf)).draw(path.getPen())
    # FontTools emits circle/ellipse curves returning to their start, but does
    # not emit closePath. SVG intrinsic shapes are closed regardless of caps;
    # stroking them as open creates numerical seams and can lose their face.
    # Do not infer closure for paths/polylines, even if endpoints coincide.
    if _local_tag(leaf.tag) in {'circle', 'ellipse', 'rect', 'polygon'}:
        commands = list(path)
        if commands and commands[-1][0] != pathops.PathVerb.CLOSE:
            path.close()
    return path


def _native_geometry(path, tolerance):
    """Flatten an already expanded native outline adaptively, in canvas units."""
    class Pen(BasePen):
        def __init__(self):
            super().__init__(None)
            self.chains, self.points = [], []

        def _moveTo(self, p):
            self._endPath()
            self.points = [p]

        def _lineTo(self, p):
            self.points.append(p)

        def curve(self, points, depth=0):
            start, end = points[0], points[-1]
            dx, dy = end[0]-start[0], end[1]-start[1]
            length2 = dx*dx + dy*dy
            def distance(p):
                t = max(0, min(1, ((p[0]-start[0])*dx+(p[1]-start[1])*dy)/length2)) if length2 else 0
                return math.hypot(p[0]-start[0]-t*dx, p[1]-start[1]-t*dy)
            if depth >= 14 or max(distance(p) for p in points[1:-1]) <= tolerance:
                self.points.append(end)
                return
            levels = [points]
            while len(levels[-1]) > 1:
                levels.append([((a[0]+b[0])/2, (a[1]+b[1])/2) for a, b in zip(levels[-1], levels[-1][1:])])
            self.curve([r[0] for r in levels], depth+1)
            self.curve([r[-1] for r in reversed(levels)], depth+1)

        def _curveToOne(self, a, b, c):
            self.curve([self.points[-1], a, b, c])

        def _qCurveToOne(self, a, b):
            self.curve([self.points[-1], a, b])

        def _closePath(self):
            if self.points:
                self.points.append(self.points[0])
            self._endPath()

        def _endPath(self):
            if self.points:
                self.chains.append((self.points, True))
            self.points = []
    path.convertConicsToQuads(tolerance)
    pen = Pen()
    path.draw(pen)
    pen._endPath()
    rule = 'evenodd' if path.fillType == pathops.FillType.EVEN_ODD else 'nonzero'
    return _filled_path_geometry(pen.chains, rule)


def parse_all_shapes(svg_path, include_fills=False):
    """Parse SVG, extract all stroked shape elements.

    Walks the element tree, composing `transform` attributes down the chain,
    expanding `<use>` references into `<defs>`/`<symbol>`, and sampling
    rounded-rect corners.

    Returns (root, viewbox, shapes) where shapes is a list of dicts with:
        coords, closed, stroke_width, cap, join
    """
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    tree = ET.parse(svg_path)
    root = tree.getroot()
    _inline_svg_styles(root)
    parent_map = _build_parent_map(root)
    id_map = _build_id_map(root)

    vb = root.get('viewBox')
    if vb:
        viewbox = tuple(float(x) for x in vb.replace(',', ' ').split())
    else:
        viewbox = (0.0, 0.0, _svg_length(root.get('width', '300')),
                   _svg_length(root.get('height', '150')))
    if len(viewbox) != 4 or not all(math.isfinite(v) for v in viewbox) or min(viewbox[2:]) <= 0:
        raise ValueError('SVG must have a finite viewBox with positive width and height')

    shapes = []

    def _extract_leaf_coords(elem, tag):
        """Return a list of (coords, closed) pairs for a leaf shape, or []."""
        out = []
        if tag == 'path':
            d = elem.get('d', '').strip()
            if not d:
                return out
            for ls in path_to_linestrings(d):
                if ls.is_empty:
                    continue
                c = list(ls.coords)
                closed = len(c) >= 3 and (
                    abs(c[0][0] - c[-1][0]) < 1e-3
                    and abs(c[0][1] - c[-1][1]) < 1e-3
                )
                out.append((c, closed))
        elif tag == 'circle':
            cx, cy, r = _get_float(elem, 'cx'), _get_float(elem, 'cy'), _get_float(elem, 'r')
            if r > 0:
                out.append((_circle_to_coords(cx, cy, r), True))
        elif tag == 'ellipse':
            cx, cy = _get_float(elem, 'cx'), _get_float(elem, 'cy')
            rx, ry = _get_float(elem, 'rx'), _get_float(elem, 'ry')
            if rx > 0 and ry > 0:
                out.append((_ellipse_to_coords(cx, cy, rx, ry), True))
        elif tag == 'rect':
            x, y = _get_float(elem, 'x'), _get_float(elem, 'y')
            w, h = _get_float(elem, 'width'), _get_float(elem, 'height')
            if w > 0 and h > 0:
                rx = _get_float(elem, 'rx')
                ry = _get_float(elem, 'ry')
                if rx > 0 and ry <= 0:
                    ry = rx
                elif ry > 0 and rx <= 0:
                    rx = ry
                if rx > 0 or ry > 0:
                    out.append((_rounded_rect_to_coords(x, y, w, h, rx, ry), True))
                else:
                    out.append((_rect_to_coords(x, y, w, h), True))
        elif tag == 'line':
            c = [
                (_get_float(elem, 'x1'), _get_float(elem, 'y1')),
                (_get_float(elem, 'x2'), _get_float(elem, 'y2')),
            ]
            out.append((c, False))
        elif tag == 'polyline':
            c = _parse_points(elem.get('points', ''))
            if len(c) >= 2:
                out.append((c, False))
        elif tag == 'polygon':
            c = _parse_points(elem.get('points', ''))
            if len(c) >= 3:
                if c[0] != c[-1]:
                    c.append(c[0])
                out.append((c, True))
        return out

    clip_cache = {}

    def clip_geometry(reference, ctm):
        key = (reference, ctm)
        if key in clip_cache:
            return clip_cache[key]
        match = re.fullmatch(r'url\(\s*[\'\"]?#([^\s\'\")]+)[\'\"]?\s*\)', reference)
        clip = id_map.get(match.group(1)) if match else None
        if clip is None or _local_tag(clip.tag) != 'clipPath':
            raise ValueError('Unresolved SVG clip-path: ' + reference)
        if clip.get('clipPathUnits', 'userSpaceOnUse') != 'userSpaceOnUse':
            raise ValueError('objectBoundingBox clipping needs explicit support')
        parts = []
        def walk_clip(el, matrix):
            matrix = _compose(matrix, _parse_transform(el.get('transform', '')))
            tag = _local_tag(el.tag)
            if tag in ('clipPath', 'g'):
                for child in el:
                    walk_clip(child, matrix)
            else:
                chains = _extract_leaf_coords(el, tag)
                geometry = _filled_path_geometry(chains, _resolve_attr(el, 'clip-rule', parent_map, 'nonzero'))
                a, b, c, d, e, f = matrix
                parts.append(affine_transform(geometry, (a, c, b, d, e, f)))
        walk_clip(clip, ctm)
        clip_cache[key] = unary_union(parts)
        return clip_cache[key]

    def _walk(elem, ctm, visited, clip=None):
        tag = _local_tag(elem.tag)
        local = _parse_transform(elem.get('transform', ''))
        current_ctm = _compose(ctm, local)

        if elem.get('display') == 'none' or elem.get('visibility') in ('hidden', 'collapse'):
            return

        if tag in ('defs', 'symbol'):
            return

        reference = elem.get('clip-path', 'none')
        if reference != 'none':
            local_clip = clip_geometry(reference, current_ctm)
            clip = local_clip if clip is None else clip.intersection(local_clip)

        if tag == 'use':
            target_id = _resolve_href(elem)
            if not target_id or target_id not in id_map or target_id in visited:
                return
            ux = _get_float(elem, 'x')
            uy = _get_float(elem, 'y')
            use_ctm = _compose(current_ctm, (1.0, 0.0, 0.0, 1.0, ux, uy))
            _walk(id_map[target_id], use_ctm, visited | {target_id}, clip)
            return

        if tag in ('svg', 'g', 'a', 'marker', 'clipPath', 'mask', 'pattern'):
            for child in elem:
                _walk(child, current_ctm, visited, clip)
            return

        chains = _extract_leaf_coords(elem, tag)
        fill = _resolve_attr(elem, 'fill', parent_map, 'black')
        if include_fills and fill.lower() not in ('none', 'transparent', 'white', '#fff', '#ffffff'):
            geometry = _filled_path_geometry(chains, _resolve_attr(elem, 'fill-rule', parent_map, 'nonzero'))
            if not geometry.is_empty:
                a, b, c, d, e, f = current_ctm
                geometry = affine_transform(geometry, (a, c, b, d, e, f))
                if clip is not None:
                    geometry = geometry.intersection(clip)
                shapes.append({'kind': 'fill', 'geometry': geometry,
                               'source_id': elem.get('id') or f'{tag}-{len(shapes) + 1}'})

        # Stroke geometry is separate from existing solid details.
        stroke = _resolve_attr(elem, 'stroke', parent_map, 'none')
        stroke_width_str = _resolve_attr(elem, 'stroke-width', parent_map, '1')
        cap = _resolve_attr(elem, 'stroke-linecap', parent_map, 'butt')
        join = _resolve_attr(elem, 'stroke-linejoin', parent_map, 'miter')
        try:
            miter_limit = float(_resolve_attr(elem, 'stroke-miterlimit', parent_map, '4'))
            if not math.isfinite(miter_limit) or miter_limit < 1:
                miter_limit = 4.0
        except (TypeError, ValueError):
            miter_limit = 4.0
        if stroke.lower() == 'none':
            return
        try:
            stroke_width = _svg_length(stroke_width_str, math.hypot(*viewbox[2:]) / math.sqrt(2))
        except ValueError:
            return
        if stroke_width <= 0:
            return

        data_line = elem.get('data-line')
        native_contours = [p for p in _native_path(elem).contours if len(p.verbs) > 1] if chains else []
        if len(native_contours) != len(chains):
            # Explicit M commands remain separate even when endpoints touch.
            # svgpathtools' segment iteration alone loses that distinction.
            chains = []
            for contour in native_contours:
                contour.convertConicsToQuads(.001)
                pen = SVGPathPen(None)
                contour.draw(pen)
                lines = path_to_linestrings(pen.getCommands())
                if not lines:
                    # SVGPathPen drops redundant zero-length L commands, but
                    # these are visible dots with round/square caps.
                    points = [p for _, values in contour for p in values]
                    if points and all(_points_close(p, points[0]) for p in points):
                        lines = [LineString([points[0], points[0]])]
                if len(lines) != 1:
                    raise ValueError('Cannot sample native SVG subpath')
                chains.append((list(lines[0].coords), contour.verbs[-1] == pathops.PathVerb.CLOSE))
        for (coords, closed), native_path in zip(chains, native_contours):
            closed = native_path.verbs[-1] == pathops.PathVerb.CLOSE
            source_coords = coords
            coords = _apply_xform(source_coords, current_ctm)
            shapes.append({
                'coords': coords, 'closed': closed,
                'source_coords': source_coords, 'transform': current_ctm,
                'non_scaling_stroke': elem.get('vector-effect') == 'non-scaling-stroke',
                'source_id': elem.get('id') or f'{tag}-{len(shapes) + 1}',
                'stroke_width': stroke_width, 'cap': cap, 'join': join,
                'miter_limit': miter_limit,
                'native_path': native_path, 'clip_geometry': clip,
                'data_line': data_line,
            })

    _walk(root, _IDENTITY, set())
    return root, viewbox, shapes


def build_hybrid_polygon(df, viewbox, hole_width=45, normal_width=70,
                         cap='round', join='round', hole_fill_lookup=None,
                         propagate_along_chains=True):
    """Buffer each stroke in a combined df with per-stroke width.

    Decision rule:
      - If `hole_fill_lookup` is provided (maps "H{rid}" → 'fill'/'keep'/None):
        a stroke uses `hole_width` when any of its ringed holes has fill='fill',
        else `normal_width`.
      - Fallback (no lookup): any stroke with non-empty `hole_ids` uses
        `hole_width`.

    Chain propagation (`propagate_along_chains=True`, default):
      Strokes that connect endpoint-to-endpoint (via the `connects_to` column)
      form a continuous line visually. A line should not jump widths mid-way,
      so once initial widths are computed, every connected component takes the
      MAX width found among its members — i.e. 45 is preserved only when the
      entire chain would be 45. This stops the "thick / thin / thick" beading
      effect when a silhouette stroke happens to pass through a filled-hole
      neighbourhood.
    """
    cap_s = SHAPELY_CAP.get(cap, 'round')
    join_s = SHAPELY_JOIN.get(join, 'round')

    if isinstance(viewbox, str):
        nums = [float(x) for x in viewbox.strip('()').replace(',', ' ').split()]
    else:
        nums = list(viewbox)
    vb_max = max(abs(nums[2]), abs(nums[3])) if len(nums) >= 4 else 1024
    tolerance = vb_max * 0.0005

    strokes = df[df['type'] == 'stroke'] if 'type' in df.columns else df

    # Step 1: initial per-stroke width
    widths = {}
    for _, row in strokes.iterrows():
        hids = row.get('hole_ids') or set()
        if hole_fill_lookup is not None:
            rings_filled = any(hole_fill_lookup.get(hid) == 'fill' for hid in hids)
            widths[row['id']] = hole_width if rings_filled else normal_width
        else:
            widths[row['id']] = hole_width if hids else normal_width

    # Step 2: propagate MAX width along connected chains (union-find)
    if propagate_along_chains and widths:
        parent = {sid: sid for sid in widths}

        def _find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def _union(a, b):
            ra, rb = _find(a), _find(b)
            if ra != rb:
                parent[ra] = rb

        for _, row in strokes.iterrows():
            sid = row['id']
            if sid not in parent:
                continue
            for c in (row.get('connects_to') or set()):
                if c in parent:
                    _union(sid, c)

        comp_max = {}
        for sid, w in widths.items():
            root = _find(sid)
            if w > comp_max.get(root, 0):
                comp_max[root] = w
        widths = {sid: comp_max[_find(sid)] for sid in widths}

    # Step 3: buffer each stroke with its (possibly promoted) width
    all_buffered = []
    for _, row in strokes.iterrows():
        geom = row['geometry']
        if geom is None or geom.is_empty or geom.length < 1e-6:
            continue
        sw = widths.get(row['id'], normal_width)
        buffered = geom.buffer(sw / 2.0, cap_style=cap_s, join_style=join_s,
                               quad_segs=8)
        if not buffered.is_empty:
            all_buffered.append(buffered)

    if not all_buffered:
        return None
    merged = unary_union(all_buffered)
    return merged.simplify(tolerance, preserve_topology=True)


# ---------------------------------------------------------------------------
# Stroke → polygon
# ---------------------------------------------------------------------------

def stroke_to_polygon(shapes, viewbox, stroke_width=None):
    """Buffer each shape into a filled polygon, merge, simplify.

    Args:
        shapes: list of shape dicts from parse_all_shapes()
        viewbox: (x, y, w, h) tuple
        stroke_width: override stroke-width for all shapes (None = use original)

    Returns:
        merged Shapely geometry (Polygon/MultiPolygon), or None
    """
    vb_max = max(abs(viewbox[2]), abs(viewbox[3])) if len(viewbox) >= 4 else 1024
    tolerance = vb_max * 0.0005

    all_buffered = []
    for shape in shapes:
        if shape.get('kind') == 'fill':
            continue
        sw = stroke_width if stroke_width is not None else shape['stroke_width']
        half_width = sw / 2.0

        cap = SHAPELY_CAP.get(shape['cap'], 'flat')
        join = SHAPELY_JOIN.get(shape['join'], 'mitre')

        if 'native_path' in shape:
            path = pathops.Path(shape['native_path'])
            matrix = shape.get('transform', _IDENTITY)
            if shape.get('non_scaling_stroke'):
                path = path.transform(*matrix)
                matrix = _IDENTITY
            # Expand the original Beziers, not their sampled centerline: joins
            # belong at source vertices, never at curve sampling points.
            path = path.transform(16, 0, 0, 16)
            path.stroke(sw*16,
                        {'round': pathops.LineCap.ROUND_CAP, 'square': pathops.LineCap.SQUARE_CAP}.get(shape['cap'], pathops.LineCap.BUTT_CAP),
                        {'round': pathops.LineJoin.ROUND_JOIN, 'bevel': pathops.LineJoin.BEVEL_JOIN}.get(shape['join'], pathops.LineJoin.MITER_JOIN),
                        shape.get('miter_limit', 4.0))
            path.convertConicsToQuads(.016)
            path.simplify()
            path = path.transform(1/16, 0, 0, 1/16).transform(*matrix)
            buffered = _native_geometry(path, vb_max / 8000)
            if shape.get('clip_geometry') is not None:
                buffered = buffered.intersection(shape['clip_geometry'])
            if not buffered.is_empty:
                all_buffered.append(buffered)
            continue

        transform = shape.get('transform', _IDENTITY)
        if shape.get('non_scaling_stroke'):
            transform = _IDENTITY
            coords = shape['coords']
        else:
            coords = shape.get('source_coords', shape['coords'])
        a, b, c, d, e, f = transform
        def to_canvas(geometry):
            return affine_transform(geometry, (a, c, b, d, e, f)) if transform != _IDENTITY else geometry
        if len(coords) < 2:
            continue

        if shape['closed'] and len(coords) >= 3:
            geom = LinearRing(coords)
        else:
            geom = LineString(coords)

        if geom.is_empty:
            continue
        if geom.length < 1e-6:
            point = Point(coords[0])
            if cap == 'round':
                all_buffered.append(to_canvas(point.buffer(half_width, quad_segs=8)))
            elif cap == 'square':
                all_buffered.append(to_canvas(shapely_box(point.x-half_width, point.y-half_width,
                                               point.x+half_width, point.y+half_width)))
            continue

        # Compatibility for callers constructing sampled shapes directly.
        buffered = geom.buffer(half_width, cap_style=cap, join_style=join,
                               mitre_limit=shape.get('miter_limit', 4.0), quad_segs=8)
        if not buffered.is_empty:
            all_buffered.append(to_canvas(buffered))

    if not all_buffered:
        return None

    merged = unary_union(all_buffered)
    merged = merged.simplify(tolerance, preserve_topology=True)
    # Buffering sampled curves leaves tiny sub-pixel interior slivers along
    # the inner offset where adjacent segment buffers don't tile cleanly.
    # Drop any interior whose area is below a sub-pixel threshold.
    min_hole_area = tolerance * tolerance * 4
    merged = _drop_tiny_holes(merged, min_hole_area)
    return merged


def _drop_tiny_holes(geom, min_area):
    """Rebuild Polygon/MultiPolygon dropping interior rings smaller than min_area."""
    if geom is None or geom.is_empty:
        return geom
    if isinstance(geom, MultiPolygon):
        return MultiPolygon([_drop_tiny_holes(p, min_area) for p in geom.geoms])
    if isinstance(geom, Polygon):
        keep = [r for r in geom.interiors if Polygon(r).area >= min_area]
        if len(keep) == len(list(geom.interiors)):
            return geom
        return Polygon(geom.exterior, keep)
    return geom


# ---------------------------------------------------------------------------
# Load raw SVGs → parse + buffer → DataFrame
# ---------------------------------------------------------------------------

def close_open_bottoms(shapes, viewbox, stroke_width=None):
    """Close lower endpoints of each open shape, independent of canvas position.

    Only join endpoints belonging to the same chain. Reject top/side openings,
    shallow marks, closed outlines, and self-intersecting proposed closures.
    Distances scale with the shape's own stroke and the SVG viewBox.
    """
    closed_shapes, closures = [], []
    scale = max(viewbox[2:])
    original = stroke_to_polygon(shapes, viewbox, stroke_width)
    envelopes = unary_union([Polygon(p.exterior) for p in to_polys(original)])
    for shape in shapes:
        closed_shapes.append(shape)
        if shape.get('kind') == 'fill':
            continue
        coords = shape['coords']
        if shape['closed'] or len(coords) < 3:
            continue
        sw = stroke_width if stroke_width is not None else shape['stroke_width']
        if not shape.get('non_scaling_stroke'):
            a, b, c, d, _, _ = shape.get('transform', _IDENTITY)
            sw *= math.sqrt(abs(a*d-b*c))
        min_y, max_y = min(y for x, y in coords), max(y for x, y in coords)
        x0, y0 = coords[0]
        x1, y1 = coords[-1]
        alignment = max(sw * 0.5, scale * 0.005)
        if abs(y0-y1) > alignment or max_y-min(y0, y1) > alignment:
            continue
        if max_y-min_y < max(sw * 1.5, scale * 0.01) or abs(x1-x0) < sw * 1.5:
            continue
        area = Polygon(coords)
        if not area.is_valid or area.area < sw * sw * 2:
            continue
        # Do not subdivide an opening already enclosed by other source paths
        # (for example a roof whose walls complete the outline).
        if area.difference(envelopes).area < sw * sw * 0.5:
            continue
        closed = dict(shape, closed=True, coords=[*coords, coords[0]])
        if 'source_coords' in shape:
            local = shape['source_coords']
            closed['source_coords'] = [*local, local[0]]
        if 'native_path' in shape:
            closed['native_path'] = pathops.Path(shape['native_path'])
            closed['native_path'].close()
        closed_shapes[-1] = closed
        closures.append({'edge': 'bottom', 'shape': shape.get('source_id'),
                         'from': [x0, y0], 'to': [x1, y1]})
    return closed_shapes, closures


def adjacency_distance(viewbox, override=None):
    """Keep the former 70/1024 proportion in the input's coordinate units."""
    if isinstance(viewbox, str):
        viewbox = _parse_viewbox(viewbox)
    distance = max(viewbox[2:]) * (70 / 1024) if override is None else override
    if not math.isfinite(distance) or distance < 0:
        raise ValueError('Adjacency buffer must be finite and non-negative')
    return distance


def load_one(svg_path, stroke_width=None, edge_close=False):
    """Parse a single raw SVG → stroke-to-polygon → dict with polygon + metadata.

    Args:
        svg_path: path to the raw stroke-based SVG file
        stroke_width: optional override; default uses each shape's SVG stroke width

    Returns:
        dict with: file, filename, viewbox, num_shapes, polygon
    """
    if stroke_width is not None and (not math.isfinite(stroke_width) or stroke_width <= 0):
        raise ValueError('Stroke width override must be finite and positive')
    root, viewbox, shapes = parse_all_shapes(svg_path, include_fills=True)
    closures = []
    if edge_close:
        shapes, closures = close_open_bottoms(shapes, viewbox, stroke_width)
    stroke_polygon = stroke_to_polygon(shapes, viewbox, stroke_width) if shapes else None
    filled = [s['geometry'] for s in shapes if s.get('kind') == 'fill']
    filled_polygon = unary_union(filled) if filled else None
    parts = [p for p in (stroke_polygon, filled_polygon) if p is not None and not p.is_empty]
    polygon = unary_union(parts) if parts else None
    viewbox_str = f"({viewbox[0]}, {viewbox[1]}, {viewbox[2]}, {viewbox[3]})" if len(viewbox) >= 4 else "(0, 0, 1024, 1024)"

    return {
        'file': svg_path,
        'filename': os.path.basename(svg_path),
        'viewbox': viewbox_str,
        'num_shapes': len(shapes),
        'polygon': polygon,
        'stroke_polygon': stroke_polygon,
        'filled_polygon': filled_polygon,
        'shapes': [s for s in shapes if s.get('kind') != 'fill'],
        'filled_shapes': [s for s in shapes if s.get('kind') == 'fill'],
        'closures': closures,
        'closed_edges': [c['edge'] for c in closures],
        'width': root.get('width', f'{viewbox[2]:g}'),
        'height': root.get('height', f'{viewbox[3]:g}'),
    }


def load(path=DEFAULT_INPUT_DIR, stroke_width=None, filter_ids_file=None, algo_filter=None,
         edge_close=False, recursive=False):
    """Load raw SVGs, parse and buffer into polygons → DataFrame.

    Args:
        path: SVG file or directory of SVGs (default: assets_todo_svg_1024_60)
        stroke_width: optional stroke-width override (default: source SVG widths)
        filter_ids_file: optional JSON file with list of {id:...} to filter SVGs
        algo_filter: optional algo_type value to keep (e.g. 'smart_fill_v2');
                     only items matching this algo_type are included

    Returns:
        DataFrame with columns: file, filename, viewbox, num_shapes, polygon
    """
    if os.path.isfile(path) and path.endswith('.svg'):
        svg_files = [path]
    elif os.path.isdir(path):
        pattern = os.path.join(path, '**', '*.svg') if recursive else os.path.join(path, '*.svg')
        svg_files = sorted(glob.glob(pattern, recursive=recursive))
    else:
        print(f"Error: {path} not found")
        return pd.DataFrame()

    if not svg_files:
        print(f"No SVG files found in {path}")
        return pd.DataFrame()

    # Filter by IDs if provided; also build per-file algo map
    algo_map = {}  # id → algo_type
    if filter_ids_file and os.path.exists(filter_ids_file):
        with open(filter_ids_file, 'r') as f:
            filter_data = json.load(f)
        if algo_filter:
            filter_data = [item for item in filter_data
                           if item.get('algo_type') == algo_filter]
        filter_ids = {item['id'] for item in filter_data}
        for item in filter_data:
            if 'algo_type' in item:
                algo_map[item['id']] = item['algo_type']
        svg_files = [p for p in svg_files
                     if os.path.splitext(os.path.basename(p))[0] in filter_ids]
        print(f"Filtered to {len(svg_files)} SVGs from {len(filter_ids)} IDs"
              + (f" (algo_type={algo_filter})" if algo_filter else ""))

    total = len(svg_files)
    rows = []
    for idx, svg_path in enumerate(svg_files, 1):
        if idx % 100 == 0 or idx == total:
            print(f"  Loading: {idx}/{total} ({idx*100//total}%)", flush=True)
        try:
            row = load_one(svg_path, stroke_width, edge_close=edge_close)
            # Attach per-file algo_type from JSON if available
            file_id = os.path.splitext(os.path.basename(svg_path))[0]
            row['algo_type'] = algo_map.get(file_id)
            rows.append(row)
        except Exception as e:
            print(f"  Skip {os.path.basename(svg_path)}: {e}")

    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Polygon helpers
# ---------------------------------------------------------------------------

def to_polys(polygon):
    """Normalize Polygon/MultiPolygon to list of Polygons."""
    if polygon is None:
        return []
    if isinstance(polygon, MultiPolygon):
        return list(polygon.geoms)
    if isinstance(polygon, Polygon):
        return [polygon]
    return []


# ---------------------------------------------------------------------------
# Build region DataFrame
# ---------------------------------------------------------------------------

def _compute_adjacency_df(regions_df, buffer_dist):
    """Compute adjacency between hole regions by buffering and checking overlap.

    Updates the 'adjacent_to' column in-place.
    """
    if buffer_dist <= 0:
        return

    holes = regions_df[regions_df.ring == 'hole']
    if len(holes) < 2:
        return

    # Buffer all hole geometries
    buffered = {rid: row.geometry.buffer(buffer_dist) for rid, row in holes.iterrows()}

    hole_ids = list(holes.index)
    for i in range(len(hole_ids)):
        for j in range(i + 1, len(hole_ids)):
            ri, rj = hole_ids[i], hole_ids[j]
            if buffered[ri].intersects(buffered[rj]):
                regions_df.at[ri, 'adjacent_to'].add(rj)
                regions_df.at[rj, 'adjacent_to'].add(ri)


def build_region_dataframe(polygon, buffer_dist=70):
    """Walk polygon nesting → one row per region as a DataFrame.

    Every sub-polygon and every hole at every nesting level becomes a row:

    region_id | geometry | level | ring     | area   | parent_id | has_children | adjacent_to | pct_of_parent | fill
    ----------|----------|-------|----------|--------|-----------|--------------|-------------|---------------|-----
    0         | Poly()   | 1     | exterior | 50000  | None      | True         | set()       | None          | None
    1         | Poly()   | 2     | hole     | 8000   | 0         | True         | {2}         | 16.0          | None

    Odd levels (1, 3, 5...) = exterior (solid regions).
    Even levels (2, 4, 6...) = hole (fill candidates).

    Args:
        polygon: Shapely Polygon or MultiPolygon (step 1 output)
        buffer_dist: distance for adjacency detection between holes

    Returns:
        pd.DataFrame with columns: region_id, geometry, level, ring, area,
                                    parent_id, has_children, adjacent_to,
                                    pct_of_parent, fill
    """
    polys = to_polys(polygon)
    if not polys:
        return pd.DataFrame(columns=[
            'region_id', 'geometry', 'level', 'ring', 'area',
            'parent_id', 'has_children', 'adjacent_to', 'pct_of_parent', 'fill',
        ])

    rows = []
    next_id = 0

    def _walk(geom_list, level, parent_id, parent_area):
        """Recursively walk polygon nesting.

        At each level:
          - Odd level: each Polygon exterior is a solid region
          - Even level: each hole (interior ring) is an empty region
        """
        nonlocal next_id

        for poly in geom_list:
            if not isinstance(poly, Polygon) or poly.is_empty:
                continue

            # This polygon's exterior = a solid region at this level
            ext_id = next_id
            next_id += 1
            ext_area = poly.area  # includes holes
            full_area = ext_area + sum(Polygon(i).area for i in poly.interiors)
            pct = (full_area / parent_area * 100) if parent_area and parent_area > 0 else None

            rows.append({
                'region_id': ext_id,
                'geometry': poly,
                'level': level,
                'ring': 'exterior',
                'area': full_area,
                'parent_id': parent_id,
                'has_children': len(poly.interiors) > 0,
                'adjacent_to': set(),
                'pct_of_parent': pct,
                'fill': None,
            })

            # Each hole = an empty region at level+1
            for interior in poly.interiors:
                hole_poly = Polygon(interior)
                hole_id = next_id
                next_id += 1
                hole_area = hole_poly.area
                hole_pct = (hole_area / full_area * 100) if full_area > 0 else 0

                # Check if any other top-level polys are nested inside this hole
                children_in_hole = []
                for other in polys:
                    if other is poly:
                        continue
                    if hole_poly.contains(other.representative_point()):
                        children_in_hole.append(other)

                rows.append({
                    'region_id': hole_id,
                    'geometry': hole_poly,
                    'level': level + 1,
                    'ring': 'hole',
                    'area': hole_area,
                    'parent_id': ext_id,
                    'has_children': len(children_in_hole) > 0,
                    'adjacent_to': set(),
                    'pct_of_parent': hole_pct,
                    'fill': None,
                })

                # Recurse into children nested inside this hole
                if children_in_hole:
                    _walk(children_in_hole, level + 2, hole_id, hole_area)

    # Start: level 1 exteriors — only top-level polys (not nested inside another)
    # Find which polys are "top-level" (not contained in any other poly's hole)
    nested_indices = set()
    for pi, poly in enumerate(polys):
        for pj, other in enumerate(polys):
            if pi == pj:
                continue
            for interior in other.interiors:
                hole_poly = Polygon(interior)
                if hole_poly.contains(poly.representative_point()):
                    nested_indices.add(pi)

    top_level = [p for i, p in enumerate(polys) if i not in nested_indices]
    _walk(top_level, level=1, parent_id=None, parent_area=None)

    df = pd.DataFrame(rows)
    if df.empty:
        return df

    df = df.set_index('region_id', drop=False)

    # Compute adjacency between holes
    _compute_adjacency_df(df, buffer_dist)

    return df


# ---------------------------------------------------------------------------
# SVG output
# ---------------------------------------------------------------------------

def _format_coord(val):
    value = f'{val:.6f}'.rstrip('0').rstrip('.')
    return '0' if value in ('', '-0') else value


def _polygon_to_path_d(poly):
    parts = []
    coords = list(poly.exterior.coords)
    if coords:
        parts.append(f"M {_format_coord(coords[0][0])},{_format_coord(coords[0][1])}")
        for x, y in coords[1:]:
            parts.append(f"L {_format_coord(x)},{_format_coord(y)}")
    for interior in poly.interiors:
        coords = list(interior.coords)
        if coords:
            parts.append(f"M {_format_coord(coords[0][0])},{_format_coord(coords[0][1])}")
            for x, y in coords[1:]:
                parts.append(f"L {_format_coord(x)},{_format_coord(y)}")
    return " ".join(parts)


def geometry_to_svg(geometry, viewbox_str, width=None, height=None):
    """Convert a Shapely geometry to a complete SVG string."""
    vb = tuple(float(x) for x in viewbox_str.strip('()').replace(',', ' ').split())
    vb_str = f"{vb[0]} {vb[1]} {vb[2]} {vb[3]}" if len(vb) >= 4 else "0 0 1024 1024"

    polys = to_polys(geometry)
    path_parts = [_polygon_to_path_d(p) for p in polys]
    path_d = " ".join(path_parts)
    from xml.sax.saxutils import quoteattr
    width = quoteattr(str(width if width is not None else f'{vb[2]:g}'))
    height = quoteattr(str(height if height is not None else f'{vb[3]:g}'))

    return (f"<?xml version='1.0' encoding='utf-8'?>\n"
            f"<svg xmlns=\"http://www.w3.org/2000/svg\" "
            f"width={width} height={height} viewBox=\"{vb_str}\">\n"
            f"  <path d=\"{path_d}\" fill=\"#000000\" fill-rule=\"nonzero\" />\n"
            f"</svg>")


# ---------------------------------------------------------------------------
# Edge closing
# ---------------------------------------------------------------------------

def _parse_viewbox(viewbox_str):
    """Parse viewbox string like '(0.0, 0.0, 1024.0, 1024.0)' → (x, y, w, h)."""
    return tuple(float(x) for x in viewbox_str.strip('()').replace(',', ' ').split())[:4]


def close_open_edges(polygon, viewbox_str, edge_threshold=None):
    """Close open shapes near viewbox edges.

    Detects sub-polygons with disconnected "fingers" near a viewbox edge
    and closes them by adding a connecting strip along the edge.

    Args:
        polygon: Shapely Polygon or MultiPolygon
        viewbox_str: viewbox string like "(0, 0, 1024, 1024)"
        edge_threshold: max distance from polygon extent to viewbox edge
                        (default: 6% of max viewbox dim)

    Returns (new_polygon, closed_edges_list).
    """
    vb_x, vb_y, vb_w, vb_h = _parse_viewbox(viewbox_str)

    if edge_threshold is None:
        edge_threshold = max(vb_w, vb_h) * 0.06

    probe_offset = max(max(vb_w, vb_h) * 5 / 1024, edge_threshold * 0.4)
    closing_depth = edge_threshold * 0.5

    polys = to_polys(polygon)
    closings = []
    closed_edges = []

    for poly in polys:
        minx, miny, maxx, maxy = poly.bounds
        checks = []

        vb_bottom = vb_y + vb_h

        # Bottom edge
        if vb_bottom - maxy < edge_threshold:
            edge_y = min(maxy, vb_bottom)
            py = edge_y - probe_offset
            margin = max(vb_w, vb_h) / 1024
            probe = LineString([(minx - margin, py), (maxx + margin, py)])
            checks.append(('bottom', probe, 'x',
                            lambda xs, _ey=edge_y: shapely_box(
                                min(xs), _ey - closing_depth, max(xs), _ey)))

        for edge_name, probe, span_axis, make_closing in checks:
            intersection = poly.intersection(probe)
            if intersection.is_empty:
                continue

            if intersection.geom_type == 'LineString':
                continue
            if intersection.geom_type != 'MultiLineString':
                continue

            segments = list(intersection.geoms)
            if len(segments) < 2:
                continue

            if span_axis == 'x':
                coords_per_seg = [
                    (min(c[0] for c in seg.coords), max(c[0] for c in seg.coords))
                    for seg in segments
                ]
            else:
                coords_per_seg = [
                    (min(c[1] for c in seg.coords), max(c[1] for c in seg.coords))
                    for seg in segments
                ]

            coords_per_seg.sort()
            max_gap = 0
            for i in range(len(coords_per_seg) - 1):
                gap = coords_per_seg[i + 1][0] - coords_per_seg[i][1]
                max_gap = max(max_gap, gap)

            if max_gap < edge_threshold * 0.5:
                continue

            all_vals = []
            for lo, hi in coords_per_seg:
                all_vals.extend([lo, hi])
            closing = make_closing(all_vals)
            closings.append(closing)
            closed_edges.append(edge_name)

    if closings:
        result = unary_union(list(polys) + closings)
        return result, closed_edges
    return polygon, closed_edges


# ---------------------------------------------------------------------------
# Assemble output polygon from DataFrame
# ---------------------------------------------------------------------------

def _build_filled_hole(df, hole_row):
    """Build a solid polygon from a filled hole, recursively handling nested
    cutouts and deeper flip fills.

    When a hole is filled, its children (exteriors) marked 'cutout' are
    subtracted.  Inside each cutout, grandchild holes marked 'fill' are
    added back — and this process repeats recursively for arbitrary depth.

    Returns a list of Shapely Polygons.
    """
    hole_poly = Polygon(hole_row.geometry.exterior)
    children = df[(df.parent_id == hole_row.region_id) & (df.ring == 'exterior')]

    cutout_geoms = []
    flip_parts = []

    for _, child_row in children.iterrows():
        if child_row.fill == 'cutout':
            # Build cutout polygon: preserve 'keep' holes, discard 'cutout'/'fill'
            grandchildren = df[(df.parent_id == child_row.region_id) & (df.ring == 'hole')]
            kept_holes = []
            for _, gc_row in grandchildren.iterrows():
                if gc_row.fill == 'keep':
                    kept_holes.append(gc_row.geometry.exterior)
                elif gc_row.fill == 'fill':
                    flip_parts.extend(_build_filled_hole(df, gc_row))
                # 'cutout' holes → not preserved (included in subtracted area)

            cutout = Polygon(child_row.geometry.exterior, kept_holes)
            cutout_geoms.append(cutout)

    # Subtract cutouts from the hole polygon
    for cutout in cutout_geoms:
        hole_poly = hole_poly.difference(cutout)

    parts = []
    if not hole_poly.is_empty:
        if isinstance(hole_poly, MultiPolygon):
            parts.extend(hole_poly.geoms)
        else:
            parts.append(hole_poly)

    # Add back recursive flip fills
    parts.extend(p for p in flip_parts if not p.is_empty)

    return parts


def assemble_polygon(df):
    """Read the 'fill' column → build output Shapely polygon.

    For each level-1 exterior:
      - fill='drop' → skip the exterior entirely; holes marked 'fill' become
        standalone solid polygons (with cutout children subtracted)
      - fill='keep' (normal mode):
        - Holes marked 'fill' → removed (filled in)
        - Holes marked 'keep' → kept as holes
        - Children inside filled holes → subtracted as cutouts (recursively)

    Returns a Shapely Polygon or MultiPolygon.
    """
    if df.empty:
        return None

    result_parts = []

    # Process each level-1 exterior
    level1 = df[(df.level == 1) & (df.ring == 'exterior')]
    for _, ext_row in level1.iterrows():
        ext_id = ext_row.region_id
        poly = ext_row.geometry

        # Get this exterior's holes (level 2)
        holes = df[(df.parent_id == ext_id) & (df.ring == 'hole')]

        if ext_row.fill == 'drop':
            # Border dropped — each filled hole becomes a standalone polygon
            for _, hole_row in holes.iterrows():
                if hole_row.fill != 'fill':
                    continue
                parts = _build_filled_hole(df, hole_row)
                result_parts.extend(parts)
            continue

        kept_interiors = []
        cutout_geoms = []
        flip_fill_parts = []

        for _, hole_row in holes.iterrows():
            if hole_row.fill == 'keep':
                # Keep hole as-is
                kept_interiors.append(hole_row.geometry.exterior)
            elif hole_row.fill == 'fill':
                # Hole is filled — find children to cut out (recursively)
                children = df[(df.parent_id == hole_row.region_id) & (df.ring == 'exterior')]
                for _, child_row in children.iterrows():
                    if child_row.fill == 'cutout':
                        # Build cutout: preserve 'keep' holes, discard 'cutout'/'fill'
                        grandchildren = df[(df.parent_id == child_row.region_id) & (df.ring == 'hole')]
                        kept_holes = []
                        for _, gc_row in grandchildren.iterrows():
                            if gc_row.fill == 'keep':
                                kept_holes.append(gc_row.geometry.exterior)
                            elif gc_row.fill == 'fill':
                                flip_fill_parts.extend(_build_filled_hole(df, gc_row))
                            # 'cutout' → not preserved
                        cutout_geoms.append(Polygon(child_row.geometry.exterior, kept_holes))
            # else: also fill (default)

        # Rebuild polygon with only kept holes
        new_poly = Polygon(poly.exterior, kept_interiors)
        result_parts.append(new_poly)

        # Subtract cutouts
        for cutout in cutout_geoms:
            result_parts_new = []
            for part in result_parts:
                diff = part.difference(cutout)
                if not diff.is_empty:
                    if isinstance(diff, MultiPolygon):
                        result_parts_new.extend(diff.geoms)
                    else:
                        result_parts_new.append(diff)
            result_parts = result_parts_new

        # Add back flip fills (recursively built)
        result_parts.extend(p for p in flip_fill_parts if not p.is_empty)

    if not result_parts:
        return None

    result = unary_union(result_parts)
    return result
