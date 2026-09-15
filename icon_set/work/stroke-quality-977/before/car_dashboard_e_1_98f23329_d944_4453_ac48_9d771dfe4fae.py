"""Car dashboard e 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98f23329-d944-4453-ac48-9d771dfe4fae'
SOURCE_PATH = 'pictographic-primitives/symbol/car dashboard e 1_98f23329-d944-4453-ac48-9d771dfe4fae.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CarDashboardE1(Solo48):
    icon_id = 'car-dashboard-e-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('car', 'dashboard', 'e', 'symbol')

    def build(self):
        self.add_line('e0', (20, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 27))
        self.add_line('e2', (8, 27), (19, 27))
        self.add_line('e3', (8, 16), (18, 16))
        self.add_line('e4', (40, 18), (14, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c1', 'c0')
