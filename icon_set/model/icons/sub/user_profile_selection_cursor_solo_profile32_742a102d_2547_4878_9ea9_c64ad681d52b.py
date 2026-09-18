"""Independent 32px profile of user-profile-selection-cursor-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '742a102d-2547-4878-9ea9-c64ad681d52b'
SOURCE_PATH = 'pictographic-primitives/other/cursor head_742a102d-2547-4878-9ea9-c64ad681d52b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('742a102d-2547-4878-9ea9-c64ad681d52b', 'pictographic-primitives/other/cursor head_742a102d-2547-4878-9ea9-c64ad681d52b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/user-profile-selection-cursor-solo',)
SOLO_SOURCE_ICON_IDS = ('user-profile-selection-cursor-solo',)
REFERENCE_EXPORT_SHA256 = 'bc3f3f367b641f5add882cfef713d7fd0ac4bb34d099939cf15333f1ab3625f5'

class Drawing(Sub32):
    icon_id = 'user-profile-selection-cursor-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (12, 22), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (18, 17), (30, 23))
        self.add_line('p2-r1-2', (30, 23), (25, 25))
        self.add_line('p2-r1-3', (25, 25), (22, 30))
        self.add_line('p2-r1-4', (22, 30), (18, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
