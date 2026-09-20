"""Independent 32px profile of slipping-figure.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e57a8798-e336-4231-a2ff-19c5a3653fb7'
SOURCE_PATH = 'pictographic-primitives/transportation/slippery_e57a8798-e336-4231-a2ff-19c5a3653fb7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e57a8798-e336-4231-a2ff-19c5a3653fb7', 'pictographic-primitives/transportation/slippery_e57a8798-e336-4231-a2ff-19c5a3653fb7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/slipping-figure',)
SOLO_SOURCE_ICON_IDS = ('slipping-figure',)
REFERENCE_EXPORT_SHA256 = '31411aea5a54b5f42152c09e8ceacc893b3a5406798ba49cd4c9128a1fbde0e6'

class Drawing(Sub32):
    icon_id = 'slipping-figure-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (21, 5), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (27, 5), (21, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (5, 5), (16, 13))
        self.add_line('p2-r1-2', (16, 13), (24, 18))
        self.add_line('p2-r1-3', (24, 18), (30, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (16, 13), (11, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (11, 22), (2, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (11, 22), (19, 27))
        self.add_line('p5-r1-2', (19, 27), (16, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
