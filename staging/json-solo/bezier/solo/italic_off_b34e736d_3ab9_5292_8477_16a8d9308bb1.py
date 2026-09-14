"""Italic off (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b34e736d-3ab9-5292-8477-16a8d9308bb1'
SOURCE_PATH = 'icons-json/interface-essential/italic off_b34e736d-3ab9-5292-8477-16a8d9308bb1.json'
AUTHOR = 'json_to_solo'

class ItalicOffInterfaceEssential(Solo48):
    icon_id = 'italic-off-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('italic', 'off', 'interface-essential')

    def build(self):
        self.add_line('e0', (16, 4), (40, 4))
        self.add_line('e1', (40, 4), (38, 9))
        self.add_line('e2', (28, 4), (15, 44))
        self.add_line('e3', (8, 4), (37, 44))
        self.add_line('e4', (8, 44), (23, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c3')
