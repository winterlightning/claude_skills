"""Christian cross (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a430e65a-0cec-4395-9319-08052a2b400e'
SOURCE_PATH = 'pictographic-primitives/symbol/christian cross_a430e65a-0cec-4395-9319-08052a2b400e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ChristianCross(Solo48):
    icon_id = 'christian-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('christian', 'cross', 'symbol')

    def build(self):
        self.add_line('e0', (24, 4), (24, 44))
        self.add_line('e1', (8, 18), (40, 18))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
