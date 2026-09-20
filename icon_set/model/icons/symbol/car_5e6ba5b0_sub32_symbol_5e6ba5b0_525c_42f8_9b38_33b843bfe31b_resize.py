"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5e6ba5b0-525c-42f8-9b38-33b843bfe31b'
SOURCE_PATH = 'icon_set/model/icons/symbol/car_5e6ba5b0_sub32_symbol_5e6ba5b0_525c_42f8_9b38_33b843bfe31b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7a7320a64725dbdf782f219a62d6c80df48e4113d1e76eaaaa538746587af389'
SOURCE_REFERENCES = (('5e6ba5b0-525c-42f8-9b38-33b843bfe31b', 'pictographic-primitives/transportation/car_5e6ba5b0-525c-42f8-9b38-33b843bfe31b.svg'), ('796e3289-99b8-4ef8-bce0-4e8fa2bfefc8', 'pictographic-primitives/transportation/car_796e3289-99b8-4ef8-bce0-4e8fa2bfefc8.svg'), ('eaa7f06c-57de-4d21-aaa7-d89d24b33193', 'pictographic-primitives/transportation/car_eaa7f06c-57de-4d21-aaa7-d89d24b33193.svg'), ('edd4874e-4e76-4ead-a51d-24426b253623', 'pictographic-primitives/transportation/car_edd4874e-4e76-4ead-a51d-24426b253623.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'car-5e6ba5b0-sub32-symbol-resize'
    variant_of = 'car-5e6ba5b0-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 8), (8, 3))
        self.add_bezier('p1-r1-2', (8, 3), ((9, 2), (10, 2), (12, 2)))
        self.add_bezier('p1-r1-3', (12, 2), ((14, 2), (15, 2), (16, 3)))
        self.add_line('p1-r1-4', (16, 3), (18, 8))
        self.add_bezier('p2-r1-1', (4, 15), ((3, 15), (2, 13), (2, 11)))
        self.add_line('p2-r1-2', (2, 11), (2, 10))
        self.add_bezier('p2-r1-3', (2, 10), ((2, 9), (3, 7), (6, 8)))
        self.add_line('p2-r1-4', (6, 8), (18, 8))
        self.add_bezier('p2-r1-5', (18, 8), ((21, 8), (22, 9), (22, 10)))
        self.add_line('p2-r1-6', (22, 10), (22, 11))
        self.add_bezier('p2-r1-7', (22, 11), ((22, 13), (21, 15), (20, 15)))
        self.add_arc('p3-r1-1', (4, 15), (7, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (7, 12), (10, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (10, 15), (7, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (7, 18), (4, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-1', (14, 15), (17, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (17, 12), (20, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-3', (20, 15), (17, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-4', (17, 18), (14, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p5-r1-1', (10, 15), (14, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-5')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-4')
        self.relate('connect', 'p2-r1-7', 'p4-r1-2')
        self.relate('connect', 'p2-r1-7', 'p4-r1-3')
        self.relate('connect', 'p3-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-3', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
