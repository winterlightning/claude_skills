"""Three curved chili peppers in a vertical stack, each with a right stem. Lucide bean informs a coherent curved pod; repeated geometry preserves the count and direction. Upper edges flattened to keep the narrow pod openings clear; lower contours retain the tapering curve.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='928dd597-914b-4e96-8b61-a0c0fab4c55c'
SOURCE_PATH='pictographic-primitives/symbol/three chilies_928dd597-914b-4e96-8b61-a0c0fab4c55c.svg'
AUTHOR='gpt-6'

class ChiliPeppersThree(Solo48):
    icon_id='chili-peppers-three'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('chili', 'pepper', 'spicy', 'hot', 'food', 'mexican', 'cooking', 'vegetable')

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

        for j,y in enumerate((9,24,39)):
            n='pepper-'+str(j)
            self.add_line(n+'-top',(6,y-3),(36,y-3))
            self.add_arc(n+'-end-top',(36,y-3),(39,y),radius_x=3)
            self.add_arc(n+'-end-bottom',(39,y),(36,y+3),radius_x=3)
            self.add_arc(n+'-bottom',(36,y+3),(6,y-3),radius_x=30,radius_y=6)
            self.add_contour(n,n+'-top',n+'-end-top',n+'-end-bottom',n+'-bottom',closed=True)
            self.path(n+'-stem',[(39,y),(42,y),(42,y-3)])
            self.relate('connect',n,n+'-stem')
