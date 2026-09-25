"""Diagonal sprig with two right-angle branch pairs. Lucide sprout informs a single stem hierarchy; the reference straight angular branches are retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='7226cd2e-c0cb-4f06-8d8b-28b0ea71ef5c'
SOURCE_PATH='pictographic-primitives/symbol/vein leaf_7226cd2e-c0cb-4f06-8d8b-28b0ea71ef5c.svg'
AUTHOR='gpt-6'

class SprigDiagonal(Solo48):
    icon_id='sprig-diagonal'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('sprig', 'branch', 'twig', 'herb', 'plant', 'leaf', 'nature', 'rosemary')

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

        self.path('stem',[(6,42),(18,30),(30,18),(42,6)])
        for j,(x,y) in enumerate(((18,30),(30,18))):
            self.path('branch-'+str(j),[(x,y-8),(x,y),(x+8,y)])
            self.relate('connect','stem','branch-'+str(j))
