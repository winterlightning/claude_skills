"""Whole-drawing exact parallel groups and midpoint-normal measurements."""
import math
from collections import defaultdict
from ..model.primitives import Line
from ..model.profiles import STROKE_WIDTH

EPS = 1e-9

def analyze(drawing, required=8.0):
    """Group exact parallel runs, then cast finite midpoint normals on both sides.

    Contiguous collinear pieces in the SAME emitted path are merged so a split
    attachment node cannot change a run's midpoint. Distinct paths never merge.
    Every source keeps zero, one or two nearest positive-distance hits. Equal
    nearest hits are all retained. Collinear overlaps are reported separately.
    Relations annotate measurements; they do not silently exempt close pairs.
    """
    owners = {m: c.contour_id for c in drawing.contours for m in c.members}
    buckets = defaultdict(list)
    raw = []
    for p in drawing.primitives:
        if not isinstance(p, Line) or p.is_dot:
            continue
        ax, ay = p.start.as_tuple(); bx, by = p.end.as_tuple()
        dx, dy = bx-ax, by-ay
        if any(int(v) != v for v in (ax, ay, bx, by)):
            raise ValueError(f'{p.element_id}: non-integer authored line')
        divisor = math.gcd(int(abs(dx)), int(abs(dy)))
        dx, dy = int(dx)//divisor, int(dy)//divisor
        if dx < 0 or (dx == 0 and dy < 0): dx, dy = -dx, -dy
        # Integer projections retain exact direction, offset, and interval tests.
        start, end = sorted((ax*dx+ay*dy, bx*dx+by*dy))
        offset = -ax*dy+ay*dx
        row = dict(members=[p.element_id], path=owners.get(p.element_id,p.element_id),
                   direction=[dx,dy], offset=offset, lo=start, hi=end)
        raw.append(row.copy())
        buckets[(dx,dy,offset,row['path'])].append(row)
    runs = []
    for key, pieces in sorted(buckets.items()):
        for piece in sorted(pieces,key=lambda x:(x['lo'],x['hi'],x['members'])):
            if runs and tuple(runs[-1]['direction']) == key[:2] and runs[-1]['offset']==key[2] and runs[-1]['path']==key[3] and runs[-1]['hi']==piece['lo']:
                runs[-1]['hi']=piece['hi']; runs[-1]['members']+=piece['members']
            else: runs.append(dict(piece))
    groups = defaultdict(list)
    for index,r in enumerate(runs):
        r['id']=index
        dx,dy=r['direction']; norm=math.hypot(dx,dy)
        def point(t):
            return [(dx*t-dy*r['offset'])/(norm*norm),(dy*t+dx*r['offset'])/(norm*norm)]
        r['start']=point(r['lo']); r['end']=point(r['hi'])
        r['midpoint']=point((r['lo']+r['hi'])/2)
        groups[tuple(r['direction'])].append(r)
    hits=[]; overlaps=[]; coincident=[]
    for direction,group in sorted(groups.items()):
        norm=math.hypot(*direction)
        for a in group:
            mid=(a['lo']+a['hi'])/2
            candidates={-1:[],1:[]}
            for b in group:
                delta=b['offset']-a['offset']
                if a['id']==b['id'] or delta==0 or not b['lo']<=mid<=b['hi']: continue
                candidates[1 if delta>0 else -1].append((abs(delta),b))
            for side,options in candidates.items():
                if not options: continue
                nearest=min(d for d,_ in options)
                for delta,b in options:
                    if delta!=nearest: continue
                    distance=delta/norm
                    dx,dy=direction
                    target=[a['midpoint'][0]-dy/norm*side*distance,
                            a['midpoint'][1]+dx/norm*side*distance]
                    names_a=set(a['members']+[a['path']]); names_b=set(b['members']+[b['path']])
                    relations=[{'kind':r.kind,'members':list(r.members)} for r in drawing.relationships
                               if names_a.intersection(r.members) and names_b.intersection(r.members)]
                    hits.append(dict(source=a['id'],target=b['id'],side=side,start=a['midpoint'],end=target,
                                     centerline_distance=distance,ink_gap=distance-STROKE_WIDTH,
                                     below_minimum=distance+EPS<required,
                                     target_endpoint=mid in (b['lo'],b['hi']),relationships=relations))
        for i,a in enumerate(group):
            for b in group[i+1:]:
                lo,hi=max(a['lo'],b['lo']),min(a['hi'],b['hi'])
                if hi<=lo: continue
                delta=abs(b['offset']-a['offset'])
                if delta==0:
                    coincident.append(dict(pair=[a['id'],b['id']],overlap_length=(hi-lo)/norm))
                else:
                    t=(lo+hi)/2; dx,dy=direction; norm2=dx*dx+dy*dy
                    pa=[(dx*t-dy*a['offset'])/norm2,(dy*t+dx*a['offset'])/norm2]
                    pb=[(dx*t-dy*b['offset'])/norm2,(dy*t+dx*b['offset'])/norm2]
                    overlaps.append(dict(pair=[a['id'],b['id']],start=pa,end=pb,centerline_distance=delta/norm,
                                         ink_gap=delta/norm-STROKE_WIDTH,overlap_length=(hi-lo)/norm,
                                         below_minimum=delta/norm+EPS<required))
    measured={tuple(sorted((h['source'],h['target']))) for h in hits}
    missed=[]
    for pair in overlaps:
        if tuple(pair['pair']) in measured: continue
        a,b=(runs[i] for i in pair['pair'])
        mids=((a['lo']+a['hi'])/2,(b['lo']+b['hi'])/2)
        reason='occluded-by-nearer-parallel' if (b['lo']<=mids[0]<=b['hi'] or a['lo']<=mids[1]<=a['hi']) else 'both-midpoints-miss'
        missed.append(dict(pair,reason=reason))
    return dict(required_centerline=required,stroke_width=STROKE_WIDTH,required_ink=required-STROKE_WIDTH,
                raw_line_count=len(raw),runs=runs,
                groups=[dict(direction=list(k),runs=[r['id'] for r in v]) for k,v in sorted(groups.items())],
                hits=hits,unmeasured_overlaps=missed,collinear_overlaps=coincident,
                measured_pair_count=len(measured),
                below_minimum_pair_count=len({tuple(sorted((h['source'],h['target']))) for h in hits if h['below_minimum']}))

