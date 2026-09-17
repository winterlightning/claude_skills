"""Triple Right Arrows — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5bc453e9-2915-4a73-b462-1289b9c71f70'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation arrows right_5bc453e9-2915-4a73-b462-1289b9c71f70.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triple-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('triple', 'right', 'arrows')

    def build(self):
        # Plan: a full foreground triangle and two partially occluded arrow outlines.
        # HRECT_L extremes4,8,44,40. Lucide layers informs repeated occlusion.
        self.add_polyline('front',(4,8),(20,24),(4,40),closed=True)
        for i,x in enumerate((16,28)):self.add_polyline(f'rear-{i}',(x,8),(x+16,24),(x,40))


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

