"""Independent 32px profile of card-a525cc8f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a525cc8f-6e57-4f1c-931a-9f1999e26316'
SOURCE_PATH = 'pictographic-primitives/business/card_a525cc8f-6e57-4f1c-931a-9f1999e26316.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a525cc8f-6e57-4f1c-931a-9f1999e26316', 'pictographic-primitives/business/card_a525cc8f-6e57-4f1c-931a-9f1999e26316.svg'),)
PROFILE_SOURCE_KEYS = ('solo/card-a525cc8f',)
SOLO_SOURCE_ICON_IDS = ('card-a525cc8f',)
REFERENCE_EXPORT_SHA256 = '83cf2dfd353fa8a2169657a02a78af2808d74426525de8da3605902600dab092'

class Drawing(Sub32):
    icon_id = 'card-a525cc8f-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 5), (27, 5))
        self.add_arc('p1-r1-2', (27, 5), (30, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 8), (30, 24))
        self.add_arc('p1-r1-4', (30, 24), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 27), (5, 27))
        self.add_arc('p1-r1-6', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 24), (2, 8))
        self.add_arc('p1-r1-8', (2, 8), (5, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (20, 20), (22, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
