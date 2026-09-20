"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b70ed0a4-9193-4eb1-aa64-53f88bcf4fe3'
SOURCE_PATH = 'icon_set/model/icons/symbol/arrows_inward_four_sub32_b70ed0a4_9193_4eb1_aa64_53f88bcf4fe3.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f1684abe801ccc95a6539cf8900ff15030643de2df97eb0dcc2477e53078155b'
SOURCE_REFERENCES = (('b70ed0a4-9193-4eb1-aa64-53f88bcf4fe3', 'pictographic-primitives/symbol/four arrows pointing_b70ed0a4-9193-4eb1-aa64-53f88bcf4fe3.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'arrows-inward-four-sub32-resize'
    variant_of = 'arrows-inward-four-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (12, 8))
        self.add_line('p2-r1-1', (8, 4), (12, 8))
        self.add_line('p2-r1-2', (12, 8), (16, 4))
        self.add_line('p3-r1-1', (22, 12), (16, 12))
        self.add_line('p4-r1-1', (20, 8), (16, 12))
        self.add_line('p4-r1-2', (16, 12), (20, 16))
        self.add_line('p5-r1-1', (12, 22), (12, 16))
        self.add_line('p6-r1-1', (16, 20), (12, 16))
        self.add_line('p6-r1-2', (12, 16), (8, 20))
        self.add_line('p7-r1-1', (2, 12), (8, 12))
        self.add_line('p8-r1-1', (4, 16), (8, 12))
        self.add_line('p8-r1-2', (8, 12), (4, 8))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-2')
        self.relate('connect', 'p7-r1-1', 'p8-r1-1')
        self.relate('connect', 'p7-r1-1', 'p8-r1-2')
