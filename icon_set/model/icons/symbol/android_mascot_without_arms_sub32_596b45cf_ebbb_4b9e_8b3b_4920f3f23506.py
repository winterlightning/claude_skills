"""Independent 32px profile of android-mascot-without-arms.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '596b45cf-ebbb-4b9e-8b3b-4920f3f23506'
SOURCE_PATH = 'pictographic-primitives/apps/android_596b45cf-ebbb-4b9e-8b3b-4920f3f23506.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('596b45cf-ebbb-4b9e-8b3b-4920f3f23506', 'pictographic-primitives/apps/android_596b45cf-ebbb-4b9e-8b3b-4920f3f23506.svg'), ('c737ad22-037b-47d7-883f-17a8b36a58e5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/android_c737ad22-037b-47d7-883f-17a8b36a58e5.svg'))
PROFILE_SOURCE_KEYS = ('solo/android-mascot-without-arms',)
SOLO_SOURCE_ICON_IDS = ('android-mascot-without-arms',)
REFERENCE_EXPORT_SHA256 = '9a276fa98e5b2467894aaa8d6eeb2018465f59ecb286b0248d9502dadf4d6801'

class Drawing(Sub32):
    icon_id = 'android-mascot-without-arms-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'apps'
    categories = ('apps', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Dome head 8 units tall over the eye band, body, legs and antennae.
        self.add_arc('p1-r1-1', (4, 12), (16, 4), radius_x=12, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 4), (28, 12), radius_x=12, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (28, 12), (28, 23))
        self.add_arc('p1-r1-6', (28, 23), (25, 26), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (25, 26), (22, 26))
        self.add_line('p1-r1-8', (22, 26), (10, 26))
        self.add_line('p1-r1-9', (10, 26), (7, 26))
        self.add_arc('p1-r1-10', (7, 26), (4, 23), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (4, 23), (4, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=True)
        self.add_line('p2-r1-1', (4, 12), (28, 12))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 26), (10, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 26), (22, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (10, 5), (7, 2))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (22, 5), (25, 2))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-11', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p6-r1-1')
        self.relate('connect', 'p1-r1-7', 'p4-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-8', 'p3-r1-1')
        self.relate('connect', 'p1-r1-9', 'p3-r1-1')
        self.relate('connect', 'path-1-1', 'path-5-1')
        self.relate('connect', 'path-1-1', 'path-6-1')
