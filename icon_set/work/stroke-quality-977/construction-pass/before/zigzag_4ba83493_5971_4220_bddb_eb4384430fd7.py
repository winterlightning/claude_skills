"""Zigzag (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ba83493-5971-4220-bddb-eb4384430fd7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/zigzag_4ba83493-5971-4220-bddb-eb4384430fd7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ZigzagInterfaceEssential(Solo48):
    icon_id = 'zigzag-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zigzag', 'interface-essential')

    def build(self):
        self.add_line('e0', (34, 25), (40, 31))
        self.add_line('e1', (40, 31), (32, 36))
        self.add_line('e2', (32, 36), (40, 44))
        self.add_line('e3', (12, 24), (17, 31))
        self.add_line('e4', (17, 31), (8, 35))
        self.add_line('e5', (8, 35), (14, 44))
        self.add_line('e6', (20, 4), (27, 10))
        self.add_line('e7', (27, 10), (20, 15))
        self.add_line('e8', (20, 15), (27, 21))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5')
        self.add_contour('c2', 'e6', 'e7', 'e8')
