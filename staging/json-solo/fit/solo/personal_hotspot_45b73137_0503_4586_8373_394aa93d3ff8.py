"""Personal hotspot (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45b73137-0503-4586-8373-394aa93d3ff8'
SOURCE_PATH = 'icons-json/symbol/personal hotspot_45b73137-0503-4586-8373-394aa93d3ff8.json'
AUTHOR = 'json_to_solo'

class PersonalHotspot45b73137(Solo48):
    icon_id = 'personal-hotspot-45b73137'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('personal', 'hotspot', 'symbol')

    def build(self):
        self.add_line('e0', (29, 19), (20, 19))
        self.add_line('e1', (21, 40), (32, 40))
        self.add_line('e2', (15, 8), (29, 8))
        self.add_arc('e3-1', (20, 19), (12, 27), radius_x=10, sweep=False)
        self.add_arc('e3-2', (12, 27), (21, 40), radius_x=10, sweep=False)
        self.add_line('e4-1', (32, 40), (39, 39))
        self.add_arc('e4-2', (39, 39), (43, 35), radius_x=8, sweep=False)
        self.add_line('e4-3', (43, 35), (44, 30))
        self.add_arc('e4-4', (44, 30), (44, 28), radius_x=32)
        self.add_line('e5-1', (4, 21), (5, 14))
        self.add_arc('e5-2', (5, 14), (15, 8), radius_x=12)
        self.add_arc('e6-1', (29, 8), (36, 25), radius_x=10)
        self.add_arc('e6-2', (36, 25), (21, 29), radius_x=15)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e2', 'e6-1', 'e6-2')
