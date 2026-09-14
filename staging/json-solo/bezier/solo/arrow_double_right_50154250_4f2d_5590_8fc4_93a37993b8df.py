"""Arrow double right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50154250-4f2d-5590-8fc4-93a37993b8df'
SOURCE_PATH = 'icons-json/arrows/arrow double right_50154250-4f2d-5590-8fc4-93a37993b8df.json'
AUTHOR = 'json_to_solo'

class ArrowDoubleRightArrows(Solo48):
    icon_id = 'arrow-double-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'double', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (29, 39), (44, 24))
        self.add_line('e1', (44, 24), (28, 8))
        self.add_line('e2', (4, 40), (20, 24))
        self.add_line('e3', (20, 24), (4, 8))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
