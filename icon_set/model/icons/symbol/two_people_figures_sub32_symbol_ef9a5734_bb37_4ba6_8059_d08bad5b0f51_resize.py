"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'ef9a5734-bb37-4ba6-8059-d08bad5b0f51'
SOURCE_PATH = 'icon_set/model/icons/symbol/two_people_figures_sub32_symbol_ef9a5734_bb37_4ba6_8059_d08bad5b0f51.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4949f238e3f6155d2d31c3dfbb6e2d964dc119d7e409b1be1bb9f29c594793c9'
SOURCE_REFERENCES = (('ef9a5734-bb37-4ba6-8059-d08bad5b0f51', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/couple_ef9a5734-bb37-4ba6-8059-d08bad5b0f51.svg'), ('bacf1dca-6143-4371-a879-10b3112e2203', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_bacf1dca-6143-4371-a879-10b3112e2203.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'two-people-figures-sub32-symbol-resize'
    variant_of = 'two-people-figures-sub32-symbol'
    variant_label = 'Resize 24 × 18'
    canvas_width = 24
    canvas_height = 18
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (4, 4), (6, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (6, 2), (8, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (8, 4), (6, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (6, 6), (4, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 16), (2, 12))
        self.add_arc('p2-r1-2', (2, 12), (10, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (10, 12), (10, 16))
        self.add_arc('p3-r1-1', (16, 4), (18, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (18, 2), (20, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (20, 4), (18, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (18, 6), (16, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p4-r1-1', (14, 16), (14, 12))
        self.add_arc('p4-r1-2', (14, 12), (22, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p4-r1-3', (22, 12), (22, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
