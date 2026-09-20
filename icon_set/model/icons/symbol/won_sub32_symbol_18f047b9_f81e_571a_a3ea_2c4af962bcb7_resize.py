"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '18f047b9-f81e-571a-a3ea-2c4af962bcb7'
SOURCE_PATH = 'icon_set/model/icons/symbol/won_sub32_symbol_18f047b9_f81e_571a_a3ea_2c4af962bcb7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '1657db0c058192055dd3227856402c7f1991a534e7170ff53c0439655ac93f22'
SOURCE_REFERENCES = (('18f047b9-f81e-571a-a3ea-2c4af962bcb7', 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'won-sub32-symbol-resize'
    variant_of = 'won-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'money'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (22, 2), (18, 18))
        self.add_line('p1-r1-2', (18, 18), (12, 2))
        self.add_line('p1-r1-3', (12, 2), (6, 17))
        self.add_line('p1-r1-4', (6, 17), (2, 2))
        self.add_line('p2-r1-1', (22, 9), (2, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
