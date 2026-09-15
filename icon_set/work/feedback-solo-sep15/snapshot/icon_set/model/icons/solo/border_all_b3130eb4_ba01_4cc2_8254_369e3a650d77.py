"""Border all (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3130eb4-ba01-4cc2-8254-369e3a650d77'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/border all_b3130eb4-ba01-4cc2-8254-369e3a650d77.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class BorderAll(Solo48):
    icon_id = 'border-all'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('border', 'all', '_uncategorized')

    def build(self):
        self.add_line('e0', (42, 24), (24, 24))
        self.add_line('e1', (24, 42), (24, 24))
        self.add_line('e2', (6, 24), (24, 24))
        self.add_line('e3', (24, 6), (24, 24))
        self.add_line('e4', (6, 42), (42, 42))
        self.add_line('e5', (42, 42), (42, 6))
        self.add_line('e6', (42, 6), (6, 6))
        self.add_line('e7', (6, 6), (6, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e6', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
