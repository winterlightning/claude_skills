"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '031da5e5-a8c4-45af-9b74-e8c1dae95201'
SOURCE_PATH = 'icon_set/model/icons/symbol/circle_half_symbol_sub32_v2_031da5e5_a8c4_45af_9b74_e8c1dae95201.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'b9c1e1470c124bda424e950319d4dd1f6554ec67f2aa662445820106c389ea9a'
SOURCE_REFERENCES = (('031da5e5-a8c4-45af-9b74-e8c1dae95201', 'pictographic-primitives/symbol/circle half_031da5e5-a8c4-45af-9b74-e8c1dae95201.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'circle-half-symbol-sub32-v2-resize'
    variant_of = 'circle-half-symbol-sub32-v2'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('half-upper', (19, 2), (2, 12), radius_x=17, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('half-lower', (2, 12), (19, 22), radius_x=17, radius_y=10, large_arc=False, sweep=False)
        self.add_line('diameter', (19, 22), (19, 2))
        self.add_contour('path-1-1', 'half-upper', 'half-lower', 'diameter', closed=True)
