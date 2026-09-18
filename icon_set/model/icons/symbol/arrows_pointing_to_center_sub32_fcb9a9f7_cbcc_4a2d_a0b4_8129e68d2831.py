"""Independent 32px profile of arrows-pointing-to-center.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'fcb9a9f7-cbcc-4a2d-a0b4-8129e68d2831'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows pointing to center_fcb9a9f7-cbcc-4a2d-a0b4-8129e68d2831.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fcb9a9f7-cbcc-4a2d-a0b4-8129e68d2831', 'pictographic-primitives/symbol/arrows pointing to center_fcb9a9f7-cbcc-4a2d-a0b4-8129e68d2831.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrows-pointing-to-center',)
SOLO_SOURCE_ICON_IDS = ('arrows-pointing-to-center',)
REFERENCE_EXPORT_SHA256 = '9ec433d905c38ca18ca02090d5b838ea1f895b7ee6754ad57514781731f01669'

class Drawing(Sub32):
    icon_id = 'arrows-pointing-to-center-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (11, 11))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (5, 11), (11, 11))
        self.add_line('p2-r1-2', (11, 11), (11, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (30, 2), (21, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27, 11), (21, 11))
        self.add_line('p4-r1-2', (21, 11), (21, 5))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 30), (11, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (5, 21), (11, 21))
        self.add_line('p6-r1-2', (11, 21), (11, 27))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (30, 30), (21, 21))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (27, 21), (21, 21))
        self.add_line('p8-r1-2', (21, 21), (21, 27))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-2')
        self.relate('connect', 'p7-r1-1', 'p8-r1-1')
        self.relate('connect', 'p7-r1-1', 'p8-r1-2')
