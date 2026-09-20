"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf'
SOURCE_PATH = 'icon_set/model/icons/symbol/prohibition_sign_sub32_symbol_ea16df49_fc08_4bf0_8bb3_41d6a1fb33cf.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'cef84237d91bb2db2be1243b6a0c5ce03adab3273c781e6bad1baa9b16230e0b'
SOURCE_REFERENCES = (('ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/prohitbition_ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'prohibition-sign-sub32-symbol-resize'
    variant_of = 'prohibition-sign-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (6, 4), ((8, 3), (10, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((13, 2), (13, 2), (13, 2)))
        self.add_bezier('p1-r1-3', (13, 2), ((16, 3), (18, 4), (20, 6)))
        self.add_bezier('p1-r1-4', (20, 6), ((21, 8), (22, 10), (22, 12)))
        self.add_bezier('p1-r1-5', (22, 12), ((22, 13), (22, 13), (22, 13)))
        self.add_bezier('p1-r1-6', (22, 13), ((21, 16), (20, 18), (18, 20)))
        self.add_bezier('p1-r1-7', (18, 20), ((16, 21), (14, 22), (12, 22)))
        self.add_bezier('p1-r1-8', (12, 22), ((11, 22), (11, 22), (11, 22)))
        self.add_bezier('p1-r1-9', (11, 22), ((8, 21), (6, 20), (4, 18)))
        self.add_bezier('p1-r1-10', (4, 18), ((3, 16), (2, 14), (2, 12)))
        self.add_bezier('p1-r1-11', (2, 12), ((2, 11), (2, 11), (2, 11)))
        self.add_bezier('p1-r1-12', (2, 11), ((3, 8), (4, 6), (6, 4)))
        self.add_line('p2-r1-1', (4, 18), (20, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
