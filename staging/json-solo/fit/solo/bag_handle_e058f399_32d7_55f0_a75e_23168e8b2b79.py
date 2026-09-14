"""Batch-02/bag handle (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e058f399-32d7-55f0-a75e-23168e8b2b79'
SOURCE_PATH = 'icons-json/accessories/batch-02/bag handle_e058f399-32d7-55f0-a75e-23168e8b2b79.json'
AUTHOR = 'json_to_solo'

class Batch02BagHandle(Solo48):
    icon_id = 'batch-02-bag-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'bag', 'handle', 'accessories')

    def build(self):
        self.add_line('e0', (16, 19), (16, 12))
        self.add_line('e1', (32, 12), (32, 19))
        self.add_line('e2', (37, 44), (10, 44))
        self.add_line('e3', (9, 27), (10, 15))
        self.add_line('e4', (10, 15), (38, 15))
        self.add_line('e5', (38, 15), (40, 41))
        self.add_arc('e6-1', (16, 12), (24, 4), radius_x=8)
        self.add_arc('e6-2', (24, 4), (32, 12), radius_x=8)
        self.add_arc('e7', (40, 41), (37, 44), radius_x=3)
        self.add_arc('e8-1', (10, 44), (8, 42), radius_x=2)
        self.add_line('e8-2', (8, 42), (9, 27))
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1')
        self.add_contour('c1', 'e7', 'e2', 'e8-1', 'e8-2', 'e3', 'e4', 'e5', closed=True)
