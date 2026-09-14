"""Circle (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07d4663b-adbb-4a88-b7fd-e15635d71d01'
SOURCE_PATH = 'icons-json/symbol/circle_07d4663b-adbb-4a88-b7fd-e15635d71d01.json'
AUTHOR = 'json_to_solo'

class Circle07d4663b(Solo48):
    icon_id = 'circle-07d4663b'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('circle', 'symbol')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
