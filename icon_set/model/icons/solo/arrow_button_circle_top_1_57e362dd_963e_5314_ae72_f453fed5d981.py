"""Arrow button circle top 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57e362dd-963e-5314-ae72-f453fed5d981'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow button circle top 1_57e362dd-963e-5314-ae72-f453fed5d981.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowButtonCircleTop1(Solo48):
    icon_id = 'arrow-button-circle-top-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'button', 'circle', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (34, 27), (24, 17))
        self.add_line('e1', (24, 17), (14, 27))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
