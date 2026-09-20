"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '1895f89b-67da-4327-b67f-f9726c4899c7'
SOURCE_PATH = 'icon_set/model/icons/symbol/globe_symbol_sub32_symbol_1895f89b_67da_4327_b67f_f9726c4899c7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'd2815b638b89be988a49e71be43b0e56fd2b858b79c1142fdbac279f8101d16d'
SOURCE_REFERENCES = (('1895f89b-67da-4327-b67f-f9726c4899c7', 'pictographic-primitives/symbol/globe_1895f89b-67da-4327-b67f-f9726c4899c7.svg'), ('c71b55db-b3c3-429a-ae0f-378e045b24c3', 'pictographic-primitives/maps/earth_c71b55db-b3c3-429a-ae0f-378e045b24c3.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'globe-symbol-sub32-symbol-resize'
    variant_of = 'globe-symbol-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (21, 16), (3, 16))
        self.add_line('p2-r1-1', (12, 22), (12, 2))
        self.add_arc('p2-r1-2', (12, 2), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (2, 12), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p2-r1-4', (12, 22), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p2-r1-5', (22, 12), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('p3-r1-1', (21, 8), (3, 8))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
