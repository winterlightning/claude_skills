"""Pin wave (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79f28f0f-6da1-42b3-a142-474d81fe6b26'
SOURCE_PATH = 'pictographic-primitives/state/pin wave_79f28f0f-6da1-42b3-a142-474d81fe6b26.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PinWave(Solo48):
    icon_id = 'pin-wave'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('pin', 'wave', 'state')

    def build(self):
        self.add_arc('sym-e0', (18, 19), (30, 19), radius_x=6, radius_y=5)
        self.add_arc('sym-e1', (30, 19), (18, 19), radius_x=6, radius_y=5)
        self.add_arc('sym-e2', (22, 42), (15, 34), radius_x=77)
        self.add_line('sym-e3', (15, 34), (11, 28))
        self.add_arc('sym-e4', (11, 28), (8, 19), radius_x=18)
        self.add_line('sym-e6', (8, 19), (8, 18))
        self.add_arc('sym-e7', (8, 18), (23, 4), radius_x=16)
        self.add_arc('sym-e8', (23, 4), (24, 4), radius_x=69, sweep=False)
        self.add_arc('sym-e11', (24, 4), (25, 4), radius_x=76, sweep=False)
        self.add_arc('sym-e12', (25, 4), (40, 18), radius_x=16)
        self.add_line('sym-e13', (40, 18), (40, 19))
        self.add_arc('sym-e15', (40, 19), (37, 28), radius_x=17)
        self.add_arc('sym-e16', (37, 28), (33, 34), radius_x=59)
        self.add_arc('sym-e17', (33, 34), (26, 42), radius_x=76, sweep=False)
        self.add_line('sym-e18', (26, 42), (24, 44))
        self.add_line('sym-e19', (24, 44), (22, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
