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
        # User avatar: head above rounded shoulders, 4 units apart.
        self.add_arc('head-1', (11, 7), (21, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-2', (21, 7), (11, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('s-1', (4, 30), (4, 28))
        self.add_arc('s-2', (4, 28), (12, 20), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('s-3', (12, 20), (20, 20))
        self.add_arc('s-4', (20, 20), (28, 28), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('s-5', (28, 28), (28, 30))
        self.add_contour('shoulders', 's-1', 's-2', 's-3', 's-4', 's-5')
