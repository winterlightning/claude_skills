"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2a9d95b0-3301-4030-a069-703a97ff8a06'
SOURCE_PATH = 'icon_set/model/icons/symbol/graph_line_health_sub32_v2_2a9d95b0_3301_4030_a069_703a97ff8a06.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '1d9a5e77f775640aa231fd06f03e15e996f8a45aaea3d17b529de81efafc7227'
SOURCE_REFERENCES = (('2a9d95b0-3301-4030-a069-703a97ff8a06', 'pictographic-primitives/health/graph line_2a9d95b0-3301-4030-a069-703a97ff8a06.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'graph-line-health-sub32-v2-resize'
    variant_of = 'graph-line-health-sub32-v2'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'health'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (18, 8), (18, 10))
        self.add_bezier('p1-r1-2', (18, 10), ((18, 11), (18, 12), (19, 12)))
        self.add_line('p1-r1-3', (19, 12), (22, 12))
        self.add_line('p2-r1-1', (2, 12), (6, 12))
        self.add_bezier('p2-r1-2', (6, 12), ((8, 12), (8, 12), (8, 10)))
        self.add_line('p2-r1-3', (8, 10), (10, 2))
        self.add_line('p3-r1-1', (10, 2), (14, 19))
        self.add_line('p3-r1-2', (14, 19), (18, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
