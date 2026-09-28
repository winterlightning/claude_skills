"""Three Item Bullet List — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '02e48e7e-64bd-4cc3-9556-251a9280c625'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/list bullet indent_02e48e7e-64bd-4cc3-9556-251a9280c625.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-item-bullet-list'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('three', 'item', 'bullet', 'list')

    def build(self):
        # Plan: three identical outlined bullets with equal list strokes.
        # SQUARE extremes (6,6)-(42,42). Lucide ellipsis informs circular repetition.
        for i,y in enumerate((9,24,39)):
            self.circle(f'bullet-{i}',9,y,3)
            self.add_line(f'row-{i}',(22,y),(42,y))


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

