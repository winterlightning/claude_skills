"""Star burst (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcbfa235-b6ab-4926-bc2a-34d5ce7146d8'
SOURCE_PATH = 'pictographic-primitives/symbol/star burst_dcbfa235-b6ab-4926-bc2a-34d5ce7146d8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class StarBurst(Solo48):
    icon_id = 'star-burst'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('star', 'burst', 'symbol')

    def build(self):
        self.add_line('e0', (15, 40), (14, 32))
        self.add_line('e1', (14, 32), (4, 31))
        self.add_line('e2', (4, 31), (9, 24))
        self.add_line('e3', (9, 24), (5, 16))
        self.add_line('e4', (5, 16), (15, 16))
        self.add_line('e5', (15, 16), (19, 8))
        self.add_line('e6', (19, 8), (28, 15))
        self.add_line('e7', (28, 15), (38, 12))
        self.add_line('e8', (38, 12), (38, 21))
        self.add_line('e9', (38, 21), (44, 27))
        self.add_line('e10', (44, 27), (34, 29))
        self.add_line('e11', (34, 29), (31, 38))
        self.add_line('e12', (31, 38), (24, 33))
        self.add_line('e13', (24, 33), (15, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', closed=True)
