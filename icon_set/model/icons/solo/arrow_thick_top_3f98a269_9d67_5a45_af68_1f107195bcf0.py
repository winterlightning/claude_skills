"""Arrow thick top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f98a269-9d67-5a45-af68-1f107195bcf0'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick top_3f98a269-9d67-5a45-af68-1f107195bcf0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThickTop(Solo48):
    icon_id = 'arrow-thick-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'thick', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (42, 23), (24, 6))
        self.add_line('e1', (6, 23), (24, 6))
        self.add_line('e2', (24, 6), (24, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
