"""Three Connected Progress Nodes — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cc676bf5-7ee4-404c-b69a-cfe91e511008'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/web form progress_cc676bf5-7ee4-404c-b69a-cfe91e511008.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-connected-progress-nodes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('three', 'connected', 'progress', 'nodes')

    def build(self):
        # Plan: three equal circles on one horizontal baseline with shared connectors.
        # CIRCLE center24,24; exact radial centerline extent20 preserves horizontal form.
        # Lucide ellipsis informs equal repetition, re-authored as hollow circles.
        radius=4; centers=(8, 24, 40)
        for i,x in enumerate(centers):self.circle(f'node-{i}',x,24,radius)
        for i in range(2):
            self.add_line(f'link-{i}',(centers[i]+radius,24),(centers[i+1]-radius,24))
            self.relate('connect',f'link-{i}',f'node-{i}');self.relate('connect',f'link-{i}',f'node-{i+1}')


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

