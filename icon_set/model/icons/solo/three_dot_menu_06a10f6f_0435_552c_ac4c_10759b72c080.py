"""Three Dot Menu — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '06a10f6f-0435-552c-ac4c-10759b72c080'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation menu horizontal_06a10f6f-0435-552c-ac4c-10759b72c080.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-dot-menu'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('three', 'dot', 'menu')

    def build(self):
        # Plan: three equal circles on one horizontal baseline.
        # CIRCLE center24,24; exact radial centerline extent20 preserves horizontal form.
        # Lucide ellipsis informs equal repetition, re-authored as hollow circles.
        radius=3; centers=(7, 24, 41)
        for i,x in enumerate(centers):self.circle(f'node-{i}',x,24,radius)


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

