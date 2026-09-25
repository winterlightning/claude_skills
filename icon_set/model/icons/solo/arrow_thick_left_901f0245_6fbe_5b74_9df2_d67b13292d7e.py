"""Arrow thick left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '901f0245-6fbe-5b74-9df2-d67b13292d7e'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick left_901f0245-6fbe-5b74-9df2-d67b13292d7e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThickLeftArrows(Solo48):
    icon_id = 'arrow-thick-left-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (23, 6), (6, 24))
        self.add_line('e1', (23, 42), (6, 24))
        self.add_line('e2', (6, 24), (42, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
