"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '37404b45-6940-44fc-b7c8-3c963f7c35dd'
SOURCE_PATH = 'icon_set/model/icons/symbol/basket_shopping_sub32_symbol_37404b45_6940_44fc_b7c8_3c963f7c35dd.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3b0bbf3bda9ab2381736b541f010733c6e79b13d9756a2b23cd79c94a8f057cf'
SOURCE_REFERENCES = (('37404b45-6940-44fc-b7c8-3c963f7c35dd', 'pictographic-primitives/symbol/basket_37404b45-6940-44fc-b7c8-3c963f7c35dd.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'basket-shopping-sub32-symbol-resize'
    variant_of = 'basket-shopping-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 11), (8, 11))
        self.add_line('p1-r1-2', (8, 11), (16, 11))
        self.add_line('p1-r1-3', (16, 11), (22, 11))
        self.add_line('p2-r1-1', (2, 11), (4, 20))
        self.add_arc('p2-r1-2', (4, 20), (6, 22), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (6, 22), (18, 22))
        self.add_arc('p2-r1-4', (18, 22), (20, 20), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (20, 20), (22, 11))
        self.add_arc('p3-r1-1', (8, 11), (16, 11), radius_x=4, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
