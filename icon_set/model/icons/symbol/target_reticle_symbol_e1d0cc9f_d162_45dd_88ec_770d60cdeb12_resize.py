"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e1d0cc9f-d162-45dd-88ec-770d60cdeb12'
SOURCE_PATH = 'icon_set/model/icons/symbol/target_reticle_symbol_e1d0cc9f_d162_45dd_88ec_770d60cdeb12.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ef3674f3cc324c66ddac0f4d627ce6c63e99de52904a872aaea9b09a89d21a8b'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'target-reticle-symbol-resize'
    variant_of = 'target-reticle-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('ring-top', (4, 12), (20, 12), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('ring-bottom', (20, 12), (4, 12), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('top', (12, 2), (12, 6))
        self.add_line('bottom', (12, 18), (12, 22))
        self.add_line('left', (2, 12), (6, 12))
        self.add_line('right', (18, 12), (22, 12))
        self.add_line('centre', (12, 12), (12, 12))
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
        self.relate('connect', 'ring', 'top')
        self.relate('connect', 'ring', 'bottom')
        self.relate('connect', 'ring', 'left')
        self.relate('connect', 'ring', 'right')
