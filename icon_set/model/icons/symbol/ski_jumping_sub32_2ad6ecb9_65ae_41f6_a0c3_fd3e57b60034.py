"""Independent 32px profile of ski-jumping.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034'
SOURCE_PATH = 'pictographic-primitives/symbol/snow jumping_2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034', 'pictographic-primitives/symbol/snow jumping_2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ski-jumping',)
SOLO_SOURCE_ICON_IDS = ('ski-jumping',)
REFERENCE_EXPORT_SHA256 = '088da368a26089e36048a8104fb8f151e13a028c97d19ddde86b07f4da733bb4'

class Drawing(Sub32):
    icon_id = 'ski-jumping-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Skier leaning forward: head ring, straight body and leg down to a long ski with an upturned tip.
        self.add_arc('p1-r1-1', (10, 6), (14, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (14, 2), (18, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (18, 6), (14, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (14, 10), (10, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=True)
        self.add_line('p2-r1-1', (14, 10), (4, 20))
        self.add_line('p2-r1-2', (4, 20), (12, 28))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (10, 30), (12, 28))
        self.add_line('p3-r1-2', (12, 28), (28, 12))
        self.add_line('p3-r1-3', (28, 12), (28, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
