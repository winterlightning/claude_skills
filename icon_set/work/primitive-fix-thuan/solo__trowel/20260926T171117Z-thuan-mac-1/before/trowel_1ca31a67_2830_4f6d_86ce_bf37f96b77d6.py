"""Diagonal pointed garden trowel with a bent shaft. Lucide shovel informs the blade/shaft hierarchy; deliberate blade corners preserve the triangular spade shape.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='1ca31a67-2830-4f6d-86ce-bf37f96b77d6'
SOURCE_PATH='pictographic-primitives/symbol/trowel_1ca31a67-2830-4f6d-86ce-bf37f96b77d6.svg'
AUTHOR='gpt-6'

class Trowel(Solo48):
    icon_id='trowel'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol",)
    aliases=()
    keywords=('trowel', 'garden', 'gardening', 'tool', 'planting', 'dig', 'shovel', 'construction')

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

        self.path('blade',[(6,42),(16,20),(20,18),(26,22),(32,28),(30,32),(10,42)],True)
        self.path('shaft',[(20,28),(26,22),(26,18),(42,6)])
        self.relate('connect','blade','shaft')
