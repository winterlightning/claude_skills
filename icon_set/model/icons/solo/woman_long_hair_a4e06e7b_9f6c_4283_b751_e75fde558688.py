"""Woman with long arched hair around a parted shield-shaped face. Lucide user-round informs the major arch; no exact local hair match. Shared axis keeps the face balanced.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='a4e06e7b-9f6c-4283-b751-e75fde558688'
SOURCE_PATH='pictographic-primitives/symbol/women_a4e06e7b-9f6c-4283-b751-e75fde558688.svg'
AUTHOR='gpt-6'

class WomanLongHair(Solo48):
    icon_id='woman-long-hair'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('woman', 'female', 'girl', 'person', 'avatar', 'hair', 'user', 'lady')

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

        self.add_line('hair-left',(6,42),(6,24));self.add_arc('hair-top',(6,24),(42,24),radius_x=18)
        self.add_line('hair-right',(42,24),(42,42));self.add_contour('hair','hair-left','hair-top','hair-right')
        self.raw('face-top',[(16,30),(16,22),(24,16),(32,22),(32,30)])
        self.add_arc('chin',(32,30),(16,30),radius_x=8,radius_y=10)
        self.add_contour('face',*['face-top-'+str(j) for j in range(1,5)],'chin',closed=True)
