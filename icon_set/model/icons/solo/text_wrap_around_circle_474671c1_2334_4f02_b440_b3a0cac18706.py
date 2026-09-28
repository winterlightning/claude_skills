"""Text Wrap around Circle — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '474671c1-2334-4f02-b440-b3a0cac18706'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/warp around object shape_474671c1-2334-4f02-b440-b3a0cac18706.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'text-wrap-around-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('text', 'wrap', 'around', 'circle')

    def build(self):
        # Plan: central circle surrounded by six text-placeholder strokes.
        # SQUARE extremes (6,6)-(42,42). No literal letters; Lucide table guides spacing.
        self.circle("object",24,24,8)
        for i,y in enumerate((6,42)):self.add_line(f'full-row-{i}',(6,y),(42,y))
        for i,y in enumerate((18,30)):
            self.add_line(f'left-{i}',(6,y),(8,y));self.add_line(f'right-{i}',(40,y),(42,y))


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

