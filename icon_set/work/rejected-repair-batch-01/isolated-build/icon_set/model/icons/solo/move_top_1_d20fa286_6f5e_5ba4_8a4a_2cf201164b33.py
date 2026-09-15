"""Move top 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd20fa286-6f5e-5ba4-8a4a-2cf201164b33'
SOURCE_PATH = 'pictographic-primitives/arrows/move top 1_d20fa286-6f5e-5ba4-8a4a-2cf201164b33.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MoveTop1(Solo48):
    icon_id = 'move-top-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('move', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (8, 4), (40, 4))
        self.add_line('e1', (34, 26), (24, 15))
        self.add_line('e2', (24, 15), (24, 44))
        self.add_line('e3', (24, 15), (14, 26))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
