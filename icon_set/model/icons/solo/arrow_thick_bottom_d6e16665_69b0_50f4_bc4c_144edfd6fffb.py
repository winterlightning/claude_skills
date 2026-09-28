"""Arrow thick bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6e16665-69b0-50f4-bc4c-144edfd6fffb'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick bottom_d6e16665-69b0-50f4-bc4c-144edfd6fffb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThickBottom(Solo48):
    icon_id = 'arrow-thick-bottom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'thick', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (6, 25), (24, 42))
        self.add_line('e1', (42, 25), (24, 42))
        self.add_line('e2', (24, 42), (24, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
