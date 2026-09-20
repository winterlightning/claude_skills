"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'bb0c2575-3757-4901-bb6b-1d9b04b3a433'
SOURCE_PATH = 'icon_set/model/icons/symbol/skull_with_crossed_bones_sub32_bb0c2575_3757_4901_bb6b_1d9b04b3a433.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '26fc07a2b81e5b6beffb4670d0870fe4c3f56be2bc17c0e655dec31608fa7893'
SOURCE_REFERENCES = (('bb0c2575-3757-4901-bb6b-1d9b04b3a433', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/skull_bb0c2575-3757-4901-bb6b-1d9b04b3a433.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'skull-with-crossed-bones-sub32-resize'
    variant_of = 'skull-with-crossed-bones-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (6, 6), ((8, 5), (10, 4), (12, 4)))
        self.add_bezier('p1-r1-2', (12, 4), ((14, 4), (16, 5), (18, 6)))
        self.add_bezier('p1-r1-3', (18, 6), ((18, 8), (19, 10), (19, 12)))
        self.add_bezier('p1-r1-4', (19, 12), ((19, 13), (18, 16), (16, 16)))
        self.add_line('p1-r1-5', (16, 16), (16, 20))
        self.add_line('p1-r1-6', (16, 20), (12, 20))
        self.add_line('p1-r1-7', (12, 20), (8, 20))
        self.add_line('p1-r1-8', (8, 20), (8, 16))
        self.add_bezier('p1-r1-9', (8, 16), ((6, 16), (4, 13), (4, 12)))
        self.add_bezier('p1-r1-10', (4, 12), ((4, 10), (6, 8), (6, 6)))
        self.add_line('p2-r1-1', (9, 11), (9, 11))
        self.add_line('p3-r1-1', (6, 6), (2, 2))
        self.add_line('p4-r1-1', (8, 16), (2, 22))
        self.add_line('p5-r1-1', (15, 11), (15, 11))
        self.add_line('p6-r1-1', (18, 6), (22, 2))
        self.add_line('p7-r1-1', (16, 16), (22, 22))
        self.add_line('p8-r1-1', (12, 16), (12, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p6-r1-1')
        self.relate('connect', 'p1-r1-3', 'p6-r1-1')
        self.relate('connect', 'p1-r1-4', 'p7-r1-1')
        self.relate('connect', 'p1-r1-5', 'p7-r1-1')
        self.relate('connect', 'p1-r1-6', 'p8-r1-1')
        self.relate('connect', 'p1-r1-7', 'p8-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-9', 'p4-r1-1')
        self.relate('connect', 'p1-r1-10', 'p3-r1-1')
