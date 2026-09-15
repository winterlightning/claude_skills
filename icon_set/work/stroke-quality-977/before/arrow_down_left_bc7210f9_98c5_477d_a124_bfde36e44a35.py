"""Arrow down left (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc7210f9-98c5-477d-a124-bfde36e44a35'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow down left_bc7210f9-98c5-477d-a124-bfde36e44a35.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowDownLeft(Solo48):
    icon_id = 'arrow-down-left-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'down', 'left', 'symbol')

    def build(self):
        self.add_line('e0', (42, 6), (6, 42))
        self.add_line('e1', (6, 25), (6, 42))
        self.add_line('e2', (23, 42), (6, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
