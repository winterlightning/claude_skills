"""Hierarchical Process Flow Diagram.

Symbol plan: Vertical hierarchy with top capsule and two rightward round terminals. Lucide workflow and git-branch inform rounded elbow and cardinal circle attachment. Shared terminal radius3 and 15-unit pitch. Deliberate rightward asymmetry.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ea3253b-378d-56cb-a56a-7fc7c2770411'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/diagrams/flow_8ea3253b-378d-56cb-a56a-7fc7c2770411.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'vertical-process-branch-with-two-round-terminals'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('hierarchical', 'process', 'flow', 'diagram')

    def build(self):
        self.add_line('start-top',(11,6),(25,6));self.add_arc('start-right',(25,6),(25,16),radius_x=5)
        self.run('start-bottom',(25,16),(18,16),(11,16));self.add_arc('start-left',(11,16),(11,6),radius_x=5)
        self.add_contour('start','start-top','start-right','start-bottom-1','start-bottom-2','start-left',closed=True)
        self.run('stem',(18,16),(18,24),(18,33));self.add_arc('elbow',(18,33),(24,39),radius_x=6,sweep=False)
        self.add_line('bottom',(24,39),(36,39));self.add_contour('trunk','stem-1','stem-2','elbow','bottom');self.relate('connect','trunk','start')
        for i,y in enumerate((24,39)):
            self.circle(f'end-{i}',39,y,3)
        self.add_line('middle',(18,24),(36,24));self.relate('connect','middle','trunk');self.relate('connect','middle','end-0');self.relate('connect','trunk','end-1')

    def circle(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        names=[]
        for i,start in enumerate(points):
            part=f'{name}-{i}';self.add_arc(part,start,points[(i+1)%4],radius_x=r);names.append(part)
        self.add_contour(name,*names,closed=True)

    def rect(self,name,x,y,w,h,r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,start in enumerate(points):
            end=points[(i+1)%8];part=f'{name}-{i}'
            if start==end: continue
            if i%2:self.add_arc(part,start,end,radius_x=r)
            else:self.add_line(part,start,end)
            names.append(part)
        self.add_contour(name,*names,closed=True)

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'{name}-{i}',a,b)
