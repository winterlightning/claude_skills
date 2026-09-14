"""Double bread (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dc3acdf-3a36-428c-9473-1d9cbc8584e9'
SOURCE_PATH = 'icons-json/symbol/double bread_8dc3acdf-3a36-428c-9473-1d9cbc8584e9.json'
AUTHOR = 'json_to_solo'

class DoubleBread(Solo48):
    icon_id = 'double-bread'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('double', 'bread', 'symbol')

    def build(self):
        self.add_line('e0', (27, 40), (26, 22))
        self.add_line('e1', (7, 22), (6, 40))
        self.add_line('e2', (6, 40), (42, 40))
        self.add_line('e3', (42, 40), (41, 22))
        self.add_line('e4', (30, 8), (24, 10))
        self.add_arc('e5-1', (26, 22), (28, 14), radius_x=6, sweep=False)
        self.add_arc('e5-2', (28, 14), (26, 11), radius_x=24, sweep=False)
        self.add_arc('e5-3', (26, 11), (16, 8), radius_x=19, sweep=False)
        self.add_arc('e5-4', (16, 8), (11, 9), radius_x=14, sweep=False)
        self.add_arc('e5-5', (11, 9), (7, 11), radius_x=12, sweep=False)
        self.add_arc('e5-6', (7, 11), (4, 17), radius_x=8, sweep=False)
        self.add_line('e5-7', (4, 17), (4, 19))
        self.add_arc('e5-8', (4, 19), (7, 22), radius_x=7, sweep=False)
        self.add_arc('e6-1', (41, 22), (44, 17), radius_x=6, sweep=False)
        self.add_arc('e6-2', (44, 17), (41, 11), radius_x=8, sweep=False)
        self.add_arc('e6-3', (41, 11), (33, 8), radius_x=15, sweep=False)
        self.add_line('e6-4', (33, 8), (30, 8))
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e1', 'e2', 'e3', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e4')
