"""Three Cell Row — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0237638d-10fe-435f-be3f-042d60a75995'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/row selected single_0237638d-10fe-435f-be3f-042d60a75995.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-cell-row'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('three', 'cell', 'row')

    def build(self):
        # Plan: one horizontal capsule with two shared upright dividers.
        # CIRCLE radial extent20; preserves the source's long horizontal proportion.
        # Lucide table informs cell divisions. Integer cell widths13,14,13 are balanced.
        self.add_polyline('top',(10,18),(17,18),(31,18),(38,18))
        self.add_arc('right',(38,18),(38,30),radius_x=6)
        self.add_polyline('bottom',(38,30),(31,30),(17,30),(10,30))
        self.add_arc('left',(10,30),(10,18),radius_x=6)
        self.contours.clear()
        self.add_contour('row','top-1','top-2','top-3','right','bottom-1','bottom-2','bottom-3','left',closed=True)
        for i,x in enumerate((17,31)):
            self.add_line(f'divider-{i}',(x,18),(x,30));self.relate('connect',f'divider-{i}','row')


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

