"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2e3a17fb-a451-57ee-9080-18af2bbac9d9'
SOURCE_PATH = 'icon_set/model/icons/symbol/walking_stick_figure_sub32_2e3a17fb_a451_57ee_9080_18af2bbac9d9.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3d3f94c3fdaac3efa4a5be1e33a81ae780f934a83b2707b5a0a9c1b42288607b'
SOURCE_REFERENCES = (('2e3a17fb-a451-57ee-9080-18af2bbac9d9', 'pictographic-primitives/wayfinding/walking_2e3a17fb-a451-57ee-9080-18af2bbac9d9.svg'), ('7ce62344-aeae-474c-9800-f2104921b059', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/walking_7ce62344-aeae-474c-9800-f2104921b059.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'walking-stick-figure-sub32-resize'
    variant_of = 'walking-stick-figure-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/wayfinding'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (9, 3), ((9, 3), (10, 2), (11, 2)))
        self.add_bezier('p1-r1-2', (11, 2), ((12, 2), (13, 3), (13, 3)))
        self.add_arc('p1-r1-3', (13, 3), (9, 3), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (10, 10), (9, 16))
        self.add_line('p3-r1-1', (3, 14), (10, 10))
        self.add_line('p3-r1-2', (10, 10), (16, 15))
        self.add_line('p4-r1-1', (2, 22), (9, 16))
        self.add_line('p4-r1-2', (9, 16), (15, 22))
        self.add_line('p4-r1-3', (15, 22), (18, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
