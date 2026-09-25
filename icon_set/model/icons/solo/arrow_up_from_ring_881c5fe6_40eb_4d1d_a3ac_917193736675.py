"""Upward arrow rises from a ring above two level lines. Lucide git-branch informs a ring attached to a stem; all intrinsic symbol parts retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='881c5fe6-40eb-4d1d-a3ac-917193736675'
SOURCE_PATH='pictographic-primitives/symbol/ups with small circle and lines_881c5fe6-40eb-4d1d-a3ac-917193736675.svg'
AUTHOR='gpt-6'

class ArrowUpFromRing(Solo48):
    icon_id='arrow-up-from-ring'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('up', 'arrow', 'rise', 'lift', 'upload', 'increase', 'level', 'elevate')

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

        self.oval('ring',24,21,4)
        self.add_line('stem',(24,6),(24,17));self.relate('connect','stem','ring')
        self.path('arrow',[(20,9),(24,6),(28,9)]);self.relate('connect','arrow','stem')
        for j,y in enumerate((34,42)):self.add_line('level-'+str(j),(6,y),(42,y))
