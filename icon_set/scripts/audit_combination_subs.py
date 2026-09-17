"""Audit proportional SUB32 reuse without rounding nodes or weakening validation."""
from __future__ import annotations
from collections import Counter
from dataclasses import asdict
import json
from pathlib import Path
from icon_set.model.icons.registry import create
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.primitives import Line, Arc, Bezier, Point
from icon_set.validation.envelope import centerline_bounds, centerline_radial_extent
from icon_set.validation.library_qa import inspect_icon

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'work/sub32-migration'


def proportional_candidate(source, keyshape):
    drawing=source.draw();left,top,right,bottom=centerline_bounds(drawing.primitives)
    cx,cy=(left+right)/2,(top+bottom)/2
    bounds=keyshape.bounds_for(Profile.SUB32)
    if keyshape.is_radial:
        scale=14/centerline_radial_extent(drawing.primitives,(cx,cy))
    else:
        scale=min((bounds[2]-bounds[0]-4)/(right-left) if right>left else float('inf'),
                  (bounds[3]-bounds[1]-4)/(bottom-top) if bottom>top else float('inf'))
    issues=[]
    def scalar(value,label):
        if abs(value-round(value))>1e-7:issues.append(f'{label}: {value:.6f}')
        return round(value) if abs(value-round(value))<1e-7 else value
    def point(p,label):return Point(scalar(16+(p.x-cx)*scale,label+'.x'),scalar(16+(p.y-cy)*scale,label+'.y'))
    def xy(p):return (16+(p[0]-cx)*scale,16+(p[1]-cy)*scale)
    cls=type('ReuseCandidate',(Sub32,),{'icon_id':source.icon_id+'-sub32','keyshape':keyshape,'build':lambda self:None,
                                      'semantic_role':source.semantic_role,'semantic_kind':source.semantic_kind,'category':source.category})
    candidate=cls()
    for p in drawing.primitives:
        start,end=point(p.start,p.element_id+'.start'),point(p.end,p.element_id+'.end')
        if isinstance(p,Line):new=Line(p.element_id,start,end)
        elif isinstance(p,Arc):new=Arc(p.element_id,start,end,scalar(p.radius_x*scale,p.element_id+'.rx'),scalar(p.radius_y*scale,p.element_id+'.ry'),p.large_arc,p.sweep)
        else:new=Bezier(p.element_id,start,end,tuple(tuple(xy(v) for v in segment) for segment in p.segments))
        candidate.primitives.append(new)
    candidate.contours=list(drawing.contours);candidate.relationships=list(drawing.relationships)
    candidate.human_figures=list(drawing.human_figures)
    return candidate,scale,sorted(set(issues))


def audit():
    OUT.mkdir(exist_ok=True)
    pairs=json.loads((ROOT/'icon_set/data/combination-pairs.json').read_text())['rows']
    usage=Counter(s['icon'] for row in pairs for s in row['subs'] if s['family']!='sub')
    results=[]
    for index,(uid,count) in enumerate(usage.most_common(),1):
        source=create(uid);keyshape=source.keyshape
        row={'icon_id':uid,'pair_count':count,'source_profile':source.profile.name,'target_profile':'SUB32',
             'source_keyshape':keyshape.name,'status':'needs_redraw','source_parts':len(source.draw().primitives)}
        if keyshape is Keyshape.FREE:
            row['reason']='Source uses a family-specific FREE exception; needs an independent SUB32 design.'
        else:
            candidate,scale,issues=proportional_candidate(source,keyshape)
            row.update(scale=scale,target_keyshape=keyshape.name,target_ink_bounds=list(keyshape.bounds_for(Profile.SUB32)),off_grid=issues)
            # Save the unchanged-proportions attempt as audit evidence only.
            if issues:
                row['reason']='Proportional resize puts authored nodes or arc radii off the integer grid.'
            else:
                qa=inspect_icon(candidate);svg=qa.pop('_svg',None)
                row['validation']=qa
                if qa['status']=='pass':
                    row['status']='geometry_pass_needs_visual_review'
                    row['reason']='Proportional geometry passes all numeric checks; visual and source-part review is still required.'
                    candidate.export_json_graph(OUT/(uid+'-candidate.json'))
                    (OUT/(uid+'-candidate.svg')).write_text(svg or candidate.to_svg())
                else:row['reason']='Grid fits, but profile or spacing checks fail.'
        results.append(row)
        (OUT/'audit.json').write_text(json.dumps({'rows':results},indent=2,default=str)+'\n')
        print(f'{index}/{len(usage)} {uid}: {row["status"]}',flush=True)
    print(dict(Counter(r['status'] for r in results)),flush=True)
    return results

if __name__=='__main__':audit()
