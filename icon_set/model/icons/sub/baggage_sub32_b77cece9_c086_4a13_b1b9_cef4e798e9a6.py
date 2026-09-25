"""Independent 32px profile of baggage.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b77cece9-c086-4a13-b1b9-cef4e798e9a6'
SOURCE_PATH = 'pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b77cece9-c086-4a13-b1b9-cef4e798e9a6', 'pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/baggage',)
SOLO_SOURCE_ICON_IDS = ('baggage',)
REFERENCE_EXPORT_SHA256 = '213d1c74a470559cf1a2d287ca36c172b715e9cb17771825422c64b652de7aa6'

class Drawing(Sub32):
    icon_id = 'baggage-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'travel'
    categories = ('travel', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 10), (27, 10))
        self.add_arc('p1-r1-2', (27, 10), (30, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 13), (30, 24))
        self.add_arc('p1-r1-4', (30, 24), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 27), (5, 27))
        self.add_arc('p1-r1-6', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 24), (2, 13))
        self.add_arc('p1-r1-8', (2, 13), (5, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (10, 10), (10, 2))
        self.add_line('p2-r1-2', (10, 2), (22, 2))
        self.add_line('p2-r1-3', (22, 2), (22, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (8, 27), (8, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 27), (24, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
