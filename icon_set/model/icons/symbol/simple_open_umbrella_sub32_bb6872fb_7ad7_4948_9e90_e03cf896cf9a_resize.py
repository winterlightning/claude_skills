"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'bb6872fb-7ad7-4948-9e90-e03cf896cf9a'
SOURCE_PATH = 'icon_set/model/icons/symbol/simple_open_umbrella_sub32_bb6872fb_7ad7_4948_9e90_e03cf896cf9a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'd5636ca7b6e511a7694b9abcce031296be73f25f0654d4c1962eef70ee25d618'
SOURCE_REFERENCES = (('bb6872fb-7ad7-4948-9e90-e03cf896cf9a', 'pictographic-primitives/accessories/batch-02/umbrella_bb6872fb-7ad7-4948-9e90-e03cf896cf9a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'simple-open-umbrella-sub32-resize'
    variant_of = 'simple-open-umbrella-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/accessories'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 13), ((2, 11), (3, 8), (4, 7)))
        self.add_bezier('p1-r1-2', (4, 7), ((6, 6), (8, 5), (10, 5)))
        self.add_bezier('p1-r1-3', (10, 5), ((12, 5), (14, 6), (16, 7)))
        self.add_bezier('p1-r1-4', (16, 7), ((17, 8), (18, 11), (18, 13)))
        self.add_line('p1-r1-5', (18, 13), (10, 13))
        self.add_line('p1-r1-6', (10, 13), (2, 13))
        self.add_line('p2-r1-1', (10, 2), (10, 5))
        self.add_line('p3-r1-1', (10, 13), (10, 19))
        self.add_bezier('p3-r1-2', (10, 19), ((10, 21), (9, 22), (7, 22)))
        self.add_bezier('p3-r1-3', (7, 22), ((6, 22), (5, 21), (5, 19)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
