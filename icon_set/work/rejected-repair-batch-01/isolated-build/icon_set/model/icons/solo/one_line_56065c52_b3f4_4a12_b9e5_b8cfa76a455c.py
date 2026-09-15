"""One line (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56065c52-b3f4-4a12-b9e5-b8cfa76a455c'
SOURCE_PATH = 'pictographic-primitives/symbol/one line_56065c52-b3f4-4a12-b9e5-b8cfa76a455c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class OneLine(Solo48):
    icon_id = 'one-line'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('one', 'line', 'symbol')

    def build(self):
        self.add_line('e0', (40, 4), (8, 44))
        self.add_contour('c0', 'e0')
