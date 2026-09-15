"""Drug (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f8c6783-8fc1-48cd-91eb-d70ff753e4b6'
SOURCE_PATH = 'pictographic-primitives/symbol/drug_1f8c6783-8fc1-48cd-91eb-d70ff753e4b6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Drug(Solo48):
    icon_id = 'drug'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('drug', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 24), (31, 31))
        self.add_line('sym-e1', (31, 31), (39, 23))
        self.add_arc('sym-e2', (39, 23), (42, 16), radius_x=10, sweep=False)
        self.add_arc('sym-e4', (42, 16), (39, 9), radius_x=10, sweep=False)
        self.add_arc('sym-e5', (39, 9), (32, 6), radius_x=10, sweep=False)
        self.add_arc('sym-e7', (32, 6), (25, 9), radius_x=10, sweep=False)
        self.add_line('sym-e8', (25, 9), (17, 17))
        self.add_line('sym-e9', (17, 17), (24, 24))
        self.add_arc('sym-e10', (9, 39), (16, 42), radius_x=10, sweep=False)
        self.add_arc('sym-e12', (16, 42), (23, 39), radius_x=10, sweep=False)
        self.add_line('sym-e13', (23, 39), (31, 31))
        self.add_arc('sym-e14', (9, 39), (6, 32), radius_x=10)
        self.add_arc('sym-e16', (6, 32), (9, 25), radius_x=10)
        self.add_line('sym-e17', (9, 25), (17, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14', 'sym-e16', 'sym-e17')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
