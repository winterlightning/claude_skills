"""Independent 32px profile of hamburger.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4eb3fceb-2f4c-4167-ac6b-944c1693b563'
SOURCE_PATH = 'pictographic-primitives/symbol/hamburger_4eb3fceb-2f4c-4167-ac6b-944c1693b563.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4eb3fceb-2f4c-4167-ac6b-944c1693b563', 'pictographic-primitives/symbol/hamburger_4eb3fceb-2f4c-4167-ac6b-944c1693b563.svg'), ('8dc1040e-1d03-4e50-a902-d55864c7103f', 'pictographic-primitives/symbol/hamburger_8dc1040e-1d03-4e50-a902-d55864c7103f.svg'))
PROFILE_SOURCE_KEYS = ('solo/hamburger', 'solo/hamburger-symbol')
SOLO_SOURCE_ICON_IDS = ('hamburger', 'hamburger-symbol')
REFERENCE_EXPORT_SHA256 = '0d981a03352aeaf10768305676891d49a70ea3287e10ba404086b3bac0bd9ef9'

class Drawing(Sub32):
    icon_id = 'hamburger-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Burger: dome bun, patty band and bottom bun, each 8 units tall (no room for the wavy lettuce).
        self.add_arc('p1-r1-1', (4, 12), (16, 4), radius_x=12, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 4), (28, 12), radius_x=12, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (28, 12), (4, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=True)
        self.add_line('p2-r1-1', (2, 20), (30, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (4, 20), (4, 24))
        self.add_arc('p3-r1-2', (4, 24), (8, 28), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p3-r1-3', (8, 28), (24, 28))
        self.add_arc('p3-r1-4', (24, 28), (28, 24), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p3-r1-5', (28, 24), (28, 20))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-5')
