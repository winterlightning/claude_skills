"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '23650838-a114-42c4-968f-13c9b79fbbd0'
SOURCE_PATH = 'icon_set/model/icons/symbol/capsule_pill_23650838_sub32_symbol_23650838_a114_42c4_968f_13c9b79fbbd0.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'e6170fd4c0b1bc76f3539b3b957e8f0bbf01b68b3f8a08a115088744c9955f5e'
SOURCE_REFERENCES = (('23650838-a114-42c4-968f-13c9b79fbbd0', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_23650838-a114-42c4-968f-13c9b79fbbd0.svg'), ('57704ac1-8756-4a8f-8e7c-b9a940937812', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_57704ac1-8756-4a8f-8e7c-b9a940937812.svg'), ('6cb102ae-38d0-4d2c-a4ad-c70db66b2436', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_6cb102ae-38d0-4d2c-a4ad-c70db66b2436.svg'), ('fc8e0c39-0672-4642-808f-efcc29625d76', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_fc8e0c39-0672-4642-808f-efcc29625d76.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'capsule-pill-23650838-sub32-symbol-resize'
    variant_of = 'capsule-pill-23650838-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/health'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (12, 4), ((14, 2), (16, 2), (18, 2)))
        self.add_bezier('p1-r1-2', (18, 2), ((18, 2), (18, 2), (18, 2)))
        self.add_bezier('p1-r1-3', (18, 2), ((21, 2), (22, 4), (22, 8)))
        self.add_bezier('p1-r1-4', (22, 8), ((22, 10), (21, 11), (20, 12)))
        self.add_line('p1-r1-5', (20, 12), (16, 16))
        self.add_line('p1-r1-6', (16, 16), (12, 20))
        self.add_bezier('p1-r1-7', (12, 20), ((10, 22), (8, 22), (6, 22)))
        self.add_bezier('p1-r1-8', (6, 22), ((3, 22), (2, 20), (2, 16)))
        self.add_bezier('p1-r1-9', (2, 16), ((2, 14), (3, 13), (4, 12)))
        self.add_line('p1-r1-10', (4, 12), (8, 8))
        self.add_line('p1-r1-11', (8, 8), (12, 4))
        self.add_line('p2-r1-1', (8, 8), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p1-r1-11', 'p2-r1-1')
