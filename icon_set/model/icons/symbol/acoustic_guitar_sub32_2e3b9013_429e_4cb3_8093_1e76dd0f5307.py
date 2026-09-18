"""Independent 32px profile of acoustic-guitar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2e3b9013-429e-4cb3-8093-1e76dd0f5307'
SOURCE_PATH = 'pictographic-primitives/music/guitar_2e3b9013-429e-4cb3-8093-1e76dd0f5307.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2e3b9013-429e-4cb3-8093-1e76dd0f5307', 'pictographic-primitives/music/guitar_2e3b9013-429e-4cb3-8093-1e76dd0f5307.svg'),)
PROFILE_SOURCE_KEYS = ('solo/acoustic-guitar',)
SOLO_SOURCE_ICON_IDS = ('acoustic-guitar',)
REFERENCE_EXPORT_SHA256 = '44cd8f3f11e7c65201dedc9ad2eac3493ff48839cbeab06008c97c605f734883'

class Drawing(Sub32):
    icon_id = 'acoustic-guitar-sub32'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/music'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 10), ((13, 10), (10, 11), (10, 14)))
        self.add_bezier('p1-r1-2', (10, 14), ((10, 15), (10, 15), (10, 16)))
        self.add_bezier('p1-r1-3', (10, 16), ((11, 17), (11, 18), (11, 18)))
        self.add_bezier('p1-r1-4', (11, 18), ((11, 19), (11, 19), (10, 20)))
        self.add_bezier('p1-r1-5', (10, 20), ((9, 22), (8, 23), (8, 24)))
        self.add_bezier('p1-r1-6', (8, 24), ((8, 29), (12, 30), (16, 30)))
        self.add_bezier('p1-r1-7', (16, 30), ((20, 30), (24, 29), (24, 24)))
        self.add_bezier('p1-r1-8', (24, 24), ((24, 23), (23, 22), (22, 20)))
        self.add_bezier('p1-r1-9', (22, 20), ((21, 19), (21, 19), (21, 18)))
        self.add_bezier('p1-r1-10', (21, 18), ((21, 18), (21, 17), (22, 16)))
        self.add_bezier('p1-r1-11', (22, 16), ((22, 15), (22, 15), (22, 14)))
        self.add_bezier('p1-r1-12', (22, 14), ((22, 11), (19, 10), (16, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 2), (20, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 22), (16, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-12', 'p2-r1-1')
