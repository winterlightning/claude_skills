"""Arrow thick corner 1 top right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82abce10-c1dc-5abf-a684-b7b1f25e0355'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner 1 top right_82abce10-c1dc-5abf-a684-b7b1f25e0355.json'
AUTHOR = 'json_to_solo'

class ArrowThickCorner1TopRightArrows(Solo48):
    icon_id = 'arrow-thick-corner-1-top-right-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'top', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (42, 38), (42, 6))
        self.add_line('e1', (42, 6), (8, 6))
        self.add_line('e2', (30, 18), (6, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
