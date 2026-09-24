"""monitoring activity tracking 2.
Plan: Magnifying glass with two staggered sole/heel pairs. Solid rounded sole strokes replace tiny outlined ovals, retaining all four footprint parts. Exact circular lens and shared handle endpoint. Human anatomy reference inspected; no head gap. No useful Lucide exact match.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3932acf9-d8a9-4dab-a9e2-4e0a52270bc7'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/monitoring activity tracking 2_3932acf9-d8a9-4dab-a9e2-4e0a52270bc7.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='monitoring-activity-tracking-2'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('monitoring', 'activity', 'tracking', '2')
    def build(self):
        # Circle center(23,23), radius17; handle node(31,38) uses exact 8-15-17 triangle.
        self.path('lens',(6,23),[('A',(40,23),17,17,True),('A',(31,38),17,17,True),('A',(6,23),17,17,True)],True)
        self.add_line('handle',(31,38),(42,42));self.relate('connect','lens','handle')
        for n,x,y in [('left',18,16),('right',28,18)]:
            self.add_line(n+'-sole',(x,y),(x,y+2))
            self.add_dot(n+'-heel',(x,y+10))

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
