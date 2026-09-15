"""Controls pause (video), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99180e7b-910b-4846-bb7f-7207185069f4'
SOURCE_PATH = 'pictographic-primitives/video/controls pause_99180e7b-910b-4846-bb7f-7207185069f4.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ControlsPauseVideo(Solo48):
    icon_id = 'controls-pause-video'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'pause', 'video')

    def build(self):
        self.add_line('e0', (40, 4), (40, 44))
        self.add_line('e1', (8, 4), (8, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
