"""Independent 32px profile of archery-bow-and-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9765457f-3e30-4835-b25c-e413e4bbcd41'
SOURCE_PATH = 'pictographic-primitives/sports/archery_9765457f-3e30-4835-b25c-e413e4bbcd41.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9765457f-3e30-4835-b25c-e413e4bbcd41', 'pictographic-primitives/sports/archery_9765457f-3e30-4835-b25c-e413e4bbcd41.svg'),)
PROFILE_SOURCE_KEYS = ('solo/archery-bow-and-arrow',)
SOLO_SOURCE_ICON_IDS = ('archery-bow-and-arrow',)
REFERENCE_EXPORT_SHA256 = '2215762105b4d7270ebd4ac4895bbc395ec0ee05bde3a117c0614b42b5fb2c34'

class Drawing(Sub32):
    icon_id = 'archery-bow-and-arrow-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 2), (16, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 16), (2, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 16), (16, 16))
        self.add_line('p2-r1-2', (16, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (24, 10), (30, 16))
        self.add_line('p3-r1-2', (30, 16), (24, 22))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
