"""Independent 32px profile of user-profile.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3352ce5f-f0e1-4497-86c8-0c433016cab6'
SOURCE_PATH = 'pictographic-primitives/symbol/profile_3352ce5f-f0e1-4497-86c8-0c433016cab6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3352ce5f-f0e1-4497-86c8-0c433016cab6', 'pictographic-primitives/symbol/profile_3352ce5f-f0e1-4497-86c8-0c433016cab6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/user-profile',)
SOLO_SOURCE_ICON_IDS = ('user-profile',)
REFERENCE_EXPORT_SHA256 = '8ff20e505b1112f40db5c43684fe6c3818fac4cce051ee76f31656a1c12c378c'

class Drawing(Sub32):
    icon_id = 'user-profile-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 8), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 8), (10, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (5, 30), (27, 30), radius_x=11, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
