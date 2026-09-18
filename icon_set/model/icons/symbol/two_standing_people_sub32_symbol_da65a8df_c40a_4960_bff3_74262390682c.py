"""Independent 32px profile of two-standing-people.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'da65a8df-c40a-4960-bff3-74262390682c'
SOURCE_PATH = 'pictographic-primitives/users/multiple man_da65a8df-c40a-4960-bff3-74262390682c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('da65a8df-c40a-4960-bff3-74262390682c', 'pictographic-primitives/users/multiple man_da65a8df-c40a-4960-bff3-74262390682c.svg'), ('5e8b621f-4f10-4323-943d-1337196c6e73', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_5e8b621f-4f10-4323-943d-1337196c6e73.svg'))
PROFILE_SOURCE_KEYS = ('solo/two-standing-people',)
SOLO_SOURCE_ICON_IDS = ('two-standing-people',)
REFERENCE_EXPORT_SHA256 = 'cbfb479fbf96c0aac0266d16da300e7cd0c1ee99857f525854f0148da8cbde69'

class DrawingContainerSymbol(Sub32):
    icon_id = 'two-standing-people-sub32-symbol'
    related_origin_icon_id = 'two-standing-people-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/two-standing-people-sub32'
    counterpart_icon_id = 'two-standing-people-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'people/groups'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (8, 2), (8, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (8, 9), (8, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (5, 20), (12, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (12, 20), (12, 22))
        self.add_line('p2-r1-3', (12, 22), (11, 22))
        self.add_line('p2-r1-4', (11, 22), (11, 30))
        self.add_line('p2-r1-5', (11, 30), (6, 30))
        self.add_line('p2-r1-6', (6, 30), (6, 22))
        self.add_line('p2-r1-7', (6, 22), (5, 22))
        self.add_line('p2-r1-8', (5, 22), (5, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_arc('p3-r1-1', (24, 2), (24, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (24, 9), (24, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (20, 20), (27, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p4-r1-2', (27, 20), (27, 22))
        self.add_line('p4-r1-3', (27, 22), (26, 22))
        self.add_line('p4-r1-4', (26, 22), (26, 30))
        self.add_line('p4-r1-5', (26, 30), (21, 30))
        self.add_line('p4-r1-6', (21, 30), (21, 22))
        self.add_line('p4-r1-7', (21, 22), (20, 22))
        self.add_line('p4-r1-8', (20, 22), (20, 20))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', 'p4-r1-8', closed=False)
