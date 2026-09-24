"""face awesome.
Plan: Circular smiling face with two five-point star eyes. Lucide star alternating mirrored points; human-reference facial vocabulary. Equal eye definitions, no substitution of defining stars.
Keyshape CIRCLE: visible bounds (2, 2, 46, 46); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='236451ca-3512-494c-8c17-87481ad251f8'
SOURCE_PATH='pictographic-primitives/_uncategorized_17/face awesome_236451ca-3512-494c-8c17-87481ad251f8.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='face-awesome'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('face', 'awesome')
    def build(self):
        self.circle('head',24,24,20)
        for i,x in enumerate((16,32)):
            self.add_polyline(f'star-{i}',(x,15),(x+1,18),(x+4,18),(x+2,21),(x+3,24),(x,22),(x-3,24),(x-2,21),(x-4,18),(x-1,18),closed=True)
        self.add_arc('smile',(20,31),(28,31),radius_x=5,sweep=False)

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
