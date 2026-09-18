"""Independent 32px profile of hand-over-heat.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e2391138-4aaf-4587-83d5-f636e7ba5379'
SOURCE_PATH = 'pictographic-primitives/symbol/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2391138-4aaf-4587-83d5-f636e7ba5379', 'pictographic-primitives/symbol/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-over-heat',)
SOLO_SOURCE_ICON_IDS = ('hand-over-heat',)
REFERENCE_EXPORT_SHA256 = '7144bb3357aa279a4a7628efb46b92249dac4d41746e3302ba244ba39652c6e3'

class Drawing(Sub32):
    icon_id = 'hand-over-heat-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 13), (13, 4))
        self.add_line('p1-r1-2', (13, 4), (24, 4))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 13), (11, 10))
        self.add_line('p2-r1-2', (11, 10), (18, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (11, 10), (11, 13))
        self.add_arc('p3-r1-2', (11, 13), (14, 16), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p3-r1-3', (14, 16), (21, 16))
        self.add_line('p3-r1-4', (21, 16), (30, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_arc('p4-r1-1', (11, 23), (10, 25), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p4-r1-2', (10, 25), (11, 26), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p4-r1-3', (11, 26), (13, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p4-r1-4', (13, 28), (11, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_arc('p5-r1-1', (21, 23), (19, 25), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p5-r1-2', (19, 25), (21, 26), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p5-r1-3', (21, 26), (22, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p5-r1-4', (22, 28), (21, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
