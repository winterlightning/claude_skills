"""Independent 32px profile of dumbbell-tall-plates.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9c8857a3-198d-47d1-be28-3a6d0762e293'
SOURCE_PATH = 'pictographic-primitives/sports/dumbbell_9c8857a3-198d-47d1-be28-3a6d0762e293.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c8857a3-198d-47d1-be28-3a6d0762e293', 'pictographic-primitives/sports/dumbbell_9c8857a3-198d-47d1-be28-3a6d0762e293.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dumbbell-tall-plates',)
SOLO_SOURCE_ICON_IDS = ('dumbbell-tall-plates',)
REFERENCE_EXPORT_SHA256 = 'f87dfd6cd2acc0b166890b2776b76114a2fe12f0cfe76a40e9d48271542ed0b4'

class Drawing(Sub32):
    icon_id = 'dumbbell-tall-plates-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (9, 2))
        self.add_arc('p1-r1-2', (9, 2), (11, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (11, 4), (11, 16))
        self.add_line('p1-r1-4', (11, 16), (11, 28))
        self.add_arc('p1-r1-5', (11, 28), (9, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (9, 30), (5, 30))
        self.add_arc('p1-r1-7', (5, 30), (3, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (3, 28), (3, 16))
        self.add_line('p1-r1-9', (3, 16), (3, 4))
        self.add_arc('p1-r1-10', (3, 4), (5, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (23, 2), (27, 2))
        self.add_arc('p2-r1-2', (27, 2), (29, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (29, 4), (29, 16))
        self.add_line('p2-r1-4', (29, 16), (29, 28))
        self.add_arc('p2-r1-5', (29, 28), (27, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (27, 30), (23, 30))
        self.add_arc('p2-r1-7', (23, 30), (21, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-8', (21, 28), (21, 16))
        self.add_line('p2-r1-9', (21, 16), (21, 4))
        self.add_arc('p2-r1-10', (21, 4), (23, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.add_line('p3-r1-1', (11, 16), (21, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 16), (3, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (29, 16), (30, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-9', 'p4-r1-1')
        self.relate('connect', 'p2-r1-3', 'p5-r1-1')
        self.relate('connect', 'p2-r1-4', 'p5-r1-1')
        self.relate('connect', 'p2-r1-8', 'p3-r1-1')
        self.relate('connect', 'p2-r1-9', 'p3-r1-1')
