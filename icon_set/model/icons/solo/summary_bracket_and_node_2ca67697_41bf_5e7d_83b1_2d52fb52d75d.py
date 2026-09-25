"""Summary Bracket and Node — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ca67697-41bf-5e7d-83b1-2d52fb52d75d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/summary organize_2ca67697-41bf-5e7d-83b1-2d52fb52d75d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'summary-bracket-and-node'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('summary', 'bracket', 'and', 'node')

    def build(self):
        # Plan: mirrored brace arms gather at a central node, connected to a box.
        # SQUARE extremes (6,6)-(42,42). Lucide braces informs smooth turnarounds.
        self.add_line('top-tip',(6,6),(8,6))
        self.add_bezier('upper',(8,6),((15,6),(10,22),(18,24)))
        self.add_bezier('lower',(18,24),((10,26),(15,42),(8,42)))
        self.add_line('bottom-tip',(8,42),(6,42))
        self.add_contour('brace','top-tip','upper','lower','bottom-tip')
        self.add_line('stem',(18,24),(26,24))
        self.box('node',26,18,16,12,attachments=((26,24),))
        self.relate('connect','stem','brace');self.relate('connect','stem','node')


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

