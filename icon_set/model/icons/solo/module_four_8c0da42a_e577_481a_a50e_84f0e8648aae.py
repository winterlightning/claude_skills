"""module four.
Plan: Four-stud toy brick with the reference 2x2 stud arrangement. Use a top-facing reduction of the solid block; omit perspective side seams so each stud has a full clearance band. No useful exact Lucide match. Shared circular stud definition and square symmetric face.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='8c0da42a-e577-481a-a50e-84f0e8648aae'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/module four_8c0da42a-e577-481a-a50e-84f0e8648aae.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='module-four'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('module', 'four')
    def build(self):
        self.path('brick',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        for row,y in enumerate((17,31)):
            for col,x in enumerate((17,31)):
                self.circle(f'stud-{row}-{col}',x,y,2)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
