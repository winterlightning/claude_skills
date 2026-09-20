"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '487f3a05-de28-44cf-9e49-3130e24b6363'
SOURCE_PATH = 'icon_set/model/icons/symbol/seven_lobed_cannabis_leaf_sub32_487f3a05_de28_44cf_9e49_3130e24b6363.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4025d8f5b51d47948a6a7de79fd9ad846d681e0a519f50fc6b8d6edb5e919ba9'
SOURCE_REFERENCES = (('487f3a05-de28-44cf-9e49-3130e24b6363', 'pictographic-primitives/cannabis/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg'), ('8a80ee4f-5c0f-47e3-8f69-d4a34318a6b1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/cannabis/cannabis_8a80ee4f-5c0f-47e3-8f69-d4a34318a6b1.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'seven-lobed-cannabis-leaf-sub32-resize'
    variant_of = 'seven-lobed-cannabis-leaf-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'cannabis'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (12, 2), ((13, 5), (14, 6), (14, 8)))
        self.add_bezier('p1-r1-2', (14, 8), ((14, 8), (14, 9), (14, 10)))
        self.add_bezier('p1-r1-3', (14, 10), ((16, 8), (18, 6), (21, 6)))
        self.add_bezier('p1-r1-4', (21, 6), ((21, 9), (18, 11), (16, 12)))
        self.add_bezier('p1-r1-5', (16, 12), ((17, 12), (17, 12), (17, 12)))
        self.add_bezier('p1-r1-6', (17, 12), ((19, 12), (21, 13), (22, 14)))
        self.add_bezier('p1-r1-7', (22, 14), ((21, 16), (20, 17), (18, 17)))
        self.add_bezier('p1-r1-8', (18, 17), ((18, 17), (17, 16), (16, 16)))
        self.add_bezier('p1-r1-9', (16, 16), ((18, 18), (18, 21), (18, 21)))
        self.add_bezier('p1-r1-10', (18, 21), ((16, 21), (13, 21), (12, 19)))
        self.add_bezier('p1-r1-11', (12, 19), ((11, 21), (8, 21), (6, 21)))
        self.add_bezier('p1-r1-12', (6, 21), ((6, 21), (6, 18), (8, 16)))
        self.add_bezier('p1-r1-13', (8, 16), ((7, 16), (6, 17), (6, 17)))
        self.add_bezier('p1-r1-14', (6, 17), ((4, 17), (3, 16), (2, 14)))
        self.add_bezier('p1-r1-15', (2, 14), ((3, 13), (5, 12), (7, 12)))
        self.add_bezier('p1-r1-16', (7, 12), ((7, 12), (7, 12), (8, 12)))
        self.add_bezier('p1-r1-17', (8, 12), ((6, 11), (3, 9), (3, 6)))
        self.add_bezier('p1-r1-18', (3, 6), ((6, 6), (8, 8), (10, 10)))
        self.add_bezier('p1-r1-19', (10, 10), ((10, 9), (10, 8), (10, 8)))
        self.add_bezier('p1-r1-20', (10, 8), ((10, 6), (11, 5), (12, 2)))
        self.add_line('p2-r1-1', (12, 19), (12, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p1-r1-11', 'p2-r1-1')
