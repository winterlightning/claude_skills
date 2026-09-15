"""Two curved chili pods taper left and carry upturned right stems. Lucide bean informs curved pod construction; repeated parameters preserve their pairing.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='2d596f49-a091-4ed3-be42-188e0442128e'
SOURCE_PATH='pictographic-primitives/symbol/two chilies_2d596f49-a091-4ed3-be42-188e0442128e.svg'
AUTHOR='gpt-6'

class ChiliPeppersTwo(Solo48):
    icon_id='chili-peppers-two'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
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

        for j,y in enumerate((14,36)):
            n='pepper-'+str(j)
            self.add_arc(n+'-top',(6,y-4),(34,y-6),radius_x=40,sweep=False)
            self.add_arc(n+'-end-top',(34,y-6),(40,y),radius_x=6)
            self.add_arc(n+'-end-bottom',(40,y),(34,y+6),radius_x=6)
            self.add_arc(n+'-bottom',(34,y+6),(6,y-4),radius_x=28,radius_y=10)
            self.add_contour(n,n+'-top',n+'-end-top',n+'-end-bottom',n+'-bottom',closed=True)
            self.path(n+'-stem',[(40,y),(42,y-2),(42,y-8)]);self.relate('connect',n,n+'-stem')
