"""Independent 32px profile of two-people-figures.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ef9a5734-bb37-4ba6-8059-d08bad5b0f51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/couple_ef9a5734-bb37-4ba6-8059-d08bad5b0f51.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef9a5734-bb37-4ba6-8059-d08bad5b0f51', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/couple_ef9a5734-bb37-4ba6-8059-d08bad5b0f51.svg'), ('bacf1dca-6143-4371-a879-10b3112e2203', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_bacf1dca-6143-4371-a879-10b3112e2203.svg'))
PROFILE_SOURCE_KEYS = ('solo/two-people-figures', 'solo/two-person-user-group')
SOLO_SOURCE_ICON_IDS = ('two-people-figures', 'two-person-user-group')
REFERENCE_EXPORT_SHA256 = '920bc3d7d7d9c7f6d2eb3d4c71201a2257f490ab8dc99438fdd9063da4d4c306'

class DrawingContainerSymbol(Sub32):
    icon_id = 'two-people-figures-sub32-symbol'
    related_origin_icon_id = 'two-people-figures-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/two-people-figures-sub32'
    counterpart_icon_id = 'two-people-figures-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Two people side by side: dot heads over rounded shoulders, 4 units apart.
        self.add_arc('head-l-1', (5, 8), (9, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-l-2', (9, 8), (5, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head-l', 'head-l-1', 'head-l-2', closed=True)
        self.add_arc('head-r-1', (23, 8), (27, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-r-2', (27, 8), (23, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head-r', 'head-r-1', 'head-r-2', closed=True)
        self.add_line('l-1', (2, 26), (2, 23))
        self.add_arc('l-2', (2, 23), (12, 23), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('l-3', (12, 23), (12, 26))
        self.add_contour('body-l', 'l-1', 'l-2', 'l-3')
        self.add_line('r-1', (20, 26), (20, 23))
        self.add_arc('r-2', (20, 23), (30, 23), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('r-3', (30, 23), (30, 26))
        self.add_contour('body-r', 'r-1', 'r-2', 'r-3')
