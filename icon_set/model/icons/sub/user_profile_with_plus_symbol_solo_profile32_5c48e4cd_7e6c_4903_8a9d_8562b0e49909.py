"""Independent 32px profile of user-profile-with-plus-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5c48e4cd-7e6c-4903-8a9d-8562b0e49909'
SOURCE_PATH = 'pictographic-primitives/other/doctor_5c48e4cd-7e6c-4903-8a9d-8562b0e49909.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5c48e4cd-7e6c-4903-8a9d-8562b0e49909', 'pictographic-primitives/other/doctor_5c48e4cd-7e6c-4903-8a9d-8562b0e49909.svg'),)
PROFILE_SOURCE_KEYS = ('solo/user-profile-with-plus-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('user-profile-with-plus-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '4f7bb313309b9583c1e9623fba4d8e56c0a25d7fb79e80859cf9a17af233ddcd'

class Drawing(Sub32):
    icon_id = 'user-profile-with-plus-symbol-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 8), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 8), (10, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 30), (30, 30), radius_x=14, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (11, 27), (16, 27))
        self.add_line('p3-r1-2', (16, 27), (21, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 25), (16, 27))
        self.add_line('p4-r1-2', (16, 27), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-2')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-2')
