"""Powder detergent (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '806035e4-7e36-4174-a964-011dcc4ffae8'
SOURCE_PATH = 'icons-json/wayfinding/powder detergent_806035e4-7e36-4174-a964-011dcc4ffae8.json'
AUTHOR = 'json_to_solo'

class PowderDetergent(Solo48):
    icon_id = 'powder-detergent'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('powder', 'detergent', 'wayfinding')

    def build(self):
        self.add_line('e0', (44, 8), (29, 8))
        self.add_line('e1', (29, 8), (28, 37))
        self.add_line('e2', (26, 40), (8, 40))
        self.add_line('e3', (6, 37), (4, 8))
        self.add_line('e4', (4, 8), (29, 8))
        self.add_line('e5', (28, 37), (26, 40))
        self.add_arc('e6', (8, 40), (6, 37), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
