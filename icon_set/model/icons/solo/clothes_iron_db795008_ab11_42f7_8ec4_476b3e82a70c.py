'A clothes iron faces left with a pointed sloping nose and a long flat soleplate. A low control sits above the body beneath an open handle joining the tall rear edge.\n\nConstruction: Sloping iron body with an overhead handle. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db795008-ab11-42f7-8ec4-476b3e82a70c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/laundry iron water_db795008-ab11-42f7-8ec4-476b3e82a70c.svg'
AUTHOR = 'gpt-6'

class ClothesIron(Solo48):
    icon_id = 'clothes-iron'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('iron', 'clothes', 'laundry', 'soleplate', 'handle', 'appliance')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('sole-1', (4, 40), (16, 24))
        self.add_line('sole-2', (16, 24), (44, 24))
        self.add_line('sole-3', (44, 24), (44, 40))
        self.add_line('sole-4', (44, 40), (4, 40))
        self.add_line('handle-1', (20, 8), (36, 8))
        self.add_line('handle-2', (36, 8), (44, 16))
        self.add_line('handle-3', (44, 16), (44, 24))
        self.add_contour('sole', 'sole-1', 'sole-2', 'sole-3', 'sole-4', closed=True)
        self.add_contour('handle', 'handle-1', 'handle-2', 'handle-3', closed=False)
        self.relate('connect', 'sole', 'handle')
