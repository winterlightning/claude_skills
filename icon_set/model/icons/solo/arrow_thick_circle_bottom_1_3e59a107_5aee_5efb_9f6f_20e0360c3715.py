"""Arrow thick circle bottom 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e59a107-5aee-5efb-9f6f-20e0360c3715'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick circle bottom 1_3e59a107-5aee-5efb-9f6f-20e0360c3715.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThickCircleBottom1(Solo48):
    icon_id = 'arrow-thick-circle-bottom-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'thick', 'circle', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (15, 24), (24, 33))
        self.add_line('e1', (33, 24), (24, 33))
        self.add_line('e2', (24, 33), (24, 13))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
