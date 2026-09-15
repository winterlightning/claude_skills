"""Arrow thick left bottom corner (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6782d65-b970-59da-aa80-2b67aeac5839'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick left bottom corner_c6782d65-b970-59da-aa80-2b67aeac5839.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThickLeftBottomCornerC6782d65(Solo48):
    icon_id = 'arrow-thick-left-bottom-corner-c6782d65'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'bottom', 'corner', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (6, 42))
        self.add_line('e1', (6, 42), (42, 42))
        self.add_line('e2', (6, 42), (42, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
