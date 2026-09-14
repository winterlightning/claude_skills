"""Y (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc0d410c-f52a-5925-a5e0-1ed264034307'
SOURCE_PATH = 'icons-json/typeface/Y_bc0d410c-f52a-5925-a5e0-1ed264034307.json'
AUTHOR = 'json_to_solo'

class YBc0d410c(Solo48):
    icon_id = 'y-bc0d410c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('y', 'typeface')

    def build(self):
        self.add_line('e0', (40, 4), (24, 26))
        self.add_line('e1', (8, 4), (24, 26))
        self.add_line('e2', (24, 26), (24, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
