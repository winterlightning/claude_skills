"""7 (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd29775d2-bb3b-472e-8992-afaefe7dfa23'
SOURCE_PATH = 'icons-json/typeface/7_d29775d2-bb3b-472e-8992-afaefe7dfa23.json'
AUTHOR = 'json_to_solo'

class Icon7D29775d2(Solo48):
    icon_id = 'icon-7-d29775d2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('typeface',)

    def build(self):
        self.add_line('e0', (8, 4), (40, 4))
        self.add_line('e1', (40, 4), (18, 44))
        self.add_contour('c0', 'e0', 'e1')
