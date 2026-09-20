"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '209827a6-da89-4cf7-a37d-a474d679eb0b'
SOURCE_PATH = 'icon_set/model/icons/symbol/shirt_width_content_sub32_209827a6_da89_4cf7_a37d_a474d679eb0b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '6b8f68d0270f92b48cfdfce5dcc946504d2e6bd4d903eca6bee31ac0e789d462'
SOURCE_REFERENCES = (('209827a6-da89-4cf7-a37d-a474d679eb0b', 'icon_set/dist/gallery/combination-originals/209827a6-da89-4cf7-a37d-a474d679eb0b.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'shirt-width-content-sub32-resize'
    variant_of = 'shirt-width-content-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (10, 7))
        self.add_line('p1-r1-2', (10, 7), (12, 11))
        self.add_line('p1-r1-3', (12, 11), (12, 19))
        self.add_line('p1-r1-4', (12, 19), (28, 19))
        self.add_line('p1-r1-5', (28, 19), (28, 11))
        self.add_line('p1-r1-6', (28, 11), (30, 7))
        self.add_line('p1-r1-7', (30, 7), (28, 2))
        self.add_line('p2-r1-1', (28, 2), (24, 2))
        self.add_arc('p2-r1-2', (24, 2), (16, 2), radius_x=4, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (16, 2), (12, 2))
        self.add_line('p3-r1-1', (2, 26), (38, 26))
        self.add_line('p4-r1-1', (6, 21), (2, 26))
        self.add_line('p4-r1-2', (2, 26), (7, 30))
        self.add_line('p5-r1-1', (34, 21), (38, 26))
        self.add_line('p5-r1-2', (38, 26), (33, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-2')
