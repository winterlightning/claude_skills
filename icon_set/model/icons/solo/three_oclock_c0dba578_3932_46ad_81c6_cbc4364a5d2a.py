"""Three OClock — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c0dba578-3932-46ad-81c6-cbc4364a5d2a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time clock twelve to three_c0dba578-3932-46ad-81c6-cbc4364a5d2a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-oclock'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('three', 'oclock')

    def build(self):
        # Plan: circular dial, four rim ticks and a 3:00 hand pair.
        # CIRCLE center24,24 radius20. Lucide clock-3 informs the joined hands.
        self.circle('rim',24,24,20)
        for i,(dx,dy) in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
            self.add_line(f'tick-{i}',(24+dx*20,24+dy*20),(24+dx*16,24+dy*16));self.relate('connect',f'tick-{i}','rim')
        self.add_polyline('hands',(24,16),(24,24),(30,24))


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

