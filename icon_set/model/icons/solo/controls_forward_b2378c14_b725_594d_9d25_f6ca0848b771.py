"""Controls forward (video), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2378c14-b725-594d-9d25-f6ca0848b771'
SOURCE_PATH = 'pictographic-primitives/video/controls forward_b2378c14-b725-594d-9d25-f6ca0848b771.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ControlsForward(Solo48):
    icon_id = 'controls-forward'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    categories = ('video', 'primitives')
    aliases = ()
    keywords = ('controls', 'forward', 'video')

    def build(self):
        self.add_line('e0', (22, 21), (4, 8))
        self.add_line('e1', (4, 8), (4, 40))
        self.add_line('e2', (4, 40), (22, 27))
        self.add_line('e3', (22, 27), (22, 40))
        self.add_line('e4', (22, 40), (44, 24))
        self.add_line('e5', (44, 24), (22, 8))
        self.add_line('e6', (22, 8), (22, 21))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
