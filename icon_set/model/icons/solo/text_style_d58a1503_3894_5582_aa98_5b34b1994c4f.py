"""Text style (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd58a1503-3894-5582-aa98-5b34b1994c4f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/text style_d58a1503-3894-5582-aa98-5b34b1994c4f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class TextStyle(Solo48):
    icon_id = 'text-style'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('text', 'style', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 6), (42, 6))
        self.add_line('e1', (24, 6), (24, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.relate('connect', 'c1', 'c0')
