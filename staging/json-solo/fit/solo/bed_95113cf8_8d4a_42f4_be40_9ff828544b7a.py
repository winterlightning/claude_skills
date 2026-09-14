"""Bed (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95113cf8-8d4a-42f4-be40-9ff828544b7a'
SOURCE_PATH = 'icons-json/symbol/bed_95113cf8-8d4a-42f4-be40-9ff828544b7a.json'
AUTHOR = 'json_to_solo'

class Bed95113cf8(Solo48):
    icon_id = 'bed-95113cf8'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bed', 'symbol')

    def build(self):
        self.add_line('e0', (44, 23), (4, 23))
        self.add_line('e1', (44, 34), (4, 34))
        self.add_line('e2', (4, 33), (4, 8))
        self.add_line('e3', (4, 40), (4, 33))
        self.add_line('e4', (44, 40), (44, 23))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c3')
