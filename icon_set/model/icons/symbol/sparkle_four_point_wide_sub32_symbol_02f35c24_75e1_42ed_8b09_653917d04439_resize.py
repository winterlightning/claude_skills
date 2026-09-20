"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '02f35c24-75e1-42ed-8b09-653917d04439'
SOURCE_PATH = 'icon_set/model/icons/symbol/sparkle_four_point_wide_sub32_symbol_02f35c24_75e1_42ed_8b09_653917d04439.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0084a67ecdfe6bbc923620b4463e330e33aa1fff927fac999ba097b05e4f19eb'
SOURCE_REFERENCES = (('02f35c24-75e1-42ed-8b09-653917d04439', 'pictographic-primitives/symbol/spark_02f35c24-75e1-42ed-8b09-653917d04439.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'sparkle-four-point-wide-sub32-symbol-resize'
    variant_of = 'sparkle-four-point-wide-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (12, 2), (22, 12), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (22, 12), (12, 22), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (12, 22), (2, 12), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (2, 12), (12, 2), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
