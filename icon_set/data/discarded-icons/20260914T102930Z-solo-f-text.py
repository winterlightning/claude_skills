"""F (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '370104c4-5cc3-47d6-becb-202e28c32463'
SOURCE_PATH = 'icons-json/symbol/F (text)_370104c4-5cc3-47d6-becb-202e28c32463.json'
AUTHOR = 'json_to_solo'

class FText(Solo48):
    icon_id = 'f-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('f', 'text', 'symbol')

    def build(self):
        self.add_line('e0', (40, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 44))
        self.add_line('e2', (29, 24), (8, 24))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.relate('connect', 'c1', 'c0')
