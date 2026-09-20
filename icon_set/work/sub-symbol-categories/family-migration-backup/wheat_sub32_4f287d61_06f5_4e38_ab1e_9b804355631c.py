"""Independent 32px profile of wheat.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4f287d61-06f5-4e38-ab1e-9b804355631c'
SOURCE_PATH = 'pictographic-primitives/farming/wheat_4f287d61-06f5-4e38-ab1e-9b804355631c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4f287d61-06f5-4e38-ab1e-9b804355631c', 'pictographic-primitives/farming/wheat_4f287d61-06f5-4e38-ab1e-9b804355631c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wheat',)
SOLO_SOURCE_ICON_IDS = ('wheat',)
REFERENCE_EXPORT_SHA256 = '5f003436f0f4287152741bafb32070ce0dc94632a9ed3c73c092a904aa7df8f1'

class Drawing(Sub32):
    icon_id = 'wheat-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'farming'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((19, 4), (22, 4), (22, 8)))
        self.add_bezier('p1-r1-2', (22, 8), ((22, 11), (19, 12), (16, 13)))
        self.add_bezier('p1-r1-3', (16, 13), ((13, 13), (10, 11), (10, 8)))
        self.add_bezier('p1-r1-4', (10, 8), ((10, 4), (13, 4), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 13), (16, 23))
        self.add_line('p2-r1-2', (16, 23), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (16, 23), ((15, 20), (9, 18), (5, 18)))
        self.add_bezier('p3-r1-2', (5, 18), ((5, 22), (8, 24), (12, 24)))
        self.add_bezier('p3-r1-3', (12, 24), ((13, 24), (15, 23), (16, 23)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_bezier('p4-r1-1', (16, 23), ((17, 20), (23, 18), (27, 18)))
        self.add_bezier('p4-r1-2', (27, 18), ((27, 22), (24, 24), (20, 24)))
        self.add_bezier('p4-r1-3', (20, 24), ((19, 24), (17, 23), (16, 23)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-3')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-3')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-3')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-3')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-3')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-3')
