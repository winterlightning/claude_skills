"""Square root (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1779227e-43ac-5789-87f5-dd737bf06f33'
SOURCE_PATH = 'icons-json/interface-essential/square root_1779227e-43ac-5789-87f5-dd737bf06f33.json'
AUTHOR = 'json_to_solo'

class SquareRoot1779227e(Solo48):
    icon_id = 'square-root-1779227e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('square', 'root', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 8), (20, 8))
        self.add_line('e1', (20, 8), (10, 40))
        self.add_line('e2', (10, 40), (4, 26))
        self.add_contour('c0', 'e0', 'e1', 'e2')
