"""Wide diagonal syringe with needle and T plunger. Lucide syringe informs the barrel/plunger hierarchy. Three measurement marks reduced to one to preserve clearances.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='e8bd0685-39d5-42cb-96ed-39a556fbf8e3'
SOURCE_PATH='pictographic-primitives/symbol/syringe_e8bd0685-39d5-42cb-96ed-39a556fbf8e3.svg'
AUTHOR='gpt-6'

class SyringeWideBarrel(Solo48):
    icon_id='syringe-wide-barrel'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('syringe', 'injection', 'vaccine', 'medical', 'needle', 'health', 'shot', 'medicine')

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

        self.raw('barrel-top',[(8,23),(21,10),(29,18),(36,25),(23,38)])
        self.add_arc('barrel-bottom-a',(23,38),(14,35),radius_x=15)
        self.add_arc('barrel-bottom-b',(14,35),(8,23),radius_x=15)
        self.add_contour('barrel',*['barrel-top-'+str(i) for i in range(1,5)],'barrel-bottom-a','barrel-bottom-b',closed=True)
        self.add_line('needle',(14,35),(6,42));self.relate('connect','needle','barrel')
        self.add_line('plunger',(29,18),(38,10));self.relate('connect','plunger','barrel')
        self.path('handle',[(34,6),(38,10),(42,14)]);self.relate('connect','handle','plunger')
        self.add_line('tick',(15,16),(21,22));self.relate('connect','tick','barrel')
