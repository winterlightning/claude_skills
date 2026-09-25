"""Move up 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '533fbc15-d25d-4b50-ad30-53c4e2ac48f5'
SOURCE_PATH = 'pictographic-primitives/interface-essential/move up 1_533fbc15-d25d-4b50-ad30-53c4e2ac48f5.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MoveUp1(Solo48):
    icon_id = 'move-up-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('move', 'up', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 6), (42, 6))
        self.add_line('e1', (17, 21), (24, 14))
        self.add_line('e2', (24, 42), (24, 14))
        self.add_line('e3', (31, 21), (24, 14))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
