"""Door left hand closed (building), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3bcb648-33a4-4112-a9ca-00bcdf092bab'
SOURCE_PATH = 'icons-json/building/door left hand closed_f3bcb648-33a4-4112-a9ca-00bcdf092bab.json'
AUTHOR = 'json_to_solo'

class DoorLeftHandClosed(Solo48):
    icon_id = 'door-left-hand-closed'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('door', 'left', 'hand', 'closed', 'building')

    def build(self):
        self.add_line('e0', (6, 42), (10, 42))
        self.add_line('e1', (42, 42), (37, 42))
        self.add_line('e2', (10, 42), (10, 8))
        self.add_line('e3', (12, 6), (35, 6))
        self.add_line('e4', (37, 8), (37, 42))
        self.add_line('e5', (10, 42), (37, 42))
        self.add_arc('e6', (10, 8), (12, 6), radius_x=2)
        self.add_arc('e7', (35, 6), (37, 8), radius_x=2)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e7', 'e4')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
