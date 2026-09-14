"""Outdoors camp fire (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e79029cc-1cc4-41cb-87c3-cb06d318b0ed'
SOURCE_PATH = 'icons-json/outdoors/outdoors camp fire_e79029cc-1cc4-41cb-87c3-cb06d318b0ed.json'
AUTHOR = 'json_to_solo'

class OutdoorsCampFire(Solo48):
    icon_id = 'outdoors-camp-fire'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('outdoors', 'camp', 'fire')

    def build(self):
        self.add_line('e0', (40, 35), (23, 39))
        self.add_line('e1', (23, 39), (8, 44))
        self.add_line('e2', (23, 39), (40, 44))
        self.add_line('e3', (8, 36), (23, 39))
        self.add_line('e4', (26, 4), (24, 5))
        self.add_arc('e5', (23, 39), (24, 39), radius_x=1, sweep=False)
        self.add_arc('e6-1', (24, 5), (16, 31), radius_x=19, sweep=False)
        self.add_arc('e6-2', (16, 31), (35, 27), radius_x=11, sweep=False)
        self.add_arc('e6-3', (35, 27), (34, 17), radius_x=13, sweep=False)
        self.add_arc('e6-4', (34, 17), (30, 12), radius_x=14, sweep=False)
        self.add_arc('e6-5', (30, 12), (29, 16), radius_x=12)
        self.add_arc('e6-6', (29, 16), (27, 16), radius_x=1)
        self.add_arc('e6-7', (27, 16), (25, 12), radius_x=9)
        self.add_arc('e6-8', (25, 12), (26, 4), radius_x=15)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3')
        self.add_contour('c5', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
