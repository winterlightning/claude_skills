"""Slide right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a5693af-1a21-4bea-a1f5-a019efe4584e'
SOURCE_PATH = 'icons-json/arrows/slide right_0a5693af-1a21-4bea-a1f5-a019efe4584e.json'
AUTHOR = 'json_to_solo'

class SlideRightArrows(Solo48):
    icon_id = 'slide-right-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('slide', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (8, 44), (8, 30))
        self.add_line('e1', (8, 30), (28, 18))
        self.add_line('e2', (28, 18), (28, 4))
        self.add_line('e3', (28, 4), (15, 9))
        self.add_line('e4', (28, 4), (40, 9))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4')
