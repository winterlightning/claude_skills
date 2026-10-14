"""Independent 32px profile of user-with-id-card-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '91136439-ae9e-4bd7-833a-71e612217d7c'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/91136439-ae9e-4bd7-833a-71e612217d7c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('91136439-ae9e-4bd7-833a-71e612217d7c', 'icon_set/dist/gallery/combination-originals/91136439-ae9e-4bd7-833a-71e612217d7c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/user-with-id-card-content',)
SOLO_SOURCE_ICON_IDS = ('user-with-id-card-content',)
REFERENCE_EXPORT_SHA256 = '9abf66accaa0f3a182e5efc89e23f0f0feafcb6facd83189e443ac6f0b344fd7'

class Drawing(Sub32):
    icon_id = 'user-with-id-card-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (6, 8), (14, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (14, 8), (6, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 28), (18, 28), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 4), (30, 4))
        self.add_line('p3-r1-2', (30, 4), (30, 12))
        self.add_line('p3-r1-3', (30, 12), (22, 12))
        self.add_line('p3-r1-4', (22, 12), (22, 4))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
