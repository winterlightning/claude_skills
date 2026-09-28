"""Sun with Eight Rays — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f7486a24-8e7b-5074-b986-bbc616939576'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/brightness_f7486a24-8e7b-5074-b986-bbc616939576.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-with-eight-rays-reference-f7486a24-8e7b-5074-b986-bbc616939576'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('sun', 'with', 'eight', 'rays', 'reference')

    def build(self):
        # Plan: one circular disk and eight symmetric detached radial strokes.
        # CIRCLE center (24,24), centerline radius20. Lucide sun informs the series.
        self.circle('disk',24,24,7)
        for i,(dx,dy) in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
            self.add_line(f'cardinal-{i}',(24+dx*16,24+dy*16),(24+dx*20,24+dy*20))
        for i,(dx,dy) in enumerate(((1,1),(-1,1),(-1,-1),(1,-1))):
            self.add_line(f'diagonal-{i}',(24+dx*11,24+dy*11),(24+dx*14,24+dy*14))


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

