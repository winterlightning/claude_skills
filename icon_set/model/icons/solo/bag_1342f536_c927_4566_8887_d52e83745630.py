"""Bag (photography), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1342f536-c927-4566-8887-d52e83745630'
SOURCE_PATH = 'icons-json/photography/bag_1342f536-c927-4566-8887-d52e83745630.json'
AUTHOR = 'json_to_solo'

class BagPhotography(Solo48):
    icon_id = 'bag-photography'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('bag', 'photography')

    def build(self):
        self.add_line('e0', (16, 19), (16, 12))
        self.add_line('e1', (32, 12), (32, 19))
        self.add_line('e2', (32, 44), (14, 44))
        self.add_line('e3', (8, 35), (11, 15))
        self.add_line('e4', (11, 15), (37, 15))
        self.add_line('e5', (37, 15), (40, 37))
        self.add_arc('e6-1', (16, 12), (24, 4), radius_x=9)
        self.add_arc('e6-2', (24, 4), (32, 12), radius_x=8)
        self.add_line('e7-1', (40, 37), (39, 41))
        self.add_arc('e7-2', (39, 41), (37, 43), radius_x=5)
        self.add_line('e7-3', (37, 43), (32, 44))
        self.add_arc('e8-1', (14, 44), (8, 38), radius_x=6)
        self.add_line('e8-2', (8, 38), (8, 35))
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e7-3', 'e2', 'e8-1', 'e8-2', 'e3', 'e4', 'e5', closed=True)
