"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4e67f929-3e9f-4fd3-aaec-bcd922b880c6'
SOURCE_PATH = 'icon_set/model/icons/symbol/irregular_potato_three_eyes_sub32_symbol_4e67f929_3e9f_4fd3_aaec_bcd922b880c6.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '12f002f3a726ba26e05af44ef93187cf32c963240f98c73b3fb6a1a5cd188b95'
SOURCE_REFERENCES = (('4e67f929-3e9f-4fd3-aaec-bcd922b880c6', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/painting_4e67f929-3e9f-4fd3-aaec-bcd922b880c6.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'irregular-potato-three-eyes-sub32-symbol-resize'
    variant_of = 'irregular-potato-three-eyes-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'food'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (12, 2), ((18, 2), (22, 4), (22, 8)))
        self.add_bezier('p1-r1-2', (22, 8), ((22, 11), (18, 11), (18, 13)))
        self.add_bezier('p1-r1-3', (18, 13), ((18, 15), (19, 16), (19, 17)))
        self.add_bezier('p1-r1-4', (19, 17), ((19, 18), (18, 19), (18, 20)))
        self.add_bezier('p1-r1-5', (18, 20), ((16, 21), (13, 22), (11, 22)))
        self.add_bezier('p1-r1-6', (11, 22), ((6, 22), (2, 18), (2, 14)))
        self.add_bezier('p1-r1-7', (2, 14), ((2, 8), (6, 2), (12, 2)))
        self.add_line('p2-r1-1', (8, 8), (8, 8))
        self.add_line('p3-r1-1', (16, 8), (16, 8))
        self.add_line('p4-r1-1', (10, 16), (10, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
