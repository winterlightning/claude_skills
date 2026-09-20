"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'da65a8df-c40a-4960-bff3-74262390682c'
SOURCE_PATH = 'icon_set/model/icons/symbol/two_standing_people_sub32_symbol_da65a8df_c40a_4960_bff3_74262390682c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3552d6839318940c04b6ccadecdcfe65109b927d72f13fb28875e329b37f23f0'
SOURCE_REFERENCES = (('da65a8df-c40a-4960-bff3-74262390682c', 'pictographic-primitives/users/multiple man_da65a8df-c40a-4960-bff3-74262390682c.svg'), ('5e8b621f-4f10-4323-943d-1337196c6e73', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_5e8b621f-4f10-4323-943d-1337196c6e73.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'two-standing-people-sub32-symbol-resize'
    variant_of = 'two-standing-people-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'people/groups'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (4, 2), (4, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (4, 7), (4, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (2, 15), (7, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (7, 15), (7, 16))
        self.add_line('p2-r1-3', (7, 16), (6, 16))
        self.add_line('p2-r1-4', (6, 16), (6, 22))
        self.add_line('p2-r1-5', (6, 22), (3, 22))
        self.add_line('p2-r1-6', (3, 22), (3, 16))
        self.add_line('p2-r1-7', (3, 16), (2, 16))
        self.add_line('p2-r1-8', (2, 16), (2, 15))
        self.add_arc('p3-r1-1', (16, 2), (16, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (16, 7), (16, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-1', (13, 15), (18, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p4-r1-2', (18, 15), (18, 16))
        self.add_line('p4-r1-3', (18, 16), (17, 16))
        self.add_line('p4-r1-4', (17, 16), (17, 22))
        self.add_line('p4-r1-5', (17, 22), (14, 22))
        self.add_line('p4-r1-6', (14, 22), (14, 16))
        self.add_line('p4-r1-7', (14, 16), (13, 16))
        self.add_line('p4-r1-8', (13, 16), (13, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', 'p4-r1-8', closed=False)
