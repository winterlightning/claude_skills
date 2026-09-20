"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'fc4c0825-2444-4f46-a5a5-c79974a41e25'
SOURCE_PATH = 'icon_set/model/icons/symbol/fragmented_brain_sub32_fc4c0825_2444_4f46_a5a5_c79974a41e25.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3ee7efeddeee65752c82a28eaed21e92494fff495cbea90df1d35585343b3563'
SOURCE_REFERENCES = (('fc4c0825-2444-4f46-a5a5-c79974a41e25', 'pictographic-primitives/symbol/fragmented brain_fc4c0825-2444-4f46-a5a5-c79974a41e25.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'fragmented-brain-sub32-resize'
    variant_of = 'fragmented-brain-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (4, 8), ((6, 4), (11, 2), (15, 2)))
        self.add_bezier('p1-r1-2', (15, 2), ((17, 2), (18, 3), (19, 4)))
        self.add_bezier('p1-r1-3', (19, 4), ((21, 6), (22, 5), (22, 7)))
        self.add_bezier('p1-r1-4', (22, 7), ((22, 9), (20, 11), (18, 11)))
        self.add_line('p1-r1-5', (18, 11), (6, 17))
        self.add_bezier('p1-r1-6', (6, 17), ((5, 18), (5, 18), (4, 18)))
        self.add_bezier('p1-r1-7', (4, 18), ((3, 18), (2, 17), (2, 15)))
        self.add_bezier('p1-r1-8', (2, 15), ((2, 13), (3, 11), (4, 8)))
        self.add_line('p2-r1-1', (4, 8), (13, 9))
        self.add_line('p2-r1-2', (13, 9), (18, 11))
        self.add_line('p3-r1-1', (6, 17), (13, 9))
        self.add_line('p3-r1-2', (13, 9), (19, 4))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
