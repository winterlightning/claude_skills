"""Pine (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '767fcc08-086c-4b8b-b66f-a127539e22fe'
SOURCE_PATH = 'icons-json/symbol/pine_767fcc08-086c-4b8b-b66f-a127539e22fe.json'
AUTHOR = 'json_to_solo'

class Pine(Solo48):
    icon_id = 'pine'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pine', 'symbol')

    def build(self):
        self.add_line('e0', (24, 25), (24, 44))
        self.add_line('e1', (24, 4), (8, 32))
        self.add_line('e2', (8, 32), (40, 32))
        self.add_line('e3', (40, 32), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', closed=True)
