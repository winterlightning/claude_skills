"""Snowflake 1 (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '360fc91b-24b0-485d-863b-30511134cdd1'
SOURCE_PATH = 'pictographic-primitives/state/snowflake 1_360fc91b-24b0-485d-863b-30511134cdd1.svg'
AUTHOR = 'gpt-6'

class Snowflake1(Solo48):
    icon_id = 'snowflake-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('snowflake', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 42))
        self.add_line('sym-e3', (15, 24), (33, 24))
        self.add_line('sym-e4', (33, 24), (38, 31))
        self.add_line('sym-e5', (31, 37), (24, 32))
        self.add_line('sym-e6', (24, 32), (17, 37))
        self.add_line('sym-e7', (42, 24), (33, 24))
        self.add_line('sym-e8', (33, 24), (38, 17))
        self.add_line('sym-e9', (31, 12), (24, 17))
        self.add_line('sym-e10', (24, 17), (17, 12))
        self.add_line('sym-e11', (10, 31), (15, 24))
        self.add_line('sym-e12', (15, 24), (6, 24))
        self.add_line('sym-e13', (10, 17), (15, 24))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', closed=False)
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', closed=False)
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', closed=False)
        self.add_contour('sym-c4', 'sym-e9', 'sym-e10', closed=False)
        self.add_contour('sym-c5', 'sym-e11', 'sym-e12', closed=False)
        self.add_contour('sym-c6', 'sym-e13', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
