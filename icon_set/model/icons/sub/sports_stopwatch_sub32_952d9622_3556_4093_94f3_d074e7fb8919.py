"""Independent 32px profile of sports-stopwatch.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '952d9622-3556-4093-94f3-d074e7fb8919'
SOURCE_PATH = 'pictographic-primitives/sports/timer_952d9622-3556-4093-94f3-d074e7fb8919.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('952d9622-3556-4093-94f3-d074e7fb8919', 'pictographic-primitives/sports/timer_952d9622-3556-4093-94f3-d074e7fb8919.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sports-stopwatch',)
SOLO_SOURCE_ICON_IDS = ('sports-stopwatch',)
REFERENCE_EXPORT_SHA256 = 'a39008e26511f672ab6d5c2915c526f363e0b6ca61e7ef1459604e80e3f6b971'

class Drawing(Sub32):
    icon_id = 'sports-stopwatch-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 20), (27, 20), radius_x=11, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (27, 20), (5, 20), radius_x=11, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (13, 2), (19, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 20), (19, 17))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
