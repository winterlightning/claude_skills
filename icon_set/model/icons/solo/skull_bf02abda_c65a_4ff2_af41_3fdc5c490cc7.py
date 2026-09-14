"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf02abda-c65a-4ff2-af41-3fdc5c490cc7'
SOURCE_PATH = 'icons-json/interface-essential/skull_bf02abda-c65a-4ff2-af41-3fdc5c490cc7.json'
AUTHOR = 'json_to_solo'

class SkullBf02abda(Solo48):
    icon_id = 'skull-bf02abda'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 38), (24, 44))
        self.add_line('e1', (12, 34), (15, 37))
        self.add_line('e2', (15, 37), (15, 40))
        self.add_line('e3', (18, 44), (30, 44))
        self.add_line('e4', (33, 40), (33, 37))
        self.add_arc('e5-1', (33, 37), (39, 28), radius_x=19, sweep=False)
        self.add_line('e5-2', (39, 28), (40, 22))
        self.add_arc('e5-3', (40, 22), (36, 10), radius_x=20, sweep=False)
        self.add_arc('e5-4', (36, 10), (24, 4), radius_x=15, sweep=False)
        self.add_arc('e5-5', (24, 4), (14, 8), radius_x=15, sweep=False)
        self.add_arc('e5-6', (14, 8), (10, 13), radius_x=18, sweep=False)
        self.add_line('e5-7', (10, 13), (8, 22))
        self.add_arc('e5-8', (8, 22), (12, 34), radius_x=20, sweep=False)
        self.add_arc('e6', (15, 40), (18, 44), radius_x=5, sweep=False)
        self.add_arc('e7', (30, 44), (33, 40), radius_x=4, sweep=False)
        self.add_dot('e8', (32, 20))
        self.add_dot('e9', (16, 20))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e1', 'e2', 'e6', 'e3', 'e7', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
