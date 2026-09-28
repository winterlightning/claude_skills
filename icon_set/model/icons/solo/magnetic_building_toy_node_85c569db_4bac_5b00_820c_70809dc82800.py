'Magnetic toy node: round central hub, equal corner balls, and explicit rod attachment points.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85c569db-4bac-5b00-820c-70809dc82800'
SOURCE_PATH = 'pictographic-primitives/internet/magnetic building toy node_85c569db-4bac-5b00-820c-70809dc82800.svg'
AUTHOR = 'gpt-6'

class MagneticBuildingToyNode(Solo48):
    icon_id = 'magnetic-building-toy-node'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    categories = ('internet', 'primitives')
    aliases = ()
    keywords = ('magnetic', 'building', 'toy', 'node', 'internet')

    def build(self) -> None:
        self.add_arc('hub-top', (17,24), (31,24), radius_x=7, radius_y=7)
        self.add_arc('hub-bottom', (31,24), (17,24), radius_x=7, radius_y=7)
        self.add_contour('hub', 'hub-top', 'hub-bottom', closed=True)

        # Four equal corner nodes connect to cardinal hub anchors with smooth diagonal rods.
        for name,cx,cy,hx,hy,ex,ey in (('nw',10,10,24,17,14,10),('ne',38,10,31,24,38,14),('se',38,38,24,31,34,38),('sw',10,38,17,24,10,34)):
            self.add_arc(name+'-a',(cx-4,cy),(cx+4,cy),radius_x=4)
            self.add_arc(name+'-b',(cx+4,cy),(cx-4,cy),radius_x=4)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
            self.add_line(name+'-rod',(hx,hy),(ex,ey))
            self.relate('connect',name+'-rod','hub');self.relate('connect',name+'-rod',name)
