# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of two-people-figures.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ef9a5734-bb37-4ba6-8059-d08bad5b0f51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/couple_ef9a5734-bb37-4ba6-8059-d08bad5b0f51.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef9a5734-bb37-4ba6-8059-d08bad5b0f51', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/couple_ef9a5734-bb37-4ba6-8059-d08bad5b0f51.svg'), ('bacf1dca-6143-4371-a879-10b3112e2203', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_bacf1dca-6143-4371-a879-10b3112e2203.svg'))
PROFILE_SOURCE_KEYS = ('solo/two-people-figures', 'solo/two-person-user-group')
SOLO_SOURCE_ICON_IDS = ('two-people-figures', 'two-person-user-group')
REFERENCE_EXPORT_SHA256 = '920bc3d7d7d9c7f6d2eb3d4c71201a2257f490ab8dc99438fdd9063da4d4c306'

class DrawingContainerSymbol(Sub32):
    icon_id = 'two-people-figures-sub32-symbol'
    variant_of = 'two-people-figures-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/two-people-figures-sub32'
    counterpart_icon_id = 'two-people-figures-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 9), (8, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (8, 6), (10, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (10, 9), (8, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (8, 12), (5, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 26), (2, 20))
        self.add_arc('p2-r1-2', (2, 20), (13, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (13, 20), (13, 26))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (22, 9), (24, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (24, 6), (27, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (27, 9), (24, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (24, 12), (22, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (19, 26), (19, 20))
        self.add_arc('p4-r1-2', (19, 20), (30, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p4-r1-3', (30, 20), (30, 26))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
