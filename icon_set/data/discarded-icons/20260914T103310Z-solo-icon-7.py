"""7 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2e450c0-559a-4dff-bbb6-ddef944b0e55'
SOURCE_PATH = 'icons-json/symbol/7_f2e450c0-559a-4dff-bbb6-ddef944b0e55.json'
AUTHOR = 'json_to_solo'

class Icon7(Solo48):
    icon_id = 'icon-7'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('symbol',)

    def build(self):
        self.add_line('e0', (8, 4), (40, 4))
        self.add_line('e1', (40, 4), (18, 44))
        self.add_contour('c0', 'e0', 'e1')
