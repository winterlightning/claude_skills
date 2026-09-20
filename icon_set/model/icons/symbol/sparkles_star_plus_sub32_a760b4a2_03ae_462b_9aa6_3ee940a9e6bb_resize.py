"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a760b4a2-03ae-462b-9aa6-3ee940a9e6bb'
SOURCE_PATH = 'icon_set/model/icons/symbol/sparkles_star_plus_sub32_a760b4a2_03ae_462b_9aa6_3ee940a9e6bb.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0d2e89b3b48b3041fa4229c64c120be8288088e64be438a0ca1b0259a1c5f4a0'
SOURCE_REFERENCES = (('a760b4a2-03ae-462b-9aa6-3ee940a9e6bb', 'pictographic-primitives/symbol/sparkles_a760b4a2-03ae-462b-9aa6-3ee940a9e6bb.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'sparkles-star-plus-sub32-resize'
    variant_of = 'sparkles-star-plus-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (8, 6), (10, 11))
        self.add_line('p1-r1-2', (10, 11), (13, 14))
        self.add_line('p1-r1-3', (13, 14), (10, 16))
        self.add_line('p1-r1-4', (10, 16), (8, 22))
        self.add_line('p1-r1-5', (8, 22), (6, 16))
        self.add_line('p1-r1-6', (6, 16), (2, 14))
        self.add_line('p1-r1-7', (2, 14), (6, 11))
        self.add_line('p1-r1-8', (6, 11), (8, 6))
        self.add_line('p2-r1-1', (14, 4), (16, 4))
        self.add_line('p2-r1-2', (16, 4), (18, 4))
        self.add_line('p3-r1-1', (16, 2), (16, 4))
        self.add_line('p3-r1-2', (16, 4), (16, 6))
        self.add_line('p4-r1-1', (18, 16), (20, 16))
        self.add_line('p4-r1-2', (20, 16), (22, 16))
        self.add_line('p5-r1-1', (20, 14), (20, 16))
        self.add_line('p5-r1-2', (20, 16), (20, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-2')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-2')
