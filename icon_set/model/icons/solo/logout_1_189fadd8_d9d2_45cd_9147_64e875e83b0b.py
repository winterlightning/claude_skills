"""Logout 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '189fadd8-d9d2-45cd-9147-64e875e83b0b'
SOURCE_PATH = 'pictographic-primitives/interface-essential/logout 1_189fadd8-d9d2-45cd-9147-64e875e83b0b.svg'
AUTHOR = 'gpt-6'

class Logout1(Solo48):
    icon_id = 'logout-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('logout', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (15, 24), (42, 24))
        self.add_line('sym-e1', (42, 24), (35, 31))
        self.add_line('sym-e2', (27, 35), (27, 40))
        self.add_arc('sym-e3', (27, 40), (26, 42), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e4', (26, 42), (8, 42))
        self.add_arc('sym-e5', (8, 42), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e6', (6, 40), (6, 8))
        self.add_arc('sym-e8', (6, 8), (8, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e9', (8, 6), (26, 6))
        self.add_arc('sym-e10', (26, 6), (27, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e11', (27, 8), (27, 13))
        self.add_line('sym-e12', (35, 17), (42, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=False)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=False)
        self.add_contour('sym-c2', 'sym-e12', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
