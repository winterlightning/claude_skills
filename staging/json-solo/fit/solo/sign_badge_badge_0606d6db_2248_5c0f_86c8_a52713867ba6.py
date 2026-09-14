"""Sign badge badge (maps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0606d6db-2248-5c0f-86c8-a52713867ba6'
SOURCE_PATH = 'icons-json/maps/sign badge badge_0606d6db-2248-5c0f-86c8-a52713867ba6.json'
AUTHOR = 'json_to_solo'

class SignBadgeBadge0606d6db(Solo48):
    icon_id = 'sign-badge-badge-0606d6db'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'maps')

    def build(self):
        self.add_line('e0', (27, 42), (24, 44))
        self.add_line('e1', (9, 24), (11, 20))
        self.add_line('e2', (11, 12), (8, 9))
        self.add_line('e3', (8, 9), (12, 4))
        self.add_line('e4', (12, 4), (18, 8))
        self.add_line('e5', (18, 8), (24, 4))
        self.add_line('e6', (24, 4), (30, 8))
        self.add_line('e7', (30, 8), (36, 4))
        self.add_line('e8', (36, 4), (39, 9))
        self.add_arc('e9-1', (39, 9), (36, 16), radius_x=11, sweep=False)
        self.add_line('e9-2', (36, 16), (40, 27))
        self.add_arc('e9-3', (40, 27), (27, 42), radius_x=17)
        self.add_arc('e10-1', (24, 44), (8, 28), radius_x=21)
        self.add_arc('e10-2', (8, 28), (9, 24), radius_x=12)
        self.add_arc('e11', (11, 20), (11, 12), radius_x=7, sweep=False)
        self.add_contour('c0', 'e9-1', 'e9-2', 'e9-3', 'e0', 'e10-1', 'e10-2', 'e1', 'e11', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', closed=True)
