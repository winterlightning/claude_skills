"""I (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3827733-b428-5d44-990e-f276333b7145'
SOURCE_PATH = 'icons-json/typeface/I_f3827733-b428-5d44-990e-f276333b7145.json'
AUTHOR = 'json_to_solo'

class ITypeface(Solo48):
    icon_id = 'i-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('i', 'typeface')

    def build(self):
        self.add_line('e0', (40, 4), (8, 4))
        self.add_line('e1', (24, 4), (24, 44))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
