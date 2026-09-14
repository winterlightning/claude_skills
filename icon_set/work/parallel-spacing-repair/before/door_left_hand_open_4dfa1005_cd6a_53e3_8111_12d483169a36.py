"""Door left hand open (building), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4dfa1005-cd6a-53e3-8111-12d483169a36'
SOURCE_PATH = 'icons-json/building/door left hand open_4dfa1005-cd6a-53e3-8111-12d483169a36.json'
AUTHOR = 'json_to_solo'

class DoorLeftHandOpen(Solo48):
    icon_id = 'door-left-hand-open'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('door', 'left', 'hand', 'open', 'building')

    def build(self):
        self.add_line('e0', (8, 44), (8, 6))
        self.add_line('e1', (11, 4), (40, 4))
        self.add_line('e2', (40, 4), (40, 44))
        self.add_line('e3', (40, 44), (35, 43))
        self.add_line('e4', (35, 43), (24, 41))
        self.add_line('e5', (20, 39), (20, 15))
        self.add_line('e6', (38, 6), (40, 6))
        self.add_arc('e7-top', (25, 25), (29, 25), radius_x=2)
        self.add_arc('e7-bottom', (29, 25), (25, 25), radius_x=2)
        self.add_line('e8-1', (8, 6), (9, 4))
        self.add_arc('e8-2', (9, 4), (11, 4), radius_x=6, sweep=False)
        self.add_arc('e9', (24, 41), (20, 39), radius_x=3)
        self.add_arc('e10-1', (20, 15), (21, 11), radius_x=4)
        self.add_line('e10-2', (21, 11), (38, 6))
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e9', 'e5', 'e10-1', 'e10-2', 'e6')
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
