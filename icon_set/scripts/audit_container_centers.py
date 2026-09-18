#!/usr/bin/env python3
"""Reproducible center audit for saved container content zones, not primitive QA."""
from pathlib import Path
import sys,json,math,hashlib,html

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist

ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from PIL import Image,ImageDraw
from shapely.geometry import Polygon,Point,LineString
from shapely.affinity import scale
from shapely.ops import polylabel
from icon_set.scripts.container_placement import polygon_mask
from icon_set.scripts.build_container_buffer_gallery import mask,expanded
BASE=ROOT/'icon_set';OUT=BASE/'work/container-center-audit';ZONES=BASE/'data/container-content-areas.json'


def distance(a,b):return math.dist(a,b)
def xy(p):return [round(p.x,3),round(p.y,3)]

def choose_center(poly):
    centroid=poly.centroid
    pole=polylabel(poly,tolerance=.05)
    maximum=pole.distance(poly.boundary)
    # A wide rectangle has many equal-radius centers. Resolve this ambiguity
    # toward its area centroid rather than reporting a spurious off-center pole.
    if poly.covers(centroid):
        for step in range(101):
            t=step/100
            candidate=Point(centroid.x+(pole.x-centroid.x)*t,centroid.y+(pole.y-centroid.y)*t)
            if poly.covers(candidate) and candidate.distance(poly.boundary)>=maximum-.1:
                pole=candidate;break
    # A region centroid is a reproducible balance point. It is not necessarily the largest fit.
    chosen=centroid if poly.covers(centroid) else pole
    snapped=Point(round(chosen.x*2)/2,round(chosen.y*2)/2)
    if poly.covers(snapped) and snapped.distance(poly.boundary)>0:chosen=snapped
    return chosen,centroid,pole


def audit():
    OUT.mkdir(parents=True,exist_ok=True)
    if not (OUT/'before.json').exists():(OUT/'before.json').write_bytes(ZONES.read_bytes())
    original=json.loads((OUT/'before.json').read_text())['areas']
    data=json.loads(ZONES.read_text());records=[]
    for name,a in data['areas'].items():
        source=development_dist(BASE.parent) / 'container64'/f'{name}.svg';sha=hashlib.sha256(source.read_bytes()).hexdigest()
        if sha!=a['source_sha256']:raise ValueError('Stale source '+name)
        old=original[name]['center'];ink=mask(source.read_text())
        evidence={'source_sha256':sha,'previous_center':old,'visual_review':'pending','scope':'Exported SVG placement; no primitive model/build certification.'}
        if a['kind']=='center-only':
            chosen=[32,32];safe=None
            evidence.update(center=chosen,method='Explicit centered overlay; no safe-zone claim',confidence_score=85,confidence_level='Medium',confidence_basis='20 source identity + 30 explicit centered-overlay rationale + 20 canvas-axis agreement + 15 visual landmark support. No clearance confidence implied.',safe_zone_verified=False,reason=a['reason'],needs_pair_review=True)
        else:
            poly=Polygon(a['polygon']);safe=polygon_mask(a['polygon'])
            if not poly.is_valid or (safe&expanded(ink)).any():raise ValueError('Invalid or unsafe zone '+name)
            c,centroid,pole=choose_center(poly);chosen=xy(c)
            x0,y0,x1,y1=poly.bounds;box=[(x0+x1)/2,(y0+y1)/2]
            ious={}
            for label,x,y in [('vertical',-1,1),('horizontal',1,-1)]:
                reflection=scale(poly,xfact=x,yfact=y,origin=tuple(box))
                ious[label]=poly.intersection(reflection).area/poly.union(reflection).area
            radius=c.distance(poly.boundary);max_radius=pole.distance(poly.boundary)
            manual=a.get('method','').startswith('manually')
            spread=distance(chosen,xy(pole));ratio=radius/max_radius if max_radius else 0
            agreement=max(0,20-round(spread*2));symmetry=15 if min(ious.values())>.98 else 10 if max(ious.values())>.98 else 5
            semantics=15 if manual else 20
            ambiguous=any(t in name for t in ('teacher','camera','open-book','sedan','hand','head-side','panoramic','tent'))
            if ambiguous:semantics=min(semantics,12)
            # Fixed rubric, explicitly not a calibrated probability of correctness.
            components={'source_identity':20,'zone_clearance_check':15,'semantic_boundary_support':semantics,'candidate_agreement':agreement,'symmetry_support':symmetry,'contained_balance_point':10 if poly.covers(centroid) else 4}
            score=sum(components.values());level='High' if score>=90 else 'Medium' if score>=75 else 'Low'
            rays={}
            for label,end in [('left',(-100,c.y)),('right',(164,c.y)),('top',(c.x,-100)),('bottom',(c.x,164))]:
                hit=LineString([(c.x,c.y),end]).intersection(poly.boundary);rays[label]=round(c.distance(hit),3)
            evidence.update(center=chosen,method='Safe-zone area centroid, rounded to nearest half unit' if poly.covers(centroid) else 'Centroid outside zone: largest-inscribed-circle center',
                centroid=xy(centroid),bounds_center=box,largest_circle_center=xy(pole),center_to_zone_edge=round(radius,3),largest_circle_radius=round(max_radius,3),
                clearance_efficiency=round(ratio,3),candidate_disagreement=round(spread,3),symmetry_overlap={k:round(v,4) for k,v in ious.items()},
                axis_gaps=rays,safe_zone_verified=True,confidence_score=score,confidence_level=level,confidence_components=components,
                confidence_basis='Rubric score out of 100; evidence strength, not a statistical probability.',reason=a['reason'],
                needs_pair_review=level!='High' or ratio<.85,
                limitations=('Manually bounded/open or context-sensitive content area. ' if manual or ambiguous else '')+'Zone checks use a conservative 4px/unit raster; optical balance depends on the actual sub icon.')
        a['center']=chosen;evidence['movement']=round(distance(old,chosen),3);a['center_audit']=evidence
        pixels=Image.new('RGB',(256,256),'white');import numpy as np
        arr=np.array(pixels)
        if safe is not None:arr[safe]=[218,241,228]
        arr[expanded(ink)]=[255,226,176];arr[ink]=[25,29,34]
        im=Image.fromarray(arr);draw=ImageDraw.Draw(im)
        def mark(point,color,style):
            x,y=[v*4 for v in point]
            if style=='circle':draw.ellipse((x-5,y-5,x+5,y+5),outline=color,width=2)
            else:draw.line((x-7,y,x+7,y),fill=color,width=2);draw.line((x,y-7,x,y+7),fill=color,width=2)
        mark(old,'#ef4444','circle')
        if 'largest_circle_center' in evidence:mark(evidence['largest_circle_center'],'#9333ea','circle')
        mark(chosen,'#2563eb','cross');im.save(OUT/f'{name}.png')
        records.append({'container':name,**evidence})
    ZONES.write_text(json.dumps(data,indent=2)+'\n')
    (OUT/'results.json').write_text(json.dumps(records,indent=2)+'\n')
    for start in range(0,len(records),30):
        sheet=Image.new('RGB',(1200,1320),'#f1f3f5');draw=ImageDraw.Draw(sheet)
        for j,r in enumerate(records[start:start+30]):
            x=j%5*240;y=j//5*220;sheet.paste(Image.open(OUT/f'{r["container"]}.png').resize((170,170)),(x+35,y))
            name=f'{start+j}: {r["container"]}';draw.text((x+5,y+171),name[:37],fill='black');draw.text((x+5,y+184),name[37:],fill='black')
            draw.text((x+5,y+200),f'{r["confidence_score"]}/100 {r["confidence_level"]}; moved {r["movement"]}u',fill='black')
        sheet.save(OUT/f'sheet-{start//30}.png')
    print(json.dumps({'reviewed':len(records),'moved_over_half_unit':sum(r['movement']>.5 for r in records),'confidence':{s:sum(r['confidence_level']==s for r in records) for s in ['High','Medium','Low']}},indent=2))

if __name__=='__main__':audit()
