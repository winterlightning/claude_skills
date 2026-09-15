"""State remove (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1db6929b-7342-43b7-a628-129ea6599ef1'
SOURCE_PATH = 'pictographic-primitives/state/state remove_1db6929b-7342-43b7-a628-129ea6599ef1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class StateRemove(Solo48):
    icon_id = 'state-remove'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('state', 'remove')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e2', (17, 17), (24, 24))
        self.add_line('sym-e3', (24, 24), (31, 17))
        self.add_line('sym-e4', (17, 31), (24, 24))
        self.add_line('sym-e5', (24, 24), (31, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5')
        self.relate('connect', 'sym-c1', 'sym-c2')
