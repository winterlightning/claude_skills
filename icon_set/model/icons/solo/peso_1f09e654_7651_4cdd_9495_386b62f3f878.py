"""Peso (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f09e654-7651-4cdd-9495-386b62f3f878'
SOURCE_PATH = 'pictographic-primitives/money/peso_1f09e654-7651-4cdd-9495-386b62f3f878.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Peso(Solo48):
    icon_id = 'peso'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('primitives', 'money')
    aliases = ()
    keywords = ('peso', 'money')

    def build(self):
        self.add_line('e0', (8, 22), (14, 22))
        self.add_line('e1', (14, 22), (14, 44))
        self.add_line('e2', (14, 22), (32, 22))
        self.add_line('e3', (30, 4), (14, 4))
        self.add_line('e4', (14, 4), (14, 22))
        self.add_arc('e5-1', (32, 22), (40, 14), radius_x=8, sweep=False)
        self.add_arc('e5-2', (40, 14), (30, 4), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e5-1', 'e5-2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
