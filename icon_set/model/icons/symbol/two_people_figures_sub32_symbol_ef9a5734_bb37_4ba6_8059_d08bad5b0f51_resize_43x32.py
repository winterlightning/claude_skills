"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'ef9a5734-bb37-4ba6-8059-d08bad5b0f51'
SOURCE_PATH = 'icon_set/model/icons/symbol/two_people_figures_sub32_symbol_ef9a5734_bb37_4ba6_8059_d08bad5b0f51.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4949f238e3f6155d2d31c3dfbb6e2d964dc119d7e409b1be1bb9f29c594793c9'
SOURCE_REFERENCES = (('ef9a5734-bb37-4ba6-8059-d08bad5b0f51', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/couple_ef9a5734-bb37-4ba6-8059-d08bad5b0f51.svg'), ('bacf1dca-6143-4371-a879-10b3112e2203', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_bacf1dca-6143-4371-a879-10b3112e2203.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'two-people-figures-sub32-symbol-resize-43x32'
    variant_of = 'two-people-figures-sub32-symbol'
    variant_label = 'Resize 43 × 32'
    canvas_width = 43
    canvas_height = 32
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (6, 6), (10, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (10, 2), (13, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (13, 6), (10, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (10, 10), (6, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 30), (2, 22))
        self.add_arc('p2-r1-2', (2, 22), (17, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (17, 22), (17, 30))
        self.add_arc('p3-r1-1', (30, 6), (33, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (33, 2), (37, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (37, 6), (33, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (33, 10), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p4-r1-1', (26, 30), (26, 22))
        self.add_arc('p4-r1-2', (26, 22), (41, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p4-r1-3', (41, 22), (41, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
