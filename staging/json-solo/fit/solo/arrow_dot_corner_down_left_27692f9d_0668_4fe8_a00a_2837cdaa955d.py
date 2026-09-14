"""Arrow dot corner down left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27692f9d-0668-4fe8-a00a-2837cdaa955d'
SOURCE_PATH = 'icons-json/arrows/arrow dot corner down left_27692f9d-0668-4fe8-a00a-2837cdaa955d.json'
AUTHOR = 'json_to_solo'

class ArrowDotCornerDownLeftArrows(Solo48):
    icon_id = 'arrow-dot-corner-down-left-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'corner', 'down', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (17, 31), (8, 40))
        self.add_line('e1', (8, 40), (21, 42))
        self.add_line('e2', (8, 40), (6, 27))
        self.add_line('e3', (25, 23), (30, 18))
        self.add_line('e4', (37, 11), (42, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
