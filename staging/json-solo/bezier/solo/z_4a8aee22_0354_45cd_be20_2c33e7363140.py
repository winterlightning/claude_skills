"""Z (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a8aee22-0354-45cd-be20-2c33e7363140'
SOURCE_PATH = 'icons-json/symbol/Z_4a8aee22-0354-45cd-be20-2c33e7363140.json'
AUTHOR = 'json_to_solo'

class ZSymbol(Solo48):
    icon_id = 'z-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('z', 'symbol')

    def build(self):
        self.add_line('e0', (10, 4), (40, 4))
        self.add_line('e1', (40, 4), (8, 44))
        self.add_line('e2', (8, 44), (39, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
