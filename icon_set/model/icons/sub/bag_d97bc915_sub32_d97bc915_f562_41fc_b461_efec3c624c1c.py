"""Independent 32px profile of bag-d97bc915.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd97bc915-f562-41fc-b461-efec3c624c1c'
SOURCE_PATH = 'pictographic-primitives/shopping/bag_d97bc915-f562-41fc-b461-efec3c624c1c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d97bc915-f562-41fc-b461-efec3c624c1c', 'pictographic-primitives/shopping/bag_d97bc915-f562-41fc-b461-efec3c624c1c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bag-d97bc915',)
SOLO_SOURCE_ICON_IDS = ('bag-d97bc915',)
REFERENCE_EXPORT_SHA256 = '9006fe3a8677e5d01079cf7b1059cd6582231ad99323db8936cdfcfc74dd8bff'

class Drawing(Sub32):
    icon_id = 'bag-d97bc915-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 10), (10, 2))
        self.add_line('p1-r1-2', (10, 2), (19, 2))
        self.add_line('p1-r1-3', (19, 2), (19, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (5, 10), (10, 10))
        self.add_line('p2-r1-2', (10, 10), (19, 10))
        self.add_line('p2-r1-3', (19, 10), (22, 10))
        self.add_line('p2-r1-4', (22, 10), (27, 16))
        self.add_line('p2-r1-5', (27, 16), (27, 30))
        self.add_line('p2-r1-6', (27, 30), (22, 30))
        self.add_line('p2-r1-7', (22, 30), (5, 30))
        self.add_line('p2-r1-8', (5, 30), (5, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_line('p3-r1-1', (22, 10), (22, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-4', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
        self.relate("connect", 'p2-r1-7', 'p3-r1-1')
