"""Arrow thick left bottom corner (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7edc5400-5396-52a8-a848-07f2f6484c49'
SOURCE_PATH = 'icons-json/arrows/arrow thick left bottom corner_7edc5400-5396-52a8-a848-07f2f6484c49.json'
AUTHOR = 'json_to_solo'

class ArrowThickLeftBottomCorner(Solo48):
    icon_id = 'arrow-thick-left-bottom-corner'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'bottom', 'corner', 'arrows')

    def build(self):
        self.add_line('e0', (33, 42), (24, 34))
        self.add_line('e1', (24, 34), (42, 16))
        self.add_line('e2', (42, 16), (32, 6))
        self.add_line('e3', (32, 6), (14, 24))
        self.add_line('e4', (14, 24), (6, 16))
        self.add_line('e5', (6, 16), (6, 42))
        self.add_line('e6', (6, 42), (33, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
