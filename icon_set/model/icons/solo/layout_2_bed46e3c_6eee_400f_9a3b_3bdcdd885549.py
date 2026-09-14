"""Layout 2 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bed46e3c-6eee-400f-9a3b-3bdcdd885549'
SOURCE_PATH = 'icons-json/interface-essential/layout 2_bed46e3c-6eee-400f-9a3b-3bdcdd885549.json'
AUTHOR = 'json_to_solo'

class Layout2(Solo48):
    icon_id = 'layout-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 31), (42, 31))
        self.add_line('e1', (24, 31), (24, 42))
        self.add_line('e2', (24, 31), (24, 19))
        self.add_line('e3', (42, 31), (42, 39))
        self.add_line('e4', (40, 42), (24, 42))
        self.add_line('e5', (42, 31), (42, 19))
        self.add_line('e6', (24, 19), (42, 19))
        self.add_line('e7', (24, 19), (24, 6))
        self.add_line('e8', (42, 19), (42, 9))
        self.add_line('e9', (39, 6), (24, 6))
        self.add_line('e10', (24, 42), (9, 42))
        self.add_line('e11', (6, 39), (6, 8))
        self.add_line('e12', (8, 6), (24, 6))
        self.add_line('e13', (42, 39), (40, 42))
        self.add_arc('e14', (42, 9), (39, 6), radius_x=4, sweep=False)
        self.add_arc('e15', (9, 42), (6, 39), radius_x=5)
        self.add_line('e16', (6, 8), (8, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e13', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e8', 'e14', 'e9')
        self.add_contour('c8', 'e10', 'e15', 'e11', 'e16', 'e12')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
