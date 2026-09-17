"""Table with Dashed Right Column — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7eddd61a-5b64-4c95-80e1-c7bd25b8ad15'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/table column selected_7eddd61a-5b64-4c95-80e1-c7bd25b8ad15.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'table-with-dashed-right-column'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('table', 'with', 'dashed', 'right', 'column')

    def build(self):
        # Plan: solid table frame and divisions, three detached right-edge dashes.
        # Extremes (6,6)-(42,42). Lucide table informs the simple orthogonal grid.
        self.add_polyline('frame',(34,6),(30,6),(10,6))
        self.add_arc('corner-top',(10,6),(6,10),radius_x=4,sweep=False)
        self.add_polyline('left',(6,10),(6,24),(6,38))
        self.add_arc('corner-bottom',(6,38),(10,42),radius_x=4,sweep=False)
        self.add_polyline('bottom',(10,42),(30,42),(34,42))
        for a,z in (('frame','corner-top'),('corner-top','left'),('left','corner-bottom'),('corner-bottom','bottom')):self.relate('connect',a,z)
        self.add_polyline('column',(30,6),(30,24),(30,42))
        self.add_line('row',(6,24),(30,24))
        for a,z in (('column','frame'),('column','bottom'),('row','left'),('row','column')):self.relate('connect',a,z)
        for i,y in enumerate((6,22,38)):self.add_line(f'dash-{i}',(42,y),(42,y+4))


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

