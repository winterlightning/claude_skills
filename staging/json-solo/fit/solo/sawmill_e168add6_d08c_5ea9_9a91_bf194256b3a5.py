"""Sawmill (tools), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e168add6-d08c-5ea9-9a91-bf194256b3a5'
SOURCE_PATH = 'icons-json/tools/sawmill_e168add6-d08c-5ea9-9a91-bf194256b3a5.json'
AUTHOR = 'json_to_solo'

class SawmillTools(Solo48):
    icon_id = 'sawmill-tools'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('sawmill', 'tools')

    def build(self):
        self.add_line('e0', (37, 29), (38, 26))
        self.add_line('e1', (9, 40), (4, 40))
        self.add_line('e2', (8, 40), (44, 40))
        self.add_arc('e3-1', (30, 40), (22, 27), radius_x=10, sweep=False)
        self.add_arc('e3-2', (22, 27), (17, 40), radius_x=14, sweep=False)
        self.add_line('e4-1', (39, 40), (41, 31))
        self.add_arc('e4-2', (41, 31), (37, 29), radius_x=3)
        self.add_line('e5-1', (38, 26), (37, 16))
        self.add_arc('e5-2', (37, 16), (32, 20), radius_x=5)
        self.add_arc('e5-3', (32, 20), (28, 8), radius_x=17, sweep=False)
        self.add_arc('e5-4', (28, 8), (27, 14), radius_x=22)
        self.add_arc('e5-5', (27, 14), (25, 14), radius_x=1)
        self.add_arc('e5-6', (25, 14), (19, 8), radius_x=8, sweep=False)
        self.add_arc('e5-7', (19, 8), (19, 15), radius_x=16)
        self.add_arc('e5-8', (19, 15), (18, 16), radius_x=1)
        self.add_arc('e5-9', (18, 16), (10, 16), radius_x=5, sweep=False)
        self.add_arc('e6-1', (13, 24), (8, 27), radius_x=11, sweep=False)
        self.add_arc('e6-2', (8, 27), (6, 31), radius_x=18, sweep=False)
        self.add_arc('e6-3', (6, 31), (7, 31), radius_x=6)
        self.add_arc('e6-4', (7, 31), (9, 40), radius_x=6)
        self.add_arc('e7', (13, 24), (10, 16), radius_x=13, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e7')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
