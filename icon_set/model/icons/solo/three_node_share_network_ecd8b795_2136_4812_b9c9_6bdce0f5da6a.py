"""Three Node Share Network — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ecd8b795-2136-4812-b9c9-6bdce0f5da6a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/share_ecd8b795-2136-4812-b9c9-6bdce0f5da6a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-node-share-network'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('three', 'node', 'share', 'network')

    def build(self):
        # Plan: shared left node connects to the two right nodes with diagonal branches.
        # SQUARE extremes6,6,42,42. Lucide share-2; use exact 3-4-5 attachment nodes.
        self.circle('left',11,24,5,attachments=((15,21),(15,27)))
        self.circle('upper',37,11,5,attachments=((33,14),))
        self.circle('lower',37,37,5,attachments=((33,34),))
        for n,a,z,target in [('upper-link',(15,21),(33,14),'upper'),('lower-link',(15,27),(33,34),'lower')]:
            self.add_line(n,a,z);self.relate('connect',n,'left');self.relate('connect',n,target)


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

