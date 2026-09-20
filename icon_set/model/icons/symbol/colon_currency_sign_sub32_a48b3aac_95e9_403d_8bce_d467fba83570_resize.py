"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a48b3aac-95e9-403d-8bce-d467fba83570'
SOURCE_PATH = 'icon_set/model/icons/symbol/colon_currency_sign_sub32_a48b3aac_95e9_403d_8bce_d467fba83570.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'd85ec51ae3c53e888562dea57464b110a7be85a84b9cf83d1cfa20265d7dbd09'
SOURCE_REFERENCES = (('a48b3aac-95e9-403d-8bce-d467fba83570', 'pictographic-primitives/symbol/colon sign_a48b3aac-95e9-403d-8bce-d467fba83570.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'colon-currency-sign-sub32-resize'
    variant_of = 'colon-currency-sign-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (18, 2), (12, 2))
        self.add_arc('p1-r1-2', (12, 2), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (2, 12), (4, 18), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (4, 18), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (12, 22), (18, 22))
        self.add_line('p2-r1-1', (2, 20), (4, 18))
        self.add_line('p2-r1-2', (4, 18), (18, 4))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
