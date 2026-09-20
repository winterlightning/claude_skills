"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '144220e1-741d-429f-9845-957359566973'
SOURCE_PATH = 'icon_set/model/icons/symbol/lgbt_heart_sub32_symbol_144220e1_741d_429f_9845_957359566973.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '00bf5858cdb4c12d5664f93cbd5044d808357f9e881bc4f86e7e86cbab1ba37f'
SOURCE_REFERENCES = (('144220e1-741d-429f-9845-957359566973', 'pictographic-primitives/symbol/lgbt heart_144220e1-741d-429f-9845-957359566973.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'lgbt-heart-sub32-symbol-resize'
    variant_of = 'lgbt-heart-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (12, 5), ((11, 3), (9, 2), (7, 2)))
        self.add_arc('p1-r1-2', (7, 2), (2, 8), radius_x=5, radius_y=6, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-3', (2, 8), ((2, 9), (3, 11), (5, 12)))
        self.add_line('p1-r1-4', (5, 12), (12, 18))
        self.add_line('p1-r1-5', (12, 18), (19, 12))
        self.add_bezier('p1-r1-6', (19, 12), ((21, 11), (22, 9), (22, 8)))
        self.add_arc('p1-r1-7', (22, 8), (17, 2), radius_x=5, radius_y=6, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-8', (17, 2), ((15, 2), (13, 3), (12, 5)))
        self.add_line('p2-r1-1', (2, 8), (22, 8))
        self.add_line('p3-r1-1', (5, 12), (19, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
