"""Independent 32px profile of remove-user-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'cfe24e77-2c14-441c-9e16-a3507e8a0079'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/cfe24e77-2c14-441c-9e16-a3507e8a0079.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cfe24e77-2c14-441c-9e16-a3507e8a0079', 'icon_set/dist/gallery/combination-originals/cfe24e77-2c14-441c-9e16-a3507e8a0079.svg'),)
PROFILE_SOURCE_KEYS = ('solo/remove-user-content',)
SOLO_SOURCE_ICON_IDS = ('remove-user-content',)
REFERENCE_EXPORT_SHA256 = 'c2d2ed8e71048aa9086be68d89f8e85edabafe056046b19f4017f37bb9d120b0'

class Drawing(Sub32):
    icon_id = 'remove-user-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (8, 9), (16, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 9), (8, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 27), (22, 27), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 9), (30, 9))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
