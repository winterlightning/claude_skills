"""Not equal (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bda617e4-9a2d-4960-ad51-778fd8967c24'
SOURCE_PATH = 'icons-json/interface-essential/not equal_bda617e4-9a2d-4960-ad51-778fd8967c24.json'
AUTHOR = 'json_to_solo'

class NotEqualInterfaceEssential(Solo48):
    icon_id = 'not-equal-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('not', 'equal', 'interface-essential')

    def build(self):
        self.add_line('e0', (33, 4), (21, 30))
        self.add_line('e1', (21, 30), (40, 30))
        self.add_line('e2', (8, 19), (40, 19))
        self.add_line('e3', (8, 30), (21, 30))
        self.add_line('e4', (21, 30), (16, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.relate('connect', 'c0', 'c2')
