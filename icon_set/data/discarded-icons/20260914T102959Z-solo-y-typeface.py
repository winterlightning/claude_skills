"""Y (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c35e25c-48db-43b6-9542-011882b555da'
SOURCE_PATH = 'icons-json/typeface/y_9c35e25c-48db-43b6-9542-011882b555da.json'
AUTHOR = 'json_to_solo'

class YTypeface(Solo48):
    icon_id = 'y-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('y', 'typeface')

    def build(self):
        self.add_line('e0', (8, 5), (25, 32))
        self.add_line('e1', (40, 4), (24, 35))
        self.add_arc('e2', (24, 35), (9, 44), radius_x=18)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
