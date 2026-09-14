"""V (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1979bd9f-a98f-4038-9879-e769cf811721'
SOURCE_PATH = 'icons-json/typeface/v_1979bd9f-a98f-4038-9879-e769cf811721.json'
AUTHOR = 'json_to_solo'

class V1979bd9f(Solo48):
    icon_id = 'v-1979bd9f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('v', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (24, 44))
        self.add_line('e1', (24, 44), (40, 4))
        self.add_contour('c0', 'e0', 'e1')
