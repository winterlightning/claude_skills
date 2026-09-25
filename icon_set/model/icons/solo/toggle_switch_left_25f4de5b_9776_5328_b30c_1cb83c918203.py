"""Toggle Switch Left — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '25f4de5b-9776-5328-b30c-1cb83c918203'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/toggle setting off_25f4de5b-9776-5328-b30c-1cb83c918203.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toggle-switch-left'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('toggle', 'switch', 'left')

    def build(self):
        # Plan: horizontal capsule and detached circular knob on the left.
        # HRECT_M extremes4,10,44,38. Lucide toggle-left informs the two nested shapes.
        self.add_line('top',(18,10),(30,10))
        self.add_arc('right',(30,10),(30,38),radius_x=14)
        self.add_line('bottom',(30,38),(18,38))
        self.add_arc('left',(18,38),(18,10),radius_x=14)
        self.add_contour('track','top','right','bottom','left',closed=True)
        self.circle('knob',18,24,5)


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

