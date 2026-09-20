"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2234e12a-05f0-48de-ba27-d943238ccfaa'
SOURCE_PATH = 'icon_set/model/icons/symbol/user_avatar_sub32_2234e12a_05f0_48de_ba27_d943238ccfaa.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c287ae399fc719002d0508ee0fccbcdad9d7873d8b533a9dc99faecf88e6157c'
SOURCE_REFERENCES = ((None, 'icon_set/references/human_ref/user.svg'), ('2234e12a-05f0-48de-ba27-d943238ccfaa', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person_2234e12a-05f0-48de-ba27-d943238ccfaa.svg'), ('55606b28-310c-4be8-8fcb-e228f769d500', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person_55606b28-310c-4be8-8fcb-e228f769d500.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'user-avatar-sub32-resize'
    variant_of = 'user-avatar-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'avatars'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (10, 2), (14, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (14, 6), (10, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (10, 10), (6, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (6, 6), (10, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 22), (2, 18))
        self.add_arc('p2-r1-2', (2, 18), (8, 12), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (8, 12), (12, 12))
        self.add_arc('p2-r1-4', (12, 12), (18, 18), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (18, 18), (18, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
