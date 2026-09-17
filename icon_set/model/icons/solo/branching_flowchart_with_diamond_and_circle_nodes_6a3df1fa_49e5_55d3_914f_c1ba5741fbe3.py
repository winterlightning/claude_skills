"""Decision Logic Flowchart Diagram.

Symbol plan: Two mirrored flowchart branches with top process parallelogram, diamond decisions and circular terminals. Lucide network/workflow informs elbow routing and node attachments. Reduce terminal circles to radius2 and omit short upper drop segments; retain every node kind.
Keyshape VRECT_L; exact visible bounds (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a3df1fa-49e5-55d3-914f-c1ba5741fbe3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/diagrams/two action_6a3df1fa-49e5-55d3-914f-c1ba5741fbe3.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'branching-flowchart-with-diamond-and-circle-nodes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams/process'
    aliases = ()
    keywords = ('decision', 'logic', 'flowchart', 'diagram')

    def build(self):
        self.add_polyline('start',(20,4),(32,4),(28,12),(24,12),(16,12),closed=True)
        self.graph([('stem',(24,12),(24,20)),('fork-l',(24,20),(14,20)),('fork-r',(24,20),(34,20))])
        self.relate('connect','stem','start')
        for i,x in enumerate((14,34)):
            self.add_polyline(f'decision-{i}',(x,20),(x+6,26),(x,32),(x-6,26),closed=True)
            self.circle(f'end-{i}',x,42,2)
            self.add_line(f'last-{i}',(x,32),(x,40))
            self.relate('connect',f'decision-{i}','fork-l' if i==0 else 'fork-r');self.relate('connect',f'last-{i}',f'decision-{i}');self.relate('connect',f'last-{i}',f'end-{i}')

    def circle(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        names=[]
        for i,start in enumerate(points):
            part=f'{name}-{i}';self.add_arc(part,start,points[(i+1)%4],radius_x=r);names.append(part)
        self.add_contour(name,*names,closed=True)

    def graph(self,edges):
        for name,a,b in edges:self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}:self.relate('connect',name,other)
