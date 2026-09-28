from pathlib import Path
import json
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=[r['uuid'] for r in rows]
SOURCE_PATH=[r['ref'] for r in rows]
helper='''
    def path(self,n,p,ops,closed=False):
        members=[]
        for i,(kind,q,*v) in enumerate(ops):
            eid=f'{n}-{i}'
            if kind=='L': self.add_line(eid,p,q)
            elif kind=='A': self.add_arc(eid,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C': self.add_bezier(eid,p,(v[0],v[1],q))
            members.append(eid);p=q
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def join(self,a,b): self.relate('connect',a,b)
'''
bodies=[
# 0 sync
'''        # Two rotationally paired elliptical sweeps; straight, mirrored A strokes.
        self.path('upper',(6,19),[('A',(42,19),18,13,True)])
        self.add_polyline('upper-head',(36,19),(42,19),(42,13));self.join('upper','upper-head')
        self.path('lower',(42,29),[('A',(6,29),18,13,True)])
        self.add_polyline('lower-head',(12,29),(6,29),(6,35));self.join('lower','lower-head')
        self.add_polyline('a',(17,31),(18,29),(24,17),(30,29),(31,31))
        self.add_line('crossbar',(18,29),(30,29));self.join('a','crossbar')
''',
# 1 bulb
'''        # Root owns a circular dial arc, centered bulb, and detached dial indicator.
        self.path('dial',(6,24),[('A',(24,6),18,18,True),('A',(39,14),18,18,True)])
        self.path('bulb',(14,23),[('A',(28,23),7,7,True),('C',(26,32),(28,27),(26,28)),('L',(26,34)),('A',(21,39),5,5,True),('A',(16,34),5,5,True),('L',(16,32)),('C',(14,23),(16,28),(14,27))],True)
        self.add_line('contact',(21,39),(21,42));self.join('bulb','contact')
        self.circle('indicator',39,30,3)
''',
# 2 yoga
'''        # Suspension has straight sides, with a tangent return. The folded leg and
        # torso share a hip. Human reference: full_body_ref.png. Neck (28,39),
        # head (39,39), r3: 11-3-4=4 visible gap; upper torso points right.
        self.add_line('strap-left',(18,6),(12,36))
        self.path('strap-right',(26,6),[('L',(24,18)),('C',(14,26),(23,24),(20,26)),('L',(14,26))])
        self.path('folded-leg',(16,16),[('C',(6,26),(9,16),(6,20)),('L',(6,36)),('A',(12,42),6,6,False),('C',(16,36),(16,42),(18,40)),('L',(12,36))])
        self.join('folded-leg','strap-left');self.join('strap-right','strap-left')
        self.path('body',(24,18),[('C',(31,26),(28,18),(34,22)),('C',(24,35),(29,30),(24,31)),('A',(28,39),4,4,False)])
        self.join('body','strap-right')
        self.circle('head',39,39,3)
        self.mark_human_figure('person',head='head',torso='body-2',torso_junction='end')
''',
#3 media
'''        # Three equal hexagons on a triangular plan, central play mark, three arrows.
        self.add_polyline('play',(19,17),(31,24),(19,31),closed=True)
        for n,x,y in [('top',24,7),('left',9,37),('right',39,37)]:
            self.add_polyline(n,(x,y-5),(x+5,y-2),(x+5,y+2),(x,y+5),(x-5,y+2),(x-5,y-2),closed=True)
        self.add_polyline('left-arrow',(9,14),(4,18),(9,22))
        self.add_polyline('right-arrow',(39,14),(44,18),(39,22))
        self.add_polyline('bottom-arrow',(20,38),(24,42),(28,38))
''',
#4 angel
'''        # A shared axis owns heart lobes, halo, and mirrored wings.
        self.path('halo',(16,10),[('A',(32,10),8,4,True),('A',(16,10),8,4,True)],True)
        self.path('heart',(24,28),[('C',(14,28),(24,20),(14,20)),('C',(24,40),(14,33),(19,37)),('C',(34,28),(29,37),(34,33)),('C',(24,28),(34,20),(24,20))],True)
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.path(n,p(14,28),[('C',p(6,28),p(14,20),p(6,20)),('L',p(6,38)),('A',p(14,38),4,4,s<0),('L',p(14,35))])
            self.join('heart',n)
''',
#5 arduino
'''        # One continuous infinity stroke: tangent directions cross diagonally.
        self.path('infinity',(14,10),[('A',(4,24),10,14,False),('A',(14,38),10,14,False),('C',(34,10),(23,38),(25,10)),('A',(44,24),10,14,True),('A',(34,38),10,14,True),('C',(14,10),(25,38),(23,10))],True)
        self.add_line('minus',(12,24),(15,24))
        self.add_line('plus-horizontal',(32,24),(36,24))
        self.add_line('plus-vertical',(34,22),(34,26));self.join('plus-horizontal','plus-vertical')
''',
#6 profile
'''        # Puzzle piece owns the round tab; continuous profile owns brow, nose,
        # jaw and neck. Deliberate asymmetric side view, no detached human head.
        self.path('piece',(6,16),[('A',(16,6),10,10,True),('L',(22,6)),('L',(22,16)),('L',(18,16)),('A',(10,16),4,4,True),('L',(6,16))],True)
        self.path('profile',(16,42),[('L',(16,39)),('C',(10,29),(16,35),(10,34)),('L',(20,29)),('A',(30,29),5,5,False),('L',(32,29)),('L',(32,14)),('C',(38,25),(36,15),(38,20)),('L',(42,30)),('L',(38,30)),('L',(38,34)),('A',(34,38),4,4,True),('L',(30,38)),('L',(30,42))])
''',
#7 car
'''        # Four equal circular sensor quadrants. Mirrored roof and true circular wheels.
        for ix in (0,1):
            for iy in (0,1):
                def p(x,y):return (48-x if ix else x,48-y if iy else y)
                self.add_arc(f'sensor-{ix}-{iy}',p(6,18),p(18,6),radius_x=12,sweep=ix==iy)
        self.path('roof',(14,29),[('L',(14,26)),('C',(19,21),(14,23),(17,24)),('C',(22,18),(20,19),(20,18)),('L',(26,18)),('C',(29,21),(28,18),(28,19)),('C',(34,26),(31,24),(34,23)),('L',(34,29))])
        self.circle('left-wheel',17,29,3);self.circle('right-wheel',31,29,3)
        self.add_line('chassis',(20,29),(28,29))
        for n in ['left-wheel','right-wheel']:
            self.join('roof',n);self.join('chassis',n)
''',
#8 rider
'''        # Equal wheel circles, circular head, right-angle parcel, smooth seated hip.
        # Shared human reference full_body_ref.png. Neck20-headBottom12=8 CL /4 ink.
        self.circle('head',24,9,3)
        self.circle('rear-wheel',9,39,3);self.circle('front-wheel',39,39,3)
        self.add_polyline('parcel',(6,16),(14,16),(14,24),(6,24),closed=True)
        self.add_line('torso',(24,20),(24,25))
        self.path('leg',(24,25),[('A',(27,28),3,3,False),('A',(30,31),3,3,True)])
        self.add_line('arm',(24,20),(38,20))
        self.add_line('fork',(38,20),(39,36))
        self.add_line('frame',(12,39),(36,39))
        for a,b in [('torso','leg'),('torso','arm'),('arm','fork'),('fork','front-wheel'),('frame','front-wheel'),('frame','rear-wheel')]:self.join(a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''',
#9 axe
'''        # Straight diagonal shaft. Blade has one smooth cutting ellipse and
        # two flowing concave shoulders; angular collar remains intentional.
        self.add_line('shaft',(6,42),(24,24))
        self.path('blade',(24,24),[('L',(18,18)),('L',(30,6)),('C',(42,18),(30,14),(36,18)),('A',(26,38),16,20,True),('C',(24,24),(28,32),(28,28))],True)
        self.join('shaft','blade')
'''
]
refs=['refresh-cw','lightbulb','human_ref/full_body_ref.png (no exact Lucide pose)','no useful exact Lucide match; reference three-way layout','heart','infinity','puzzle and human profile reference','car-front','bike and human_ref/full_body_ref.png','axe']
for i,(r,b) in enumerate(zip(rows,bodies)):
 p=Path(r['dir'])/(r['id'].replace('-','_')+'_'+r['uuid'].replace('-','_')+'.py')
 ks='HRECT_M' if i==5 else ('HRECT_L' if i==3 else 'SQUARE')
 header=f'''"""{r['id']}. Reconstructed clean centerlines from the original reference.
Construction reference: {refs[i]}. Keyshape {ks} chosen for the composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={r['uuid']!r}
SOURCE_PATH={r['ref']!r}
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id={r['id']!r}
    keyshape=Keyshape.{ks}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords={tuple(r['id'].split('-'))!r}
    def build(self):
'''
 p.write_text(header+b+helper)
