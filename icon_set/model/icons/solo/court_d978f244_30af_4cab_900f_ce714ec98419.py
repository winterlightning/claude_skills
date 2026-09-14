"""Court (building), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd978f244-30af-4cab-900f-ce714ec98419'
SOURCE_PATH = 'icons-json/building/court_d978f244-30af-4cab-900f-ce714ec98419.json'
AUTHOR = 'json_to_solo'

class Court(Solo48):
    icon_id = 'court'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('court', 'building')

    def build(self):
        self.add_line('e0', (34, 24), (44, 24))
        self.add_line('e1', (34, 40), (34, 8))
        self.add_line('e2', (4, 24), (14, 24))
        self.add_line('e3', (14, 40), (14, 8))
        self.add_line('e4', (24, 8), (24, 40))
        self.add_line('e5', (44, 40), (4, 40))
        self.add_line('e6', (4, 40), (4, 8))
        self.add_line('e7', (4, 8), (44, 8))
        self.add_line('e8', (44, 8), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e6', 'e7', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c5')
