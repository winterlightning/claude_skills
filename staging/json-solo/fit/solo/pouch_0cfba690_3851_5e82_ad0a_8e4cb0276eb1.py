"""Pouch (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cfba690-3851-5e82-ad0a-8e4cb0276eb1'
SOURCE_PATH = 'icons-json/video-games/pouch_0cfba690-3851-5e82-ad0a-8e4cb0276eb1.json'
AUTHOR = 'json_to_solo'

class Pouch0cfba690(Solo48):
    icon_id = 'pouch-0cfba690'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pouch', 'video-games')

    def build(self):
        self.add_line('e0', (21, 15), (23, 13))
        self.add_line('e1', (27, 15), (25, 13))
        self.add_line('e2', (23, 13), (19, 13))
        self.add_line('e3', (23, 13), (29, 13))
        self.add_line('e4', (27, 4), (22, 4))
        self.add_line('e5', (19, 20), (21, 15))
        self.add_line('e6', (29, 20), (27, 15))
        self.add_arc('e7-1', (29, 13), (40, 33), radius_x=24)
        self.add_line('e7-2', (40, 33), (38, 40))
        self.add_arc('e7-3', (38, 40), (35, 43), radius_x=7)
        self.add_line('e7-4', (35, 43), (29, 44))
        self.add_line('e7-5', (29, 44), (13, 43))
        self.add_arc('e7-6', (13, 43), (9, 39), radius_x=9)
        self.add_line('e7-7', (9, 39), (8, 33))
        self.add_arc('e7-8', (8, 33), (19, 13), radius_x=24)
        self.add_arc('e8-1', (29, 13), (32, 6), radius_x=17, sweep=False)
        self.add_line('e8-2', (32, 6), (31, 4))
        self.add_line('e8-3', (31, 4), (29, 4))
        self.add_line('e8-4', (29, 4), (27, 4))
        self.add_line('e9-1', (22, 4), (18, 4))
        self.add_arc('e9-2', (18, 4), (16, 6), radius_x=3, sweep=False)
        self.add_arc('e9-3', (16, 6), (19, 13), radius_x=15, sweep=False)
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e6', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', 'e7-7', 'e7-8')
        self.add_contour('c5', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e4', 'e9-1', 'e9-2', 'e9-3')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c3')
