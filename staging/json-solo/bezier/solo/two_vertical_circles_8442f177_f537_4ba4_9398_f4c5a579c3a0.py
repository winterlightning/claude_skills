"""Two vertical circles (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8442f177-f537-4ba4-9398-f4c5a579c3a0'
SOURCE_PATH = 'icons-json/symbol/two vertical circles_8442f177-f537-4ba4-9398-f4c5a579c3a0.json'
AUTHOR = 'json_to_solo'

class TwoVerticalCirclesSymbol(Solo48):
    icon_id = 'two-vertical-circles-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('two', 'vertical', 'circles', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (40, 44), (40, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
