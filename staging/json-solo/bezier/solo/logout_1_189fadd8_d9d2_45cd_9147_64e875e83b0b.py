"""Logout 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '189fadd8-d9d2-45cd-9147-64e875e83b0b'
SOURCE_PATH = 'icons-json/interface-essential/logout 1_189fadd8-d9d2-45cd-9147-64e875e83b0b.json'
AUTHOR = 'json_to_solo'

class Logout1InterfaceEssential(Solo48):
    icon_id = 'logout-1-interface-essential'
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
        self.add_bezier('sym-e3', (27, 40), ((26.501, 41.113), (27.129, 41.542), (26, 42)))
        self.add_line('sym-e4', (26, 42), (8, 42))
        self.add_bezier('sym-e5', (8, 42), ((7.296, 41.722), (6, 40.957), (6, 40)))
        self.add_line('sym-e6', (6, 40), (6, 24))
        self.add_line('sym-e7', (6, 24), (6, 8))
        self.add_bezier('sym-e8', (6, 8), ((6, 7.043), (7.296, 6.278), (8, 6)))
        self.add_line('sym-e9', (8, 6), (26, 6))
        self.add_bezier('sym-e10', (26, 6), ((27.129, 6.458), (26.501, 6.887), (27, 8)))
        self.add_line('sym-e11', (27, 8), (27, 13))
        self.add_line('sym-e12', (35, 17), (42, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e12')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
