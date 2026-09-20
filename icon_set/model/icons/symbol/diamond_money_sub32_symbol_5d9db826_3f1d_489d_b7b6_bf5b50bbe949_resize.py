"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5d9db826-3f1d-489d-b7b6-bf5b50bbe949'
SOURCE_PATH = 'icon_set/model/icons/symbol/diamond_money_sub32_symbol_5d9db826_3f1d_489d_b7b6_bf5b50bbe949.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '46cdcc25a9e299693c8118eaa9691d88efa0b5b16c57cd10e03fa12a6b664b43'
SOURCE_REFERENCES = (('5d9db826-3f1d-489d-b7b6-bf5b50bbe949', 'pictographic-primitives/money/diamond_5d9db826-3f1d-489d-b7b6-bf5b50bbe949.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'diamond-money-sub32-symbol-resize'
    variant_of = 'diamond-money-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'money'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (17, 2))
        self.add_line('p1-r1-2', (17, 2), (22, 9))
        self.add_line('p1-r1-3', (22, 9), (12, 18))
        self.add_line('p1-r1-4', (12, 18), (2, 9))
        self.add_line('p1-r1-5', (2, 9), (7, 2))
        self.add_line('p2-r1-1', (2, 9), (9, 9))
        self.add_line('p2-r1-2', (9, 9), (15, 9))
        self.add_line('p2-r1-3', (15, 9), (22, 9))
        self.add_line('p3-r1-1', (7, 2), (9, 9))
        self.add_line('p3-r1-2', (9, 9), (12, 18))
        self.add_line('p3-r1-3', (12, 18), (15, 9))
        self.add_line('p3-r1-4', (15, 9), (17, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-4')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p3-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-3')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p3-r1-3')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-3')
        self.relate('connect', 'p2-r1-2', 'p3-r1-4')
        self.relate('connect', 'p2-r1-3', 'p3-r1-3')
        self.relate('connect', 'p2-r1-3', 'p3-r1-4')
