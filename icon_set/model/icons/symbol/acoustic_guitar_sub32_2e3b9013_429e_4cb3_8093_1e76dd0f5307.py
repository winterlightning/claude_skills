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
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'music'
    categories = ('primitives', 'music')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 2), (19, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (16, 10), (10, 14), radius_x=6, radius_y=4, large_arc=False, sweep=False)
        self.add_bezier('p3-r1-2', (10, 14), ((10, 17), (6, 18), (6, 22)))
        self.add_arc('p3-r1-3', (6, 22), (16, 30), radius_x=10, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('p3-r1-4', (16, 30), (26, 22), radius_x=10, radius_y=8, large_arc=False, sweep=False)
        self.add_bezier('p3-r1-5', (26, 22), ((26, 18), (22, 17), (22, 14)))
        self.add_arc('p3-r1-6', (22, 14), (16, 10), radius_x=6, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=True)
        self.add_line('p4-r1-1', (16, 22), (16, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-6')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-4', 'p4-r1-1')
        self.relate('connect', 'p3-r1-5', 'p4-r1-1')
        self.relate('connect', 'p3-r1-6', 'p4-r1-1')
