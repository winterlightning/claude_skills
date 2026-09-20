"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'icon_set/model/icons/symbol/circular_arrow_sub_v3_symbol_a576eae9_10c6_460b_afb1_570ec971a498.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ccc3a318954b548f9ca4ccb968441fdc08e9ac49c80969b4c1b2a628e754504a'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'circular-arrow-sub-v3-symbol-resize'
    variant_of = 'circular-arrow-sub-v3-symbol'
    variant_label = 'Resize 21 × 18'
    canvas_width = 21
    canvas_height = 18
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('lower-left', (9, 16), ((8, 16), (7, 16), (6, 15)), ((5, 15), (5, 15), (4, 14)), ((3, 13), (3, 13), (3, 12)), ((2, 11), (2, 10), (2, 9)))
        self.add_bezier('upper-left', (2, 9), ((2, 8), (2, 7), (3, 6)), ((3, 5), (3, 5), (4, 4)), ((5, 3), (5, 3), (6, 3)), ((7, 2), (8, 2), (9, 2)))
        self.add_bezier('upper-right', (9, 2), ((9, 2), (9, 2), (9, 2)), ((10, 2), (10, 2), (10, 2)), ((10, 2), (11, 2), (11, 2)), ((11, 2), (12, 2), (12, 3)), ((12, 3), (13, 3), (13, 3)))
        self.add_line('extension', (13, 3), (19, 8))
        self.add_line('head-1', (13, 8), (19, 8))
        self.add_line('head-2', (19, 8), (19, 3))
        self.add_contour('sweep', 'lower-left', 'upper-left', 'upper-right', 'extension', closed=False)
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'sweep', 'head')
