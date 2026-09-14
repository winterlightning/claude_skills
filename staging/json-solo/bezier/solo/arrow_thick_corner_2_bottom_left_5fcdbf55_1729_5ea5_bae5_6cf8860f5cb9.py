"""Arrow thick corner 2 bottom left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5fcdbf55-1729-5ea5-bae5-6cf8860f5cb9'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner 2 bottom left_5fcdbf55-1729-5ea5-bae5-6cf8860f5cb9.json'
AUTHOR = 'json_to_solo'

class ArrowThickCorner2BottomLeftArrows(Solo48):
    icon_id = 'arrow-thick-corner-2-bottom-left-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'bottom', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (42, 6), (6, 42))
        self.add_line('e1', (6, 42), (6, 6))
        self.add_line('e2', (6, 42), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
