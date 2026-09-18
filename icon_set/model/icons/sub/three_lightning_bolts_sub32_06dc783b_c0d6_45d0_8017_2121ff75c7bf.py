"""Independent 32px profile of three-lightning-bolts-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '06dc783b-c0d6-45d0-8017-2121ff75c7bf'
SOURCE_PATH = 'pictographic-primitives/state/thunder heavy_06dc783b-c0d6-45d0-8017-2121ff75c7bf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('06dc783b-c0d6-45d0-8017-2121ff75c7bf', 'pictographic-primitives/state/thunder heavy_06dc783b-c0d6-45d0-8017-2121ff75c7bf.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-lightning-bolts-solo',)
SOLO_SOURCE_ICON_IDS = ('three-lightning-bolts-solo',)
REFERENCE_EXPORT_SHA256 = '5dde48edd89c3fc235d34bb3eddd75ceb154bf98c751b8187c1dcc74ea221f44'

class Drawing(Sub32):
    icon_id = 'three-lightning-bolts-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 5), (2, 14))
        self.add_line('p1-r1-2', (2, 14), (6, 17))
        self.add_line('p1-r1-3', (6, 17), (2, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (18, 5), (14, 14))
        self.add_line('p2-r1-2', (14, 14), (18, 17))
        self.add_line('p2-r1-3', (18, 17), (14, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (30, 5), (26, 14))
        self.add_line('p3-r1-2', (26, 14), (30, 17))
        self.add_line('p3-r1-3', (30, 17), (26, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
