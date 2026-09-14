"""J (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3d5de99-3cea-4c1f-bc43-0cb34bbf8f89'
SOURCE_PATH = 'icons-json/typeface/J_e3d5de99-3cea-4c1f-bc43-0cb34bbf8f89.json'
AUTHOR = 'json_to_solo'

class JTypeface(Solo48):
    icon_id = 'j-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('j', 'typeface')

    def build(self):
        self.add_line('e0', (16, 4), (40, 4))
        self.add_line('e1', (40, 4), (40, 38))
        self.add_arc('e2-1', (40, 38), (36, 42), radius_x=5)
        self.add_line('e2-2', (36, 42), (24, 44))
        self.add_line('e2-3', (24, 44), (12, 42))
        self.add_arc('e2-4', (12, 42), (8, 38), radius_x=5)
        self.add_contour('c0', 'e0', 'e1', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
