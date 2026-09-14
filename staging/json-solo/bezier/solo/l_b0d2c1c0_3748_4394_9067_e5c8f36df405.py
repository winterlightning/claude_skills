"""L (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0d2c1c0-3748-4394-9067-e5c8f36df405'
SOURCE_PATH = 'icons-json/typeface/l_b0d2c1c0-3748-4394-9067-e5c8f36df405.json'
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
        self.add_line('e0', (24, 4), (24, 44))
        self.add_line('e1', (8, 4), (40, 4))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
