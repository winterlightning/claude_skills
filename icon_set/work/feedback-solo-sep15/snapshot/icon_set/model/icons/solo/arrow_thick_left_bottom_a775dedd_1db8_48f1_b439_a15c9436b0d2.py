"""Arrow thick left bottom (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a775dedd-1db8-48f1-b439-a15c9436b0d2'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow thick left bottom_a775dedd-1db8-48f1-b439-a15c9436b0d2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThickLeftBottom(Solo48):
    icon_id = 'arrow-thick-left-bottom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'bottom', 'symbol')

    def build(self):
        self.add_line('e0', (33, 42), (24, 34))
        self.add_line('e1', (24, 34), (42, 16))
        self.add_line('e2', (42, 16), (32, 6))
        self.add_line('e3', (32, 6), (14, 24))
        self.add_line('e4', (14, 24), (6, 16))
        self.add_line('e5', (6, 16), (6, 42))
        self.add_line('e6', (6, 42), (33, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
