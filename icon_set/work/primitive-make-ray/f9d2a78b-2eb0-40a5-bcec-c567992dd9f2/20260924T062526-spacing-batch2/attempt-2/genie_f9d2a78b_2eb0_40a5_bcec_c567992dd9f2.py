"""genie.
Plan: Genie circular face and turban jewel with naturally attached curling smoke body. Continuous face/body junctions at shared cheek points; not a detached stick figure. Human references inspected. No useful Lucide match.
Keyshape VRECT_L: visible bounds (6, 2, 42, 46); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f9d2a78b-2eb0-40a5-bcec-c567992dd9f2'
SOURCE_PATH='pictographic-primitives/_uncategorized_20/genie_f9d2a78b-2eb0-40a5-bcec-c567992dd9f2.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='genie'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('genie',)
    def build(self):
        self.path('head',(14,18),[('A',(24,8),10,10,True),('A',(34,18),10,10,True),('A',(24,28),10,10,True),('A',(14,18),10,10,True)],True)
        self.circle('jewel',24,6,2)
        self.relate('connect','head','jewel')
        self.add_polyline('mustache',(22,18),(24,17),(26,18))
        self.add_bezier('smoke',(14,18),((8,24),(8,28),(8,34)),((8,41),(17,44),(24,44)),((32,44),(32,36),(24,36)),((32,36),(40,36),(40,30)),((40,25),(36,22),(34,18)))
        self.relate('connect','head','smoke')

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
