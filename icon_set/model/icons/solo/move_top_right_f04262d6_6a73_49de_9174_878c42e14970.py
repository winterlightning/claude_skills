"""Move top right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f04262d6-6a73-49de-9174-878c42e14970'
SOURCE_PATH = 'pictographic-primitives/interface-essential/move top right_f04262d6-6a73-49de-9174-878c42e14970.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MoveTopRight(Solo48):
    icon_id = 'move-top-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('move', 'top', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (9, 8), (44, 8))
        self.add_line('e1', (44, 8), (44, 39))
        self.add_line('e2', (12, 21), (25, 21))
        self.add_line('e3', (4, 40), (25, 21))
        self.add_line('e4', (25, 33), (25, 21))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
