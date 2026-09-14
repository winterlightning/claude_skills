"""Neck pillow (travel), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9cf7d8b8-f3ff-53fd-86a6-fa033f2bf90e'
SOURCE_PATH = 'icons-json/travel/neck pillow_9cf7d8b8-f3ff-53fd-86a6-fa033f2bf90e.json'
AUTHOR = 'json_to_solo'

class NeckPillowTravel(Solo48):
    icon_id = 'neck-pillow-travel'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('neck', 'pillow', 'travel')

    def build(self):
        self.add_line('e0', (29, 33), (31, 26))
        self.add_arc('e1-1', (31, 26), (20, 19), radius_x=7, sweep=False)
        self.add_arc('e1-2', (20, 19), (17, 27), radius_x=6, sweep=False)
        self.add_arc('e1-3', (17, 27), (20, 35), radius_x=16)
        self.add_arc('e1-4', (20, 35), (14, 40), radius_x=7)
        self.add_arc('e1-5', (14, 40), (8, 37), radius_x=8)
        self.add_arc('e1-6', (8, 37), (4, 24), radius_x=24)
        self.add_arc('e1-7', (4, 24), (16, 9), radius_x=16)
        self.add_line('e1-8', (16, 9), (23, 8))
        self.add_line('e1-9', (23, 8), (32, 9))
        self.add_arc('e1-10', (32, 9), (37, 11), radius_x=20)
        self.add_arc('e1-11', (37, 11), (43, 18), radius_x=15)
        self.add_line('e1-12', (43, 18), (44, 24))
        self.add_arc('e1-13', (44, 24), (40, 37), radius_x=24)
        self.add_arc('e1-14', (40, 37), (35, 40), radius_x=6)
        self.add_line('e1-15', (35, 40), (31, 39))
        self.add_arc('e1-16', (31, 39), (29, 37), radius_x=5)
        self.add_arc('e1-17', (29, 37), (29, 33), radius_x=5)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12', 'e1-13', 'e1-14', 'e1-15', 'e1-16', 'e1-17', closed=True)
