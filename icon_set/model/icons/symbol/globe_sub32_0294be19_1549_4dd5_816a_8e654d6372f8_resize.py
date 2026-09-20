"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0294be19-1549-4dd5-816a-8e654d6372f8'
SOURCE_PATH = 'icon_set/model/icons/symbol/globe_sub32_0294be19_1549_4dd5_816a_8e654d6372f8.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '04e2c3bcd6e3fcb5294878d87fcf27d456f5168c9e30f8a6328ae13bd74c863a'
SOURCE_REFERENCES = (('0294be19-1549-4dd5-816a-8e654d6372f8', 'pictographic-primitives/symbol/globe_0294be19-1549-4dd5-816a-8e654d6372f8.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'globe-sub32-resize'
    variant_of = 'globe-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (12, 2), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 12), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (12, 22), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (2, 12), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (12, 2), (7, 12), radius_x=5, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p2-r1-2', (7, 12), (12, 22), radius_x=5, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (12, 22), (17, 12), radius_x=5, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p2-r1-4', (17, 12), (12, 2), radius_x=5, radius_y=10, large_arc=False, sweep=False)
        self.add_line('p3-r1-1', (2, 12), (7, 12))
        self.add_line('p3-r1-2', (7, 12), (17, 12))
        self.add_line('p3-r1-3', (17, 12), (22, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p1-r1-1', 'p3-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p3-r1-3')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p2-r1-3', 'p3-r1-2')
        self.relate('connect', 'p2-r1-3', 'p3-r1-3')
        self.relate('connect', 'p2-r1-4', 'p3-r1-2')
        self.relate('connect', 'p2-r1-4', 'p3-r1-3')
