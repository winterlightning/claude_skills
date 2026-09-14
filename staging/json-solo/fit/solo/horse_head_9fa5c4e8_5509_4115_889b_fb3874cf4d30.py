"""Horse head (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fa5c4e8-5509-4115-889b-fb3874cf4d30'
SOURCE_PATH = 'icons-json/symbol/horse head_9fa5c4e8-5509-4115-889b-fb3874cf4d30.json'
AUTHOR = 'json_to_solo'

class HorseHead9fa5c4e8(Solo48):
    icon_id = 'horse-head-9fa5c4e8'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('horse', 'head', 'symbol')

    def build(self):
        self.add_line('e0', (26, 4), (22, 8))
        self.add_line('e1', (8, 44), (32, 44))
        self.add_line('e2', (39, 23), (40, 19))
        self.add_arc('e3-1', (22, 8), (11, 18), radius_x=15, sweep=False)
        self.add_arc('e3-2', (11, 18), (9, 27), radius_x=39, sweep=False)
        self.add_line('e3-3', (9, 27), (8, 41))
        self.add_line('e3-4', (8, 41), (8, 44))
        self.add_arc('e4-1', (32, 44), (24, 22), radius_x=63)
        self.add_line('e4-2', (24, 22), (35, 26))
        self.add_arc('e4-3', (35, 26), (39, 23), radius_x=4, sweep=False)
        self.add_arc('e5-1', (40, 19), (27, 9), radius_x=44)
        self.add_arc('e5-2', (27, 9), (26, 4), radius_x=17)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e2', 'e5-1', 'e5-2', closed=True)
