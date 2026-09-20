"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3b4771f4-de72-4538-b549-43276caa2ff1'
SOURCE_PATH = 'icon_set/model/icons/symbol/robot_3b4771f4_sub32_symbol_3b4771f4_de72_4538_b549_43276caa2ff1.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '23bfde0e846abcf3e79aedf1ae97f261567316bc4bef7b84b640c0771ceaa1d2'
SOURCE_REFERENCES = (('3b4771f4-de72-4538-b549-43276caa2ff1', 'pictographic-primitives/artificial-intelligence/robot_3b4771f4-de72-4538-b549-43276caa2ff1.svg'), ('233b4b91-c66d-47bb-8540-9a5b8f63230e', 'pictographic-primitives/artificial-intelligence/robot_233b4b91-c66d-47bb-8540-9a5b8f63230e.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'robot-3b4771f4-sub32-symbol-resize'
    variant_of = 'robot-3b4771f4-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'artificial-intelligence'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (6, 8))
        self.add_line('p2-r1-1', (14, 2), (14, 8))
        self.add_bezier('p3-r1-1', (6, 8), ((6, 8), (6, 8), (6, 8)), ((5, 8), (5, 8), (5, 8)), ((4, 8), (4, 9), (3, 9)), ((3, 9), (3, 9), (3, 10)), ((2, 10), (2, 11), (2, 11)))
        self.add_line('p3-r1-2', (2, 11), (2, 17))
        self.add_bezier('p3-r1-3', (2, 17), ((2, 18), (2, 18), (2, 19)), ((3, 19), (3, 20), (3, 20)), ((4, 21), (4, 21), (5, 21)), ((5, 22), (5, 22), (6, 22)))
        self.add_line('p3-r1-4', (6, 22), (14, 22))
        self.add_bezier('p3-r1-5', (14, 22), ((14, 22), (15, 22), (15, 22)), ((16, 21), (16, 21), (17, 21)), ((17, 20), (17, 20), (18, 19)), ((18, 19), (18, 18), (18, 18)))
        self.add_line('p3-r1-6', (18, 18), (18, 11))
        self.add_bezier('p3-r1-7', (18, 11), ((18, 11), (18, 11), (18, 11)), ((18, 10), (18, 10), (18, 10)), ((18, 9), (17, 9), (17, 8)), ((16, 8), (16, 8), (15, 8)), ((15, 8), (15, 8), (15, 8)), ((15, 8), (14, 8), (14, 8)))
        self.add_line('p4-r1-1', (6, 8), (14, 8))
        self.add_line('p5-r1-1', (7, 14), (7, 16))
        self.add_line('p6-r1-1', (13, 14), (13, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-7')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-7', 'p4-r1-1')
