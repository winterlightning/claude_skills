"""Cube (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '802601c0-689d-481d-86cd-d13aceeaf9a1'
SOURCE_PATH = 'icons-json/symbol/cube_802601c0-689d-481d-86cd-d13aceeaf9a1.json'
AUTHOR = 'json_to_solo'

class CubeSymbol(Solo48):
    icon_id = 'cube-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cube', 'symbol')

    def build(self):
        self.add_line('e0', (40, 13), (40, 34))
        self.add_line('e1', (40, 34), (24, 44))
        self.add_line('e2', (40, 13), (24, 4))
        self.add_line('e3', (24, 4), (8, 13))
        self.add_line('e4', (40, 13), (24, 21))
        self.add_line('e5', (24, 44), (24, 21))
        self.add_line('e6', (24, 44), (8, 34))
        self.add_line('e7', (8, 34), (8, 13))
        self.add_line('e8', (24, 21), (8, 13))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e7')
        self.add_contour('c5', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
