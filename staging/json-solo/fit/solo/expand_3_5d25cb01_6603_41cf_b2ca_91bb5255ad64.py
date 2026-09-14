"""Expand 3 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d25cb01-6603-41cf-b2ca-91bb5255ad64'
SOURCE_PATH = 'icons-json/interface-essential/expand 3_5d25cb01-6603-41cf-b2ca-91bb5255ad64.json'
AUTHOR = 'json_to_solo'

class Expand3InterfaceEssential(Solo48):
    icon_id = 'expand-3-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'interface-essential')

    def build(self):
        self.add_line('e0', (35, 6), (42, 6))
        self.add_line('e1', (6, 13), (6, 6))
        self.add_line('e2', (6, 35), (6, 42))
        self.add_line('e3', (13, 42), (6, 42))
        self.add_line('e4', (35, 42), (40, 42))
        self.add_line('e5', (42, 34), (42, 42))
        self.add_line('e6', (42, 13), (42, 6))
        self.add_line('e7', (42, 6), (24, 24))
        self.add_line('e8', (6, 6), (24, 24))
        self.add_line('e9', (42, 42), (24, 24))
        self.add_line('e10', (24, 24), (6, 42))
        self.add_line('e11', (13, 6), (6, 6))
        self.add_arc('e12-1', (40, 42), (41, 42), radius_x=41)
        self.add_line('e12-2', (41, 42), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e11')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3')
        self.add_contour('c5', 'e4', 'e12-1', 'e12-2')
        self.add_contour('c6', 'e5')
        self.add_contour('c7', 'e6')
        self.add_contour('c8', 'e7')
        self.add_contour('c9', 'e8')
        self.add_contour('c10', 'e9')
        self.add_contour('c11', 'e10')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c9')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c11', 'c3')
        self.relate('connect', 'c11', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c10', 'c5')
        self.relate('connect', 'c10', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c8')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c11', 'c8')
        self.relate('connect', 'c11', 'c9')
        self.relate('connect', 'c8', 'c9')
