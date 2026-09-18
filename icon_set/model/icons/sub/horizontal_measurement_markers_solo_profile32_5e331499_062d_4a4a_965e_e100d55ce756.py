"""Independent 32px profile of horizontal-measurement-markers-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5e331499-062d-4a4a-965e-e100d55ce756'
SOURCE_PATH = 'pictographic-primitives/other/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e331499-062d-4a4a-965e-e100d55ce756', 'pictographic-primitives/other/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'),)
PROFILE_SOURCE_KEYS = ('solo/horizontal-measurement-markers-solo',)
SOLO_SOURCE_ICON_IDS = ('horizontal-measurement-markers-solo',)
REFERENCE_EXPORT_SHA256 = 'e71307bcdc77a23c7b2c24c8a93d0e80f3ffe320abc3f1b400a7342ab2ce03d8'

class Drawing(Sub32):
    icon_id = 'horizontal-measurement-markers-solo-profile32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 5), (11, 5))
        self.add_line('p1-r1-2', (11, 5), (8, 10))
        self.add_line('p1-r1-3', (8, 10), (2, 10))
        self.add_line('p1-r1-4', (2, 10), (2, 5))
        self.add_line('p1-r1-5', (2, 5), (11, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (30, 27), (30, 22))
        self.add_line('p2-r1-2', (30, 22), (11, 22))
        self.add_line('p2-r1-3', (11, 22), (8, 16))
        self.add_line('p2-r1-4', (8, 16), (2, 16))
        self.add_line('p2-r1-5', (2, 16), (2, 22))
        self.add_line('p2-r1-6', (2, 22), (11, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (21, 16), (30, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
