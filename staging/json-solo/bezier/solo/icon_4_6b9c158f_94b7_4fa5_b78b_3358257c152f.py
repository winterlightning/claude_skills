"""4 (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b9c158f-94b7-4fa5-b78b-3358257c152f'
SOURCE_PATH = 'icons-json/typeface/4_6b9c158f-94b7-4fa5-b78b-3358257c152f.json'
AUTHOR = 'json_to_solo'

class Icon4Typeface(Solo48):
    icon_id = 'icon-4-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('typeface',)

    def build(self):
        self.add_line('e0', (40, 35), (8, 35))
        self.add_line('e1', (8, 35), (35, 4))
        self.add_line('e2', (35, 4), (35, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
