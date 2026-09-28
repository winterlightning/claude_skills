"""Independent 32px profile of minimal-happy-smiling-face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b3826549-0cc8-4855-a250-66873df772a9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/smiley face_b3826549-0cc8-4855-a250-66873df772a9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b3826549-0cc8-4855-a250-66873df772a9', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/smiley face_b3826549-0cc8-4855-a250-66873df772a9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/minimal-happy-smiling-face',)
SOLO_SOURCE_ICON_IDS = ('minimal-happy-smiling-face',)
REFERENCE_EXPORT_SHA256 = '3bee79d60a346ba5e12de7361ec5caa40d4e1ef3664872889cbfcdaa893cb4b1'

class Drawing(Sub32):
    icon_id = 'minimal-happy-smiling-face-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 5), (8, 9))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (24, 5), (24, 9))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 17), (30, 17), radius_x=14, radius_y=10, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
