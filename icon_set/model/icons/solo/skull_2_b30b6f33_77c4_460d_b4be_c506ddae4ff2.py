"""Skull 2 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b30b6f33-77c4-460d-b4be-c506ddae4ff2'
SOURCE_PATH = 'icons-json/interface-essential/skull 2_b30b6f33-77c4-460d-b4be-c506ddae4ff2.json'
AUTHOR = 'json_to_solo'

class Skull2(Solo48):
    icon_id = 'skull-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 24), (35, 22))
        self.add_line('e1', (18, 24), (14, 22))
        self.add_line('e2', (15, 42), (15, 38))
        self.add_line('e3', (38, 33), (35, 35))
        self.add_line('e4', (34, 38), (34, 42))
        self.add_line('e5', (24, 42), (24, 40))
        self.add_line('e6-1', (15, 38), (14, 35))
        self.add_arc('e6-2', (14, 35), (8, 31), radius_x=15)
        self.add_line('e6-3', (8, 31), (6, 24))
        self.add_arc('e6-4', (6, 24), (24, 6), radius_x=18)
        self.add_arc('e6-5', (24, 6), (42, 24), radius_x=18)
        self.add_arc('e6-6', (42, 24), (41, 29), radius_x=13)
        self.add_arc('e6-7', (41, 29), (38, 33), radius_x=7)
        self.add_arc('e7', (35, 35), (34, 38), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e3', 'e7', 'e4')
        self.add_contour('c3', 'e5')
