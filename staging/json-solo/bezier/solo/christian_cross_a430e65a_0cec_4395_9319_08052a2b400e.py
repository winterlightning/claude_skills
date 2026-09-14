"""Christian cross (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a430e65a-0cec-4395-9319-08052a2b400e'
SOURCE_PATH = 'icons-json/symbol/christian cross_a430e65a-0cec-4395-9319-08052a2b400e.json'
AUTHOR = 'json_to_solo'

class ChristianCrossSymbol(Solo48):
    icon_id = 'christian-cross-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('christian', 'cross', 'symbol')

    def build(self):
        self.add_line('e0', (24, 4), (24, 44))
        self.add_line('e1', (8, 18), (40, 18))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
