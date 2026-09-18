"""Independent 32px profile of circle-heartbeat-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e2fc54fd-f508-44e9-8bfb-11dee5fb3a31'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/e2fc54fd-f508-44e9-8bfb-11dee5fb3a31.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2fc54fd-f508-44e9-8bfb-11dee5fb3a31', 'icon_set/dist/gallery/combination-originals/e2fc54fd-f508-44e9-8bfb-11dee5fb3a31.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-heartbeat-content',)
SOLO_SOURCE_ICON_IDS = ('circle-heartbeat-content',)
REFERENCE_EXPORT_SHA256 = '4df61d9193ad2cbb29b44ee54a4695cea7f73d9f152e1b03d403b45fd31a0237'

class Drawing(Sub32):
    icon_id = 'circle-heartbeat-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (8, 16), (12, 16))
        self.add_line('p2-r1-2', (12, 16), (15, 10))
        self.add_line('p2-r1-3', (15, 10), (18, 22))
        self.add_line('p2-r1-4', (18, 22), (21, 16))
        self.add_line('p2-r1-5', (21, 16), (24, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
