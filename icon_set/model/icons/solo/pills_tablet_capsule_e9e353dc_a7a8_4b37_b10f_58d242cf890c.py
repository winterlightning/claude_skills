"""Scored round tablet above-left of a diagonal two-part capsule. Lucide pill informs semicircular caps and a shared midpoint divider; both medicines retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='e9e353dc-a7a8-4b37-b10f-58d242cf890c'
SOURCE_PATH='pictographic-primitives/symbol/two pill_e9e353dc-a7a8-4b37-b10f-58d242cf890c.svg'
AUTHOR='gpt-6'

class PillsTabletCapsule(Solo48):
    icon_id='pills-tablet-capsule'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('pills', 'medicine', 'tablet', 'capsule', 'pharmacy', 'drugs', 'health', 'prescription')

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

        self.oval('tablet',14,14,8);self.add_line('score',(6,14),(22,14));self.relate('connect','score','tablet')
        self.raw('left-edge',[(21,34),(27,26),(33,18)])
        self.add_arc('cap-top',(33,18),(41,24),radius_x=5)
        self.raw('right-edge',[(41,24),(35,32),(29,40)])
        self.add_arc('cap-bottom',(29,40),(21,34),radius_x=5)
        self.add_contour('capsule','left-edge-1','left-edge-2','cap-top','right-edge-1','right-edge-2','cap-bottom',closed=True)
        self.add_line('divider',(27,26),(35,32));self.relate('connect','divider','capsule')
