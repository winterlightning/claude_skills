"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '6be3bbdd-720f-407c-af2d-59983752017d'
SOURCE_PATH = 'icon_set/model/icons/symbol/bus_front_sub32_symbol_6be3bbdd_720f_407c_af2d_59983752017d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f5af5a476ea94e863a5d1310b8c7486e2e84c231d4d615fa6ccac10b69161a57'
SOURCE_REFERENCES = (('6be3bbdd-720f-407c-af2d-59983752017d', 'pictographic-primitives/transportation/bus_6be3bbdd-720f-407c-af2d-59983752017d.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bus-front-sub32-symbol-resize'
    variant_of = 'bus-front-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 2), (16, 2))
        self.add_arc('p1-r1-2', (16, 2), (18, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (18, 4), (18, 9))
        self.add_line('p1-r1-4', (18, 9), (18, 17))
        self.add_arc('p1-r1-5', (18, 17), (16, 19), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (16, 19), (15, 19))
        self.add_line('p1-r1-7', (15, 19), (5, 19))
        self.add_line('p1-r1-8', (5, 19), (4, 19))
        self.add_arc('p1-r1-9', (4, 19), (2, 17), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (2, 17), (2, 9))
        self.add_line('p1-r1-11', (2, 9), (2, 4))
        self.add_arc('p1-r1-12', (2, 4), (4, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 9), (18, 9))
        self.add_line('p3-r1-1', (5, 19), (5, 22))
        self.add_line('p4-r1-1', (15, 19), (15, 22))
        self.add_line('p5-r1-1', (6, 13), (7, 14))
        self.add_line('p6-r1-1', (13, 14), (14, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p4-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p4-r1-1')
        self.relate('connect', 'p1-r1-8', 'p3-r1-1')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p1-r1-11', 'p2-r1-1')
