"""W (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd06af125-6456-44c8-9d9a-4d940735ce86'
SOURCE_PATH = 'icons-json/typeface/w_d06af125-6456-44c8-9d9a-4d940735ce86.json'
AUTHOR = 'json_to_solo'

class WTypeface(Solo48):
    icon_id = 'w-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('w', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (16, 44))
        self.add_line('e1', (16, 44), (25, 16))
        self.add_line('e2', (25, 16), (34, 44))
        self.add_line('e3', (34, 44), (40, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
