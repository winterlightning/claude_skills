"""Arrow circle top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '729ca8b4-ae7f-58a2-b87a-485655c36e55'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow circle top_729ca8b4-ae7f-58a2-b87a-485655c36e55.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowCircleTop(Solo48):
    icon_id = 'arrow-circle-top'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'circle', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (35, 28), (26, 19))
        self.add_line('e1', (23, 19), (14, 28))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e3', (26, 19), (23, 19), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
