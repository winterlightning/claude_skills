"""Independent 32px profile of dumbbell-tall-plates.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

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
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (10, 2))
        self.add_arc('p1-r1-2', (10, 2), (11, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (11, 4), (11, 16))
        self.add_line('p1-r1-4', (11, 16), (11, 28))
        self.add_arc('p1-r1-5', (11, 28), (10, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (10, 30), (7, 30))
        self.add_arc('p1-r1-7', (7, 30), (5, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (5, 28), (5, 16))
        self.add_line('p1-r1-9', (5, 16), (5, 4))
        self.add_arc('p1-r1-10', (5, 4), (7, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (22, 2), (25, 2))
        self.add_arc('p2-r1-2', (25, 2), (27, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (27, 4), (27, 16))
        self.add_line('p2-r1-4', (27, 16), (27, 28))
        self.add_arc('p2-r1-5', (27, 28), (25, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (25, 30), (22, 30))
        self.add_arc('p2-r1-7', (22, 30), (21, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-8', (21, 28), (21, 16))
        self.add_line('p2-r1-9', (21, 16), (21, 4))
        self.add_arc('p2-r1-10', (21, 4), (22, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.add_line('p3-r1-1', (11, 16), (21, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 16), (5, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (27, 16), (30, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-8', 'p4-r1-1')
        self.relate("connect", 'p1-r1-9', 'p4-r1-1')
        self.relate("connect", 'p2-r1-3', 'p5-r1-1')
        self.relate("connect", 'p2-r1-4', 'p5-r1-1')
        self.relate("connect", 'p2-r1-8', 'p3-r1-1')
        self.relate("connect", 'p2-r1-9', 'p3-r1-1')
