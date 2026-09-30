"""Batch 13 standalone SOLO48 authoring; inputs retained per generated module."""
import json, re, sys, textwrap, io
from pathlib import Path
from datetime import datetime, timezone
import cairosvg
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
AUTHOR='gpt-6'
rows=json.loads((ROOT/'batch.json').read_text())
HELPERS='''
        def path(n,start,steps,closed=False):
            p=start; members=[]
            for i,step in enumerate(steps):
                k,end,*a=step; name=f'{n}-{i}'
                if k=='L': self.add_line(name,p,end)
                elif k=='A': self.add_arc(name,p,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='B': self.add_bezier(name,p,(a[0],a[1],end))
                members.append(name);p=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=4):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
'''
DESIGNS={}
def design(i,keyshape,problem,change,body,omissions='',reference='Lucide square: coherent contours and tangent quarter-circle corners.'):
    DESIGNS[i]=dict(keyshape=keyshape,problem=problem,change=change,body=textwrap.dedent(body).strip(),omissions=omissions,construction_reference=reference)

design(1,'SQUARE','Top node is offset from the branch junction and several links stop away from the circle outlines.','Center the top node and attach each edge at exact circle extrema, with larger equal nodes.', '''
for n,x,y in [('top',24,12),('left',12,36),('right',36,36)]: circle(n,x,y,6)
for n,a,b,u,v in [('left-link',(18,12),(12,30),'top','left'),('right-link',(30,12),(36,30),'top','right'),('base',(18,36),(30,36),'left','right')]:
    line(n,a,b);join(n,u);join(n,v)
''')
design(2,'SQUARE','The squat wing case, detached-looking head and missing legs read as a person rather than a beetle.','Restore a tall beetle body with three pairs of legs inside the display dome.', '''
path('dome',(6,42),[('L',(6,24)),('A',(42,24),18,18,True),('L',(42,42)),('L',(6,42))],True)
path('body',(20,24),[('A',(28,24),4,7,True),('L',(28,30)),('A',(20,30),4,5,True),('L',(20,24))],True)
for side in (-1,1):
    x=24+side*4; outer=24+side*10
    for k,y,oy in [('upper',24,17),('middle',27,27),('lower',30,35)]:
        line(f'leg-{side}-{k}',(x,y),(outer,oy));join(f'leg-{side}-{k}','body')
''','Wing seam and separate antennae omitted to preserve six legs.','Lucide bug: elongated body and three leg pairs; source dome retained.')
design(3,'CIRCLE','The refresh loop is an uneven narrow oval with a cramped arrowhead. No separate original is available.','Use a circular sweep and larger clean downward arrowhead around the central ring.', '''
path('loop',(24,44),[('A',(44,24),20,20,False),('A',(24,4),20,20,False),('A',(4,24),20,20,False)])
poly('head',(4,14),(4,24),(14,24));join('head','loop')
circle('hub',24,24,4)
''',reference='Lucide refresh-ccw: coherent circular sweep with an attached open head.')
design(4,'SQUARE','Short uneven arrowheads and a tilted uneven loop weaken the synchronize symbol. No separate original is available.','Balance two opposing round sweeps and equal open arrowheads.', '''
path('upper',(6,27),[('L',(6,24)),('A',(24,6),18,18,True),('A',(42,24),18,18,True)])
poly('upper-head',(32,14),(42,24),(42,14));join('upper-head','upper')
path('lower',(42,33),[('A',(24,42),18,9,True),('A',(6,33),18,9,True)])
poly('lower-head',(6,42),(6,33),(16,33));join('lower-head','lower')
''',reference='Lucide refresh-cw: two opposing sweeps with matching open arrowheads.')
design(5,'HRECT_L','Cap brim cuts the face in half and the bust has an excessive detached gap.','Give the worker a curved jaw beneath a cap and broad shoulders, beside a clean broom.', '''
path('head',(8,16),[('A',(20,16),6,8,True),('A',(8,16),6,6,True)],True)
line('brim',(8,16),(22,16));join('brim','head')
path('shoulders',(4,40),[('L',(4,36)),('A',(14,26),10,10,True),('A',(24,36),10,10,True),('L',(24,40))])
line('handle',(38,8),(38,30))
poly('broom',(38,30),(42,30),(44,40),(32,40),(34,30),(38,30),closed=True);join('handle','broom')
''','Facial features and collar omitted.','Shared human_ref/user.svg: round jaw and broad smooth shoulders; source cap and broom.')
design(6,'SQUARE','The snowflake has five irregular branches and inconsistent fork directions. No separate original is available.','Rebuild six evenly arranged branches with shared mirrored fork geometry.', '''
nodes=[((24,24),(24,6)),((24,24),(42,14)),((24,24),(42,34)),((24,24),(24,42)),((24,24),(6,34)),((24,24),(6,14))]
for i,(a,b) in enumerate(nodes): line(f'ray-{i}',a,b)
for i in range(6):
    for j in range(i):join(f'ray-{i}',f'ray-{j}')
for n,p in [('top',[(17,7),(24,14),(31,7)]),('bottom',[(17,41),(24,34),(31,41)]),('ul',[(6,22),(14,18),(14,10)]),('ur',[(34,10),(34,18),(42,22)]),('ll',[(6,26),(14,30),(14,38)]),('lr',[(34,38),(34,30),(42,26)])]:poly(n,*p)
for a,b in [('top','ray-0'),('bottom','ray-3'),('ul','ray-5'),('ur','ray-1'),('ll','ray-4'),('lr','ray-2')]:join(a,b)
''',reference='Lucide snowflake: sixfold branching, shared fork parameters; integer geometry mirrored.')
design(7,'HRECT_L','The separated paddle strokes read as stray marks and the dragon lacks a crest.','Restore a continuous diagonal paddle and a distinct dragon crest with a smooth hull.', '''
path('boat',(4,17),[('L',(4,10)),('L',(10,10)),('L',(13,8)),('L',(18,8)),('A',(24,18),6,10,True),('L',(20,27)),('L',(44,27)),('A',(34,40),10,13,True),('L',(14,40)),('A',(4,30),10,10,True),('B',(12,21),(4,26),(12,24)),('A',(8,17),4,4,False),('L',(4,17))],True)
line('paddle',(36,8),(27,40));join('paddle','boat')
''','Paddle grip and blade reduced to a single long shaft; fine face details omitted.')
design(8,'SQUARE','Egg is a plain circle, bacon is a rigid H-like strip and sausage has no scoring.','Use an irregular fried-egg outline, flowing bacon edges and sausage score.', '''
box('sausage',6,6,42,14,4)
line('score',(24,6),(28,14));join('score','sausage')
path('egg',(6,31),[('B',(15,23),(6,25),(10,23)),('B',(25,29),(20,23),(20,28)),('B',(20,42),(30,36),(25,42)),('B',(6,31),(10,42),(6,37))],True)
self.add_dot('yolk',(16,32))
path('bacon',(35,24),[('B',(34,42),(42,28),(28,35)),('L',(42,42)),('B',(43,24),(36,36),(48,31)),('L',(35,24))],True)
''','One sausage score and a dot yolk retain readable spacing.')
design(9,'VRECT_L','The bow replaces the top of the egg and the ribbon band and tails are absent.','Restore the full egg silhouette with a central ribbon and bow knot.', '''
path('egg',(24,4),[('B',(40,29),(33,4),(40,18)),('A',(24,44),16,15,True),('A',(8,29),16,15,True),('B',(24,4),(8,18),(15,4))],True)
poly('bow',(16,20),(24,25),(32,20),(32,30),(24,25),(16,30),closed=True)
line('band-left',(8,29),(16,29));line('band-right',(32,29),(40,29));join('band-left','egg');join('band-right','egg');join('band-left','bow');join('band-right','bow')
''','Ribbon tails omitted; band and bow prioritized.')
design(10,'VRECT_L','Outer tap halo is a shallow brow and the fingertip is too short.','Extend the rounded fingertip and restore a semicircular touch halo below the direction chevron.', '''
poly('chevron',(16,4),(24,12),(32,4))
path('halo',(8,36),[('L',(8,34)),('A',(40,34),16,14,True),('L',(40,36))])
path('finger',(20,44),[('L',(20,33)),('A',(28,33),4,4,True),('L',(28,44))])
''',reference='No useful exact Lucide match; source fingertip and concentric halo construction.')
design(11,'SQUARE','The stream curves bend away from the cube and are reduced to four disconnected hooks.','Use three long converging stream curves beside a larger clean isometric cube.', '''
path('upper',(6,6),[('B',(42,14),(12,14),(26,14))])
path('middle',(6,22),[('B',(18,28),(8,26),(12,28))])
path('lower',(6,42),[('B',(18,36),(8,38),(12,36))])
poly('cube',(34,22),(42,27),(42,37),(34,42),(26,37),(26,27),closed=True)
poly('top-seam',(26,27),(34,32),(42,27));line('stem',(34,32),(34,42));join('top-seam','cube');join('stem','top-seam');join('stem','cube')
''','Four streams reduced to three; source rightward convergence preserved.')
design(12,'VRECT_L','The broad flattened pin looks like an eye; map is a short strip.','Make a tall rounded pin above a deeper folded map.', '''
path('pin',(24,27),[('L',(16,17)),('A',(32,17),8,13,True),('L',(24,27))],True)
self.add_dot('pin-hole',(24,14))
poly('map',(8,34),(19,31),(29,34),(40,31),(40,41),(29,44),(19,41),(8,44),closed=True)
line('fold-left',(19,31),(19,41));line('fold-right',(29,34),(29,44));join('fold-left','map');join('fold-right','map')
''','Pin hole becomes a dot to retain the pointed silhouette.','Lucide map-pin: taller crown and tapered tip; source folded-map rhythm.')
design(13,'SQUARE','The source panel has been omitted, leaving only a down arrow and two dots.','Restore the rounded upper panel and horizontal fold axis around a curved down arrow.', '''
path('panel',(6,24),[('L',(6,10)),('A',(10,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,24))])
line('axis-left',(6,24),(14,24));join('axis-left','panel')
line('axis-right',(34,24),(42,24));join('axis-right','panel')
path('arrow',(25,16),[('B',(24,42),(18,25),(20,33))])
poly('head',(15,35),(24,42),(31,33));join('head','arrow')
''')
design(14,'SQUARE','The folder is a shallow tray and the document has no content marks.','Restore a tall front folder and rounded rear document with a text line.', '''
path('file',(14,25),[('L',(14,10)),('A',(18,6),4,4,True),('L',(32,6)),('L',(42,16)),('L',(42,35)),('A',(38,39),4,4,True),('L',(30,39))])
path('folder',(6,29),[('A',(10,25),4,4,True),('L',(16,25)),('L',(21,29)),('L',(26,29)),('A',(30,33),4,4,True),('L',(30,38)),('A',(26,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,29))],True)
line('text',(22,17),(31,17));join('file','folder')
''','Second text line omitted.','Lucide folder and square: clear folder tab and tangent rounded corners.')
design(15,'HRECT_L','Rounded filling resembles a handbag handle.','Replace the handle-like filling with a scalloped lettuce crest over a broad taco shell.', '''
path('shell',(4,40),[('A',(44,40),20,22,True),('L',(4,40))],True)
path('lettuce',(6,30),[('B',(13,15),(4,21),(9,16)),('B',(24,8),(14,7),(20,8)),('B',(35,15),(28,8),(34,7)),('B',(42,30),(39,16),(44,21))])
join('lettuce','shell')
''','Tiny filling bumps reduced to three broad scallops.')
design(16,'HRECT_L','The central machine is disconnected and both identifying lightning bolts are missing.','Reconnect the insulator and base, restoring paired lightning strokes.', '''
box('cap',16,8,32,16,4)
line('column',(24,16),(24,32));join('column','cap')
for y in (24,32):line(f'rib-{y}',(18,y),(30,y));join(f'rib-{y}','column')
poly('base',(16,40),(16,32),(32,32),(32,40),(16,40),closed=True);join('column','base');join('rib-32','base')
poly('left-bolt',(10,10),(4,20),(10,20),(4,30))
poly('right-bolt',(44,10),(38,20),(44,20),(38,30))
''','Bolt outlines reduced to zigzag sparks and central ribs reduced to two.')
design(17,'SQUARE','Single central division makes the shell look like a leaf or shield.','Restore three detached fanning ribs and a broad scalloped rim above the hinge.', '''
path('shell',(24,42),[('L',(9,30)),('A',(6,24),8,8,True),('A',(12,15),8,9,True),('A',(18,9),6,6,True),('A',(30,9),6,3,True),('A',(36,15),6,6,True),('A',(42,24),8,9,True),('A',(39,30),8,8,True),('L',(24,42))],True)
line('rib-center',(24,16),(24,31))
line('rib-left',(14,21),(16,28));line('rib-right',(34,21),(32,28))
''','Fine outer ribs and hinge tabs omitted; three ribs retain the fan.')
design(18,'VRECT_M','The wide angular garment looks like a sleeveless top and lacks thin straps.','Restore separate vertical straps, a fitted waist and a long tapered skirt.', '''
path('dress',(12,12),[('L',(24,22)),('L',(36,12)),('B',(33,25),(41,16),(33,20)),('B',(38,34),(33,28),(38,29)),('L',(35,44)),('L',(13,44)),('L',(10,34)),('B',(15,25),(10,29),(15,28)),('B',(12,12),(15,20),(7,16))],True)
for x in (12,36):line(f'strap-{x}',(x,4),(x,12));join(f'strap-{x}','dress')
''','Fine seam and folds omitted.','Lucide shirt: economical garment contour; source thin straps and fitted silhouette.')
design(19,'SQUARE','The shoulder triangle and hair overlap create a ribbon-like portrait instead of a woman.','Use a curved face, simple long-hair silhouette and rounded shoulders within the frame.', '''
box('frame',6,6,42,42,4)
path('hair',(15,32),[('L',(15,23)),('A',(33,23),9,9,True),('L',(33,32))])
path('jaw',(18,23),[('A',(30,23),6,6,False)])
path('shoulders',(14,42),[('L',(14,39)),('A',(24,33),10,6,True),('A',(34,39),10,6,True),('L',(34,42))])
join('shoulders','frame');join('jaw','hair')
''','Facial features omitted; long hair and rounded shoulders retained.','Shared human_ref/user.svg: circular jaw and smooth shoulders; Lucide square: frame.')
design(20,'HRECT_L','The F labels have very short bars and the needle hub fills in.','Lengthen the F bars and use a small open hub with a clean diagonal needle.', '''
path('arch',(4,24),[('A',(24,8),20,16,True),('A',(44,24),20,16,True)])
line('tick',(24,8),(24,12));join('tick','arch')
for x in (4,44):line(f'end-{x}',(x,24),(x+(4 if x==4 else -4),24));join(f'end-{x}','arch')
circle('hub',24,25,3);line('needle',(27,25),(32,18));join('needle','hub')
for x in (6,34):
    poly(f'f-{x}',(x,40),(x,32),(x+8,32))
    line(f'fbar-{x}',(x,40),(x+6,40));join(f'fbar-{x}',f'f-{x}')
''','Diagonal outer tick omitted to preserve space.','Lucide gauge: smooth arc and diagonal indicator; source F labels preserved.')

def run(i):
    row=rows[i-1]; d=DESIGNS[i]; ref=Path(row['reference']); uid=re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',ref.stem).group(); concept=ref.stem[:-(len(uid)+1)]
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'-batch13'
    out=REPO/'icon_set/work/primitive-make-ray'/uid/stamp;out.mkdir(parents=True)
    icon_id=row['key'].split('/')[1]
    metadata={'concept':concept,'source_uuid':uid,'reference_path':str(ref),'feedback':'No written feedback or disapproval reason recorded.','before_review':d['problem'],'planned_change':d['change']}
    (out/(icon_id+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
    code=f'''"""{d['change']}
Symbol plan: {d['keyshape']} on SOLO48; named shapes and source arrangement.
Before review: {d['problem']}
Construction reference: {d['construction_reference']}
Omissions: {d['omissions']}
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID={uid!r}
SOURCE_PATH={str(ref)!r}
AUTHOR={AUTHOR!r}
class Drawing(Solo48):
    icon_id={icon_id!r}
    keyshape=Keyshape.{d['keyshape']}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords={tuple(concept.split())!r}
    def build(self):
'''+HELPERS+textwrap.indent(d['body'],'        ')+'\n'
    module=out/(icon_id.replace('-','_')+'_'+uid.replace('-','_')+'.py');module.write_text(code)
    icon=load_icon(module); report=icon.validate_icon();svg=icon.to_svg(); (out/(icon_id+'.svg')).write_text(svg)
    g=gate(module);(out/'validation.txt').write_text(report.describe()+'\n'+json.dumps(g,indent=2))
    for theme,color,bg in [('light','#000000','#ffffff'),('dark','#ffffff','#181818')]:
        for size in (48,240):
            cairosvg.svg2png(bytestring=svg.replace('currentColor',color).encode(),write_to=str(out/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
    for kind in ('reference','before'):
        cairosvg.svg2png(url=row[kind],write_to=str(out/(kind+'.png')),output_width=240,output_height=240,background_color='white')
    state={'index':i,'run':str(out.relative_to(REPO)),'module':str(module.relative_to(REPO)),'svg':icon_id+'.svg','source_uuid':uid,'source_path':str(ref),'icon_id':icon_id,'author':AUTHOR,'validation_status':report.status,'errors':report.errors,'warnings':report.warnings,'build_gate':g,'visual_review':'Pending native light/dark review','omissions':d['omissions'],**{k:v for k,v in d.items() if k!='body'}}
    (out/'candidate.json').write_text(json.dumps(state,indent=2))
    latest=ROOT/'latest.json';ls=json.loads(latest.read_text()) if latest.exists() else {};ls[str(i)]=state;latest.write_text(json.dumps(ls,indent=2))
    print(i,icon_id,report.status,g['status'],flush=True)
    for e in list(report.errors)+list(report.warnings)+g['errors']+g['warnings']:print(' ',e,flush=True)

if __name__=='__main__':
    for i in map(int,sys.argv[1:]):run(i)
