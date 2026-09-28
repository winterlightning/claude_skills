"""Twelve OClock — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ac0d60d2-859d-52d9-b9b6-68e6a0bd9106'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time clock midnight_ac0d60d2-859d-52d9-b9b6-68e6a0bd9106.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twelve-oclock'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('twelve', 'oclock')

    def build(self):
        # Plan: circular dial, one upright hand, three detached cardinal ticks.
        # CIRCLE center24,24 radius20. Lucide clock-3 supplies simple dial construction.
        self.circle('rim',24,24,20)
        self.add_line('hands',(24,13),(24,24))
        for i,(dx,dy) in enumerate(((1,0),(0,1),(-1,0))):
            self.add_line(f'tick-{i}',(24+dx*9,24+dy*9),(24+dx*11,24+dy*11))


    def circle(self,n,x,y,r,attachments=()):
        from math import atan2
        pts=list(dict.fromkeys([(x+r,y),(x,y+r),(x-r,y),(x,y-r)]+list(attachments)))
        pts.sort(key=lambda p:atan2(p[1]-y,p[0]-x))
        for j in range(len(pts)):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%len(pts)],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(len(pts))],closed=True)

    def box(self,n,x,y,w,h,attachments=()):
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)];nodes=[]
        for a,z in zip(corners,corners[1:]+corners[:1]):
            dx,dy=z[0]-a[0],z[1]-a[1]
            inside=[p for p in attachments if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy);nodes.extend([a]+inside)
        self.add_polyline(n,*nodes,closed=True)

