"""Controls play (video), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64184475-f1f7-5af9-b282-174355ee8f83'
SOURCE_PATH = 'pictographic-primitives/video/controls play_64184475-f1f7-5af9-b282-174355ee8f83.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ControlsPlay(Solo48):
    icon_id = 'controls-play'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    categories = ('video', 'primitives')
    aliases = ()
    keywords = ('controls', 'play', 'video')

    def build(self):
        self.add_line('e0', (40, 24), (8, 4))
        self.add_line('e1', (8, 4), (8, 44))
        self.add_line('e2', (8, 44), (40, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
