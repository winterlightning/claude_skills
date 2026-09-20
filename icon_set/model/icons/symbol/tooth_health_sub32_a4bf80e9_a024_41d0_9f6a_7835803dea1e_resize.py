"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a4bf80e9-a024-41d0-9f6a-7835803dea1e'
SOURCE_PATH = 'icon_set/model/icons/symbol/tooth_health_sub32_a4bf80e9_a024_41d0_9f6a_7835803dea1e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0749ac51414fe54779414276b4df5c0644de191220a20d574e07ef61b88f9d9e'
SOURCE_REFERENCES = (('a4bf80e9-a024-41d0-9f6a-7835803dea1e', 'pictographic-primitives/health/tooth_a4bf80e9-a024-41d0-9f6a-7835803dea1e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'tooth-health-sub32-resize'
    variant_of = 'tooth-health-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'health'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (9, 3), ((7, 3), (6, 2), (5, 2)))
        self.add_bezier('p1-r1-2', (5, 2), ((3, 2), (2, 4), (2, 7)))
        self.add_bezier('p1-r1-3', (2, 7), ((2, 10), (3, 13), (4, 15)))
        self.add_bezier('p1-r1-4', (4, 15), ((4, 19), (4, 22), (6, 22)))
        self.add_bezier('p1-r1-5', (6, 22), ((8, 22), (7, 14), (9, 14)))
        self.add_bezier('p1-r1-6', (9, 14), ((11, 14), (11, 22), (13, 22)))
        self.add_bezier('p1-r1-7', (13, 22), ((14, 22), (14, 19), (14, 15)))
        self.add_bezier('p1-r1-8', (14, 15), ((15, 13), (16, 10), (16, 7)))
        self.add_bezier('p1-r1-9', (16, 7), ((16, 4), (16, 2), (13, 2)))
        self.add_bezier('p1-r1-10', (13, 2), ((12, 2), (11, 3), (9, 3)))
        self.add_bezier('p2-r1-1', (16, 7), ((20, 7), (21, 9), (21, 12)))
        self.add_line('p2-r1-2', (21, 12), (21, 18))
        self.add_bezier('p2-r1-3', (21, 18), ((21, 19), (21, 20), (21, 20)))
        self.add_bezier('p2-r1-4', (21, 20), ((22, 20), (22, 20), (22, 20)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
