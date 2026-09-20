"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '7099417a-0fa8-4ad5-84bf-e77a845b942a'
SOURCE_PATH = 'icon_set/model/icons/symbol/phone_1_sub32_symbol_7099417a_0fa8_4ad5_84bf_e77a845b942a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '099f7f8b78eb12e50be511b0423b9dd4c0218c4face70de804b22cee0444ca52'
SOURCE_REFERENCES = (('7099417a-0fa8-4ad5-84bf-e77a845b942a', 'pictographic-primitives/state/phone 1_7099417a-0fa8-4ad5-84bf-e77a845b942a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'phone-1-sub32-symbol-resize'
    variant_of = 'phone-1-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'state'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (10, 6))
        self.add_bezier('p1-r1-2', (10, 6), ((11, 6), (11, 6), (11, 6)))
        self.add_bezier('p1-r1-3', (11, 6), ((11, 8), (9, 8), (8, 9)))
        self.add_bezier('p1-r1-4', (8, 9), ((10, 12), (12, 14), (15, 16)))
        self.add_bezier('p1-r1-5', (15, 16), ((16, 14), (16, 13), (17, 13)))
        self.add_bezier('p1-r1-6', (17, 13), ((18, 13), (18, 14), (18, 14)))
        self.add_line('p1-r1-7', (18, 14), (22, 18))
        self.add_bezier('p1-r1-8', (22, 18), ((22, 21), (20, 22), (18, 22)))
        self.add_bezier('p1-r1-9', (18, 22), ((10, 21), (2, 13), (2, 6)))
        self.add_bezier('p1-r1-10', (2, 6), ((2, 4), (3, 2), (6, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
