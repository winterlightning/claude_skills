"""Independent 32px profile of user-avatar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2234e12a-05f0-48de-ba27-d943238ccfaa'
SOURCE_PATH = 'icon_set/references/human_ref/user.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ((None, 'icon_set/references/human_ref/user.svg'), ('2234e12a-05f0-48de-ba27-d943238ccfaa', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person_2234e12a-05f0-48de-ba27-d943238ccfaa.svg'), ('55606b28-310c-4be8-8fcb-e228f769d500', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person_55606b28-310c-4be8-8fcb-e228f769d500.svg'))
PROFILE_SOURCE_KEYS = ('solo/user-avatar',)
SOLO_SOURCE_ICON_IDS = ('user-avatar',)
REFERENCE_EXPORT_SHA256 = '1e217bdd8f1cf769f4eb6817eff6244a8546d81d04761a6b88900ea5a93e90be'

class Drawing(Sub32):
    icon_id = 'user-avatar-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 8), (16, 13), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 13), (10, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (10, 8), (16, 2), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (5, 30), (5, 24))
        self.add_arc('p2-r1-2', (5, 24), (13, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (13, 16), (19, 16))
        self.add_arc('p2-r1-4', (19, 16), (27, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (27, 24), (27, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
