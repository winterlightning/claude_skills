"""Independent 32px profile of beer-mug.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5429b76f-075c-4738-87f2-f8390c36df79'
SOURCE_PATH = 'pictographic-primitives/symbol/beer_5429b76f-075c-4738-87f2-f8390c36df79.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5429b76f-075c-4738-87f2-f8390c36df79', 'pictographic-primitives/symbol/beer_5429b76f-075c-4738-87f2-f8390c36df79.svg'),)
PROFILE_SOURCE_KEYS = ('solo/beer-mug',)
SOLO_SOURCE_ICON_IDS = ('beer-mug',)
REFERENCE_EXPORT_SHA256 = '1996f6bb769dac3ba22589eb0326ef0d9c911c932ebe1b52cace5659b0ed6a63'

class Drawing(Sub32):
    icon_id = 'beer-mug-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (4, 11), (2, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (2, 10), (8, 4), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (8, 4), (16, 4), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 4), (21, 8), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (21, 8), (21, 11))
        self.add_line('p1-r1-6', (21, 11), (21, 14))
        self.add_line('p1-r1-7', (21, 14), (21, 24))
        self.add_line('p1-r1-8', (21, 24), (21, 27))
        self.add_arc('p1-r1-9', (21, 27), (18, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (18, 30), (7, 30))
        self.add_arc('p1-r1-11', (7, 30), (4, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-12', (4, 27), (4, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (4, 11), (21, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 14), (27, 14))
        self.add_bezier('p3-r1-2', (27, 14), ((28, 14), (29, 15), (29, 15)))
        self.add_bezier('p3-r1-3', (29, 15), ((30, 16), (30, 17), (30, 18)))
        self.add_line('p3-r1-4', (30, 18), (30, 21))
        self.add_arc('p3-r1-5', (30, 21), (27, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-6', (27, 24), (21, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-6')
        self.relate('connect', 'p1-r1-8', 'p3-r1-6')
        self.relate('connect', 'p1-r1-12', 'p2-r1-1')
