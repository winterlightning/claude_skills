"""Independent 32px profile of broadcast-van-dish.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '493ede0a-6fdc-424e-ac62-2775797bcb36'
SOURCE_PATH = 'pictographic-primitives/symbol/radio van_493ede0a-6fdc-424e-ac62-2775797bcb36.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('493ede0a-6fdc-424e-ac62-2775797bcb36', 'pictographic-primitives/symbol/radio van_493ede0a-6fdc-424e-ac62-2775797bcb36.svg'),)
PROFILE_SOURCE_KEYS = ('solo/broadcast-van-dish',)
SOLO_SOURCE_ICON_IDS = ('broadcast-van-dish',)
REFERENCE_EXPORT_SHA256 = '248828e4eaffce2711a67afdde9dace5fc00aa2c6e17093d6f7c447cfd225b25'

class Drawing(Sub32):
    icon_id = 'broadcast-van-dish-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 27), (2, 27))
        self.add_line('p1-r1-2', (2, 27), (2, 23))
        self.add_line('p1-r1-3', (2, 23), (5, 18))
        self.add_line('p1-r1-4', (5, 18), (16, 18))
        self.add_line('p1-r1-5', (16, 18), (30, 18))
        self.add_line('p1-r1-6', (30, 18), (30, 27))
        self.add_line('p1-r1-7', (30, 27), (28, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (10, 27), (22, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (4, 27), (10, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (10, 27), (4, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (22, 27), (28, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (28, 27), (22, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_arc('p5-r1-1', (8, 4), (16, 11), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('p5-r1-2', (16, 11), (22, 8), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p5-r1-3', (22, 8), (15, 6))
        self.add_line('p5-r1-4', (15, 6), (8, 4))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_line('p6-r1-1', (15, 6), (20, 2))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (16, 11), (16, 18))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-2')
        self.relate("connect", 'p1-r1-4', 'p7-r1-1')
        self.relate("connect", 'p1-r1-5', 'p7-r1-1')
        self.relate("connect", 'p1-r1-7', 'p4-r1-1')
        self.relate("connect", 'p1-r1-7', 'p4-r1-2')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-2')
        self.relate("connect", 'p5-r1-1', 'p7-r1-1')
        self.relate("connect", 'p5-r1-2', 'p7-r1-1')
        self.relate("connect", 'p5-r1-3', 'p6-r1-1')
        self.relate("connect", 'p5-r1-4', 'p6-r1-1')
