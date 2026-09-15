"""Text format (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31104841-4a26-52a3-8091-8c92d4cb139e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/text format_31104841-4a26-52a3-8091-8c92d4cb139e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class TextFormat(Solo48):
    icon_id = 'text-format'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'format', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 14), (6, 6))
        self.add_line('e1', (6, 6), (42, 6))
        self.add_line('e2', (42, 6), (42, 13))
        self.add_line('e3', (24, 42), (24, 6))
        self.add_line('e4', (18, 42), (30, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
