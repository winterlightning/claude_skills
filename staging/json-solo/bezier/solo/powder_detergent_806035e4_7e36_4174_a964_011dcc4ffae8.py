"""Powder detergent (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '806035e4-7e36-4174-a964-011dcc4ffae8'
SOURCE_PATH = 'icons-json/wayfinding/powder detergent_806035e4-7e36-4174-a964-011dcc4ffae8.json'
AUTHOR = 'json_to_solo'

class PowderDetergentWayfinding(Solo48):
    icon_id = 'powder-detergent-wayfinding'
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
        self.add_bezier('e5', (28, 37), ((27.436, 39.224), (27.273, 39.088), (26, 40)))
        self.add_bezier('e6', (8, 40), ((7.964, 39.968), (7.218, 39.84), (7.182, 39.808)), ((6.436, 39.296), (6.327, 38.12), (6, 37)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
