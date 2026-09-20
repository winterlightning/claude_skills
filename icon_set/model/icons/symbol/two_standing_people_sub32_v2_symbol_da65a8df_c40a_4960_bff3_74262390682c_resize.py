"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'da65a8df-c40a-4960-bff3-74262390682c'
SOURCE_PATH = 'icon_set/model/icons/symbol/two_standing_people_sub32_v2_symbol_da65a8df_c40a_4960_bff3_74262390682c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'da06c75e71037d9277d8792799f5a077030ea7b267d779dfa9e898e0615c6824'
SOURCE_REFERENCES = (('da65a8df-c40a-4960-bff3-74262390682c', 'pictographic-primitives/users/multiple man_da65a8df-c40a-4960-bff3-74262390682c.svg'), ('5e8b621f-4f10-4323-943d-1337196c6e73', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_5e8b621f-4f10-4323-943d-1337196c6e73.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'two-standing-people-sub32-v2-symbol-resize'
    variant_of = 'two-standing-people-sub32-v2-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('head-0-a', (3, 3), ((3, 3), (4, 3), (4, 2)), ((5, 2), (5, 2), (5, 2)), ((6, 2), (6, 2), (7, 2)), ((7, 3), (8, 3), (8, 3)))
        self.add_bezier('head-0-b', (8, 3), ((8, 4), (7, 4), (7, 5)), ((6, 5), (6, 5), (6, 5)), ((5, 5), (5, 5), (4, 5)), ((4, 4), (3, 4), (3, 3)))
        self.add_line('torso-0', (6, 12), (6, 18))
        self.add_line('arms-0', (2, 12), (9, 12))
        self.add_line('legs-0-1', (3, 22), (6, 18))
        self.add_line('legs-0-2', (6, 18), (8, 22))
        self.add_bezier('head-1-a', (16, 3), ((16, 3), (17, 3), (17, 2)), ((18, 2), (18, 2), (18, 2)), ((19, 2), (19, 2), (20, 2)), ((20, 3), (21, 3), (21, 3)))
        self.add_bezier('head-1-b', (21, 3), ((21, 4), (20, 4), (20, 5)), ((19, 5), (19, 5), (18, 5)), ((18, 5), (18, 5), (17, 5)), ((17, 4), (16, 4), (16, 3)))
        self.add_line('torso-1', (18, 12), (18, 18))
        self.add_line('arms-1', (15, 12), (22, 12))
        self.add_line('legs-1-1', (16, 22), (18, 18))
        self.add_line('legs-1-2', (18, 18), (21, 22))
        self.add_contour('head-0', 'head-0-a', 'head-0-b', closed=True)
        self.add_contour('legs-0', 'legs-0-1', 'legs-0-2', closed=False)
        self.add_contour('head-1', 'head-1-a', 'head-1-b', closed=True)
        self.add_contour('legs-1', 'legs-1-1', 'legs-1-2', closed=False)
        self.relate('connect', 'torso-0', 'arms-0')
        self.relate('connect', 'torso-0', 'legs-0')
        self.relate('connect', 'torso-1', 'arms-1')
        self.relate('connect', 'torso-1', 'legs-1')
