"""Fresh primitive-make-ray runs for the ten available manual-fix claims."""
from pathlib import Path
import sys,json,re,textwrap,importlib.util,shutil,math
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from PIL import Image,ImageDraw
BATCH=Path(__file__).parent
claims=json.loads((BATCH/'claims.json').read_text())
SOURCE_ICON_ID={r['index']:re.search(r'([a-f0-9-]{36})\.svg$',r['reference']).group(1) for r in claims}
SOURCE_PATH={r['index']:r['reference'] for r in claims}
AUTHOR='gpt-6'
old=BATCH.parent/'batch-20260928T170716Z/author_batch.py'
spec=importlib.util.spec_from_file_location('prior_helpers',old);prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
HELPERS=prior.HELPERS.split('    def phone(')[0]+'''
    def node(self,n,x,y,r,extra=()):
        import math
        offsets=set([(-r,0),(0,-r),(r,0),(0,r),*extra])
        offsets=sorted(offsets,key=lambda p:math.atan2(p[1],p[0]))
        pts=[(x+dx,y+dy) for dx,dy in offsets]
        self.path(n,pts[0],[('A',q,r,r,True) for q in pts[1:]+pts[:1]],True)
'''
BODIES={
0:'''# Continuous neck and profile; no detached-head gap applies.
self.path('profile',(13,44),[('L',(13,34)),('C',(8,23),(13,30),(8,28)),('L',(8,20)),('C',(16,6),(8,14),(11,9)),('C',(24,4),(18,5),(21,4)),('C',(36,13),(30,4),(34,7)),('L',(40,25)),('L',(36,26)),('L',(36,32)),('A',(30,38),6,6,True),('L',(28,38)),('L',(28,44))])
self.add_polyline('crack',(16,6),(22,13),(18,17),(21,20))
self.relate('connect','profile','crack')
''',
1:'''# Taller message panel with a left-pointing reply arrow continuing its top edge.
self.path('bubble',(14,10),[('L',(8,10)),('A',(4,14),4,4,False),('L',(4,32)),('A',(8,36),4,4,False),('L',(12,36)),('L',(12,44)),('L',(24,36)),('L',(40,36)),('A',(44,32),4,4,False),('L',(44,14)),('A',(40,10),4,4,False),('L',(24,10))])
self.add_polyline('arrow',(30,4),(24,10),(30,16));self.relate('connect','bubble','arrow')
''',
2:'''# Housing and tape share both attachment nodes; two ruler ticks are visible.
self.path('housing',(12,8),[('L',(20,8)),('A',(28,16),8,8,True),('L',(28,28)),('L',(28,40)),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,16)),('A',(12,8),8,8,True)],True)
self.circle('hub',16,22,6)
self.add_polyline('tape',(28,28),(44,28),(44,40),(40,40),(34,40),(28,40))
self.relate('connect','housing','tape')
for x in (34,40):
    self.add_line(f'tick-{x}',(x,40),(x,36));self.relate('connect','tape',f'tick-{x}')
''',
3:'''# Wider low-profile measure; same shared case/tape construction.
self.path('housing',(12,10),[('L',(20,10)),('A',(28,18),8,8,True),('L',(28,28)),('L',(28,38)),('L',(8,38)),('A',(4,34),4,4,True),('L',(4,18)),('A',(12,10),8,8,True)],True)
self.circle('hub',16,23,6)
self.add_polyline('tape',(28,28),(44,28),(44,38),(40,38),(34,38),(28,38))
self.relate('connect','housing','tape')
for x in (34,40):
    self.add_line(f'tick-{x}',(x,38),(x,35));self.relate('connect','tape',f'tick-{x}')
''',
4:'''# Long pointed pod with two bowed ribs, mirrored around x24.
self.path('pod',(24,10),[('C',(34,27),(30,15),(34,21)),('C',(24,44),(34,33),(30,39)),('C',(14,27),(18,39),(14,33)),('C',(24,10),(14,21),(18,15))],True)
for side in (-1,1):
    n=f'rib-{side}';x=24+side*5
    self.path(n,(24,10),[('C',(24,44),(x,18),(x,36))]);self.relate('connect','pod',n)
self.relate('connect','rib--1','rib-1')
self.path('stem',(24,10),[('A',(30,4),6,6,True)]);self.relate('connect','stem','pod')
for side in (-1,1):self.relate('connect','stem',f'rib-{side}')
''',
5:'''# Outlined data nodes expose exact 3-4-5 attachment points for the connecting lines.
self.add_polyline('axes',(4,4),(4,44),(44,44))
self.node('point-a',14,18,5,[(-3,4),(4,3)])
self.node('point-b',28,30,5,[(-4,-3),(3,-4)])
self.node('point-c',39,9,5,[(-3,4)])
for name,a,b,parts in [
    ('origin-link',(4,44),(11,22),('axes','point-a')),
    ('middle-link',(18,21),(24,27),('point-a','point-b')),
    ('upper-link',(31,26),(36,13),('point-b','point-c'))]:
    self.add_line(name,a,b)
    for part in parts:self.relate('connect',part,name)
''',
6:'''# Circular elbow, flared pedestal, outlined horizontal arm and open curved claw.
self.node('elbow',12,10,5,[(4,-3),(4,3),(-3,4),(3,4)])
self.path('pedestal',(9,14),[('L',(9,32)),('C',(4,44),(9,37),(6,42)),('L',(24,44)),('C',(15,32),(22,42),(15,37)),('L',(15,14))])
self.relate('connect','elbow','pedestal')
self.add_polyline('arm',(16,7),(36,7),(36,13),(16,13))
self.relate('connect','arm','elbow')
self.add_line('forearm',(36,13),(36,19));self.relate('connect','forearm','arm')
self.path('gripper',(30,28),[('L',(28,26)),('A',(36,18),8,8,True),('A',(44,26),8,8,True),('L',(42,28))])
# Forearm meets the crown at y18.
self.add_line('wrist',(36,19),(36,18));self.relate('connect','forearm','wrist');self.relate('connect','wrist','gripper')
self.add_polyline('box',(30,34),(44,34),(44,44),(30,44),closed=True)
''',
7:'''# Roofed ceremonial figure with two side projections and three procession busts.
self.add_polyline('roof',(12,12),(24,4),(36,12),(31,12),(17,12),closed=True)
self.path('figure',(17,12),[('L',(17,21)),('C',(31,21),(21,23),(27,23)),('L',(31,12))])
self.relate('connect','roof','figure')
self.path('left-projection',(17,18),[('L',(9,16)),('A',(6,23),4,4,False),('L',(11,25)),('L',(14,17))])
self.relate('connect','figure','left-projection')
self.add_polyline('right-projection',(31,18),(41,16),(44,23));self.relate('connect','figure','right-projection')
# human_ref/user.svg: three equal circular heads and open shoulders, exact 4u ink gap.
for i,cx in enumerate((8,24,40)):
    self.circle(f'head-{i}',cx,29,3)
    self.path(f'shoulders-{i}',(cx-5,44),[('A',(cx,40),5,4,True),('A',(cx+5,44),5,4,True)])
''',
8:'''# Equal square tiles; rear outline is interrupted where the front tile occludes it.
self.box('front',4,14,24,34,3,{2:[(24,26)],4:[(14,34)]})
self.path('rear',(24,26),[('L',(33,26)),('A',(36,29),3,3,True),('L',(36,41)),('A',(33,44),3,3,True),('L',(17,44)),('A',(14,41),3,3,True),('L',(14,34))])
self.relate('connect','front','rear')
self.add_arc('rotation',(28,8),(40,20),radius_x=12)
self.add_polyline('start-head',(32,4),(28,8),(32,12))
self.add_polyline('end-head',(36,16),(40,20),(44,16))
self.relate('connect','rotation','start-head');self.relate('connect','rotation','end-head')
''',
9:'''# Low, broad visor with mirrored tangent transitions into a shallow nose notch.
self.path('visor',(15,14),[('L',(33,14)),('A',(40,21),7,7,True),('L',(40,24)),('L',(40,27)),('A',(33,34),7,7,True),('L',(30,34)),('C',(24,29),(27,34),(27,29)),('C',(18,34),(21,29),(21,34)),('L',(15,34)),('A',(8,27),7,7,True),('L',(8,24)),('L',(8,21)),('A',(15,14),7,7,True)],True)
for n,a,b in [('left-strap',(4,24),(8,24)),('right-strap',(40,24),(44,24))]:
    self.add_line(n,a,b);self.relate('connect','visor',n)
'''
}
NOTES={
0:('The profile was blocky, with a flat vertical forehead and heavy lightning-like crack.','Restored a sloping forehead/nose, rounded jaw, longer neck and finer three-segment crack at the reference location.'),
1:('The message body was flattened and the reply arrow dominated its height.','Restored a taller bubble, balanced tail and a left-pointing arrow continuing the top edge.'),
2:('The tape was too short, and all ruler ticks were missing.','Lengthened the extended tape, enlarged the housing hub and restored two measurement ticks.'),
3:('The tape was short and blank, with an overly tall case.','Restored a lower, wider case, a longer tape and two spaced measurement ticks.'),
4:('The cacao pod was squat and onion-shaped.','Restored a tall pointed pod with two long bowed ribs and a curved stem.'),
5:('The chart had tiny node openings and heavy connectors that formed a bent solid bar.','Enlarged all three node openings and rebuilt the origin-to-node and node-to-node links with exposed exact boundary joins.'),
6:('The arm collapsed into a thin pole and tiny triangular foot; the claw did not match the source.','Restored the flared pedestal, outlined arm, round elbow and wide curved claw above the box.'),
7:('The sculpture disappeared, leaving only a roof and three linked people.','Restored the torso and side projections beneath the roof, with three separate procession busts.'),
8:('Both arrowheads were heavy and poorly oriented; the rear tile was flattened.','Rebuilt the arrow with a tangent quarter-circle and correctly facing heads; restored a taller rear tile.'),
9:('The visor was too tall, nearly square, and its nose opening too deep.','Restored a broad low visor, shallow smooth nose notch and short balanced side straps.')}
REFS={0:'human_ref/user.svg; supplied profile (no useful direct Lucide match)',1:'Lucide message-square-reply',2:'Lucide ruler',3:'Lucide ruler',4:'Lucide leaf: coherent long curves',5:'Lucide chart-network',6:'No useful direct Lucide robot-arm match; source geometric construction',7:'Lucide house and users; human_ref/user.svg',8:'Lucide rotate-cw',9:'Lucide glasses: mirrored contour balance'}
SHAPES={0:'VRECT_L',1:'SQUARE',2:'HRECT_L',3:'HRECT_M',4:'VRECT_M',5:'SQUARE',6:'SQUARE',7:'SQUARE',8:'SQUARE',9:'HRECT_M'}
OMISSIONS={2:'Three tiny ruler ticks reduced to two for visible spacing.',6:'Small terminal claw thickness omitted; open gripping arc retained.',7:'Tiny facial smile omitted; roof, torso, side projections and all three people retained.',9:'Hollow strap interiors simplified to short strokes.'}
def author(indices=None,rev=1):
 for rec in claims:
    i=rec['index']
    if indices is not None and i not in indices:continue
    sid=SOURCE_ICON_ID[i];ref=Path(rec['reference']);concept=ref.stem[:-37]
    run=Path('icon_set/work/primitive-make-ray')/sid/f'20260928T171810Z-fix-{i:02d}-r{rev}';run.mkdir(parents=True,exist_ok=False)
    meta=dict(concept=concept,source_uuid=sid,reference_path=str(ref));(run/(rec['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
    before,change=NOTES[i];shape=SHAPES[i]
    review=dict(before_problem=before,feedback=rec['feedback'],changes=change,construction_reference=REFS[i],omissions=OMISSIONS.get(i,'None'))
    (run/'review.json').write_text(json.dumps(review,indent=2))
    module=run/(rec['icon_id'].replace('-','_')+'_'+sid.replace('-','_')+'.py')
    doc=f'{before} {change}\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: {REFS[i]}.\nKeyshape {shape}; intentional source proportions recorded separately when outside the nominal envelope.'
    source=f'{doc!r}\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={sid!r}\nSOURCE_PATH={str(ref)!r}\nAUTHOR="gpt-6"\nPARENT_MODULE={str(next((Path(rec["fix"])/"before").glob("*.py")))!r}\nclass Drawing(Solo48):\n    icon_id={rec["icon_id"]!r}\n    keyshape=Keyshape.{shape}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="primitives-generate"\n    aliases=()\n    keywords={tuple(concept.split())!r}\n'+HELPERS+'\n    def build(self):\n'+textwrap.indent(BODIES[i],'        ')
    module.write_text(source);icon=load_icon(module);svg=icon.to_svg();(run/(rec['icon_id']+'.svg')).write_text(svg);report=icon.validate_icon();(run/'validation.txt').write_text(report.describe());render_previews(svg,rec['icon_id'],48,run)
    for kind in ('original','before'):shutil.copyfile(Path(rec['fix'])/(kind+'.png'),run/(kind+'.png'))
    rec.update(run=str(run),module=str(module),note=change);print(i,rec['icon_id'],report.status,len(report.errors),len(report.warnings),flush=True)
 (BATCH/'authored.json').write_text(json.dumps(claims,indent=2))
def sheets():
 for start in range(0,len(claims),5):
    im=Image.new('RGB',(840,5*230),'#ddd');d=ImageDraw.Draw(im)
    for row,rec in enumerate(claims[start:start+5]):
        y=row*230;run=Path(rec['run']);d.text((8,y+2),f"{rec['index']} {rec['icon_id']}",fill='black')
        for col,name in enumerate(['original.png','before.png','preview-light-384.png','preview-dark-384.png']):
            pic=Image.open(run/name).convert('RGB');pic.thumbnail((174,174));im.paste(pic,(8+col*206,y+26))
        for col,theme in enumerate(['light','dark']):im.paste(Image.open(run/f'preview-{theme}-48.png').convert('RGB'),(420+col*206,y+178))
    im.save(BATCH/f'after-{start//5}.png')
if __name__=='__main__':author();sheets()
