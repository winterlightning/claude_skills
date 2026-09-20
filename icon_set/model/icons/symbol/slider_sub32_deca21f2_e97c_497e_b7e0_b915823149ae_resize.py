"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'deca21f2-e97c-497e-b7e0-b915823149ae'
SOURCE_PATH = 'icon_set/model/icons/symbol/slider_sub32_deca21f2_e97c_497e_b7e0_b915823149ae.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'bd820997a1eedf0e849aed4fcfe179e3887d80f2c84c55dab6a6fae2ac41551d'
SOURCE_REFERENCES = (('deca21f2-e97c-497e-b7e0-b915823149ae', 'pictographic-primitives/symbol/slider_deca21f2-e97c-497e-b7e0-b915823149ae.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'slider-sub32-resize'
    variant_of = 'slider-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (8, 6), ((8, 6), (8, 5), (8, 5)), ((9, 4), (9, 4), (9, 3)), ((10, 3), (10, 3), (11, 2)), ((11, 2), (12, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((12, 2), (12, 2), (12, 2)), ((13, 2), (13, 2), (14, 2)), ((14, 2), (15, 3), (15, 3)), ((16, 3), (16, 4), (16, 4)), ((17, 5), (17, 5), (17, 6)))
        self.add_bezier('p1-r1-3', (17, 6), ((17, 7), (17, 7), (17, 8)), ((16, 9), (16, 9), (16, 10)), ((15, 10), (15, 10), (14, 11)), ((13, 11), (13, 11), (12, 11)))
        self.add_bezier('p1-r1-4', (12, 11), ((11, 11), (11, 11), (10, 10)), ((10, 10), (9, 10), (9, 9)), ((9, 9), (8, 8), (8, 8)), ((8, 7), (8, 7), (8, 6)), ((8, 6), (8, 6), (8, 6)))
        self.add_line('p2-r1-1', (2, 6), (8, 6))
        self.add_line('p3-r1-1', (17, 6), (38, 6))
        self.add_bezier('p4-r1-1', (23, 19), ((23, 18), (23, 18), (24, 17)), ((24, 17), (24, 16), (25, 16)), ((25, 16), (26, 15), (26, 15)), ((27, 15), (27, 15), (28, 15)), ((28, 15), (28, 15), (28, 15)))
        self.add_bezier('p4-r1-2', (28, 15), ((28, 15), (29, 15), (29, 15)), ((30, 16), (30, 16), (31, 16)), ((31, 17), (31, 17), (32, 18)), ((32, 18), (32, 19), (32, 19)))
        self.add_bezier('p4-r1-3', (32, 19), ((32, 19), (32, 19), (32, 19)), ((32, 20), (32, 20), (32, 21)), ((32, 21), (31, 22), (31, 22)), ((31, 23), (30, 23), (30, 23)), ((29, 24), (29, 24), (28, 24)))
        self.add_bezier('p4-r1-4', (28, 24), ((27, 24), (27, 24), (26, 24)), ((25, 23), (25, 23), (24, 23)), ((24, 22), (24, 22), (23, 21)), ((23, 20), (23, 20), (23, 19)))
        self.add_line('p5-r1-1', (2, 19), (23, 19))
        self.add_line('p6-r1-1', (32, 19), (38, 19))
        self.add_line('p7-r1-1', (2, 30), (38, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p6-r1-1')
        self.relate('connect', 'p4-r1-3', 'p6-r1-1')
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
