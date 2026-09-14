"""Bricks (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5459f02d-65a5-4f19-bce8-1738f0b007a8'
SOURCE_PATH = 'icons-json/symbol/bricks_5459f02d-65a5-4f19-bce8-1738f0b007a8.json'
AUTHOR = 'json_to_solo'

class BricksSymbol(Solo48):
    icon_id = 'bricks-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bricks', 'symbol')

    def build(self):
        self.add_line('e0', (44, 24), (4, 24))
        self.add_line('e1', (30, 40), (30, 24))
        self.add_line('e2', (17, 8), (17, 24))
        self.add_line('e3', (44, 8), (44, 40))
        self.add_line('e4', (44, 40), (4, 40))
        self.add_line('e5', (4, 40), (4, 8))
        self.add_line('e6', (4, 8), (44, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', 'e6', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c0')
