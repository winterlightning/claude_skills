"""Three lines (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f91c6f84-9971-4a9d-a251-a2d0cd8844cb'
SOURCE_PATH = 'pictographic-primitives/symbol/three lines_f91c6f84-9971-4a9d-a251-a2d0cd8844cb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ThreeLines(Solo48):
    icon_id = 'three-lines'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('three', 'lines', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (40, 4))
        self.add_line('e1', (8, 24), (40, 24))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
