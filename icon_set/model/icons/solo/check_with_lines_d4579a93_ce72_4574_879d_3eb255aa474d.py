"""Check with lines (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4579a93-ce72-4574-879d-3eb255aa474d'
SOURCE_PATH = 'pictographic-primitives/symbol/check with lines_d4579a93-ce72-4574-879d-3eb255aa474d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CheckWithLines(Solo48):
    icon_id = 'check-with-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('check', 'with', 'lines', 'symbol')

    def build(self):
        self.add_line('e0', (37, 8), (16, 27))
        self.add_line('e1', (16, 27), (7, 18))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
