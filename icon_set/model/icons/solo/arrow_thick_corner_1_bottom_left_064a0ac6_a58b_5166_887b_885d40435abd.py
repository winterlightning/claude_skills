"""Arrow thick corner 1 bottom left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '064a0ac6-a58b-5166-887b-885d40435abd'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner 1 bottom left_064a0ac6-a58b-5166-887b-885d40435abd.json'
AUTHOR = 'json_to_solo'

class ArrowThickCorner1BottomLeft(Solo48):
    icon_id = 'arrow-thick-corner-1-bottom-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'bottom', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (6, 10), (6, 42))
        self.add_line('e1', (6, 42), (40, 42))
        self.add_line('e2', (18, 30), (42, 6))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
