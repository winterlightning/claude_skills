"""Resolution-independent container geometry, in SVG viewBox units.

Curves use the shared adaptive Hausdorff-bounded subdivision engine. GEOS
performs continuous segment distances and polygon operations, never raster masks.
Round buffers have inner/outer enclosures including curve and tessellation error.
"""
from dataclasses import dataclass
import math
import re
import xml.etree.ElementTree as ET
from cairosvg.parser import Tree
from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import unary_union, nearest_points
from icon_set.scripts.container_placement import Artwork, paths_as_commands
from icon_set.validation.stroke_distance import _contours, _Budget

TOLERANCE = 0.0005
GUARD = 1e-8  # Numerical allowance for 64-unit GEOS operations; not interval arithmetic.
QUAD_SEGS = 128
PADDING = 2.0
CANVAS = box(0, 0, 64, 64)


@dataclass
class VectorInk:
    lines: object
    error: float

    @classmethod
    def from_art(cls, art, transform=(1, 0, 0)):
        contours = _contours(paths_as_commands(art, 'ink', transform), TOLERANCE, _Budget())
        lines = []
        for contour in contours:
            # Keep contours intact to avoid a buffer circle at every subdivision.
            coords = [contour.segments[0].a] + [s.b for s in contour.segments]
            lines.append(Point(coords[0]) if len(set(coords)) == 1 else LineString(coords))
        return cls(unary_union(lines), max(c.error for c in contours))

    def envelope(self, radius, outer):
        # GEOS round buffers inscribe circular arcs. Circumscribe them for an
        # outer bound; the uninflated inscribed buffer provides the inner bound.
        r = radius + self.error + GUARD if outer else radius - self.error - GUARD
        if r <= 0:
            raise ValueError('Radius smaller than geometry error budget')
        if outer:
            r /= math.cos(math.pi / (4 * QUAD_SEGS))
        return self.lines.buffer(r, quad_segs=QUAD_SEGS)


def polygons(g):
    if g.geom_type == 'Polygon':
        return [g]
    return [p for p in getattr(g, 'geoms', []) if p.geom_type == 'Polygon']


def selected_face(free, reference):
    candidates = [p for p in polygons(free) if p.distance(CANVAS.boundary) > GUARD]
    if not candidates:
        return None
    face = max(candidates, key=lambda p: p.intersection(reference).area)
    return face if face.intersection(reference).area > 0 else None


def vector_zone(ink, area):
    if area.get('kind') == 'center-only':
        return {'status': 'overlay', 'reason': 'Intentional overlay; no containment area.'}, None, None
    if area.get('method') != 'selected semantic enclosed face':
        return {'status': 'review', 'reason': 'An explicit vector boundary is needed for this manually selected interior.'}, None, None
    reference = Polygon(area['polygon'])
    if not reference.is_valid:
        raise ValueError('Invalid saved semantic selector')
    # The legacy polygon ONLY chooses a face; none of its edges are retained.
    inner = selected_face(CANVAS.difference(ink.envelope(4, True)), reference)
    outer = selected_face(CANVAS.difference(ink.envelope(4, False)), reference)
    if inner is None or outer is None or not outer.covers(inner):
        return {'status': 'review', 'reason': 'No stable enclosed vector face matches the selected interior.'}, None, None
    centroid = inner.centroid
    center = centroid if inner.covers(centroid) else inner.representative_point()
    return {'status': 'vector', 'reason': 'Enclosed face selected using the previous semantic area; boundary rebuilt from SVG paths.',
            'area_lower_units2': inner.area, 'area_upper_units2': outer.area,
            'center_units': [center.x, center.y], 'centroid_units': [centroid.x, centroid.y],
            'center_method': 'area centroid' if center == centroid else 'interior fallback (centroid outside)',
            'bounds_units': list(inner.bounds), 'curve_error_units': ink.error}, inner, outer


def check_pair(host, sub, zone_inner=None, zone_outer=None, *, padding=PADDING):
    if not math.isfinite(padding) or padding < 0:
        raise ValueError('Padding must be a finite nonnegative number.')
    distance = host.lines.distance(sub.lines)
    uncertainty = host.error + sub.error + GUARD
    lower, upper = max(0., distance - 4 - uncertainty), max(0., distance - 4 + uncertainty)
    gap_status = 'pass' if lower >= padding else ('fail' if upper < padding else 'review')
    sub_outer, sub_inner = sub.envelope(2, True), sub.envelope(2, False)
    if zone_inner is None:
        containment = 'review'
    elif zone_inner.covers(sub_outer):
        containment = 'pass'
    elif not zone_outer.covers(sub_inner):
        containment = 'fail'
    else:
        containment = 'review'
    canvas = 'pass' if CANVAS.covers(sub_outer) else ('fail' if not CANVAS.covers(sub_inner) else 'review')
    statuses = [gap_status, containment, canvas]
    a, b = nearest_points(host.lines, sub.lines)
    # Endpoints show the nearest stroke edges on the bounded approximation.
    dx, dy = b.x-a.x, b.y-a.y
    length = math.hypot(dx, dy)
    points = [[a.x, a.y], [b.x, b.y]]
    if length > 4:
        points = [[a.x+2*dx/length, a.y+2*dy/length], [b.x-2*dx/length, b.y-2*dy/length]]
    return {'status': 'fail' if 'fail' in statuses else ('pass' if all(s == 'pass' for s in statuses) else 'review'),
            'gap_status': gap_status, 'containment_status': containment, 'canvas_status': canvas,
            'ink_gap_lower_units': lower, 'ink_gap_upper_units': upper,
            'ink_gap_estimate_units': max(0., distance-4), 'nearest_edge_points_units': points}


def reject_effects(document):
    root = ET.fromstring(document)
    unsupported = {'clip-path', 'mask', 'filter', 'stroke-dasharray', 'stroke-dashoffset',
                   'vector-effect', 'display', 'visibility', 'marker-start', 'marker-mid', 'marker-end'}
    for node in root.iter():
        if node.tag.rsplit('}', 1)[-1] in ('style', 'use', 'image', 'text'):
            raise ValueError('Unsupported SVG painting feature')
        if unsupported.intersection(node.attrib) or any(k in node.get('style', '') for k in unsupported):
            raise ValueError('Unsupported SVG paint effect')
    return root


def read_art(document):
    reject_effects(document)
    return Artwork.read(document, 64)


def pair_groups(document):
    """Read the saved pair's actual placement, not an inferred centered transform."""
    root = reject_effects(document)
    if root.get('transform') or root.get('viewBox') != '0 0 64 64':
        raise ValueError('Unsupported pair canvas')
    groups = {}
    for node in root:
        tag = node.tag.rsplit('}', 1)[-1]
        if tag in ('title', 'desc', 'metadata'):
            continue
        if tag != 'g' or node.get('id') not in ('container', 'content') or node.get('id') in groups:
            raise ValueError('Unexpected pair structure')
        match = re.fullmatch(r'translate\(([-+\d.eE]+)[ ,]+([-+\d.eE]+)\)\s*scale\(([-+\d.eE]+)\)', node.get('transform', ''))
        if not match:
            raise ValueError('Unsupported pair transform')
        dx, dy, scale = map(float, match.groups())
        if not all(math.isfinite(n) for n in (dx, dy, scale)) or not 0 < scale <= 10:
            raise ValueError('Invalid transform')
        for child in node.iter():
            if child is not node and child.get('transform'):
                raise ValueError('Nested pair transform')
        isolated = ET.Element('svg', dict(root.attrib))
        isolated.append(node)
        normalized = ET.Element('svg', {'viewBox': '0 0 64 64', 'fill': 'none', 'stroke': 'black',
                                      'stroke-width': '4', 'stroke-linecap': 'round', 'stroke-linejoin': 'round'})
        def walk(n):
            if float(n.get('opacity', 1)) != 1:
                raise ValueError('Transparent pair group')
            if n.tag in ('svg', 'g'):
                for c in n.children: walk(c)
            elif n.tag == 'path':
                if (abs(float(n.get('stroke-width', 0))*scale-4) > 1e-7 or n.get('fill') != 'none'
                    or n.get('stroke', 'none') == 'none' or n.get('stroke-linecap') != 'round'
                    or n.get('stroke-linejoin') != 'round' or float(n.get('stroke-opacity', 1)) != 1):
                    raise ValueError('Pair requires opaque round 4-unit strokes')
                ET.SubElement(normalized, 'path', {'d': n['d']})
            else:
                raise ValueError('Unsupported pair node')
        walk(Tree(bytestring=ET.tostring(isolated)))
        art = Artwork.read(ET.tostring(normalized, encoding='unicode'), 64)
        groups[node.get('id')] = (art, (scale, dx, dy))
    if set(groups) != {'container', 'content'}:
        raise ValueError('Missing pair group')
    return groups
