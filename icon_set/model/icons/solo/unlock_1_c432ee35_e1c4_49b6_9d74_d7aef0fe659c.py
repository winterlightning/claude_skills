"""Unlock 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c432ee35-e1c4-49b6-9d74-d7aef0fe659c'
SOURCE_PATH = 'icons-json/symbol/unlock 1_c432ee35-e1c4-49b6-9d74-d7aef0fe659c.json'
AUTHOR = 'gpt-6'

class Unlock1(Solo48):
    icon_id = 'unlock-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('unlock', 'symbol')

    def build(self):
        self.add_line('e0', (13, 14), (13, 21))
        self.add_line('e1', (33, 44), (14, 44))
        self.add_line('e3', (8, 21), (40, 21))
        self.add_line('e4', (40, 21), (40, 39))
        self.add_arc('e5-1', (35, 15), (24, 4), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('e5-2', (24, 4), (19, 5))
        self.add_arc('e5-3', (19, 5), (16, 7), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('e5-4', (16, 7), (13, 14), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('e6-1', (40, 39), (39, 42))
        self.add_line('e6-2', (39, 42), (33, 44))
        self.add_line('e7-1', (14, 44), (9, 42))
        self.add_line('e7-2', (9, 42), (8, 39))
        self.add_line('e7-3', (8, 39), (8, 21))
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e0', closed=False)
        self.add_contour('c1', 'e6-1', 'e6-2', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
