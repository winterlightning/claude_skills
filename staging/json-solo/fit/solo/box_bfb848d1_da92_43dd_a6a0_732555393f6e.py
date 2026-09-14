"""Box (shipping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfb848d1-da92-43dd-a6a0-732555393f6e'
SOURCE_PATH = 'icons-json/shipping/box_bfb848d1-da92-43dd-a6a0-732555393f6e.json'
AUTHOR = 'json_to_solo'

class Box(Solo48):
    icon_id = 'box'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('box', 'shipping')

    def build(self):
        self.add_line('e0', (31, 6), (31, 23))
        self.add_line('e1', (31, 23), (24, 18))
        self.add_line('e2', (24, 18), (17, 23))
        self.add_line('e3', (17, 23), (17, 6))
        self.add_line('e4', (6, 42), (42, 42))
        self.add_line('e5', (42, 42), (42, 6))
        self.add_line('e6', (42, 6), (6, 6))
        self.add_line('e7', (6, 6), (6, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e6', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
