"""Three arrows down (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fe44175-fb41-4dbd-a349-bde8c4354a91'
SOURCE_PATH = 'pictographic-primitives/state/three arrows down_4fe44175-fb41-4dbd-a349-bde8c4354a91.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ThreeArrowsDown(Solo48):
    icon_id = 'three-arrows-down'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('three', 'arrows', 'down', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 23), (24, 42))
        self.add_line('sym-e1', (24, 42), (18, 36))
        self.add_line('sym-e2', (6, 19), (12, 25))
        self.add_line('sym-e3', (12, 25), (17, 19))
        self.add_line('sym-e4', (12, 6), (12, 25))
        self.add_line('sym-e5', (30, 36), (24, 42))
        self.add_line('sym-e6', (42, 19), (36, 25))
        self.add_line('sym-e7', (36, 25), (31, 19))
        self.add_line('sym-e8', (36, 6), (36, 25))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c5', 'sym-e8')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c2')
