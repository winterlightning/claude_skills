"""Independent 32px profile of monitor-with-dollar-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a113d58d-e6b9-465b-a63a-51b045031b0b'
SOURCE_PATH = 'pictographic-primitives/symbol/monitor dollar sign_a113d58d-e6b9-465b-a63a-51b045031b0b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a113d58d-e6b9-465b-a63a-51b045031b0b', 'pictographic-primitives/symbol/monitor dollar sign_a113d58d-e6b9-465b-a63a-51b045031b0b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/monitor-with-dollar-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('monitor-with-dollar-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '9ba5df7fdc87988260ad6ce87b3597e491efb20dcfef355330b225846ed0fa97'

class Drawing(Sub32):
    icon_id = 'monitor-with-dollar-symbol-solo-profile32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 5), (27, 24))
        self.add_arc('p1-r1-4', (27, 24), (24, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 27), (8, 27))
        self.add_arc('p1-r1-6', (8, 27), (5, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 24), (5, 5))
        self.add_arc('p1-r1-8', (5, 5), (8, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (16, 27), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 9), (16, 9))
        self.add_arc('p3-r1-2', (16, 9), (16, 15), radius_x=4, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('p3-r1-3', (16, 15), (16, 20), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (16, 20), (12, 20))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (16, 8), (16, 9))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 20), (16, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p5-r1-1')
        self.relate("connect", 'p3-r1-4', 'p5-r1-1')
