from pathlib import Path
import json

ROOT = Path(__file__).parent
AUTHOR = 'gpt-6'
rows = json.loads((ROOT / 'batch.json').read_text())
SOURCE_ICON_ID = [r['source_uuid'] for r in rows]
SOURCE_PATH = [r['reference_path'] for r in rows]

# Each definition is a new SOLO48 construction based on the inspected picture.
drawings = {
1: ('VRECT_L', 'box', 'The rejected cube has stubby, filled-looking corner marks and short central axes. Restore open isometric corner junctions and longer center Y.', '''
        poly('north', (18,8),(24,4),(30,8)); line('north-axis',(24,4),(24,11)); join('north','north-axis')
        poly('south',(18,40),(24,44),(30,40)); line('south-axis',(24,37),(24,44)); join('south','south-axis')
        poly('center',(18,21),(24,25),(30,21)); line('center-axis',(24,25),(24,32)); join('center','center-axis')
        for s in (-1,1):
            p=lambda x,y:(24+s*x,y)
            n='left' if s<0 else 'right'
            poly(n+'-upper',p(10,12),p(16,16),p(16,23))
            line(n+'-upper-axis',p(16,16),p(10,20));join(n+'-upper',n+'-upper-axis')
            poly(n+'-lower',p(16,28),p(16,35),p(10,39))
            line(n+'-lower-axis',p(16,35),p(10,31));join(n+'-lower',n+'-lower-axis')
'''),
2: ('SQUARE','rotate-ccw','The rejected orbit is a narrow oval with a squat V. Restore a circular orbit, open lower-left quadrant and tangent downward arrow.', '''
        path('orbit',(24,42),[('A',(42,24),18,False),('A',(24,6),18,False),('A',(6,24),18,False)])
        poly('head',(2,18),(6,24),(12,20));join('head','orbit')
'''),
3: ('SQUARE','refresh-ccw','Rejected arrows form two compressed hooks rather than one circular cycle. Restore matching arcs of one circle and smaller opposing heads.', '''
        path('upper',(39,14),[('C',(24,6),(35,9),(30,6)),('A',(6,24),18,False)])
        poly('upper-head',(2,19),(6,24),(11,20));join('upper','upper-head')
        path('lower',(9,34),[('C',(24,42),(13,39),(18,42)),('A',(42,24),18,False)])
        poly('lower-head',(37,28),(42,24),(46,29));join('lower','lower-head')
'''),
4: ('SQUARE','rotate-ccw','Rejected refresh loop is visibly oval and its arrowhead dominates. Restore the round loop and reference lower-left opening.', '''
        path('orbit',(24,42),[('A',(42,24),18,False),('A',(24,6),18,False),('A',(6,24),18,False)])
        poly('head',(2,19),(6,24),(11,20));join('head','orbit')
'''),
5: ('SQUARE','refresh-ccw','Rejected sync arrows have narrow elliptical arcs and large heads. Rebuild a shared round cycle with equal opposing arrowheads.', '''
        path('upper',(39,14),[('C',(24,6),(35,9),(30,6)),('A',(6,24),18,False)])
        poly('upper-head',(2,19),(6,24),(11,20));join('upper','upper-head')
        path('lower',(9,34),[('C',(24,42),(13,39),(18,42)),('A',(42,24),18,False)])
        poly('lower-head',(37,28),(42,24),(46,29));join('lower','lower-head')
'''),
6: ('SQUARE','rotate-ccw','Rejected return loop is flattened and the large head collides visually with its curve. Restore a round clockwise loop and distinct upper-left break.', '''
        path('orbit',(6,20),[('C',(24,6),(8,11),(15,6)),('A',(42,24),18,True),('A',(24,42),18,True),('C',(7,27),(14,42),(7,36))])
        poly('head',(2,33),(7,27),(13,33));join('orbit','head')
'''),
7: ('HRECT_L','refresh-ccw','Rejected triangles are squat, line is too short and the curved arrow is a heavy hook. Restore two mirrored triangles across a horizontal divider and a smooth right-side downward arc.', '''
        poly('upper',(4,8),(28,8),(16,19),closed=True)
        poly('lower',(4,40),(28,40),(16,29),closed=True)
        line('mirror-axis',(4,24),(29,24))
        path('rotation',(35,12),[('C',(44,24),(41,12),(44,18)),('C',(35,36),(44,30),(41,36))])
        poly('head',(36,29),(35,36),(42,36));join('rotation','head')
'''),
8: ('VRECT_L','compass','Rejected E is displaced left and the needle merges with the rim. Center E below the dial and restore an independent northeast compass pointer.', '''
        circle('dial',24,18,14)
        poly('needle',(20,18),(29,13),(26,24),(24,20),closed=True)
        poly('e',(28,36),(20,36),(20,40),(20,44),(28,44))
        line('e-middle',(20,40),(26,40));join('e','e-middle')
'''),
9: ('SQUARE','refresh-ccw','Rejected search-refresh has tilted bulky heads and a cramped upper gap. Restore circular counterclockwise arrows and a diagonal magnifier handle.', '''
        path('left',(23,6),[('C',(6,23),(13,6),(6,13)),('C',(10,33),(6,27),(7,30))])
        poly('left-head',(3,31),(10,33),(11,26));join('left','left-head')
        path('right',(21,40),[('C',(33,35),(26,40),(30,38)),('C',(40,23),(37,31),(40,28)),('C',(31,8),(40,17),(36,11))])
        poly('right-head',(32,15),(31,8),(38,10));join('right','right-head')
        line('handle',(33,35),(42,44));join('right','handle')
'''),
10: ('SQUARE','merge','Rejected merge nodes are tiny rings and the surrounding path is squared-off. Enlarge three endpoint circles, smooth the sweeping connection and lighten the diagonal arrow.', '''
        circle('source',9,9,5)
        circle('upper-node',39,9,5)
        circle('lower-node',9,33,5)
        line('inward',(13,13),(30,30));join('source','inward')
        poly('head',(21,30),(30,30),(30,21));join('inward','head')
        path('sweep',(43,12),[('C',(44,30),(47,18),(47,25)),('C',(25,44),(41,39),(34,44)),('C',(12,37),(19,44),(14,40))])
        join('sweep','upper-node');join('sweep','lower-node')
'''),
11: ('SQUARE','merge','Rejected alternate merge also has tiny node openings and an unbalanced loop. Restore three clear circular nodes, a diagonal merge arrow and a smooth lower-right sweep.', '''
        circle('source',9,9,5)
        circle('upper-node',39,9,5)
        circle('lower-node',9,33,5)
        line('inward',(13,13),(30,30));join('source','inward')
        poly('head',(21,30),(30,30),(30,21));join('inward','head')
        path('sweep',(43,12),[('C',(44,30),(47,18),(47,25)),('C',(25,44),(41,39),(34,44)),('C',(12,37),(19,44),(14,40))])
        join('sweep','upper-node');join('sweep','lower-node')
'''),
12: ('SQUARE','wrench','Rejected wrench has a cramped jaw, kinked neck and abrupt jaw-to-handle corner. Rebuild continuous rounded head and parallel handle with a clear diagonal jaw opening.', '''
        path('wrench',(7,34),[('L',(20,21)),('C',(20,15),(22,19),(20,18)),('A',(32,3),12,True),('A',(44,15),12,True),('L',(44,17)),('L',(35,8)),('L',(27,16)),('L',(36,25)),('C',(29,28),(34,27),(31,28)),('C',(25,30),(27,28),(27,28)),('L',(14,41)),('A',(7,34),5,True)],closed=True)
'''),
13: ('SQUARE','refresh-ccw','Rejected recycling loop has squeezed elliptical arcs and boxy heads. Restore the circular clockwise two-arrow motif of this reference.', '''
        path('upper',(6,23),[('C',(24,6),(7,13),(15,6)),('C',(41,17),(32,6),(39,10))])
        poly('upper-head',(34,16),(41,17),(42,10));join('upper','upper-head')
        path('lower',(42,25),[('C',(24,42),(41,35),(33,42)),('C',(7,31),(16,42),(9,38))])
        poly('lower-head',(6,38),(7,31),(14,32));join('lower','lower-head')
'''),
14: ('SQUARE','rotate-ccw','Rejected central orbit is oval, with an overly small center ring. Restore a concentric circle inside a round three-quarter arrow.', '''
        path('orbit',(24,42),[('A',(42,24),18,False),('A',(24,6),18,False),('A',(6,24),18,False)])
        poly('head',(2,19),(6,24),(11,20));join('head','orbit')
        circle('hub',24,24,5)
'''),
15: ('SQUARE','refresh-ccw','Rejected sync-search has blunt right-angle heads and a compressed loop. Restore directional slanted heads, round flow and tangent handle placement.', '''
        path('left',(23,6),[('C',(6,23),(13,6),(6,13)),('C',(10,33),(6,27),(7,30))])
        poly('left-head',(3,31),(10,33),(11,26));join('left','left-head')
        path('right',(21,40),[('C',(33,35),(26,40),(30,38)),('C',(40,23),(37,31),(40,28)),('C',(31,8),(40,17),(36,11))])
        poly('right-head',(32,15),(31,8),(38,10));join('right','right-head')
        line('handle',(33,35),(42,44));join('right','handle')
'''),
16: ('SQUARE','clapperboard','Rejected strips have near-horizontal rails and inconsistent separators. Restore two distinctly slanted bands with parallel rails and consistently spaced diagonal dividers.', '''
        for n,pts in [('upper-top',[(4,10),(16,8),(28,6),(40,4)]),('upper-bottom',[(4,22),(16,20),(28,18),(40,16)]),('lower-top',[(4,26),(16,29),(28,32),(40,35)]),('lower-bottom',[(4,35),(16,38),(28,41),(40,44)])]:
            poly(n,*pts)
        for i in range(2):
            x=16+12*i
            line('upper-divider-'+str(i),(x,8-2*i),(x-4,20-2*i+1))
            line('lower-divider-'+str(i),(x,29+3*i),(x-4,38+3*i-1))
'''),
17: ('SQUARE','satellite','Rejected Sputnik sphere dominates while rods are shortened and steepened. Restore smaller spherical body and three long, unequal antenna rods at original angles.', '''
        path('sphere',(31,4),[('A',(43,16),12,True),('A',(43,16),12,True)])
'''),
18: ('SQUARE','satellite','Rejected Sputnik has short stubby antennas. Restore original long leftward and downward rods and a circular upper-right sphere.', '''
        circle('sphere',31,16,12)
'''),
19: ('HRECT_L','gauge','Rejected speedometer substitutes dots for ticks and shows few dial details. Restore radial tick strokes, open needle pivot and smooth domed housing.', '''
        path('housing',(4,34),[('L',(4,28)),('A',(24,8),20,True),('A',(44,28),20,True),('L',(44,34)),('A',(38,40),6,True),('L',(10,40)),('A',(4,34),6,True)],closed=True)
        circle('pivot',24,30,3)
        line('needle',(27,28),(35,22));join('pivot','needle')
        for n,a,b in [('top',(24,14),(24,17)),('left',(11,26),(14,27)),('upper-left',(15,18),(17,21)),('upper-right',(33,18),(31,21))]:line(n,a,b)
'''),
20: ('SQUARE','message-square','Feedback explicitly says line not connected. Rejected bubble has two disconnected crack ends and a broken tail. Restore one continuous perimeter with a joined lightning-shaped crack and connected speech tail.', '''
        path('bubble',(18,6),[('L',(10,6)),('A',(6,10),4,False),('L',(6,32)),('A',(10,36),4,False),('L',(14,36)),('L',(14,42)),('L',(22,36)),('L',(38,36)),('A',(42,32),4,False),('L',(42,10)),('A',(38,6),4,False),('L',(29,6)),('L',(32,15)),('L',(28,18)),('L',(32,28)),('L',(20,18)),('L',(25,14)),('L',(18,6))],closed=True)
'''),
}

helpers = '''
    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)
'''

# Sphere attachment points use the exact 5-12-13 circle for real joins.
for i in (17,18):
    k,l,n,_=drawings[i]
    drawings[i]=(k,l,n,'''
        path('sphere',(29,4),[('A',(42,17),13,True),('A',(41,22),13,True),('A',(29,30),13,True),('A',(17,22),13,True),('A',(16,17),13,True),('A',(24,5),13,True),('A',(29,4),13,True)],closed=True)
        for n,a,b in [('upper',(4,11),(24,5)),('lower-left',(4,44),(17,22)),('lower-right',(36,44),(41,22))]:
            line(n,a,b);join(n,'sphere')
''')

for i,m in enumerate(rows,1):
    key,ref,note,body=drawings[i];rd=Path(m['result_dir'])
    m.update(comparison=note,lucide=ref,keyshape=key,author=AUTHOR)
    (rd/'comparison.md').write_text(f"# Reference/current review\n\n{note}\n\nReviewer: {m['feedback']}\n\nConstruction: Lucide {ref}; inspected original and atomic-debug. Use coherent contours and matched arc tangents. Preserve source orientation and arrangement.\n")
    module=rd/(m['icon_id'].replace('-','_')+'_'+m['source_uuid'].replace('-','_')+'.py')
    module.write_text(f'''"""{note}
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: {ref}. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {m['source_uuid']!r}
SOURCE_PATH = {m['reference_path']!r}
AUTHOR = {AUTHOR!r}
class Drawing(Solo48):
    icon_id = {m['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = {tuple(m['concept'].split())!r}
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)
{body}
{helpers}
''')
    m['module']=str(module)
(ROOT/'batch.json').write_text(json.dumps(rows,indent=2))
