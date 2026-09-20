"""Independent 32px profile of user-profile-with-selection-square-batch-033.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '074e5864-86d5-4165-aa6c-bccd7b6883f3'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/074e5864-86d5-4165-aa6c-bccd7b6883f3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('074e5864-86d5-4165-aa6c-bccd7b6883f3', 'icon_set/dist/gallery/combination-originals/074e5864-86d5-4165-aa6c-bccd7b6883f3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/user-profile-with-selection-square-batch-033',)
SOLO_SOURCE_ICON_IDS = ('user-profile-with-selection-square-batch-033',)
REFERENCE_EXPORT_SHA256 = '4205acb16f1a79fa12741378418c4470737b230cc89b4e4354707c0a5928aed1'

class Drawing(Sub32):
    icon_id = 'user-profile-with-selection-square-batch-033-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 9), (24, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 9), (16, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (10, 27), (30, 27), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 5), (8, 5))
        self.add_line('p3-r1-2', (8, 5), (8, 13))
        self.add_line('p3-r1-3', (8, 13), (2, 13))
        self.add_line('p3-r1-4', (2, 13), (2, 5))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
