"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2ba7093-6168-49b2-9277-4703ccb6506f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house_a2ba7093-6168-49b2-9277-4703ccb6506f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class HouseA2ba7093(Solo48):
    icon_id = 'house-a2ba7093'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 24), (11, 19))
        self.add_line('e1', (42, 24), (37, 19))
        self.add_line('e2', (24, 33), (24, 42))
        self.add_line('e3', (37, 19), (24, 6))
        self.add_line('e4', (24, 6), (11, 19))
        self.add_line('e5', (37, 19), (37, 42))
        self.add_line('e6', (37, 42), (11, 42))
        self.add_line('e7', (11, 42), (11, 19))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.add_contour('c4', 'e5', 'e6', 'e7')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c4')
