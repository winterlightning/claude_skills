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
    category = 'users'
    categories = ('users', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Two standing people: dot heads over rounded 8-unit bodies.
        self.add_arc('head-l-1', (6, 4), (10, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-l-2', (10, 4), (6, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head-l', 'head-l-1', 'head-l-2', closed=True)
        self.add_arc('head-r-1', (22, 4), (26, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-r-2', (26, 4), (22, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head-r', 'head-r-1', 'head-r-2', closed=True)
        self.add_line('l-1', (4, 30), (4, 18))
        self.add_arc('l-2', (4, 18), (12, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('l-3', (12, 18), (12, 30))
        self.add_contour('body-l', 'l-1', 'l-2', 'l-3')
        self.add_line('r-1', (20, 30), (20, 18))
        self.add_arc('r-2', (20, 18), (28, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('r-3', (28, 18), (28, 30))
        self.add_contour('body-r', 'r-1', 'r-2', 'r-3')
