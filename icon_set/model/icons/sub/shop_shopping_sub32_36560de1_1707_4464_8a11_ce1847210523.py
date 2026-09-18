"""Independent 32px profile of shop-shopping.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '36560de1-1707-4464-8a11-ce1847210523'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_36560de1-1707-4464-8a11-ce1847210523.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('36560de1-1707-4464-8a11-ce1847210523', 'pictographic-primitives/shopping/shop_36560de1-1707-4464-8a11-ce1847210523.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shop-shopping',)
SOLO_SOURCE_ICON_IDS = ('shop-shopping',)
REFERENCE_EXPORT_SHA256 = '5ec300bc93b378ab45109cf83ee39bad95024fa6f7933e608d71cc89df845b11'

class Drawing(Sub32):
    icon_id = 'shop-shopping-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 5), (5, 5))
        self.add_line('p1-r1-2', (5, 5), (9, 5))
        self.add_line('p1-r1-3', (9, 5), (16, 5))
        self.add_line('p1-r1-4', (16, 5), (23, 5))
        self.add_line('p1-r1-5', (23, 5), (27, 5))
        self.add_line('p1-r1-6', (27, 5), (28, 5))
        self.add_arc('p1-r1-7', (28, 5), (30, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (30, 7), (30, 11))
        self.add_arc('p1-r1-9', (30, 11), (28, 13), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (28, 13), (27, 13))
        self.add_line('p1-r1-11', (27, 13), (23, 13))
        self.add_line('p1-r1-12', (23, 13), (16, 13))
        self.add_line('p1-r1-13', (16, 13), (9, 13))
        self.add_line('p1-r1-14', (9, 13), (5, 13))
        self.add_line('p1-r1-15', (5, 13), (4, 13))
        self.add_arc('p1-r1-16', (4, 13), (2, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-17', (2, 11), (2, 7))
        self.add_arc('p1-r1-18', (2, 7), (4, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', closed=False)
        self.add_line('p2-r1-1', (9, 5), (9, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 5), (16, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 5), (23, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (5, 13), (5, 27))
        self.add_line('p5-r1-2', (5, 27), (16, 27))
        self.add_line('p5-r1-3', (16, 27), (27, 27))
        self.add_line('p5-r1-4', (27, 27), (27, 13))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_line('p6-r1-1', (16, 13), (16, 27))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p4-r1-1')
        self.relate("connect", 'p1-r1-5', 'p4-r1-1')
        self.relate("connect", 'p1-r1-10', 'p5-r1-4')
        self.relate("connect", 'p1-r1-11', 'p4-r1-1')
        self.relate("connect", 'p1-r1-11', 'p5-r1-4')
        self.relate("connect", 'p1-r1-12', 'p3-r1-1')
        self.relate("connect", 'p1-r1-12', 'p4-r1-1')
        self.relate("connect", 'p1-r1-12', 'p6-r1-1')
        self.relate("connect", 'p1-r1-13', 'p2-r1-1')
        self.relate("connect", 'p1-r1-13', 'p3-r1-1')
        self.relate("connect", 'p1-r1-13', 'p6-r1-1')
        self.relate("connect", 'p1-r1-14', 'p2-r1-1')
        self.relate("connect", 'p1-r1-14', 'p5-r1-1')
        self.relate("connect", 'p1-r1-15', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p6-r1-1')
        self.relate("connect", 'p5-r1-2', 'p6-r1-1')
        self.relate("connect", 'p5-r1-3', 'p6-r1-1')
