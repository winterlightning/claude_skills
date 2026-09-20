"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '7f0ac7d1-2c65-44de-9523-d762d29b36e3'
SOURCE_PATH = 'icon_set/model/icons/symbol/person_slipping_backward_sub32_7f0ac7d1_2c65_44de_9523_d762d29b36e3.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'dfbdf573fd03401b770c300cda0a0a8872ffe36eb9a2f71bfdecd9d743a3487f'
SOURCE_REFERENCES = (('7f0ac7d1-2c65-44de-9523-d762d29b36e3', 'pictographic-primitives/symbol/person slipping rocky_7f0ac7d1-2c65-44de-9523-d762d29b36e3.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'person-slipping-backward-sub32-resize'
    variant_of = 'person-slipping-backward-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (12, 5), (18, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (18, 5), (12, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-1', (12, 11), ((11, 13), (11, 15), (10, 16)))
        self.add_line('p3-r1-1', (10, 16), (6, 22))
        self.add_line('p4-r1-1', (12, 11), (6, 10))
        self.add_line('p4-r1-2', (6, 10), (4, 4))
        self.add_line('p5-r1-1', (12, 11), (18, 14))
        self.add_line('p5-r1-2', (18, 14), (22, 16))
        self.add_line('p6-r1-1', (10, 16), (4, 16))
        self.add_line('p6-r1-2', (4, 16), (2, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
