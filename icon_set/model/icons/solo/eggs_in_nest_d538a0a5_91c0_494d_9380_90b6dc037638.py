"""Two upright oval eggs in a shallow nest. Lucide egg informs paired oval bodies; woven interior marks omitted to keep the nest opening clear.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='d538a0a5-91c0-494d-9380-90b6dc037638'
SOURCE_PATH='pictographic-primitives/symbol/two eggs_d538a0a5-91c0-494d-9380-90b6dc037638.svg'
AUTHOR='gpt-6'

class EggsInNest(Solo48):
    icon_id='eggs-in-nest'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol",)
    aliases=()
    keywords=('eggs', 'nest', 'bird', 'easter', 'breakfast', 'farm', 'spring', 'food')

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

        for n,cx in [('left',13),('right',35)]:self.oval(n+'-egg',cx,18,5,10)
        self.raw('rim',[(4,28),(13,28),(35,28),(44,28)])
        self.add_arc('nest-base',(44,28),(4,28),radius_x=20,radius_y=12)
        self.add_contour('nest','rim-1','rim-2','rim-3','nest-base',closed=True)
        self.relate('connect','nest','left-egg');self.relate('connect','nest','right-egg')
