"""Independent 32px profile of virus-spiked.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4d083734-a49d-4b8f-b296-051afc8c7552'
SOURCE_PATH = 'pictographic-primitives/symbol/virus_4d083734-a49d-4b8f-b296-051afc8c7552.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4d083734-a49d-4b8f-b296-051afc8c7552', 'pictographic-primitives/symbol/virus_4d083734-a49d-4b8f-b296-051afc8c7552.svg'),)
PROFILE_SOURCE_KEYS = ('solo/virus-spiked',)
SOLO_SOURCE_ICON_IDS = ('virus-spiked',)
REFERENCE_EXPORT_SHA256 = '29a11de8f4c322ca748bfd1c54a05bfc6e8e6815fa447f319f68ff665755fb66'

class Drawing(Sub32):
    icon_id = 'virus-spiked-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 6), (22, 8), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 8), (26, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (26, 16), (22, 24), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (22, 24), (16, 26), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (16, 26), (10, 24), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (10, 24), (6, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (6, 16), (10, 8), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-8', (10, 8), (16, 6), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (16, 6), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 8), (24, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (26, 16), (30, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 24), (24, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (16, 26), (16, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (10, 24), (8, 27))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (6, 16), (2, 16))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (10, 8), (8, 5))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_line('p10-r1-1', (16, 16), (16, 16))
        self.add_contour('path-10-1', 'p10-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p6-r1-1')
        self.relate('connect', 'p1-r1-5', 'p6-r1-1')
        self.relate('connect', 'p1-r1-5', 'p7-r1-1')
        self.relate('connect', 'p1-r1-6', 'p7-r1-1')
        self.relate('connect', 'p1-r1-6', 'p8-r1-1')
        self.relate('connect', 'p1-r1-7', 'p8-r1-1')
        self.relate('connect', 'p1-r1-7', 'p9-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p9-r1-1')
