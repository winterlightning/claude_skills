"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2'
SOURCE_PATH = 'icon_set/model/icons/symbol/car_skidding_sub32_9ba9924a_41d3_4ed9_93c5_d475f8bd2fd2.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'fbb660f508d8ed6e51df33c5c4eeca8d9de77acf25944003749979177d284813'
SOURCE_REFERENCES = (('9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2', 'pictographic-primitives/symbol/car with wave lines_9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'car-skidding-sub32-resize'
    variant_of = 'car-skidding-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (3, 7), (5, 7))
        self.add_line('p1-r1-2', (5, 7), (15, 7))
        self.add_line('p1-r1-3', (15, 7), (17, 7))
        self.add_arc('p1-r1-4', (17, 7), (18, 8), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (18, 8), (18, 10))
        self.add_arc('p1-r1-6', (18, 10), (17, 11), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (17, 11), (3, 11))
        self.add_arc('p1-r1-8', (3, 11), (2, 10), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 10), (2, 8))
        self.add_arc('p1-r1-10', (2, 8), (3, 7), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (5, 7), (7, 2))
        self.add_line('p2-r1-2', (7, 2), (13, 2))
        self.add_line('p2-r1-3', (13, 2), (15, 7))
        self.add_arc('p3-r1-1', (6, 16), (6, 19), radius_x=2, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('p3-r1-2', (6, 19), (6, 22), radius_x=2, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('p4-r1-1', (14, 16), (14, 19), radius_x=2, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('p4-r1-2', (14, 19), (14, 22), radius_x=2, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
