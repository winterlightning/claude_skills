"""House with Door Division; standalone reconstruction of the supplied reference.
Construction: Lucide house informed coherent contours and structural joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae6e559-27d0-490b-b13a-e0950315fc03'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house_5ae6e559-27d0-490b-b13a-e0950315fc03.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-door-division'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    tags = ('sub icon',)
    aliases = ()
    keywords = ('house', 'home', 'roof', 'door', 'building', 'outline')

    def build(self):
        # Plan: mirrored house about x=24; SQUARE extremes (6,6)-(42,42).
        # Door and wall dimensions belong to the facade; roof shares exact wall nodes.
        axis=24
        left,right=10,38
        base=42
        self.add_polyline("roof", (6,24),(left,20),(axis,6),(right,20),(42,24))
        self.add_polyline("walls",(left,20),(left,base),(axis,base),(right,base),(right,20))
        self.relate("connect","roof","walls")
        self.add_line("door-division",(axis,30),(axis,base))
        self.relate("connect","door-division","walls")
