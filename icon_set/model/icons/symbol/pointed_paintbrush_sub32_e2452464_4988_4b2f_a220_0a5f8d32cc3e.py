"""Independent 32px profile of pointed-paintbrush.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e2452464-4988-4b2f-a220-0a5f8d32cc3e'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2452464-4988-4b2f-a220-0a5f8d32cc3e', 'pictographic-primitives/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pointed-paintbrush',)
SOLO_SOURCE_ICON_IDS = ('pointed-paintbrush',)
REFERENCE_EXPORT_SHA256 = 'c08360479dd7b1b10a838fb970123073510b81133fec70f30615988d16ed0729'

class Drawing(Sub32):
    icon_id = 'pointed-paintbrush-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Handle: two parallel 45-degree edges 8.5 units apart, square cap with one round corner.
        self.add_line('p1-r1-1', (10, 14), (22, 2))
        self.add_line('p1-r1-2', (22, 2), (27, 2))
        self.add_arc('p1-r1-3', (27, 2), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (30, 5), (30, 6))
        self.add_line('p1-r1-5', (30, 6), (16, 20))
        # Ferrule edge, square to the handle.
        self.add_line('p1-r1-6', (16, 20), (10, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=True)
        # Bristles: two smooth curves meeting at the tip.
        self.add_bezier('p2-r1-1', (10, 14), ((5, 17), (2, 22), (2, 30)))
        self.add_bezier('p2-r1-2', (2, 30), ((7, 29), (13, 25), (16, 20)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-6', 'p2-r1-2')
