# Variant of state32-ce80faa0-dd47-4d1a-9ecb-fb349333dde8; parent file remains unchanged.
"""Independent 32px profile of state32-ce80faa0-dd47-4d1a-9ecb-fb349333dde8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ce80faa0-dd47-4d1a-9ecb-fb349333dde8'
SOURCE_PATH = 'icon_set/assets/combination-state32/ce80faa0-dd47-4d1a-9ecb-fb349333dde8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ce80faa0-dd47-4d1a-9ecb-fb349333dde8', 'icon_set/assets/combination-state32/ce80faa0-dd47-4d1a-9ecb-fb349333dde8.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '915ffab8ead313a6bc74b5dd5c1fe12f80234e42bdda65045985b98d302c9722'

class DrawingVariant2(Sub32):
    icon_id = 'state32-ce80faa0-dd47-4d1a-9ecb-fb349333dde8-v2'
    variant_label = 'Open the thumb gap and smooth the rounded fingertip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (24, 2), (21, 4))
        self.add_bezier('p1-r1-2', (21, 4), ((20.333333333333332, 5.333333333333333), (19.333333333333332, 6), (18, 6)))
        self.add_bezier('p1-r1-3', (18, 6), ((17.333333333333332, 6), (16.333333333333332, 5.666666666666667), (15, 5)))
        self.add_bezier('p1-r1-4', (15, 5), ((14.333333333333334, 5), (13.666666666666666, 5), (13, 5)))
        self.add_bezier('p1-r1-5', (13, 5), ((11, 5), (8.666666666666666, 6), (6, 8)))
        self.add_line('p1-r1-6', (6, 8), (3, 11))
        self.add_bezier('p1-r1-7', (3,11), ((2,12),(2,13),(2,14)))
        self.add_bezier('p1-r1-8', (2,14), ((2,16),(2,18),(4,17)))
        self.add_line('p1-r1-9', (4, 17), (12, 13))
        self.add_line('p1-r1-10', (12, 13), (6, 25))
        self.add_bezier('p1-r1-11', (6, 25), ((5.333333333333333, 25.666666666666668), (5, 26.333333333333332), (5, 27)))
        self.add_bezier('p1-r1-12', (5, 27), ((5, 29), (6.666666666666667, 30), (10, 30)))
        self.add_line('p1-r1-13', (10, 30), (16, 30))
        self.add_line('p1-r1-14', (16, 30), (25, 14))
        self.add_line('p1-r1-15', (25, 14), (30, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', closed=False)
