"""Three Column Layout — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '072623ab-aa4c-4582-99b7-048ec0c75d51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/layout array_072623ab-aa4c-4582-99b7-048ec0c75d51.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-column-layout'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('three', 'column', 'layout')

    def build(self):
        # Plan: three equally spaced outlined panels; Lucide table informs edges.
        # HRECT_L extremes (4,8)-(44,40). Equalize widths to retain three clear panels.
        for i,x in enumerate((4,20,36)):self.box(f'panel-{i}',x,8,8,32)


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4): self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

    def box(self,n,x,y,w,h,attachments=()):
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)];nodes=[]
        for a,z in zip(corners,corners[1:]+corners[:1]):
            dx,dy=z[0]-a[0],z[1]-a[1]
            inside=[p for p in attachments if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy);nodes.extend([a]+inside)
        self.add_polyline(n,*nodes,closed=True)

