"""Independent 32px profile of hiker-backpack-pole.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4ddc386a-2885-4d7a-9893-72e2a6726f6d'
SOURCE_PATH = 'pictographic-primitives/symbol/trekking_4ddc386a-2885-4d7a-9893-72e2a6726f6d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ddc386a-2885-4d7a-9893-72e2a6726f6d', 'pictographic-primitives/symbol/trekking_4ddc386a-2885-4d7a-9893-72e2a6726f6d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hiker-backpack-pole',)
SOLO_SOURCE_ICON_IDS = ('hiker-backpack-pole',)
REFERENCE_EXPORT_SHA256 = 'f5dbe1213c58d96d396da87a0e90064090b1e39c292972e38ea5205db355a408'

class Drawing(Sub32):
    icon_id = 'hiker-backpack-pole-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 6), (24, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 6), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (16, 15), ((15, 18), (14, 20), (13, 22)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 22), (2, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 22), (21, 24))
        self.add_line('p4-r1-2', (21, 24), (24, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (8, 12), (16, 15))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_bezier('p6-r1-1', (16, 15), ((15, 18), (14, 20), (13, 22)))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (13, 22), (5, 18))
        self.add_line('p7-r1-2', (5, 18), (8, 12))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.add_line('p8-r1-1', (16, 15), (22, 19))
        self.add_line('p8-r1-2', (22, 19), (30, 19))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.add_line('p9-r1-1', (30, 10), (30, 19))
        self.add_line('p9-r1-2', (30, 19), (30, 30))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p6-r1-1')
        self.relate('connect', 'p2-r1-1', 'p7-r1-1')
        self.relate('connect', 'p2-r1-1', 'p8-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p7-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p7-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p7-r1-2')
        self.relate('connect', 'p5-r1-1', 'p8-r1-1')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
        self.relate('connect', 'p6-r1-1', 'p8-r1-1')
        self.relate('connect', 'p8-r1-2', 'p9-r1-1')
        self.relate('connect', 'p8-r1-2', 'p9-r1-2')
