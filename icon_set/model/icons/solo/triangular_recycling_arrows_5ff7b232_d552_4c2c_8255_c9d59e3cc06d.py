"""Triangular Recycling Arrows — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5ff7b232-d552-4c2c-8255-c9d59e3cc06d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/synchronize arrows triangle_5ff7b232-d552-4c2c-8255-c9d59e3cc06d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triangular-recycling-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('triangular', 'recycling', 'arrows')

    def build(self):
        # Plan: three independently readable arrows around a clockwise triangle.
        # SQUARE extremes6,6,42,42. Lucide recycle informs bent shafts and open heads.
        self.add_bezier('top-shaft',(16,14),((20,6),(22,6),(24,6)),((26,6),(28,10),(34,20)))
        self.add_polyline('top-head',(26,18),(34,20),(36,12));self.relate('connect','top-shaft','top-head')
        self.add_line('right-start',(42,28),(42,32))
        self.add_arc('right-turn',(42,32),(38,36),radius_x=4)
        self.add_line('right-end',(38,36),(26,36))
        self.add_contour('right-shaft','right-start','right-turn','right-end')
        self.add_polyline('right-head',(32,30),(26,36),(32,42));self.relate('connect','right-shaft','right-head')
        self.add_line('left-start',(16,38),(10,38))
        self.add_arc('left-turn',(10,38),(6,34),radius_x=4)
        self.add_line('left-end',(6,34),(12,22))
        self.add_contour('left-shaft','left-start','left-turn','left-end')
        self.add_polyline('left-head',(6,24),(12,22),(14,28));self.relate('connect','left-shaft','left-head')


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

