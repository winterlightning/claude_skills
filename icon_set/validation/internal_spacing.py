"""Review clearance between sustained opposing edges of connected geometry.

Sampled geometry is a review heuristic, not a certified distance measurement.
An unresolved finding prevents publication through library_qa. Adjacent
segments, common endpoints, endpoint neighbourhoods, and complete circular
contours are excluded. Circle diameter remains the hole check's responsibility.
"""
import html
import math

from ..model.primitives import Arc, Bezier, Line, Point
from ..model.profiles import STROKE_WIDTH
from .envelope import arc_geometry
from .circle_exceptions import circle_candidates
from ..renderers.svg import build_paths

RULES = {'version': 2, 'sample_step': 0.25, 'minimum_run': 2.0,
         'endpoint_margin': 0.5, 'maximum_parallel_angle_degrees': 30,
         'blocking': False, 'publication_requires_clear_review': True}


def _samples(primitive):
    import numpy as np
    step = RULES['sample_step']
    if isinstance(primitive, Line):
        a, b = np.array(primitive.start.as_tuple()), np.array(primitive.end.as_tuple())
        length = float(np.linalg.norm(b-a))
        points = np.linspace(a, b, max(2, math.ceil(length/step)+1))
    elif isinstance(primitive, Bezier):
        rough = primitive.sample(16)
        length = sum(math.dist(p, q) for p, q in zip(rough, rough[1:]))
        per = max(2, math.ceil(length/step/len(primitive.segments)))
        points = np.array(primitive.sample(per))
    else:
        arc = arc_geometry(primitive)
        count = max(2, math.ceil(abs(arc.delta_angle)*max(arc.radius_x, arc.radius_y)/step)+1)
        angles = np.linspace(arc.start_angle, arc.start_angle+arc.delta_angle, count)
        points = np.column_stack((arc.center_x+arc.radius_x*np.cos(angles), arc.center_y+arc.radius_y*np.sin(angles)))
    deltas = np.diff(points, axis=0)
    lengths = np.linalg.norm(deltas, axis=1)
    keep = lengths > 1e-12
    return points[:-1][keep], deltas[keep], lengths[keep]


def _run(first, second, required):
    import numpy as np
    a, da, la = first
    b, db, lb = second
    if not len(la) or not len(lb):
        return None
    mid = a + da/2
    t = np.clip(np.sum((mid[:,None,:]-b)*db, axis=2)/(lb*lb), 0, 1)
    nearest = b + t[:,:,None]*db
    displacement = nearest-mid[:,None,:]
    distances = np.linalg.norm(displacement, axis=2)
    indices = np.argmin(distances, axis=1)
    selected = np.arange(len(la))
    distance = distances[selected,indices]
    target = nearest[selected,indices]
    ta, tb = da/la[:,None], db[indices]/lb[indices,None]
    along_a = np.cumsum(la)-la/2
    along_b = (np.cumsum(lb)-lb)[indices]+t[selected,indices]*lb[indices]
    normal = (target-mid)/np.maximum(distance[:,None],1e-12)
    margin = RULES['endpoint_margin']
    valid = ((distance < required-1e-6)
             & (np.abs(np.sum(ta*tb,axis=1)) >= math.cos(math.radians(RULES['maximum_parallel_angle_degrees']))))
    valid &= (np.abs(np.sum(ta*normal,axis=1)) <= .5) & (np.abs(np.sum(tb*normal,axis=1)) <= .5)
    valid &= (along_a >= margin) & (along_a <= la.sum()-margin)
    valid &= (along_b >= margin) & (along_b <= lb.sum()-margin)
    best = None
    start = 0
    for end in range(len(valid)+1):
        if end < len(valid) and valid[end]:
            continue
        if end > start:
            span = float(la[start:end].sum())
            if span >= RULES['minimum_run']:
                index = start+int(np.argmin(distance[start:end]))
                item = {'sustained_length': round(span,4), 'centerline_distance': round(float(distance[index]),4),
                        'ink_gap': round(float(distance[index])-STROKE_WIDTH,4),
                        'nearest_points': [mid[index].tolist(),target[index].tolist()]}
                if best is None or item['sustained_length'] > best['sustained_length']:
                    best = item
        start = end+1
    return best


def _avatar_tangent_contact(icon, first, second, first_node, second_node, drawing):
    """Accept only the avatar's analytically verified circle/shoulder ink tangency."""
    if icon.family != 'solo' or icon.category != 'avatars':
        return False
    arc, line = (first, second) if isinstance(first, Arc) else (second, first)
    if not isinstance(arc, Arc) or not isinstance(line, Line):
        return False
    if arc.radius_x != arc.radius_y or line.start.y != line.end.y:
        return False
    if not line.element_id.startswith('body-top') and line.element_id != 'shoulder-top':
        return False
    geometry = arc_geometry(arc)
    from .envelope import centerline_bounds
    bottom = centerline_bounds([arc])[3]
    if abs(geometry.center_x - 24) > 1e-9 or abs(bottom - geometry.center_y - geometry.radius_y) > 1e-9:
        return False
    if abs(line.start.y - bottom - STROKE_WIDTH) > 1e-9:
        return False
    if not min(line.start.x, line.end.x) <= 24 <= max(line.start.x, line.end.x):
        return False
    return any(r.kind == 'connect' and {first_node, second_node}.issubset(r.members)
               for r in drawing.relationships)


def analyze_internal_spacing(icon, drawing):
    required = float(icon.profile.spec.equal_stroke_centerline_min)
    circular = {c['element_id'] for c in circle_candidates('<svg/>',drawing)}
    by_id = drawing.by_id()
    samples = {}
    findings = []
    # Resolve connected components without treating a contact as permission for
    # every distant edge of those parts to overlap. Local shared endpoints and
    # ordinary adjacent contour segments remain excluded.
    primitive_owner = {m: c.contour_id for c in drawing.contours for m in c.members}
    nodes = {c.contour_id: list(c.members) for c in drawing.contours}
    nodes.update({p.element_id: [p.element_id] for p in drawing.primitives
                  if p.element_id not in primitive_owner})
    parent = {name: name for name in nodes}
    def root(name):
        while parent[name] != name:
            name = parent[name]
        return name
    for relation in drawing.relationships:
        if relation.kind != 'connect':
            continue
        names = [primitive_owner.get(m, m) for m in relation.members]
        names = [n for n in names if n in parent]
        for name in names[1:]:
            parent[root(name)] = root(names[0])
    components = {}
    owners = {}
    adjacent = set()
    for node, names in nodes.items():
        parts = []
        for name in names:
            primitive = by_id[name]
            if isinstance(primitive, Bezier) and len(primitive.segments) > 1:
                for index, (p0, c1, c2, p3) in enumerate(primitive.cubics()):
                    key = (name, index)
                    parts.append(Bezier(key, Point(*p0), Point(*p3), ((c1,c2,p3),)))
                    owners[key] = name
            else:
                parts.append(primitive)
                owners[primitive.element_id] = name
        for first, second in zip(parts, parts[1:]):
            adjacent.add(frozenset((first.element_id, second.element_id)))
        if any(c.contour_id == node and c.closed for c in drawing.contours) and len(parts) > 1:
            adjacent.add(frozenset((parts[0].element_id, parts[-1].element_id)))
        components.setdefault(root(node), []).extend((node,p) for p in parts)
    for component in components.values():
        for i, (first_node, first) in enumerate(component):
            for second_node, second in component[i+1:]:
                if first_node == second_node and first_node in circular:
                    continue
                if frozenset((first.element_id,second.element_id)) in adjacent:
                    continue
                if {first.start,first.end} & {second.start,second.end}:
                    continue
                if _avatar_tangent_contact(icon, first, second, first_node, second_node, drawing):
                    continue
                for p in (first,second):
                    if p.element_id not in samples:
                        samples[p.element_id] = _samples(p)
                forward = _run(samples[first.element_id],samples[second.element_id],required)
                reverse = _run(samples[second.element_id],samples[first.element_id],required)
                choices = [r for r in (forward,reverse) if r]
                if not choices:
                    continue
                result = max(choices,key=lambda r:r['sustained_length'])
                if result is reverse:
                    result['nearest_points'].reverse()
                label = first_node if first_node == second_node else first_node + ' / ' + second_node
                findings.append({'contour':label,'elements':[owners[first.element_id],owners[second.element_id]],
                                 'status':'review', **result})
    return {'status':'review' if findings else 'pass', 'blocking':False,
            'required_ink_gap':float(icon.profile.spec.mic), 'rules':RULES,
            'findings':findings,
            'notice':'Sampled opposing-edge review; unresolved findings prevent publication. Ordinary joins and complete circular contours are excluded. Negative gap indicates overlapping ink.'}


def internal_overlay(icon,drawing,result):
    canvas = icon.profile.spec.canvas_size
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas}" height="{canvas}" viewBox="0 0 {canvas} {canvas}">',
           '<rect width="100%" height="100%" fill="white"/>']
    def path(d,color,width):
        out.append(f'<path d="{html.escape(d,quote=True)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')
    for p in build_paths(drawing):
        path(p['d'],'#cbd5e1',STROKE_WIDTH)
    from ..model.primitives import ResolvedDrawing
    flagged = {element for finding in result['findings'] for element in finding['elements']}
    for primitive in drawing.primitives:
        if primitive.element_id in flagged:
            path(build_paths(ResolvedDrawing((primitive,),(),(),()))[0]['d'],'#d97706',STROKE_WIDTH)
    for index,finding in enumerate(result['findings'],1):
        (x1,y1),(x2,y2) = finding['nearest_points']
        path(f'M{x1} {y1}L{x2} {y2}','#b91c1c',.5)
        out.append(f'<text x="{(x1+x2)/2}" y="{(y1+y2)/2}" font-size="2" fill="#7f1d1d">{index}</text>')
    return '\n'.join(out+['</svg>'])
