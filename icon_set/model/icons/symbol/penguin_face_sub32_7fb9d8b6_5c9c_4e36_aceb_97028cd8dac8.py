"""Independent 32px profile of penguin-face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7fb9d8b6-5c9c-4e36-aceb-97028cd8dac8'
SOURCE_PATH = 'pictographic-primitives/animals/bird_7fb9d8b6-5c9c-4e36-aceb-97028cd8dac8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7fb9d8b6-5c9c-4e36-aceb-97028cd8dac8', 'pictographic-primitives/animals/bird_7fb9d8b6-5c9c-4e36-aceb-97028cd8dac8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/penguin-face',)
SOLO_SOURCE_ICON_IDS = ('penguin-face',)
REFERENCE_EXPORT_SHA256 = 'bbd3ace3546f50bb1c51de6b6bec28b9cbfc191cb8fe4dd698ad2038410cb84e'

class Drawing(Sub32):
    icon_id = 'penguin-face-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (4, 20))
        self.add_line('p1-r1-2', (4, 20), (4, 14))
        self.add_arc('p1-r1-3', (4, 14), (16, 2), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 2), (28, 14), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (28, 14), (28, 20))
        self.add_line('p1-r1-6', (28, 20), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (11, 14), (11, 15))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 14), (21, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (12, 22), (16, 28))
        self.add_line('p4-r1-2', (16, 28), (20, 22))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
