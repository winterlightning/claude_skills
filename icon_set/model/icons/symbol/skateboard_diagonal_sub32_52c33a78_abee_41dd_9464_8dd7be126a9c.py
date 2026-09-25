"""Independent 32px profile of skateboard-diagonal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '52c33a78-abee-41dd-9464-8dd7be126a9c'
SOURCE_PATH = 'pictographic-primitives/symbol/skate_52c33a78-abee-41dd-9464-8dd7be126a9c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('52c33a78-abee-41dd-9464-8dd7be126a9c', 'pictographic-primitives/symbol/skate_52c33a78-abee-41dd-9464-8dd7be126a9c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/skateboard-diagonal',)
SOLO_SOURCE_ICON_IDS = ('skateboard-diagonal',)
REFERENCE_EXPORT_SHA256 = '143c287380d39d787ae31ab3f25cb496fea6773a8b9d421d9f8eb71463d95bcc'

class Drawing(Sub32):
    icon_id = 'skateboard-diagonal-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 24), (7, 22))
        self.add_line('p1-r1-2', (7, 22), (11, 18))
        self.add_line('p1-r1-3', (11, 18), (21, 8))
        self.add_line('p1-r1-4', (21, 8), (25, 4))
        self.add_line('p1-r1-5', (25, 4), (27, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (16, 25), (16, 30), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (16, 30), (16, 25), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (11, 18), (16, 25))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (28, 14), (28, 18), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (28, 18), (28, 14), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (21, 8), (28, 14))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
