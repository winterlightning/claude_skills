from pathlib import Path
import json,re
B=Path(__file__).parent
allrows=json.loads((B/'sources.json').read_text());rows=[allrows[i] for i in [0,1,2,3,4,5,6,8,9,11]]
HELPERS='''
    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';end=c[1]
            if c[0]=='L':self.add_line(k,start,end)
            elif c[0]=='A':self.add_arc(k,start,end,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,start,(c[2],c[3],end))
            ids.append(k);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
'''
bodies=[
'''        self.path('pin',(10,18),[('A',(38,18),14,14,True),('C',(24,36),(38,24),(30,31)),('C',(10,18),(18,31),(10,24))],True)
        self.circle('opening',24,18,5)
        self.add_line('baseline',(12,44),(36,44))
''',
'''        self.path('basket',(38,14),[('L',(6,14)),('L',(9,23)),('A',(13,26),4,4,False),('L',(34,26)),('L',(38,14))],True)
        self.path('handle',(38,14),[('L',(40,8)),('A',(42,6),2,2,True)])
        self.relate('connect','handle','basket')
        self.path('support',(34,26),[('A',(34,34),4,4,True),('L',(14,34))])
        self.relate('connect','support','basket')
        for x in (14,34):
            self.path(f'wheel-{x}',(x,34),[('A',(x,42),4,4,True),('A',(x,34),4,4,True)],True)
            self.relate('connect','support',f'wheel-{x}')
''',
'''        # Mirrored fuselage: seven-unit straight nose before swept wings.
        right=[(29,11),(29,18),(42,26),(42,34),(29,28),(29,33),(35,36),(35,42),(24,38)]
        points=right+[(48-x,y) for x,y in reversed(right[:-1])]
        self.path('plane',points[0],[('L',p) for p in points[1:]]+[('A',points[0],5,5,True)],True)
''',
'''        # Flat mortarboard, visible cap band, open face and V-shaped gown.
        self.add_polyline('board',(8,12),(24,4),(40,12),(24,20),(8,12))
        self.add_polyline('cap-band',(14,15),(14,22),(34,22),(34,15))
        self.relate('connect','board','cap-band')
        self.add_arc('jaw',(34,22),(14,22),radius_x=10)
        self.relate('connect','jaw','cap-band')
        self.add_line('tassel',(8,12),(8,26));self.relate('connect','board','tassel')
        self.path('shoulders',(8,44),[('C',(16,36),(8,40),(12,36)),('L',(24,44)),('L',(32,36)),('C',(40,44),(36,36),(40,40))])
''',
'''        self.path('screen',(8,34),[('L',(8,10)),('A',(12,6),4,4,True),('L',(36,6)),('A',(40,10),4,4,True),('L',(40,34)),('L',(8,34))],True)
        self.add_polyline('base',(8,34),(6,42),(42,42),(40,34))
        self.relate('connect','screen','base')
        self.path('dollar',(29,14),[('L',(24,14)),('L',(21,14)),('C',(21,22),(16,14),(16,22)),('L',(27,22)),('C',(27,30),(32,22),(32,30)),('L',(24,30)),('L',(19,30))])
        self.add_line('currency-top',(24,11),(24,14));self.add_line('currency-bottom',(24,30),(24,33))
        self.relate('connect','dollar','currency-top');self.relate('connect','dollar','currency-bottom')
''',
'''        self.box('phone',8,4,40,44,4)
        self.add_line('footer',(8,36),(40,36));self.relate('connect','phone','footer')
        self.path('dollar',(29,13),[('L',(24,13)),('L',(21,13)),('C',(21,21),(16,13),(16,21)),('L',(27,21)),('C',(27,29),(32,21),(32,29)),('L',(24,29)),('L',(19,29))])
        self.add_line('currency-top',(24,10),(24,13));self.add_line('currency-bottom',(24,29),(24,32))
        self.relate('connect','dollar','currency-top');self.relate('connect','dollar','currency-bottom')
''',
'''        # Tall fingers keep source hand anatomy; shared four-unit tip radii.
        first=10;step=8;r=4;heights=(14,10,14,20)
        cmds=[]
        for i,y in enumerate(heights):
            x=first+i*step;cmds += [('L',(x,y)),('A',(x+step,y),r,r,True)]
        cmds += [('L',(42,30)),('C',(30,42),(42,37),(37,42)),('L',(24,42)),('C',(14,37),(19,42),(16,40)),('L',(6,28)),('C',(10,24),(2,23),(6,19)),('L',(10,27))]
        self.path('hand',(10,27),cmds,True)
        for i in range(3):
            x=first+(i+1)*step;y=max(heights[i],heights[i+1]);self.add_line(f'crease-{i}',(x,y),(x,26));self.relate('connect','hand',f'crease-{i}')
''',
'''        self.add_polyline('basket',(6,14),(38,14),(35,26),(10,26),(6,14),closed=True)
        self.add_polyline('handle',(38,14),(40,6),(42,6));self.relate('connect','basket','handle')
        self.path('support',(35,26),[('C',(32,34),(35,30),(35,34)),('L',(14,34))])
        self.relate('connect','basket','support')
        for x in (14,32):
            self.path(f'wheel-{x}',(x,34),[('A',(x,42),4,4,True),('A',(x,34),4,4,True)],True)
            self.relate('connect','support',f'wheel-{x}')
''',
'''        # Tall straight tube and smoothly swelling round bulb.
        self.path('outline',(15,13),[('A',(33,13),9,9,True),('L',(33,27)),('C',(38,34),(36,29),(38,31)),('C',(24,44),(38,41),(32,44)),('C',(10,34),(16,44),(10,41)),('C',(15,27),(10,31),(12,29)),('L',(15,13))],True)
        self.add_line('mercury',(24,14),(24,25));self.add_dot('bulb-dot',(24,35))
''',
'''        # Equal cap-height lettering, coherent S with horizontal tangents.
        self.path('s',(18,14),[('C',(11,8),(17,10),(14,8)),('C',(4,16),(7,8),(4,11)),('C',(11,24),(4,21),(8,23)),('C',(18,32),(15,25),(18,27)),('C',(11,40),(18,37),(15,40)),('C',(4,34),(8,40),(5,38))])
        self.add_polyline('e',(44,8),(28,8),(28,24),(28,40),(44,40))
        self.add_line('e-middle',(28,24),(40,24));self.relate('connect','e','e-middle')
'''
]
names=['location-pin-above-baseline','shopping-cart-rounded-basket','airplane-top-view-swept-wings','man-graduate-avatar','laptop-dollar-symbol','mobile-phone-dollar-sign','open-palm-hand','shopping-cart-right-grip-lower-rail','thermometer-mercury','se-text']
keys=['VRECT_M','SQUARE','SQUARE','VRECT_L','SQUARE','VRECT_L','SQUARE','SQUARE','VRECT_M','HRECT_L']
plans=['Narrowed and lengthened teardrop, larger centered circular opening, long detached baseline.','Restore basket depth, support curl and equal outlined wheels.','Lengthen fuselage nose vertically and restore swept wings; mirrored about x24.','Restore flat graduation board, band, tassel, jaw and V-neck gown.','Restore laptop base divider and dollar currency ticks.','Restore phone footer and dollar currency ticks.','Restore long fingers and upright palm instead of horizontal mitten.','Restore deep tapered basket, right handle and continuous wheel support.','Narrow bulb relative to taller stem; restore separate mercury line and bulb point.','Equal-height SE capitals, rounded S and shortened E middle stroke.']
for i,row in enumerate(rows):
 out=Path(row['run']);row.update(icon_id=names[i],keyshape=keys[i],plan=plans[i]);(out/'input.metadata.json').write_text(json.dumps(row,indent=2))
 src=f'''"""{plans[i]} Native SOLO48 redraw, preserving all defining source features."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = 'gpt-6'
PARENT_MODULE = {row['parent']!r}
class Drawing(Solo48):
    icon_id = {names[i]!r}
    keyshape = Keyshape.{keys[i]}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = {'avatars' if i==3 else 'objects'!r}
    aliases = ()
    keywords = ({row['concept']!r},)
'''+HELPERS+'\n    def build(self):\n'+bodies[i]
 p=out/(names[i].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py');p.write_text(src);row['module']=str(p)
(B/'inputs.json').write_text(json.dumps(rows,indent=2))
