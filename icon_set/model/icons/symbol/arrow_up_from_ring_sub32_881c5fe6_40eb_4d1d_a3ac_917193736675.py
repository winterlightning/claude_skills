"""Independent 32px profile of arrow-up-from-ring.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '881c5fe6-40eb-4d1d-a3ac-917193736675'
SOURCE_PATH = 'pictographic-primitives/symbol/ups with small circle and lines_881c5fe6-40eb-4d1d-a3ac-917193736675.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('881c5fe6-40eb-4d1d-a3ac-917193736675', 'pictographic-primitives/symbol/ups with small circle and lines_881c5fe6-40eb-4d1d-a3ac-917193736675.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-up-from-ring',)
SOLO_SOURCE_ICON_IDS = ('arrow-up-from-ring',)
REFERENCE_EXPORT_SHA256 = 'a983573273b91f08bcc564f5c357b2e0a3840400ca8457732aaa88d09b9d53d9'

class Drawing(Sub32):
    icon_id = 'arrow-up-from-ring-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (13, 14), (19, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (19, 14), (13, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 4), (16, 2))
        self.add_line('p3-r1-2', (16, 2), (19, 4))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 24), (30, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (30, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
