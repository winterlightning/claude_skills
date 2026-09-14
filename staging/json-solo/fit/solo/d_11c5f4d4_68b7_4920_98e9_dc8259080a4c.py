"""D (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11c5f4d4-68b7-4920-98e9-dc8259080a4c'
SOURCE_PATH = 'icons-json/typeface/d_11c5f4d4-68b7-4920-98e9-dc8259080a4c.json'
AUTHOR = 'json_to_solo'

class D11c5f4d4(Solo48):
    icon_id = 'd-11c5f4d4'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('d', 'typeface')

    def build(self):
        self.add_line('e0', (40, 4), (40, 38))
        self.add_arc('e1-1', (40, 38), (33, 43), radius_x=9)
        self.add_line('e1-2', (33, 43), (25, 44))
        self.add_line('e1-3', (25, 44), (18, 43))
        self.add_arc('e1-4', (18, 43), (14, 41), radius_x=17)
        self.add_arc('e1-5', (14, 41), (8, 31), radius_x=12)
        self.add_arc('e1-6', (8, 31), (14, 21), radius_x=12)
        self.add_arc('e1-7', (14, 21), (40, 22), radius_x=24)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7')
