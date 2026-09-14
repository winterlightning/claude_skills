"""Personal hotspot (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f'
SOURCE_PATH = 'icons-json/symbol/personal hotspot_c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f.json'
AUTHOR = 'json_to_solo'

class PersonalHotspotC4cba21b(Solo48):
    icon_id = 'personal-hotspot-c4cba21b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('personal', 'hotspot', 'symbol')

    def build(self):
        self.add_line('e0', (20, 4), (31, 4))
        self.add_line('e1', (18, 44), (27, 44))
        self.add_line('e2', (28, 17), (23, 17))
        self.add_arc('e3-1', (29, 30), (16, 31), radius_x=17)
        self.add_arc('e3-2', (16, 31), (8, 19), radius_x=13)
        self.add_line('e3-3', (8, 19), (10, 11))
        self.add_arc('e3-4', (10, 11), (20, 4), radius_x=14)
        self.add_arc('e4-1', (27, 44), (35, 41), radius_x=13, sweep=False)
        self.add_arc('e4-2', (35, 41), (39, 35), radius_x=15, sweep=False)
        self.add_line('e4-3', (39, 35), (40, 29))
        self.add_arc('e4-4', (40, 29), (28, 17), radius_x=12, sweep=False)
        self.add_arc('e5', (23, 17), (19, 18), radius_x=7, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0')
        self.add_contour('c1', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e2', 'e5')
