"""Batch-06/cap (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f6ee542-cdce-408a-b798-b60860e5b325'
SOURCE_PATH = 'icons-json/accessories/batch-06/cap_5f6ee542-cdce-408a-b798-b60860e5b325.json'
AUTHOR = 'json_to_solo'

class Batch06Cap(Solo48):
    icon_id = 'batch-06-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'cap', 'accessories')

    def build(self):
        self.add_line('e0', (38, 20), (38, 33))
        self.add_line('e1', (38, 33), (27, 39))
        self.add_line('e2', (20, 39), (9, 33))
        self.add_line('e3', (9, 33), (9, 20))
        self.add_line('e4', (44, 17), (25, 26))
        self.add_line('e5', (20, 25), (4, 17))
        self.add_line('e6', (4, 17), (19, 10))
        self.add_line('e7', (25, 8), (44, 17))
        self.add_line('e8-1', (27, 39), (23, 40))
        self.add_line('e8-2', (23, 40), (20, 39))
        self.add_arc('e9', (25, 26), (20, 25), radius_x=6)
        self.add_line('e10-1', (19, 10), (24, 8))
        self.add_line('e10-2', (24, 8), (25, 8))
        self.add_contour('c0', 'e0', 'e1', 'e8-1', 'e8-2', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e9', 'e5', 'e6', 'e10-1', 'e10-2', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
