"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '45b73137-0503-4586-8373-394aa93d3ff8'
SOURCE_PATH = 'icon_set/model/icons/symbol/personal_hotspot_sub32_45b73137_0503_4586_8373_394aa93d3ff8.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'eb1b88a6b509b535a2243e1a635656616180cf22fc4d9bf17968a4650234e793'
SOURCE_REFERENCES = (('45b73137-0503-4586-8373-394aa93d3ff8', 'pictographic-primitives/symbol/personal hotspot_45b73137-0503-4586-8373-394aa93d3ff8.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'personal-hotspot-sub32-resize'
    variant_of = 'personal-hotspot-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (25, 11), (16, 11))
        self.add_bezier('p1-r1-2', (16, 11), ((12, 11), (8, 17), (8, 22)))
        self.add_bezier('p1-r1-3', (8, 22), ((8, 22), (8, 24), (8, 25)))
        self.add_bezier('p1-r1-4', (8, 25), ((10, 29), (14, 30), (17, 30)))
        self.add_bezier('p1-r1-5', (17, 30), ((17, 30), (17, 30), (17, 30)))
        self.add_bezier('p1-r1-6', (17, 30), ((17, 30), (17, 30), (17, 30)))
        self.add_bezier('p1-r1-7', (17, 30), ((17, 30), (17, 30), (17, 30)))
        self.add_line('p1-r1-8', (17, 30), (28, 30))
        self.add_bezier('p1-r1-9', (28, 30), ((28, 30), (28, 30), (28, 30)))
        self.add_bezier('p1-r1-10', (28, 30), ((32, 30), (35, 30), (37, 26)))
        self.add_bezier('p1-r1-11', (37, 26), ((38, 25), (38, 24), (38, 24)))
        self.add_bezier('p1-r1-12', (38, 24), ((38, 24), (38, 24), (38, 24)))
        self.add_bezier('p1-r1-13', (38, 24), ((38, 22), (38, 21), (38, 20)))
        self.add_bezier('p2-r1-1', (2, 13), ((2, 12), (2, 11), (2, 10)))
        self.add_bezier('p2-r1-2', (2, 10), ((2, 10), (2, 8), (2, 8)))
        self.add_bezier('p2-r1-3', (2, 8), ((5, 5), (8, 2), (11, 2)))
        self.add_bezier('p2-r1-4', (11, 2), ((12, 2), (12, 2), (12, 2)))
        self.add_line('p2-r1-5', (12, 2), (25, 2))
        self.add_bezier('p2-r1-6', (25, 2), ((25, 2), (25, 2), (25, 2)))
        self.add_bezier('p2-r1-7', (25, 2), ((26, 2), (28, 2), (29, 2)))
        self.add_bezier('p2-r1-8', (29, 2), ((32, 3), (33, 7), (33, 10)))
        self.add_bezier('p2-r1-9', (33, 10), ((33, 12), (32, 16), (30, 19)))
        self.add_bezier('p2-r1-10', (30, 19), ((28, 20), (25, 21), (23, 21)))
        self.add_bezier('p2-r1-11', (23, 21), ((21, 21), (20, 20), (19, 20)))
        self.add_bezier('p2-r1-12', (19, 20), ((17, 20), (17, 20), (17, 20)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
