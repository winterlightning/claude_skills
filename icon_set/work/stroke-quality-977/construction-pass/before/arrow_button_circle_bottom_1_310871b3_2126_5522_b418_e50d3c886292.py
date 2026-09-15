"""Arrow button circle bottom 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '310871b3-2126-5522-b418-e50d3c886292'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow button circle bottom 1_310871b3-2126-5522-b418-e50d3c886292.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowButtonCircleBottom1(Solo48):
    icon_id = 'arrow-button-circle-bottom-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'circle', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (14, 21), (24, 31))
        self.add_line('e1', (24, 31), (34, 21))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
