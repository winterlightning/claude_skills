"""Three Quarter Stopwatch — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5966030c-8d58-4551-9127-e5481d9c3ef2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time stopwatch 3 quarters_5966030c-8d58-4551-9127-e5481d9c3ef2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-quarter-stopwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('three', 'quarter', 'stopwatch')

    def build(self):
        # Plan: round dial, top plunger, side button and upper-left quarter sector.
        # VRECT_L extremes8,4,40,44. Lucide timer informs the button and circular body.
        self.circle('dial',24,28,16)
        self.add_polyline('sector',(24,12),(24,28),(8,28))
        self.relate('connect','sector','dial')
        self.add_line('plunger',(24,4),(24,12))
        self.add_polyline('cap',(20,4),(24,4),(28,4))
        self.relate('connect','cap','plunger');self.relate('connect','plunger','dial');self.relate('connect','plunger','sector')
        self.add_line('side-button',(38,8),(40,6))


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

