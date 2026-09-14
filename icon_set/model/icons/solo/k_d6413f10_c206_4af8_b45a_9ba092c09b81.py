"""K (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6413f10-c206-4af8-b45a-9ba092c09b81'
SOURCE_PATH = 'icons-json/typeface/k_d6413f10-c206-4af8-b45a-9ba092c09b81.json'
AUTHOR = 'json_to_solo'

class KTypeface(Solo48):
    icon_id = 'k-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('k', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (37, 12), (8, 24))
        self.add_line('e2', (40, 44), (15, 21))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
