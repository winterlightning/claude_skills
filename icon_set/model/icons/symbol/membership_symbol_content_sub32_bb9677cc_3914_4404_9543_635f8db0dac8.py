"""Independent 32px profile of membership-symbol-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bb9677cc-3914-4404-9543-635f8db0dac8'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/bb9677cc-3914-4404-9543-635f8db0dac8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bb9677cc-3914-4404-9543-635f8db0dac8', 'icon_set/dist/gallery/combination-originals/bb9677cc-3914-4404-9543-635f8db0dac8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/membership-symbol-content',)
SOLO_SOURCE_ICON_IDS = ('membership-symbol-content',)
REFERENCE_EXPORT_SHA256 = 'faa60f8b181d65b3b560ee4ebad167e4eea052ff95170c4aeb26fae3d930de4b'

class Drawing(Sub32):
    icon_id = 'membership-symbol-content-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (26, 2), (20, 2))
        self.add_arc('p1-r1-2', (20, 2), (6, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (6, 16), (20, 30), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (20, 30), (26, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (6, 16), (23, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
