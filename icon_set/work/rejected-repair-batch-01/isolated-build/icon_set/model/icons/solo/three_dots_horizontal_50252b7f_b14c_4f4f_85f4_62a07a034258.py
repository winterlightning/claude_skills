"""Three dots horizontal (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50252b7f-b14c-4f4f-85f4-62a07a034258'
SOURCE_PATH = 'pictographic-primitives/state/three dots horizontal_50252b7f-b14c-4f4f-85f4-62a07a034258.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ThreeDotsHorizontal(Solo48):
    icon_id = 'three-dots-horizontal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('three', 'dots', 'horizontal', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 24), (24, 24))
        self.add_line('sym-e1', (24, 40), (40, 40))
        self.add_arc('sym-e2', (40, 40), (41, 40), radius_x=41)
        self.add_arc('sym-e3-1', (41, 40), (43, 39), radius_x=3, sweep=False)
        self.add_line('sym-e3-2', (43, 39), (44, 36))
        self.add_line('sym-e4', (44, 36), (44, 12))
        self.add_arc('sym-e5', (44, 12), (42, 8), radius_x=5, sweep=False)
        self.add_line('sym-e6', (42, 8), (24, 8))
        self.add_line('sym-e7', (24, 8), (6, 8))
        self.add_arc('sym-e8', (6, 8), (4, 12), radius_x=5, sweep=False)
        self.add_line('sym-e9', (4, 12), (4, 36))
        self.add_line('sym-e10-1', (4, 36), (5, 39))
        self.add_arc('sym-e10-2', (5, 39), (7, 40), radius_x=4, sweep=False)
        self.add_arc('sym-e11', (7, 40), (8, 40), radius_x=20)
        self.add_line('sym-e12', (8, 40), (24, 40))
        self.add_line('sym-e13', (35, 24), (35, 24))
        self.add_line('sym-e14', (13, 24), (13, 24))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e11', 'sym-e12', closed=True)
        self.add_contour('sym-c2', 'sym-e13')
        self.add_contour('sym-c3', 'sym-e14')
