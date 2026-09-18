"""Independent 32px profile of car-side.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '695aca30-f091-42f4-b8c1-dabb9d4a8a44'
SOURCE_PATH = 'pictographic-primitives/symbol/car side_695aca30-f091-42f4-b8c1-dabb9d4a8a44.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('695aca30-f091-42f4-b8c1-dabb9d4a8a44', 'pictographic-primitives/symbol/car side_695aca30-f091-42f4-b8c1-dabb9d4a8a44.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-side',)
SOLO_SOURCE_ICON_IDS = ('car-side',)
REFERENCE_EXPORT_SHA256 = 'a6c8e1a0946edf245160fc0b9b9cf12938d7fe1e9444e4116177a28c42ae379e'

class Drawing(Sub32):
    icon_id = 'car-side-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 24), (2, 22))
        self.add_line('p1-r1-2', (2, 22), (2, 13))
        self.add_line('p1-r1-3', (2, 13), (8, 5))
        self.add_line('p1-r1-4', (8, 5), (16, 5))
        self.add_line('p1-r1-5', (16, 5), (22, 13))
        self.add_line('p1-r1-6', (22, 13), (27, 13))
        self.add_arc('p1-r1-7', (27, 13), (30, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (30, 16), (30, 22))
        self.add_line('p1-r1-9', (30, 22), (27, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_arc('p2-r1-1', (5, 24), (8, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (8, 22), (10, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (10, 24), (8, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (8, 27), (5, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_arc('p3-r1-1', (22, 24), (24, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (24, 22), (27, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (27, 24), (24, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (24, 27), (22, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (10, 24), (22, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 13), (22, 13))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-4')
        self.relate("connect", 'p1-r1-2', 'p5-r1-1')
        self.relate("connect", 'p1-r1-3', 'p5-r1-1')
        self.relate("connect", 'p1-r1-5', 'p5-r1-1')
        self.relate("connect", 'p1-r1-6', 'p5-r1-1')
        self.relate("connect", 'p1-r1-9', 'p3-r1-2')
        self.relate("connect", 'p1-r1-9', 'p3-r1-3')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-3', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
