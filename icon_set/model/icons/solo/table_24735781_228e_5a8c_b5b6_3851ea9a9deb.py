"""Table (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24735781-228e-5a8c-b5b6-3851ea9a9deb'
SOURCE_PATH = 'pictographic-primitives/furnitures/table_24735781-228e-5a8c-b5b6-3851ea9a9deb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Table(Solo48):
    icon_id = 'table'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('table', 'furnitures')

    def build(self):
        self.add_line('e0', (44, 16), (44, 8))
        self.add_line('e1', (44, 8), (4, 8))
        self.add_line('e2', (4, 8), (4, 16))
        self.add_line('e3', (44, 16), (4, 16))
        self.add_line('e4', (9, 40), (9, 16))
        self.add_line('e5', (39, 16), (39, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c1')
