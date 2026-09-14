"""Arrow button bottom 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cccc0ae2-455e-5543-acd2-86328a04cbec'
SOURCE_PATH = 'icons-json/arrows/arrow button bottom 1_cccc0ae2-455e-5543-acd2-86328a04cbec.json'
AUTHOR = 'json_to_solo'

class ArrowButtonBottom1Arrows(Solo48):
    icon_id = 'arrow-button-bottom-1-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (44, 8), (25, 40))
        self.add_line('e1', (23, 38), (4, 8))
        self.add_bezier('e2', (25, 40), ((24.836, 40), (24.573, 40), (24.409, 40)), ((23.627, 40), (23.5, 38.8), (23, 38)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
