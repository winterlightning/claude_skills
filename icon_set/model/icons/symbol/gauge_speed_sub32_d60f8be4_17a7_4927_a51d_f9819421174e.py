"""Independent 32px profile of gauge-speed.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd60f8be4-17a7-4927-a51d-f9819421174e'
SOURCE_PATH = 'pictographic-primitives/symbol/gauge_d60f8be4-17a7-4927-a51d-f9819421174e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d60f8be4-17a7-4927-a51d-f9819421174e', 'pictographic-primitives/symbol/gauge_d60f8be4-17a7-4927-a51d-f9819421174e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gauge-speed',)
SOLO_SOURCE_ICON_IDS = ('gauge-speed',)
REFERENCE_EXPORT_SHA256 = '86641707802867642094d908448bb903d2b562ffd6c1dfafee76641623d935b1'

class Drawing(Sub32):
    icon_id = 'gauge-speed-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 28), (18, 13), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (18, 13), (27, 16), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (4, 5), (7, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 2), (27, 5))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 21), (18, 30))
        self.add_arc('p5-r1-2', (18, 30), (13, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p5-r1-3', (13, 25), (22, 21))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
