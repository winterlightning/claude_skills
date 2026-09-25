"""Independent 32px profile of happy-face-with-closed-eyes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5ee1d8ff-a85e-4f98-8d10-414df21c0f8a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/smiley face_5ee1d8ff-a85e-4f98-8d10-414df21c0f8a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5ee1d8ff-a85e-4f98-8d10-414df21c0f8a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/smiley face_5ee1d8ff-a85e-4f98-8d10-414df21c0f8a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/happy-face-with-closed-eyes',)
SOLO_SOURCE_ICON_IDS = ('happy-face-with-closed-eyes',)
REFERENCE_EXPORT_SHA256 = 'f342d95f382c1d2c7c093baf9b1b4b0ae2139ca4e881ef3e6c111787ca8de4ae'

class Drawing(Sub32):
    icon_id = 'happy-face-with-closed-eyes-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 8), (11, 8), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (21, 8), (30, 8), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (4, 19), (28, 19), radius_x=12, radius_y=11, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
