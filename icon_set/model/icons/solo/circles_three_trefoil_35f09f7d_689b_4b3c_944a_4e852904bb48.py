"""Three interlinked circles in a triangular cluster. Lucide circle informs equal radii. Broader real intersections enlarge the overlap regions; all seven resulting openings pass QA.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='35f09f7d-689b-4b3c-944a-4e852904bb48'
SOURCE_PATH='pictographic-primitives/symbol/three circles_35f09f7d-689b-4b3c-944a-4e852904bb48.svg'
AUTHOR='gpt-6'

class CirclesThreeTrefoil(Solo48):
    icon_id='circles-three-trefoil'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('circles', 'trefoil', 'group', 'community', 'overlap', 'shapes', 'cluster', 'venn')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def raw(self,n,points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(n+'-'+str(j),a,b)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        radius=12
        for n,cx,cy in [('top',24,18),('left',18,30),('right',30,30)]:self.oval(n,cx,cy,radius)
        for a,b in [('top','left'),('top','right'),('left','right')]:self.relate('connect',a,b)
