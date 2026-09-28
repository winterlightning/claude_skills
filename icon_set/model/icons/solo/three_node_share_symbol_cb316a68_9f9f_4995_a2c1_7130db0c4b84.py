"""Three Node Share Symbol — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cb316a68-9f9f-4995-a2c1-7130db0c4b84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/share 1_cb316a68-9f9f-4995-a2c1-7130db0c4b84.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-node-share-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "state")
    aliases = ()
    keywords = ('three', 'node', 'share', 'symbol')

    def build(self):
        # Plan: dominant top circle and mirrored lower pair; exact radial attachment nodes.
        # SQUARE extremes6,6,42,42. Lucide share-2 informs outlined nodes and clear branches.
        self.circle('top',24,16,10,attachments=((18,24),(30,24)))
        for side,sign in [('left',-1),('right',1)]:
            self.circle(side,24+sign*13,37,5,attachments=((24+sign*10,33),))
            self.add_line(side+'-link',(24+sign*6,24),(24+sign*10,33))
            self.relate('connect',side+'-link','top');self.relate('connect',side+'-link',side)


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

