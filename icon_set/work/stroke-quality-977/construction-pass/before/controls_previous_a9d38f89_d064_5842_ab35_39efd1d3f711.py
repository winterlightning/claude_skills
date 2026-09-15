"""Controls previous (video), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9d38f89-d064-5842-ab35-39efd1d3f711'
SOURCE_PATH = 'pictographic-primitives/video/controls previous_a9d38f89-d064-5842-ab35-39efd1d3f711.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ControlsPrevious(Solo48):
    icon_id = 'controls-previous'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'previous', 'video')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (40, 5), (16, 24))
        self.add_line('e2', (16, 24), (40, 43))
        self.add_line('e3', (40, 43), (40, 5))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', closed=True)
