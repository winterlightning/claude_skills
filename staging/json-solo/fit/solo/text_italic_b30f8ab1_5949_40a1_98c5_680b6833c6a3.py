"""Text italic (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b30f8ab1-5949-40a1-98c5-680b6833c6a3'
SOURCE_PATH = 'icons-json/interface-essential/text italic_b30f8ab1-5949-40a1-98c5-680b6833c6a3.json'
AUTHOR = 'json_to_solo'

class TextItalicInterfaceEssential(Solo48):
    icon_id = 'text-italic-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'italic', 'interface-essential')

    def build(self):
        self.add_line('e0', (25, 4), (33, 4))
        self.add_line('e1', (8, 44), (16, 44))
        self.add_line('e2', (16, 44), (33, 4))
        self.add_line('e3', (16, 44), (24, 44))
        self.add_line('e4', (40, 4), (33, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
