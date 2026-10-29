"""Source selection, native SVG paint and transparent geometry serialization."""
import copy
import hashlib
import math
import xml.etree.ElementTree as ET
import pathops

from shapely.geometry import Polygon, GeometryCollection
from shapely.ops import unary_union
from svgpathtools import parse_path, Line, Path

from ..vendor import fill_utils as fu

NS = '{http://www.w3.org/2000/svg}'
LEAVES = {'path', 'line', 'rect', 'circle', 'ellipse', 'polyline', 'polygon'}
DEFINITIONS = {'defs', 'clipPath', 'mask', 'pattern', 'symbol', 'marker'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def leaves(root):
    """Historical leaf:n convention: drawing leaves only, excluding definitions."""
    result = []
    def walk(e):
        tag = fu._local_tag(e.tag)
        if tag in DEFINITIONS:
            return
        if tag == 'use':
            raise ValueError('use elements require explicit ownership mapping')
        if tag in LEAVES:
            result.append(e)
        for child in e:
            walk(child)
    walk(root)
    return result


def validate_source(root):
    fu._inline_svg_styles(root)
    vb = [float(x) for x in root.get('viewBox', '').replace(',', ' ').split()]
    if vb != [0, 0, 48, 48]:
        raise ValueError('This treatment version requires a 0 0 48 48 viewBox')
    parents = fu._build_parent_map(root)
    for e in root.iter():
        if e.get('mask') or e.get('filter'):
            raise ValueError('Masks and filters require explicit treatment')
        for key in ('opacity', 'fill-opacity', 'stroke-opacity'):
            if float(e.get(key, '1')) != 1:
                raise ValueError('Partial opacity requires explicit treatment')
    for e in leaves(root):
        for key in ('fill', 'stroke'):
            value = fu._resolve_attr(e, key, parents, 'black' if key == 'fill' else 'none').lower()
            if value in {'white', '#fff', '#ffffff'} or value.startswith(('rgb', 'hsl')):
                raise ValueError('Paint-order color overlays require explicit treatment')
    return vb


def subset(root, selectors):
    tree = copy.deepcopy(root)
    items = leaves(tree)
    allowed = {'leaf:' + str(i) for i in range(len(items))}
    if not selectors or len(set(selectors)) != len(selectors) or not set(selectors) <= allowed:
        raise ValueError('Invalid or duplicate source element selectors')
    for i, e in enumerate(items):
        if 'leaf:' + str(i) not in selectors:
            e.set('display', 'none')
            e.set('style', 'display:none!important')
    return tree


def paint(root, destination):
    ET.ElementTree(root).write(destination, encoding='unicode')
    _, vb, shapes = fu.parse_all_shapes(destination, include_fills=True)
    parts = []
    for shape in shapes:
        if shape.get('kind') == 'fill':
            parts.append(shape['geometry'])
            continue
        if 'native_path' not in shape:
            fallback = fu.stroke_to_polygon([shape], vb)
            if fallback is not None:
                parts.append(fallback)
            continue
        # Same native expansion as the corrected vendor engine, without its
        # preview-sized simplification: fixed .001 gaps need tighter geometry.
        native = pathops.Path(shape['native_path'])
        matrix = shape.get('transform', fu._IDENTITY)
        if shape.get('non_scaling_stroke'):
            native = native.transform(*matrix)
            matrix = fu._IDENTITY
        native = native.transform(16, 0, 0, 16)
        native.stroke(shape['stroke_width']*16,
            {'round': pathops.LineCap.ROUND_CAP, 'square': pathops.LineCap.SQUARE_CAP}.get(shape['cap'], pathops.LineCap.BUTT_CAP),
            {'round': pathops.LineJoin.ROUND_JOIN, 'bevel': pathops.LineJoin.BEVEL_JOIN}.get(shape['join'], pathops.LineJoin.MITER_JOIN),
            shape.get('miter_limit', 4))
        native.convertConicsToQuads(.016)
        native.simplify()
        native = native.transform(1/16, 0, 0, 1/16).transform(*matrix)
        expanded = fu._native_geometry(native, .0001)
        if shape.get('clip_geometry') is not None:
            expanded = expanded.intersection(shape['clip_geometry'])
        parts.append(expanded)
    geom = unary_union(parts)
    if geom is None or geom.is_empty or not geom.is_valid:
        raise ValueError('Selected source has no valid visible paint')
    return geom


def faces(paint_geometry):
    # Subtract all original paint so nested solid details remain holes when reversed.
    holes = [Polygon(hole) for polygon in fu.to_polys(paint_geometry) for hole in polygon.interiors]
    return fu.to_polys(unary_union(holes).difference(paint_geometry))


NUMERIC_COMPONENT_AREA = 1e-10
MAX_NUMERIC_REMOVAL_AREA = 1e-8


def clean(geometry, audit=None):
    """Keep polygonal material, removing only disconnected numerical zero areas.

    Boolean intersection can leave a collinear polygon with area ~1e-14; it has
    no representable SVG surface but can inflate the bounds/topology before
    export. Merge polygonal parts FIRST so a small connecting piece cannot be
    mistaken for a disconnected component. Never remove holes or components
    with holes. This is not a visual small-detail filter (eyes and dots are many
    orders of magnitude larger), and does not rescue thin rim fragments above
    the strict numerical threshold.
    """
    def parts(value):
        if value.is_empty:return []
        if value.geom_type=='GeometryCollection':
            return [polygon for child in value.geoms for polygon in parts(child)]
        return fu.to_polys(value)
    polygonal=unary_union(parts(geometry))
    polygons=fu.to_polys(polygonal)
    removed=[p for p in polygons if p.area<NUMERIC_COMPONENT_AREA and not p.interiors]
    discarded_area=sum(p.area for p in removed)
    if discarded_area>MAX_NUMERIC_REMOVAL_AREA:
        raise ValueError('Numerical zero-area components exceed cleanup budget; repair source operation')
    retained=[p for p in polygons if p.area>=NUMERIC_COMPONENT_AREA or p.interiors]
    if audit is not None and removed:
        audit.append({'operation':'remove_numeric_zero_area_components',
            'maximum_component_area_exclusive':NUMERIC_COMPONENT_AREA,
            'discarded_component_count':len(removed),'discarded_area':discarded_area,
            'maximum_total_removal_area':MAX_NUMERIC_REMOVAL_AREA,
            'discarded_bounds':[list(p.bounds) for p in removed],
            'holes_removed':0})
    return unary_union(retained)


def topology(g):
    polygons = fu.to_polys(g)
    return {'components': len(polygons), 'holes': sum(len(p.interiors) for p in polygons)}


def serialize(g):
    def ring(r):
        points = list(r.coords)[:-1]
        # Six decimals can sever a narrow contact between native expanded curves
        # before Skia's float representation sees it. Nine preserves observed
        # source contacts; final exported topology/bounds are still validated.
        return 'M' + 'L'.join(f'{x:.9f},{y:.9f}' for x, y in points) + 'Z'
    d = ''.join(ring(r) for p in fu.to_polys(g) for r in [p.exterior, *p.interiors])
    root = ET.Element(NS+'svg', viewBox='0 0 48 48', width='48', height='48', fill='currentColor', stroke='none')
    ET.SubElement(root, NS+'path', {'d': d, 'fill-rule': 'evenodd'})
    return ET.tostring(root, encoding='unicode')


def read_export(path):
    """Measure serialized output at tighter precision than preview rasterization."""
    root = ET.parse(path).getroot()
    parts = []
    for e in root:
        if fu._local_tag(e.tag) != 'path':
            continue
        native = fu._native_path(e)
        native.fillType = pathops.FillType.EVEN_ODD
        parts.append(fu._native_geometry(native, .00001))
    return unary_union(parts)


def extend_straight(root, selectors, endpoint, target_bounds):
    """Extend a single source line in canvas space; preserve its local paint/transform."""
    if len(selectors) != 1 or endpoint not in {'start', 'end'}:
        raise ValueError('Extension needs one straight element and start/end endpoint')
    e = leaves(root)[int(selectors[0].split(':')[1])]
    tag = fu._local_tag(e.tag)
    if tag == 'path':
        path = parse_path(e.get('d', ''))
    elif tag == 'line':
        path = Path(Line(complex(float(e.get('x1', 0)), float(e.get('y1', 0))),
                         complex(float(e.get('x2', 0)), float(e.get('y2', 0)))))
    else:
        raise ValueError('Extension supports a straight path or line only')
    if len(path) != 1 or not isinstance(path[0], Line) or path[0].length() < 1e-9:
        raise ValueError('Curved or compound opening extensions need a separate decision')
    parents = fu._build_parent_map(root)
    chain, node = [], e
    while node is not None:
        chain.append(node)
        node = parents.get(node)
    matrix = (1, 0, 0, 1, 0, 0)
    for node in reversed(chain):
        matrix = fu._compose(matrix, fu._parse_transform(node.get('transform', '')))
    a, b, c, d, tx, ty = matrix
    determinant = a*d-b*c
    if abs(determinant) < 1e-12:
        raise ValueError('Singular transform on opening stroke')
    def canvas(z):
        return complex(a*z.real+c*z.imag+tx, b*z.real+d*z.imag+ty)
    original = path[0]
    point = canvas(original.start if endpoint == 'start' else original.end)
    other = canvas(original.end if endpoint == 'start' else original.start)
    direction = (point-other)/abs(point-other)
    xmin, ymin, xmax, ymax = target_bounds
    if not xmin-1e-6 <= point.real <= xmax+1e-6 or not ymin-1e-6 <= point.imag <= ymax+1e-6:
        raise ValueError('Opening endpoint is outside the target bounds')
    distances = [((hi if step > 0 else lo)-coordinate)/step
                 for coordinate, step, lo, hi in [(point.real, direction.real, xmin, xmax),
                                                  (point.imag, direction.imag, ymin, ymax)] if abs(step) > 1e-12]
    # A full target diagonal clears the exterior even for square/round end caps.
    distance = min(v for v in distances if v >= -1e-6) + math.hypot(xmax-xmin, ymax-ymin)
    end = point+direction*distance
    x, y = end.real-tx, end.imag-ty
    local = complex((d*x-c*y)/determinant, (-b*x+a*y)/determinant)
    if tag == 'path':
        e.set('d', Path(Line(local, original.end) if endpoint == 'start' else Line(original.start, local)).d())
    else:
        n = '1' if endpoint == 'start' else '2'
        e.set('x'+n, str(local.real)); e.set('y'+n, str(local.imag))
    return {'endpoint': endpoint, 'original_canvas_point': [point.real, point.imag],
            'extended_canvas_point': [end.real, end.imag], 'extension_distance': distance}
