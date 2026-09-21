"""H (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f79667f-2c08-4b1a-9ba6-926c5e637a31'
SOURCE_PATH = 'icons-json/typeface/h_4f79667f-2c08-4b1a-9ba6-926c5e637a31.json'
AUTHOR = 'json_to_solo'

class HTypeface(Solo48):
    icon_id = 'h-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('h', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (40, 23), (8, 23))
        self.add_line('e2', (40, 43), (40, 22))
        self.add_line('e3', (40, 4), (40, 25))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c2')
