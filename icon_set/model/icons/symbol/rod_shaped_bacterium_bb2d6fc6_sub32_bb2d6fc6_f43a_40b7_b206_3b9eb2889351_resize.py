"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'bb2d6fc6-f43a-40b7-b206-3b9eb2889351'
SOURCE_PATH = 'icon_set/model/icons/symbol/rod_shaped_bacterium_bb2d6fc6_sub32_bb2d6fc6_f43a_40b7_b206_3b9eb2889351.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '1d25e6f501a97dc4c911fb5de89a82b2102832cc1a164aecae9cf36bc1b4694e'
SOURCE_REFERENCES = (('bb2d6fc6-f43a-40b7-b206-3b9eb2889351', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/bacteria_bb2d6fc6-f43a-40b7-b206-3b9eb2889351.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'rod-shaped-bacterium-bb2d6fc6-sub32-resize'
    variant_of = 'rod-shaped-bacterium-bb2d6fc6-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'health'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 13), (8, 8))
        self.add_line('p1-r1-2', (8, 8), (11, 4))
        self.add_bezier('p1-r1-3', (11, 4), ((11, 3), (12, 3), (13, 3)))
        self.add_bezier('p1-r1-4', (13, 3), ((13, 2), (14, 2), (16, 2)))
        self.add_arc('p1-r1-5', (16, 2), (21, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (21, 8), (20, 11), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (20, 11), (16, 16))
        self.add_line('p1-r1-8', (16, 16), (13, 20))
        self.add_bezier('p1-r1-9', (13, 20), ((13, 21), (12, 21), (11, 21)))
        self.add_bezier('p1-r1-10', (11, 21), ((11, 22), (10, 22), (8, 22)))
        self.add_arc('p1-r1-11', (8, 22), (3, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-12', (3, 16), (4, 13), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (3, 16), (2, 16))
        self.add_line('p3-r1-1', (21, 8), (22, 8))
        self.add_line('p4-r1-1', (8, 8), (4, 6))
        self.add_line('p5-r1-1', (16, 16), (20, 18))
        self.add_line('p6-r1-1', (11, 4), (8, 2))
        self.add_line('p7-r1-1', (13, 20), (16, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p6-r1-1')
        self.relate('connect', 'p1-r1-3', 'p6-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p5-r1-1')
        self.relate('connect', 'p1-r1-8', 'p5-r1-1')
        self.relate('connect', 'p1-r1-8', 'p7-r1-1')
        self.relate('connect', 'p1-r1-9', 'p7-r1-1')
        self.relate('connect', 'p1-r1-11', 'p2-r1-1')
        self.relate('connect', 'p1-r1-12', 'p2-r1-1')
