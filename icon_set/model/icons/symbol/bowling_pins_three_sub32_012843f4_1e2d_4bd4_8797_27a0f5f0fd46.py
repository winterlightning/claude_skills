"""Independent 32px profile of bowling-pins-three.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '012843f4-1e2d-4bd4-8797-27a0f5f0fd46'
SOURCE_PATH = 'pictographic-primitives/symbol/three bowlings_012843f4-1e2d-4bd4-8797-27a0f5f0fd46.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('012843f4-1e2d-4bd4-8797-27a0f5f0fd46', 'pictographic-primitives/symbol/three bowlings_012843f4-1e2d-4bd4-8797-27a0f5f0fd46.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bowling-pins-three',)
SOLO_SOURCE_ICON_IDS = ('bowling-pins-three',)
REFERENCE_EXPORT_SHA256 = 'f40013f945816a6507c09660de05131e7fc85a9a539d7ed162a74c5cc194d69b'

class Drawing(Sub32):
    icon_id = 'bowling-pins-three-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 8), (8, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (8, 8), (8, 12))
        self.add_line('p1-r1-3', (8, 12), (8, 16))
        self.add_arc('p1-r1-4', (8, 16), (2, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (2, 16), (2, 12))
        self.add_line('p1-r1-6', (2, 12), (2, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (2, 12), (8, 12))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (24, 8), (30, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (30, 8), (30, 12))
        self.add_line('p3-r1-3', (30, 12), (30, 16))
        self.add_arc('p3-r1-4', (30, 16), (24, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (24, 16), (24, 12))
        self.add_line('p3-r1-6', (24, 12), (24, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (24, 12), (30, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (13, 17), (19, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p5-r1-2', (19, 17), (19, 20))
        self.add_bezier('p5-r1-3', (19, 20), ((19, 22), (20, 23), (20, 24)))
        self.add_bezier('p5-r1-4', (20, 24), ((20, 27), (18, 27), (16, 27)))
        self.add_bezier('p5-r1-5', (16, 27), ((14, 27), (12, 27), (13, 24)))
        self.add_bezier('p5-r1-6', (13, 24), ((13, 23), (13, 22), (13, 20)))
        self.add_line('p5-r1-7', (13, 20), (13, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', 'p5-r1-7', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-5', 'p4-r1-1')
        self.relate('connect', 'p3-r1-6', 'p4-r1-1')
