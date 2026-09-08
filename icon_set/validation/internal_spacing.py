"""Advisory clearance between sustained opposing edges of one contour.

Sampled geometry is a review heuristic, not a certified distance gate. Adjacent
segments, common endpoints, endpoint neighbourhoods, and complete circular
contours are excluded. Circle diameter remains the hole check's responsibility.
"""
import html
import math

from ..model.primitives import Line
from ..model.profiles import STROKE_WIDTH
from .envelope import arc_geometry
from .circle_exceptions import circle_candidates
from ..renderers.svg import build_paths

RULES = {'version': 1, 'sample_step': 0.25, 'minimum_run': 2.0,
         'endpoint_margin': 0.5, 'maximum_parallel_angle_degrees': 30,
         'blocking': False}


def _samples(primitive):
    import numpy as np
    step = RULES['sample_step']
    if isinstance(primitive, Line):
        a, b = np.array(primitive.start.as_tuple()), np.array(primitive.end.as_tuple())
        length = float(np.linalg.norm(b-a))
        points = np.linspace(a, b, max(2, math.ceil(length/step)+1))
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


def analyze_internal_spacing(icon, drawing):
    required = float(icon.profile.spec.equal_stroke_centerline_min)
    circular = {c['element_id'] for c in circle_candidates('<svg/>',drawing)}
    by_id = drawing.by_id()
    samples = {}
    findings = []
    for contour in drawing.contours:
        if contour.contour_id in circular:
            continue
        members = [by_id[m] for m in contour.members]
        for i, first in enumerate(members):
            for j in range(i+2,len(members)):
                second = members[j]
                if contour.closed and i == 0 and j == len(members)-1:
                    continue
                if {first.start,first.end} & {second.start,second.end}:
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
                findings.append({'contour':contour.contour_id,'elements':[first.element_id,second.element_id],
                                 'status':'review', **result})
    return {'status':'review' if findings else 'pass', 'blocking':False,
            'required_ink_gap':float(icon.profile.spec.mic), 'rules':RULES,
            'findings':findings,
            'notice':'Advisory sampled opposing-edge check; ordinary joins and complete circular contours excluded. Negative gap indicates overlapping ink.'}


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
