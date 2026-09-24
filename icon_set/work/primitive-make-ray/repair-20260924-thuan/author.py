from pathlib import Path
import json
AUTHOR='gpt-6'
# Each input's exact SOURCE_ICON_ID and SOURCE_PATH is retained in batch.json and emitted module.
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch.json').read_text())
HELPER='''        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                k,end,*args=c; name=f'{n}-{j}'
                if k=='L': self.add_line(name,here,end)
                elif k=='A': self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif k=='C': self.add_bezier(name,here,(args[0],args[1],end))
                here=end; members.append(name)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
D=[]
def add(shape,note,code):D.append((shape,note,code))
add('SQUARE','Rounded muzzle and open jaw, pointed ear and separate ball; natural side-view asymmetry.',"""
path('head',(42,16),[('A',(38,6),12,12,False),('L',(34,14)),('L',(27,14)),('A',(21,18),6,4,False),('L',(16,18)),('A',(16,28),5,5,False),('L',(26,28)),('A',(26,36),4,4,True),('L',(24,38)),('A',(32,38),4,3,False),('L',(36,36)),('L',(42,42))])
circle('ball',12,36,6)
""")
add('HRECT_L','Flowing leaping dog silhouette and open vertical hoop; retain directional pose.',"""
path('hoop',(14,8),[('A',(4,24),10,16,False),('A',(14,40),10,16,False)])
path('dog',(4,24),[('L',(30,16)),('L',(34,8)),('L',(38,16)),('L',(44,18)),('A',(38,24),6,6,True),('L',(32,24)),('A',(38,30),6,6,True),('A',(34,34),4,4,True),('L',(26,28)),('L',(18,30)),('A',(12,38),6,8,False)])
join('hoop','dog')
""")
add('SQUARE','Smooth sitting dog with lifted forepaw, muzzle, pointed ear and curved tail.',"""
path('dog',(28,18),[('A',(24,6),8,12,False),('L',(20,12)),('L',(10,14)),('A',(16,22),6,8,False),('L',(20,22)),('L',(20,30)),('L',(12,26)),('A',(8,32),4,4,False),('L',(18,38)),('L',(26,38)),('L',(24,42)),('L',(32,42)),('A',(38,30),6,12,False),('L',(28,18))],True)
path('tail',(38,30),[('A',(42,18),4,12,False)])
join('dog','tail')
""")
add('SQUARE','Round dog head and muzzle above a cupped human hand; remove angular fist.',"""
path('dog',(42,30),[('L',(42,16)),('A',(26,16),8,10,False),('L',(18,16)),('A',(24,24),6,8,False),('L',(28,24)),('L',(28,34))])
path('hand',(6,30),[('L',(12,30)),('L',(20,34)),('L',(32,34)),('A',(32,42),4,4,True),('L',(20,42)),('L',(6,38))])
join('dog','hand')
""")
add('SQUARE','Round muzzle and pointed ear above recovery cone; two visible neck edges.',"""
poly('cone',(6,30),(42,14),(36,34),(20,42),(6,30))
path('head',(14,26),[('L',(14,20)),('A',(22,14),8,6,True),('L',(22,6)),('A',(34,18),12,12,True)])
join('head','cone')
line('neck',(36,34),(42,42));join('neck','cone')
""")
add('SQUARE','Restore bass waist, continuous rounded body and long diagonal neck.',"""
path('body',(28,18),[('C',(18,20),(24,12),(18,12)),('C',(12,24),(18,26),(14,26)),('C',(6,32),(8,20),(6,26)),('C',(18,42),(6,38),(12,42)),('C',(26,34),(26,42),(30,38)),('C',(30,28),(22,30),(26,28)),('C',(28,18),(38,28),(36,22))],True)
poly('neck',(28,18),(40,6),(42,8));join('body','neck')
""")
add('SQUARE','Capsule mouse and two curved right-click waves.',"""
path('mouse',(6,26),[('A',(18,14),12,12,True),('A',(30,26),12,12,True),('L',(30,30)),('A',(6,30),12,12,True),('L',(6,26))],True)
poly('button',(18,14),(18,26),(30,26));join('button','mouse')
path('wave-inner',(28,6),[('A',(34,14),10,12,True)])
path('wave-outer',(38,6),[('A',(42,22),26,28,True)])
""")
add('VRECT_L','Matched hooks, round beads and symmetric diamond drops using shared series geometry.',"""
for x in (15,33):
 n=f'earring-{x}'
 path(n+'-hook',(x-5,10),[('A',(x+5,10),5,6,True),('A',(x,16),5,6,True)])
 circle(n+'-bead',x,19,3)
 poly(n+'-drop',(x,22),(x+7,33),(x,44),(x-7,33),(x,22))
 join(n+'-hook',n+'-bead');join(n+'-bead',n+'-drop')
""")
add('VRECT_L','Circular globe inside curved meridian with stable pedestal.',"""
circle('globe',20,16,12)
path('meridian',(36,4),[('C',(24,36),(46,18),(40,36)),('C',(8,32),(18,36),(12,35))])
line('stem',(24,36),(24,44));poly('base',(12,44),(24,44),(36,44));join('stem','base');join('stem','meridian')
""")
add('HRECT_L','Eight curved mirrored legs and distinct round head and abdomen.',"""
circle('head',24,16,8)
path('abdomen',(24,24),[('A',(24,40),8,8,True),('A',(24,24),8,8,True)],True)
join('head','abdomen')
for s in (-1,1):
 def p(x,y):return (24+s*x,y)
 for j,(start,end,c1,c2) in enumerate([(p(8,16),p(12,8),p(12,16),p(12,12)),(p(8,16),p(20,16),p(14,24),p(18,22)),(p(8,32),p(20,32),p(14,24),p(18,26)),(p(8,32),p(12,40),p(12,32),p(12,36))]):
  path(f'leg-{s}-{j}',start,[('C',end,c1,c2)]);join(f'leg-{s}-{j}','head' if j<2 else 'abdomen')
 for a,b in [(0,1),(2,3)]:join(f'leg-{s}-{a}',f'leg-{s}-{b}')
""")
add('SQUARE','Balanced crossed x and smooth superscript two.',"""
poly('x-a',(6,22),(15,32),(24,42));poly('x-b',(6,42),(15,32),(24,22));join('x-a','x-b')
path('two',(30,10),[('A',(36,6),6,5,True),('A',(42,12),6,6,True),('C',(32,22),(42,16),(34,19)),('L',(42,22))])
""")
add('SQUARE','Almond eye with circular iris and separate round contact lens.',"""
path('eye',(18,14),[('C',(30,6),(22,8),(26,6)),('C',(42,18),(36,6),(40,12)),('C',(28,30),(38,26),(34,30))])
circle('iris',30,18,3)
circle('lens',15,33,9)
""")
add('SQUARE','Rounded diagonal medicine bottle, broad nozzle and teardrop.',"""
path('bottle',(18,16),[('L',(32,6)),('A',(36,8),4,4,True),('L',(42,20)),('A',(40,24),4,4,True),('L',(28,30)),('L',(14,24)),('L',(18,16))],True)
line('collar',(18,16),(28,30));join('collar','bottle')
path('drop',(10,32),[('C',(6,38),(8,34),(6,36)),('A',(14,38),4,4,False),('C',(10,32),(14,36),(12,34))],True)
""")
add('SQUARE','Coherent diagonal pipette with round bulb and separate round sample.',"""
path('tool',(24,14),[('L',(30,8)),('A',(40,18),7,7,True),('L',(34,24)),('L',(16,34)),('L',(6,36)),('L',(8,26)),('L',(24,14))],True)
poly('collar',(18,6),(24,14),(34,24));join('collar','tool')
circle('sample',37,37,5)
""")
add('SQUARE','Round bulb and diagonal pipette over a smooth open pointed outline.',"""
path('tool',(28,12),[('L',(34,6)),('A',(42,14),6,6,True),('L',(26,30)),('L',(20,32)),('L',(22,24)),('L',(28,18)),('L',(28,12))],True)
poly('collar',(22,8),(28,14),(36,22));join('collar','tool')
path('outline',(12,22),[('A',(6,28),6,6,False),('C',(16,42),(6,34),(12,40)),('L',(22,38))])
""")
add('HRECT_L','Smooth upward accelerating arc with aligned broken tail and arrowhead.',"""
path('shaft',(18,36),[('C',(38,8),(30,30),(38,18))])
poly('head',(32,14),(38,8),(44,14));join('shaft','head')
line('dash-1',(4,40),(6,40));line('dash-2',(12,38),(13,38))
""")
add('VRECT_L','Flamingo with arched back, long S neck, beak and bent leg.',"""
path('bird',(8,28),[('C',(26,24),(12,16),(20,18)),('L',(26,10)),('A',(36,10),5,6,True),('L',(40,12)),('L',(32,12)),('L',(32,24)),('A',(20,34),12,10,True),('L',(8,28))],True)
line('leg',(20,34),(20,44));join('bird','leg')
poly('bent-leg',(20,34),(12,40),(20,40));join('bird','bent-leg');join('leg','bent-leg')
""")
add('SQUARE','Smooth scalloped foam, rounded mug, two spaced ribs and generous handle.',"""
path('body',(6,18),[('L',(6,38)),('A',(10,42),4,4,False),('L',(30,42)),('A',(34,38),4,4,False),('L',(34,30)),('L',(34,18))])
path('foam',(6,18),[('A',(10,10),5,5,True),('A',(22,6),8,5,True),('A',(30,10),6,5,True),('A',(34,18),5,5,True),('L',(18,18)),('A',(6,18),6,4,True)])
path('handle',(34,18),[('A',(34,30),8,6,True)])
join('body','foam');join('body','handle');join('foam','handle')
for x in (15,25):line(f'rib-{x}',(x,27),(x,33))
""")
add('HRECT_L','Anatomical ankle and continuous heel, arch and rounded toes; omit extraction specks.',"""
path('foot',(10,8),[('L',(10,20)),('C',(4,34),(10,28),(4,28)),('C',(16,38),(4,42),(10,40)),('C',(32,38),(22,34),(26,38)),('L',(38,38)),('A',(38,28),6,5,False),('C',(24,18),(32,28),(24,22)),('L',(24,8))])
""")
add('VRECT_M','Sole silhouette with round toe contours and broad reflexology regions.',"""
path('sole',(10,16),[('A',(22,10),6,10,True),('A',(30,10),4,4,True),('A',(38,18),8,8,True),('L',(36,24)),('L',(34,32)),('A',(24,44),10,12,True),('A',(10,32),14,12,True),('L',(10,24)),('L',(10,16))],True)
path('arch',(10,24),[('C',(24,20),(16,24),(20,24)),('C',(36,24),(28,24),(32,24))]);join('arch','sole')
line('heel',(10,32),(34,32));join('heel','sole')
""")
for r,(shape,note,code) in zip(rows,D):
 run=Path(r['result_dir']);uid=r['source_uuid'];iid=r['icon_id'];r.update(keyshape=shape,note=note)
 src=f'''"""{note}\nPlan: named coherent contours; paired features derive from shared parameters.\nReference: supplied original plus rejected production SVG.\nLucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).\nHuman parts: human_ref/full_body_ref.png; no detached human head in these subjects.\n"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={uid!r}
SOURCE_PATH={r['reference_path']!r}
AUTHOR={AUTHOR!r}
class Drawing(Solo48):
    icon_id={iid!r}
    keyshape=Keyshape.{shape}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=({r['concept']!r},)
    def build(self):
'''+HELPER+'\n'.join('        '+l for l in code.strip().splitlines())+'\n'
 (run/(iid.replace('-','_')+'_'+uid.replace('-','_')+'.py')).write_text(src)
(ROOT/'batch.json').write_text(json.dumps(rows,indent=2))
