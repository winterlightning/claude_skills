from pathlib import Path
import json, re, textwrap,sys
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
BATCH=Path(__file__).parent
runs=sorted((ROOT/'icon_set/work/primitive-fix-thuan').glob('*/20260924T160658Z-thuan-mac'))
HELPERS='''
        def path(n,p,steps,closed=False):
            members=[]
            for i,s in enumerate(steps):
                k,q,*a=s; m=f'{n}-{i}'
                if k=='L': self.add_line(m,p,q)
                elif k=='A': self.add_arc(m,p,q,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='C': self.add_bezier(m,p,(a[0],a[1],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
'''
def author(i,keyshape,plan,body,reference='No useful exact Lucide match; shared geometric construction.',omissions='None'):
 r=runs[i];item=json.loads((r/'claim.json').read_text())['item'];ref=next((r/'reference').glob('*.svg')).relative_to(ROOT)
 uuid=re.search(r'[0-9a-f-]{36}$',ref.stem)[0];concept=ref.stem[:-37];icon=item['icon_id']
 out=ROOT/'icon_set/work/primitive-make-ray'/uuid/'20260924T160658Z-thuan-mac-centerlines';out.mkdir(parents=True,exist_ok=True)
 metadata=dict(concept=concept,source_uuid=uuid,reference_path=str(ref),icon_id=icon,author=AUTHOR,keyshape=keyshape,plan=plan,construction_reference=reference,omissions=omissions)
 (out/f'{icon}.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
 mod=out/(icon.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
 mod.write_text(repr(plan+'\nConstruction: '+reference+'\nOmissions: '+omissions)+'\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n'+f'SOURCE_ICON_ID = {uuid!r}\nSOURCE_PATH = {str(ref)!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {icon!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(icon.split("-"))!r}\n\n    def build(self):\n'+HELPERS+textwrap.indent(textwrap.dedent(body).strip()+'\n','        '))
 return out

author(0,'HRECT_L','Front-facing brassiere. Mirrored teardrop cups, shared axis x24; straps and bridge join at explicit nodes. Bounds (4,8)-(44,40).', '''
for k in range(2):
 def p(x,y): return (x if k==0 else 48-x,y)
 path(f'cup-{k}',p(6,22),[('C',p(20,33),p(13,22),p(20,27)),('C',p(12,40),p(20,37),p(16,40)),('C',p(4,32),p(7,40),p(4,37)),('C',p(6,22),p(4,28),p(6,25))],True)
 line(f'strap-{k}',p(6,8),p(6,22));join(f'strap-{k}',f'cup-{k}')
line('bridge',(20,33),(28,33));join('bridge','cup-0');join('bridge','cup-1')
''')
author(1,'VRECT_L','Symmetric light bulb; broad glass dome flows smoothly into a narrow neck and rounded base. Bounds (8,4)-(40,44).','''
path('bulb',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True),('C',(32,34),(40,27),(32,28)),('L',(32,40)),('A',(28,44),4,4,True),('L',(20,44)),('A',(16,40),4,4,True),('L',(16,34)),('C',(8,20),(16,28),(8,27))],True)
line('base-seam',(16,34),(32,34));join('base-seam','bulb')
''','Lucide lightbulb: circular dome and smooth narrowing shoulder.','Filament absent in source.')
author(2,'VRECT_L','Ice cream scoop above a tapered cone. Circular dome, mirrored lip lobes and straight cone sides. Bounds (8,4)-(40,44).','''
path('scoop',(12,16),[('A',(24,4),12,12,True),('A',(36,16),12,12,True),('C',(40,21),(36,19),(40,18)),('A',(35,26),5,5,True),('L',(13,26)),('A',(8,21),5,5,True),('C',(12,16),(8,18),(12,19))],True)
poly('cone',(13,26),(24,44),(35,26));join('cone','scoop')
''','Lucide ice-cream-cone: coherent scoop and tapered cone.','Small lower scallops simplified into the scoop lip.')
author(3,'HRECT_M','Teacup with flat rim, rounded bowl and right loop handle. Bowl sides tangent to quarter circles. Bounds (4,10)-(44,38).','''
path('cup',(4,10),[('L',(32,10)),('L',(32,14)),('L',(32,28)),('A',(18,38),14,10,True),('A',(4,28),14,10,True),('L',(4,10))],True)
path('handle',(32,14),[('A',(44,21),12,7,True),('A',(32,28),12,7,True)]);join('handle','cup')
''','Lucide coffee: quarter-circle bowl and continuous external handle.')
author(4,'VRECT_L','Grenade with rounded body, central meridian, horizontal groove and safety ring. Cap and ring share exact nodes. Bounds (8,4)-(40,44).','''
path('body',(20,16),[('A',(32,30),12,14,True),('A',(20,44),12,14,True),('A',(8,30),12,14,True),('A',(20,16),12,14,True)],True)
poly('cap',(20,16),(12,16),(12,4),(28,4),(28,6),(28,16),closed=True);join('cap','body')
line('meridian',(20,16),(20,44));join('meridian','body')
poly('groove',(8,30),(20,30),(32,30));join('groove','body');join('groove','meridian')
path('ring',(28,6),[('A',(40,18),12,12,True),('A',(32,30),8,12,True)]);join('ring','cap');join('ring','body')
''',omissions='Dense segmentation reduced to one meridian and one cross groove.')
author(5,'SQUARE','Sea dragon sigil with long swept horn, projecting jaw and coiled body. Smooth neck and tail; intentional directional asymmetry. Bounds (6,6)-(42,42).','''
path('dragon',(15,20),[('L',(9,23)),('L',(6,17)),('L',(18,12)),('L',(38,6)),('L',(30,14)),('C',(42,24),(38,16),(42,20)),('C',(12,34),(42,31),(12,25)),('C',(27,42),(12,40),(19,42)),('C',(42,32),(36,42),(42,38))])
''',omissions='Double neck outline reduced to one smooth S-shaped stroke to keep the coil open at 48px.')
author(6,'SQUARE','Shopping cart. Straight sloped basket walls, continuous left handle slope, equal round wheels at one baseline. Bounds (6,6)-(42,42).','''
poly('handle',(6,6),(12,6),(14,14))
poly('basket',(14,14),(42,14),(38,28),(18,28),closed=True);join('handle','basket')
for i,x in enumerate((20,36)):circle(f'wheel-{i}',x,39,3)
''','Lucide shopping-cart: basket rails and equal wheel circles.')
author(7,'SQUARE','Bumper car side silhouette. Single rounded nose flowing into the seat recess, high rear body and vertical power pole. Bounds (6,6)-(42,42).','''
path('bumper',(10,34),[('L',(38,34)),('A',(42,38),4,4,True),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('A',(10,34),4,4,True)],True)
path('body',(10,34),[('C',(18,22),(10,26),(12,22)),('L',(20,22)),('A',(24,26),4,4,False),('L',(28,26)),('A',(32,22),4,4,False),('L',(32,20)),('A',(38,14),6,6,True),('L',(42,14)),('L',(42,34)),('L',(38,34))]);join('body','bumper')
line('pole',(42,6),(42,14));join('pole','body')
''')
author(8,'SQUARE','Perspective soap bar behind a broad foam outline. Straight box edges and circular lather lobes. Bounds (6,6)-(42,42).','''
poly('bar',(6,30),(6,16),(22,6),(42,6),(42,28),(36,32))
poly('top',(6,16),(28,16),(42,6));join('top','bar')
line('edge',(28,16),(28,28));join('edge','top')
path('foam',(6,30),[('A',(14,22),8,8,True),('A',(22,30),8,8,True),('A',(28,28),6,6,True),('A',(36,32),8,6,True),('A',(42,37),6,5,True),('A',(24,42),18,5,True),('A',(6,37),18,5,True),('L',(6,30))],True)
join('foam','bar');join('foam','edge')
''','Lucide cloud: coherent rounded foam lobes.','Lower soap edges hidden behind foam.')
author(9,'SQUARE','Sonic hedgehog head in three-quarter view. Swept curved spines, projecting muzzle, pointed ear and oval eye. Bounds (6,6)-(42,42).','''
path('head',(10,20),[('L',(10,8)),('L',(19,12)),('C',(39,6),(25,8),(33,6)),('L',(35,16)),('C',(42,23),(39,17),(42,20)),('L',(35,26)),('C',(42,35),(40,29),(42,32)),('C',(26,42),(35,36),(33,42)),('L',(18,42)),('A',(6,30),12,12,True),('L',(10,28)),('L',(10,20))],True)
line('eye-left',(19,22),(19,23))
line('eye-right',(27,22),(27,23))
path('smile',(18,33),[('C',(28,32),(22,34),(25,34))])
''',omissions='Fine eye/muzzle partition and second pupil omitted to keep the face open at 48px.')
author(10,'SQUARE','Steaming car with raised hood. Connected roof/body silhouette, equal round wheels, raised hood and one steam stroke. Bounds (6,6)-(42,42).','''
path('body',(9,37),[('L',(6,37)),('L',(6,28)),('L',(15,17)),('L',(24,17)),('L',(32,25)),('L',(38,28)),('A',(42,32),4,4,True),('L',(42,37)),('L',(39,37))])
for n,x in [('rear',14),('front',34)]:circle(n,x,37,5);join(n,'body')
line('sill',(19,37),(29,37));join('sill','rear');join('sill','front')
line('hood',(32,25),(42,21));join('hood','body')
path('steam',(36,6),[('C',(36,13),(31,9),(40,10))])
''','Lucide car: wheels share the body sill and the body stays continuous.','Inset window and second steam wisp omitted for clearance.')
author(11,'SQUARE','Shop with three scalloped awning panels over a centered doorway. Shared panel width and mirror symmetry. Bounds (6,6)-(42,42).','''
path('awning',(6,18),[('L',(10,6)),('L',(38,6)),('L',(42,18)),('A',(30,18),6,6,True),('A',(18,18),6,6,True),('A',(6,18),6,6,True)],True)
for x in (18,30):line(f'seam-{x}',(x,6),(x,18));join(f'seam-{x}','awning')
poly('shop',(12,24),(12,42),(20,42),(28,42),(36,42),(36,24));join('shop','awning')
poly('door',(20,42),(20,33),(28,33),(28,42));join('door','shop')
''','Lucide store: consistent repeated scallops and centered entrance.')
author(12,'HRECT_L','Sun setting over three horizontal water waves. All waves share one smooth cubic pattern and a 10-unit vertical step. Bounds (4,8)-(44,40).','''
for i,y in enumerate((20,30,40)):
 path(f'wave-{i}',(4,y),[('C',(14,y-2),(8,y),(8,y-2)),('C',(24,y),(20,y-2),(20,y)),('C',(34,y-2),(28,y),(28,y-2)),('C',(44,y),(40,y-2),(40,y))])
path('sun',(14,18),[('A',(24,8),10,10,True),('A',(34,18),10,10,True)]);join('sun','wave-0')
''',omissions='None; wave amplitude kept shallow for spacing.')
author(13,'HRECT_L','Sydney Opera House. Three distinct curved shells rise from a straight podium, tallest at the center. Bounds (4,8)-(44,40).','''
poly('podium',(4,32),(14,32),(26,32),(40,32),(44,32),(44,40),(4,40),closed=True)
path('left-shell',(14,32),[('L',(8,18)),('C',(26,32),(17,19),(23,24))]);join('left-shell','podium')
path('middle-shell',(26,32),[('L',(20,8)),('C',(34,24),(30,10),(34,18))]);join('middle-shell','podium')
path('right-shell',(26,32),[('C',(34,24),(28,28),(30,25)),('C',(44,22),(37,23),(40,22)),('L',(40,32))]);join('right-shell','podium');join('right-shell','middle-shell')
''',omissions='Smallest rear shell omitted to retain clear separation.')
author(14,'VRECT_L','Three round berries in a triangular cluster with a curved stem and pointed leaf. Equal circular upper berries. Bounds (8,4)-(40,44).','''
circle('left',16,28,8);circle('right',32,28,8);join('left','right')
path('bottom',(16,36),[('A',(32,36),8,8,False)]);join('bottom','left');join('bottom','right')
path('stem',(24,28),[('L',(24,12)),('C',(14,4),(24,8),(18,4))]);join('stem','left');join('stem','right')
path('leaf',(24,12),[('C',(40,4),(26,4),(34,4)),('C',(24,12),(40,12),(30,16))],True);join('leaf','stem')
''','Lucide grape: shared berry radii and coherent clustered fruit.')
author(15,'HRECT_L','Tracked bulldozer with sloping cab roof front, continuous engine body, capsule track and curved blade. Bounds (4,8)-(44,40).','''
path('track',(9,30),[('L',(10,30)),('L',(25,30)),('A',(30,35),5,5,True),('A',(25,40),5,5,True),('L',(9,40)),('A',(4,35),5,5,True),('A',(9,30),5,5,True)],True)
poly('cab',(10,30),(10,20),(14,20),(14,8),(24,8),(29,20),(30,20),(30,30),(25,30));join('cab','track')
line('arm',(30,30),(40,30));join('arm','cab')
path('blade',(42,18),[('C',(40,30),(41,22),(40,26)),('C',(44,40),(40,35),(42,38)),('L',(38,40)),('L',(38,20)),('L',(42,18))],True);join('blade','arm')
''','Lucide car: unified vehicle outline and round track ends.','Track rollers and inset cab window omitted.')
author(16,'SQUARE','Three equal circular atoms form a triangle joined by three exact straight bonds. Bounds (6,6)-(42,42).','''
# Cardinal circle nodes keep all bonds attached exactly.
circle('left',12,24,6);circle('top',36,12,6);circle('bottom',36,36,6)
line('upper-bond',(12,18),(30,12));join('upper-bond','left');join('upper-bond','top')
line('lower-bond',(12,30),(30,36));join('lower-bond','left');join('lower-bond','bottom')
line('right-bond',(36,18),(36,30));join('right-bond','top');join('right-bond','bottom')
''')
author(17,'SQUARE','Two falling bombs staggered diagonally. Each has an elongated capsule body and identical straight tail fins. Bounds (6,6)-(42,42).','''
for i,(x,y) in enumerate(((6,6),(30,18))):
 path(f'bomb-{i}',(x,y+14),[('A',(x+6,y+8),6,6,True),('A',(x+12,y+14),6,6,True),('L',(x+12,y+18)),('A',(x+6,y+24),6,6,True),('A',(x,y+18),6,6,True),('L',(x,y+14))],True)
 poly(f'fins-{i}',(x,y+14),(x,y),(x+6,y+4),(x+12,y),(x+12,y+14));join(f'fins-{i}',f'bomb-{i}')
''')
author(18,'HRECT_M','Upward zigzag trend arrow with equal 45-degree rising and falling segments and a square arrowhead. Bounds (4,10)-(44,38).','''
poly('trend',(4,38),(18,24),(24,30),(44,10))
poly('head',(28,10),(44,10),(44,26));join('trend','head')
''','Lucide trending-up: straight zigzag diagonals and equal arrowhead arms.')
author(19,'VRECT_L','Symmetric utility pail with elliptical opening, straight tapered sides, smooth base and semicircular bail handle. Bounds (8,4)-(40,44).','''
path('rim',(8,24),[('A',(40,24),16,5,True),('A',(8,24),16,5,True)],True)
path('pail',(8,24),[('L',(12,40)),('C',(24,44),(13,44),(18,44)),('C',(36,40),(30,44),(35,44)),('L',(40,24))]);join('pail','rim')
path('handle',(8,24),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,24))]);join('handle','rim')
''')
