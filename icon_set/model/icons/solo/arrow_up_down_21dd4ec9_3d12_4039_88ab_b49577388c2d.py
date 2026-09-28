"""Arrow up down (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21dd4ec9-3d12-4039-88ab-b49577388c2d'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow up down_21dd4ec9-3d12-4039-88ab-b49577388c2d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowUpDown(Solo48):
    icon_id = 'arrow-up-down'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('arrow', 'up', 'down', 'symbol')

    def build(self):
        self.add_line('e0', (4, 16), (12, 8))
        self.add_line('e1', (12, 8), (12, 40))
        self.add_line('e2', (12, 8), (20, 16))
        self.add_line('e3', (36, 8), (36, 40))
        self.add_line('e4', (28, 32), (36, 40))
        self.add_line('e5', (44, 32), (36, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
