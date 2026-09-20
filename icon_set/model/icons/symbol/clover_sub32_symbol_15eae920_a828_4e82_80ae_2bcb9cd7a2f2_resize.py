"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '15eae920-a828-4e82-80ae-2bcb9cd7a2f2'
SOURCE_PATH = 'icon_set/model/icons/symbol/clover_sub32_symbol_15eae920_a828_4e82_80ae_2bcb9cd7a2f2.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'b9c01995d01f69d7b2b0d6cb6b1f07eab56d250fee56368220134bbd6fb894c6'
SOURCE_REFERENCES = (('15eae920-a828-4e82-80ae-2bcb9cd7a2f2', 'pictographic-primitives/state/clover_15eae920-a828-4e82-80ae-2bcb9cd7a2f2.svg'), ('36097aaf-e256-48a1-aaeb-0f09bc96bc72', 'pictographic-primitives/symbol/clover_36097aaf-e256-48a1-aaeb-0f09bc96bc72.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'clover-sub32-symbol-resize'
    variant_of = 'clover-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'state'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 12), (6, 6))
        self.add_bezier('p1-r1-2', (6, 6), ((6, 3), (7, 2), (9, 2)))
        self.add_bezier('p1-r1-3', (9, 2), ((11, 2), (11, 3), (12, 3)))
        self.add_bezier('p1-r1-4', (12, 3), ((13, 3), (13, 2), (15, 2)))
        self.add_bezier('p1-r1-5', (15, 2), ((17, 2), (18, 3), (18, 6)))
        self.add_line('p1-r1-6', (18, 6), (12, 12))
        self.add_line('p2-r1-1', (12, 12), (18, 6))
        self.add_bezier('p2-r1-2', (18, 6), ((21, 6), (22, 7), (22, 9)))
        self.add_bezier('p2-r1-3', (22, 9), ((22, 11), (21, 11), (21, 12)))
        self.add_bezier('p2-r1-4', (21, 12), ((21, 13), (22, 13), (22, 15)))
        self.add_bezier('p2-r1-5', (22, 15), ((22, 17), (21, 18), (18, 18)))
        self.add_line('p2-r1-6', (18, 18), (12, 12))
        self.add_line('p3-r1-1', (12, 12), (18, 18))
        self.add_bezier('p3-r1-2', (18, 18), ((18, 21), (17, 22), (15, 22)))
        self.add_bezier('p3-r1-3', (15, 22), ((13, 22), (13, 21), (12, 21)))
        self.add_bezier('p3-r1-4', (12, 21), ((11, 21), (11, 22), (9, 22)))
        self.add_bezier('p3-r1-5', (9, 22), ((7, 22), (6, 21), (6, 18)))
        self.add_line('p3-r1-6', (6, 18), (12, 12))
        self.add_line('p4-r1-1', (12, 12), (6, 18))
        self.add_bezier('p4-r1-2', (6, 18), ((3, 18), (2, 17), (2, 15)))
        self.add_bezier('p4-r1-3', (2, 15), ((2, 13), (3, 13), (3, 12)))
        self.add_bezier('p4-r1-4', (3, 12), ((3, 11), (2, 11), (2, 9)))
        self.add_bezier('p4-r1-5', (2, 9), ((2, 7), (3, 6), (6, 6)))
        self.add_line('p4-r1-6', (6, 6), (12, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-6')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-6')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-5')
        self.relate('connect', 'p1-r1-1', 'p4-r1-6')
        self.relate('connect', 'p1-r1-2', 'p4-r1-5')
        self.relate('connect', 'p1-r1-2', 'p4-r1-6')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-2')
        self.relate('connect', 'p1-r1-6', 'p2-r1-6')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-6')
        self.relate('connect', 'p1-r1-6', 'p4-r1-1')
        self.relate('connect', 'p1-r1-6', 'p4-r1-6')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-6')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-6')
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-5', 'p3-r1-2')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-2')
        self.relate('connect', 'p2-r1-6', 'p3-r1-6')
        self.relate('connect', 'p2-r1-6', 'p4-r1-1')
        self.relate('connect', 'p2-r1-6', 'p4-r1-6')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-6')
        self.relate('connect', 'p3-r1-5', 'p4-r1-1')
        self.relate('connect', 'p3-r1-5', 'p4-r1-2')
        self.relate('connect', 'p3-r1-6', 'p4-r1-1')
        self.relate('connect', 'p3-r1-6', 'p4-r1-2')
        self.relate('connect', 'p3-r1-6', 'p4-r1-6')
