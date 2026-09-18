"""Independent 32px profile of two-falling-bombs-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a92b9733-23c6-4903-9f3a-c893edb5e9f4'
SOURCE_PATH = 'pictographic-primitives/state/bombs_a92b9733-23c6-4903-9f3a-c893edb5e9f4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a92b9733-23c6-4903-9f3a-c893edb5e9f4', 'pictographic-primitives/state/bombs_a92b9733-23c6-4903-9f3a-c893edb5e9f4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/two-falling-bombs-solo',)
SOLO_SOURCE_ICON_IDS = ('two-falling-bombs-solo',)
REFERENCE_EXPORT_SHA256 = '541331099ccfba43b09640cdf3f213721080150ea2b320abe3b5a2af4a61cb6c'

class Drawing(Sub32):
    icon_id = 'two-falling-bombs-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 11), (8, 11))
        self.add_arc('p1-r1-2', (8, 11), (13, 15), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (13, 15), (13, 17))
        self.add_arc('p1-r1-4', (13, 17), (8, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (8, 21), (7, 21))
        self.add_arc('p1-r1-6', (7, 21), (2, 17), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 17), (2, 15))
        self.add_arc('p1-r1-8', (2, 15), (7, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (3, 11), (3, 2))
        self.add_line('p2-r1-2', (3, 2), (7, 5))
        self.add_line('p2-r1-3', (7, 5), (12, 2))
        self.add_line('p2-r1-4', (12, 2), (12, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (24, 19), (25, 19))
        self.add_arc('p3-r1-2', (25, 19), (30, 24), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (30, 24), (30, 25))
        self.add_arc('p3-r1-4', (30, 25), (25, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (25, 30), (24, 30))
        self.add_arc('p3-r1-6', (24, 30), (19, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p3-r1-7', (19, 25), (19, 24))
        self.add_arc('p3-r1-8', (19, 24), (24, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
        self.add_line('p4-r1-1', (20, 19), (20, 11))
        self.add_line('p4-r1-2', (20, 11), (25, 14))
        self.add_line('p4-r1-3', (25, 14), (29, 11))
        self.add_line('p4-r1-4', (29, 11), (29, 19))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
