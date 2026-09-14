"""Loop forward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b54c8548-18c2-54c5-9f78-3a7907732a50'
SOURCE_PATH = 'icons-json/interface-essential/loop forward_b54c8548-18c2-54c5-9f78-3a7907732a50.json'
AUTHOR = 'json_to_solo'

class LoopForwardInterfaceEssential(Solo48):
    icon_id = 'loop-forward-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loop', 'forward', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 35), (13, 35))
        self.add_line('e1', (6, 26), (6, 13))
        self.add_line('e2', (15, 6), (35, 6))
        self.add_line('e3', (42, 12), (42, 17))
        self.add_line('e4', (31, 35), (24, 42))
        self.add_line('e5', (31, 35), (24, 27))
        self.add_arc('e6-1', (13, 35), (6, 28), radius_x=7)
        self.add_line('e6-2', (6, 28), (6, 26))
        self.add_line('e7-1', (6, 13), (8, 8))
        self.add_line('e7-2', (8, 8), (14, 6))
        self.add_line('e7-3', (14, 6), (15, 6))
        self.add_arc('e8', (35, 6), (42, 12), radius_x=8)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2', 'e8', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
