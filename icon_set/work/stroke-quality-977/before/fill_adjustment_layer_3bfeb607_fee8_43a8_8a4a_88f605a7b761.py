"""Fill adjustment layer (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bfeb607-fee8-43a8-8a4a-88f605a7b761'
SOURCE_PATH = 'pictographic-primitives/design/fill adjustment layer_3bfeb607-fee8-43a8-8a4a-88f605a7b761.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FillAdjustmentLayer(Solo48):
    icon_id = 'fill-adjustment-layer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('fill', 'adjustment', 'layer', 'design')

    def build(self):
        self.add_line('e0', (13, 24), (7, 28))
        self.add_line('e1', (7, 31), (22, 42))
        self.add_line('e2', (24, 42), (41, 31))
        self.add_line('e3', (41, 28), (35, 24))
        self.add_line('e4', (13, 24), (22, 31))
        self.add_line('e5', (25, 31), (35, 24))
        self.add_line('e6', (13, 24), (7, 20))
        self.add_line('e7', (7, 17), (23, 6))
        self.add_line('e8', (25, 6), (41, 17))
        self.add_line('e9', (41, 20), (35, 24))
        self.add_line('e10-1', (7, 28), (6, 29))
        self.add_line('e10-2', (6, 29), (7, 31))
        self.add_line('e11', (22, 42), (24, 42))
        self.add_line('e12-1', (41, 31), (42, 29))
        self.add_line('e12-2', (42, 29), (41, 28))
        self.add_arc('e13', (22, 31), (25, 31), radius_x=3, sweep=False)
        self.add_line('e14-1', (7, 20), (6, 19))
        self.add_line('e14-2', (6, 19), (7, 17))
        self.add_line('e15', (23, 6), (25, 6))
        self.add_line('e16-1', (41, 17), (42, 19))
        self.add_line('e16-2', (42, 19), (41, 20))
        self.add_contour('c0', 'e0', 'e10-1', 'e10-2', 'e1', 'e11', 'e2', 'e12-1', 'e12-2', 'e3')
        self.add_contour('c1', 'e4', 'e13', 'e5')
        self.add_contour('c2', 'e6', 'e14-1', 'e14-2', 'e7', 'e15', 'e8', 'e16-1', 'e16-2', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
