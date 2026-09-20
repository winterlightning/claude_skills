"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '33e0f679-82d2-4c2a-b9d1-af30c1a9b528'
SOURCE_PATH = 'icon_set/model/icons/symbol/person_kicking_ball_sub32_33e0f679_82d2_4c2a_b9d1_af30c1a9b528.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '63b2f55a85248a3e2f2b5799ee3bf212f6506a7ffad26df09be8fd3ae56063c4'
SOURCE_REFERENCES = (('33e0f679-82d2-4c2a-b9d1-af30c1a9b528', 'pictographic-primitives/symbol/person playing ball_33e0f679-82d2-4c2a-b9d1-af30c1a9b528.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'person-kicking-ball-sub32-resize'
    variant_of = 'person-kicking-ball-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (12, 5), (18, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (18, 5), (12, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-1', (12, 11), ((11, 13), (11, 14), (10, 16)))
        self.add_line('p3-r1-1', (12, 11), (6, 10))
        self.add_line('p3-r1-2', (6, 10), (3, 13))
        self.add_line('p4-r1-1', (12, 11), (16, 13))
        self.add_line('p4-r1-2', (16, 13), (22, 10))
        self.add_line('p5-r1-1', (10, 16), (6, 20))
        self.add_line('p5-r1-2', (6, 20), (2, 20))
        self.add_line('p6-r1-1', (10, 16), (13, 18))
        self.add_line('p6-r1-2', (13, 18), (11, 22))
        self.add_arc('p7-r1-1', (18, 20), (22, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p7-r1-2', (22, 20), (18, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
