"""mastoid.
Plan: Ear with deep inner fold and rounded lobe. Lucide ear original and atomic-debug: upper circular arch, coherent inner hook and flowing lower lobe. Intentional anatomical asymmetry; widen left inner clearance.
Keyshape VRECT_M: visible bounds (8, 2, 40, 46); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5fe7f155-57d9-4703-a38c-886ec75e5bc6'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/mastoid_5fe7f155-57d9-4703-a38c-886ec75e5bc6.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='mastoid'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('mastoid',)
    def build(self):
        self.path('outer',(10,18),[('A',(24,4),14,14,True),('A',(38,18),14,14,True)])
        self.add_bezier('lobe',(38,18),((38,29),(28,28),(28,36)),((28,41),(25,44),(20,44)),((14,44),(10,41),(10,36)))
        self.relate('connect','outer','lobe')
        self.add_bezier('fold',(20,29),((22,29),(24,24),(21,23)),((18,22),(19,14),(24,14)),((28,14),(29,18),(28,21)))

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
