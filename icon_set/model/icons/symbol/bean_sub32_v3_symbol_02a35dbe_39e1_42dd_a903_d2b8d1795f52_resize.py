"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '02a35dbe-39e1-42dd-a903-d2b8d1795f52'
SOURCE_PATH = 'icon_set/model/icons/symbol/bean_sub32_v3_symbol_02a35dbe_39e1_42dd_a903_d2b8d1795f52.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2372fa1919bcef65550758f40d7fc22967413e990fa1893d52be0d45683efaf4'
SOURCE_REFERENCES = (('02a35dbe-39e1-42dd-a903-d2b8d1795f52', 'pictographic-primitives/symbol/peanut_02a35dbe-39e1-42dd-a903-d2b8d1795f52.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bean-sub32-v3-symbol-resize'
    variant_of = 'bean-sub32-v3-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (12, 6), ((12, 4), (14, 2), (17, 2)))
        self.add_bezier('p1-r1-2', (17, 2), ((20, 2), (22, 4), (22, 6)))
        self.add_bezier('p1-r1-3', (22, 6), ((22, 10), (20, 13), (17, 15)))
        self.add_bezier('p1-r1-4', (17, 15), ((14, 17), (11, 19), (6, 19)))
        self.add_bezier('p1-r1-5', (6, 19), ((4, 19), (2, 17), (2, 15)))
        self.add_bezier('p1-r1-6', (2, 15), ((2, 13), (4, 10), (6, 10)))
        self.add_bezier('p1-r1-7', (6, 10), ((8, 10), (10, 10), (11, 9)))
        self.add_bezier('p1-r1-8', (11, 9), ((11, 8), (12, 8), (12, 6)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
