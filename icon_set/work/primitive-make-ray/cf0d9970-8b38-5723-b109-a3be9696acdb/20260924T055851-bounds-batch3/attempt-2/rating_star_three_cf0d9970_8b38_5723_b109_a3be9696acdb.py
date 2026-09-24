"""rating star three.
Plan: Three equal outlined five-point stars in a horizontal row. Lucide star: alternating tips and valleys with shared mirrored definition. No star omitted.
Keyshape HRECT_M: visible bounds (2, 8, 46, 40); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cf0d9970-8b38-5723-b109-a3be9696acdb'
SOURCE_PATH='pictographic-primitives/rating/rating star three_cf0d9970-8b38-5723-b109-a3be9696acdb.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='rating-star-three'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('rating', 'star', 'three')
    def build(self):
        # Three mirrored five-point outlines, shared width, height and spacing.
        for i,x in enumerate((8,24,40)):
            self.add_polyline(f'star-{i}',(x,10),(x+4,20),(x+4,20),(x+3,27),(x+4,38),(x,32),(x-4,38),(x-3,27),(x-4,20),(x-4,20),closed=True)

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
