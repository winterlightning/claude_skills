"""Arrow thick right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9652b24b-db39-57be-aeab-25fe6153652b'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick right_9652b24b-db39-57be-aeab-25fe6153652b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThickRight(Solo48):
    icon_id = 'arrow-thick-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (25, 42), (42, 24))
        self.add_line('e1', (25, 6), (42, 24))
        self.add_line('e2', (42, 24), (6, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
