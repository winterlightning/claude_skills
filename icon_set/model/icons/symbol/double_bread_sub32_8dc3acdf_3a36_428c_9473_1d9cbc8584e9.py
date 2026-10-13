"""Independent 32px profile of double-bread.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8dc3acdf-3a36-428c-9473-1d9cbc8584e9'
SOURCE_PATH = 'pictographic-primitives/symbol/double bread_8dc3acdf-3a36-428c-9473-1d9cbc8584e9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8dc3acdf-3a36-428c-9473-1d9cbc8584e9', 'pictographic-primitives/symbol/double bread_8dc3acdf-3a36-428c-9473-1d9cbc8584e9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/double-bread',)
SOLO_SOURCE_ICON_IDS = ('double-bread',)
REFERENCE_EXPORT_SHA256 = 'd168acd6b5a2eff766c2ce0f7341865fdb0a2ddef72718751f28c27c6d4e3bdc'

class Drawing(Sub32):
    icon_id = 'double-bread-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 28), (4, 16))
        self.add_arc('p1-r1-2', (4, 16), (2, 14), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (2, 14), (22, 14), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (22, 14), (20, 16), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (20, 16), (20, 28))
        self.add_line('p1-r1-6', (20, 28), (4, 28))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=True)
        self.add_arc('p2-r1-1', (20, 8), (30, 18), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 18), (28, 20), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (28, 20), (28, 28))
        self.add_line('p2-r1-4', (28, 28), (20, 28))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-4')
        self.relate('connect', 'p1-r1-6', 'p2-r1-4')
