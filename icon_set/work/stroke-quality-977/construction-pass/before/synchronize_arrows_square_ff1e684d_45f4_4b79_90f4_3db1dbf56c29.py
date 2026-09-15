"""Synchronize arrows square (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff1e684d-45f4-4b79-90f4-3db1dbf56c29'
SOURCE_PATH = 'pictographic-primitives/interface-essential/synchronize arrows square_ff1e684d-45f4-4b79-90f4-3db1dbf56c29.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SynchronizeArrowsSquare(Solo48):
    icon_id = 'synchronize-arrows-square'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'arrows', 'square', 'interface-essential')

    def build(self):
        self.add_line('e0', (15, 8), (36, 8))
        self.add_line('e1', (40, 13), (40, 28))
        self.add_line('e2', (36, 23), (40, 28))
        self.add_line('e3', (44, 23), (40, 28))
        self.add_line('e4', (4, 23), (9, 18))
        self.add_line('e5', (33, 40), (12, 40))
        self.add_line('e6', (9, 35), (9, 18))
        self.add_line('e7', (12, 23), (9, 18))
        self.add_arc('e8', (36, 8), (40, 13), radius_x=6)
        self.add_arc('e9', (12, 40), (9, 35), radius_x=5)
        self.add_contour('c0', 'e0', 'e8', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e9', 'e6')
        self.add_contour('c5', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
