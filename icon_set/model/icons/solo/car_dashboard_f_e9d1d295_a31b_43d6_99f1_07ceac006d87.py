"""Car dashboard f (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9d1d295-a31b-43d6-99f1-07ceac006d87'
SOURCE_PATH = 'pictographic-primitives/transportation/car dashboard f_e9d1d295-a31b-43d6-99f1-07ceac006d87.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CarDashboardF(Solo48):
    icon_id = 'car-dashboard-f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'dashboard', 'f', 'transportation')

    def build(self):
        self.add_line('e0', (21, 6), (6, 6))
        self.add_line('e1', (6, 6), (6, 20))
        self.add_line('e2', (6, 31), (6, 20))
        self.add_line('e3', (17, 19), (6, 19))
        self.add_line('e4', (42, 12), (17, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c2', 'c0')
