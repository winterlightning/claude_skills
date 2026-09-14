"""Flag plain (social), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e2d4968-05b4-5718-9166-4a59cfa1c4f8'
SOURCE_PATH = 'icons-json/social/flag plain_9e2d4968-05b4-5718-9166-4a59cfa1c4f8.json'
AUTHOR = 'json_to_solo'

class FlagPlain(Solo48):
    icon_id = 'flag-plain'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flag', 'plain', 'social')

    def build(self):
        self.add_line('e0', (40, 7), (40, 26))
        self.add_line('e1', (8, 29), (14, 27))
        self.add_line('e2', (8, 4), (8, 44))
        self.add_arc('e3-1', (8, 9), (18, 6), radius_x=53)
        self.add_arc('e3-2', (18, 6), (35, 8), radius_x=30)
        self.add_arc('e3-3', (35, 8), (40, 7), radius_x=10, sweep=False)
        self.add_arc('e4-1', (14, 27), (22, 25), radius_x=31)
        self.add_line('e4-2', (22, 25), (32, 27))
        self.add_arc('e4-3', (32, 27), (40, 26), radius_x=15, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e0')
        self.add_contour('c1', 'e1', 'e4-1', 'e4-2', 'e4-3')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
