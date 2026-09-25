"""Arrow zigzag bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2bfa046-1d2d-5b66-af55-572915e98be2'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow zigzag bottom_f2bfa046-1d2d-5b66-af55-572915e98be2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowZigzagBottom(Solo48):
    icon_id = 'arrow-zigzag-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'zigzag', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (40, 17), (29, 4))
        self.add_line('e1', (29, 4), (29, 17))
        self.add_line('e2', (29, 17), (40, 17))
        self.add_line('e3', (29, 4), (19, 4))
        self.add_line('e4', (19, 4), (19, 44))
        self.add_line('e5', (8, 32), (19, 44))
        self.add_line('e6', (19, 44), (29, 32))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
