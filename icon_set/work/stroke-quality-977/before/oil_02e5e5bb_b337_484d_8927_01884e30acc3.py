"""Oil (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02e5e5bb-b337-484d-8927-01884e30acc3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/oil_02e5e5bb-b337-484d-8927-01884e30acc3.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Oil(Solo48):
    icon_id = 'oil'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('oil', '_uncategorized')

    def build(self):
        self.add_arc('sym-e0', (24, 44), (25, 44), radius_x=40)
        self.add_arc('sym-e1', (25, 44), (40, 30), radius_x=16, sweep=False)
        self.add_arc('sym-e3', (40, 30), (40, 29), radius_x=30)
        self.add_arc('sym-e4', (40, 29), (37, 20), radius_x=16, sweep=False)
        self.add_line('sym-e5', (37, 20), (28, 9))
        self.add_line('sym-e6', (28, 9), (25, 5))
        self.add_arc('sym-e7', (25, 5), (24, 4), radius_x=7)
        self.add_arc('sym-e8', (24, 4), (23, 5), radius_x=7)
        self.add_line('sym-e9', (23, 5), (20, 9))
        self.add_line('sym-e10', (20, 9), (11, 20))
        self.add_arc('sym-e11', (11, 20), (8, 29), radius_x=16, sweep=False)
        self.add_line('sym-e12', (8, 29), (8, 30))
        self.add_arc('sym-e14', (8, 30), (23, 44), radius_x=16, sweep=False)
        self.add_arc('sym-e15', (23, 44), (24, 44), radius_x=41)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', closed=True)
