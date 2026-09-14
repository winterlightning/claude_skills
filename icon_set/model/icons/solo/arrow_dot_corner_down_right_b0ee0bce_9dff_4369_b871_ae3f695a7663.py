"""Arrow dot corner down right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0ee0bce-9dff-4369-b871-ae3f695a7663'
SOURCE_PATH = 'icons-json/arrows/arrow dot corner down right_b0ee0bce-9dff-4369-b871-ae3f695a7663.json'
AUTHOR = 'json_to_solo'

class ArrowDotCornerDownRight(Solo48):
    icon_id = 'arrow-dot-corner-down-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'corner', 'down', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (31, 31), (40, 40))
        self.add_line('e1', (40, 40), (27, 42))
        self.add_line('e2', (40, 40), (42, 27))
        self.add_line('e3', (23, 23), (18, 18))
        self.add_line('e4', (11, 11), (6, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
