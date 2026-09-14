"""Layout 12 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1fcaf8a-7c4c-41de-a51a-94fd11f5e747'
SOURCE_PATH = 'icons-json/interface-essential/layout 12_d1fcaf8a-7c4c-41de-a51a-94fd11f5e747.json'
AUTHOR = 'json_to_solo'

class Layout12InterfaceEssential(Solo48):
    icon_id = 'layout-12-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 27), (42, 27))
        self.add_line('e1', (24, 27), (24, 42))
        self.add_line('e2', (24, 27), (24, 17))
        self.add_line('e3', (42, 27), (42, 40))
        self.add_line('e4', (40, 42), (24, 42))
        self.add_line('e5', (42, 27), (42, 17))
        self.add_line('e6', (24, 17), (42, 17))
        self.add_line('e7', (24, 17), (24, 6))
        self.add_line('e8', (24, 42), (8, 42))
        self.add_line('e9', (6, 40), (6, 8))
        self.add_line('e10', (8, 6), (24, 6))
        self.add_line('e11', (42, 17), (42, 8))
        self.add_line('e12', (40, 6), (24, 6))
        self.add_line('e13', (42, 40), (40, 42))
        self.add_line('e14', (8, 42), (6, 40))
        self.add_line('e15', (6, 8), (8, 6))
        self.add_line('e16', (42, 8), (40, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e13', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e8', 'e14', 'e9', 'e15', 'e10')
        self.add_contour('c8', 'e11', 'e16', 'e12')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
