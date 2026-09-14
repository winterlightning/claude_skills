"""Keyboard arrow bottom top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2325c9b5-ebfd-5bd4-8441-0093b3c7c36d'
SOURCE_PATH = 'icons-json/arrows/keyboard arrow bottom top_2325c9b5-ebfd-5bd4-8441-0093b3c7c36d.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowBottomTopArrows(Solo48):
    icon_id = 'keyboard-arrow-bottom-top-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'bottom', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (42, 42), (6, 6))
        self.add_line('e1', (6, 6), (23, 6))
        self.add_line('e2', (6, 6), (6, 23))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
