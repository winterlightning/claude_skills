"""Door right hand open (building), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fb03413-96f1-455e-99d0-84c346c2a56f'
SOURCE_PATH = 'icons-json/building/door right hand open_8fb03413-96f1-455e-99d0-84c346c2a56f.json'
AUTHOR = 'json_to_solo'

class DoorRightHandOpen(Solo48):
    icon_id = 'door-right-hand-open'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('door', 'right', 'hand', 'open', 'building')

    def build(self):
        self.add_line('e0', (6, 42), (10, 42))
        self.add_line('e1', (10, 42), (10, 8))
        self.add_line('e2', (12, 6), (36, 6))
        self.add_line('e3', (38, 8), (38, 42))
        self.add_line('e4', (42, 42), (38, 42))
        self.add_line('e5', (36, 6), (26, 13))
        self.add_line('e6', (26, 13), (26, 39))
        self.add_line('e7', (26, 39), (32, 41))
        self.add_arc('e8', (10, 8), (12, 6), radius_x=2)
        self.add_arc('e9', (36, 6), (38, 8), radius_x=3)
        self.add_line('e10-1', (32, 41), (37, 42))
        self.add_line('e10-2', (37, 42), (38, 42))
        self.add_contour('c0', 'e0', 'e1', 'e8', 'e2', 'e9', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e6', 'e7', 'e10-1', 'e10-2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
