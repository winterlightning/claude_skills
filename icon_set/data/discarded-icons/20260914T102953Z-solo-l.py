"""L (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd85c0769-6f12-4f89-bb99-94c61578358a'
SOURCE_PATH = 'icons-json/typeface/L_d85c0769-6f12-4f89-bb99-94c61578358a.json'
AUTHOR = 'json_to_solo'

class L(Solo48):
    icon_id = 'l'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('l', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (8, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
