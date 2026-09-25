"""Arrow circle left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bcf7280-b308-577f-b75c-e9ad5dca14c1'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow circle left_6bcf7280-b308-577f-b75c-e9ad5dca14c1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowCircleLeft(Solo48):
    icon_id = 'arrow-circle-left'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'circle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (28, 13), (19, 22))
        self.add_line('e1', (19, 25), (28, 34))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e3', (19, 22), (19, 25), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
