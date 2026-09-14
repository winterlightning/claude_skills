"""Arrow thick left bottom corner (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cb5f6af-848b-5bee-8eb3-4a8f6c0cb53b'
SOURCE_PATH = 'icons-json/arrows/arrow thick left bottom corner_7cb5f6af-848b-5bee-8eb3-4a8f6c0cb53b.json'
AUTHOR = 'json_to_solo'

class ArrowThickLeftBottomCorner7cb5f6af(Solo48):
    icon_id = 'arrow-thick-left-bottom-corner-7cb5f6af'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'bottom', 'corner', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (6, 42))
        self.add_line('e1', (6, 42), (41, 6))
        self.add_line('e2', (42, 42), (6, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
