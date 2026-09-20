"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e2391138-4aaf-4587-83d5-f636e7ba5379'
SOURCE_PATH = 'icon_set/model/icons/symbol/hand_over_heat_sub32_e2391138_4aaf_4587_83d5_f636e7ba5379.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0c06b2f085cd2ac49777e68e7fa56f2f753e66a8f3c646fffbae06f45bae36b6'
SOURCE_REFERENCES = (('e2391138-4aaf-4587-83d5-f636e7ba5379', 'pictographic-primitives/symbol/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'hand-over-heat-sub32-resize'
    variant_of = 'hand-over-heat-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 10), (10, 3))
        self.add_line('p1-r1-2', (10, 3), (18, 3))
        self.add_line('p2-r1-1', (2, 10), (8, 8))
        self.add_line('p2-r1-2', (8, 8), (13, 8))
        self.add_line('p3-r1-1', (8, 8), (8, 10))
        self.add_bezier('p3-r1-2', (8, 10), ((8, 10), (8, 10), (8, 10)), ((8, 10), (8, 11), (8, 11)), ((8, 11), (9, 11), (9, 12)), ((9, 12), (10, 12), (10, 12)), ((10, 12), (10, 12), (10, 12)), ((10, 12), (11, 12), (11, 12)))
        self.add_line('p3-r1-3', (11, 12), (16, 12))
        self.add_line('p3-r1-4', (16, 12), (22, 2))
        self.add_bezier('p4-r1-1', (8, 17), ((8, 17), (8, 17), (8, 17)), ((8, 17), (8, 17), (8, 17)), ((8, 17), (8, 17), (8, 17)), ((8, 17), (8, 17), (8, 18)))
        self.add_bezier('p4-r1-2', (8, 18), ((8, 18), (8, 18), (8, 18)), ((8, 18), (8, 18), (8, 18)), ((8, 18), (8, 18), (8, 18)), ((8, 18), (8, 18), (8, 18)))
        self.add_bezier('p4-r1-3', (8, 18), ((8, 18), (9, 18), (9, 18)), ((9, 18), (10, 18), (10, 18)), ((10, 19), (10, 19), (10, 19)), ((10, 20), (10, 20), (10, 20)))
        self.add_bezier('p4-r1-4', (10, 20), ((10, 21), (10, 21), (10, 21)), ((10, 21), (10, 21), (10, 21)), ((10, 22), (10, 22), (10, 22)), ((9, 22), (9, 22), (9, 22)), ((9, 22), (9, 22), (9, 22)), ((8, 22), (8, 22), (8, 21)))
        self.add_bezier('p5-r1-1', (16, 17), ((16, 16), (16, 16), (15, 16)), ((15, 16), (15, 16), (15, 16)), ((15, 16), (15, 16), (14, 16)), ((14, 16), (14, 16), (14, 17)), ((14, 17), (14, 17), (14, 17)), ((14, 17), (14, 17), (14, 18)))
        self.add_bezier('p5-r1-2', (14, 18), ((14, 18), (14, 18), (14, 18)), ((14, 18), (14, 18), (14, 18)), ((14, 19), (14, 19), (14, 19)), ((15, 19), (15, 19), (15, 19)), ((15, 19), (15, 19), (15, 19)), ((16, 19), (16, 19), (16, 18)))
        self.add_bezier('p5-r1-3', (16, 18), ((16, 18), (17, 19), (17, 19)), ((17, 19), (17, 19), (17, 19)), ((17, 20), (17, 20), (17, 20)), ((17, 20), (16, 20), (16, 20)))
        self.add_bezier('p5-r1-4', (16, 20), ((16, 21), (16, 21), (16, 21)), ((16, 21), (16, 21), (16, 21)), ((16, 21), (16, 21), (16, 21)), ((16, 21), (16, 21), (16, 21)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
