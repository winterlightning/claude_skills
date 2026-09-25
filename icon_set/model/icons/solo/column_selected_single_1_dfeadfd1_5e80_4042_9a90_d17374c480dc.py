"""Column selected single 1 (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfeadfd1-5e80-4042-9a90-d17374c480dc'
SOURCE_PATH = 'pictographic-primitives/state/column selected single 1_dfeadfd1-5e80-4042-9a90-d17374c480dc.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ColumnSelectedSingle1State(Solo48):
    icon_id = 'column-selected-single-1-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('column', 'selected', 'single', 'state')

    def build(self):
        self.add_line('e0', (30, 8), (30, 40))
        self.add_line('e1', (18, 8), (18, 40))
        self.add_line('e2', (44, 8), (44, 40))
        self.add_line('e3', (44, 40), (4, 40))
        self.add_line('e4', (4, 40), (4, 8))
        self.add_line('e5', (4, 8), (44, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
