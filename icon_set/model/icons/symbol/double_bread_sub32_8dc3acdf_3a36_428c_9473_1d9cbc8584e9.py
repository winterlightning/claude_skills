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
        self.add_line('p1-r1-1', (18, 27), (17, 15))
        self.add_arc('p1-r1-2', (17, 15), (19, 9), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (19, 9), (17, 7), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (17, 7), (10, 5), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_arc('p1-r1-5', (10, 5), (7, 6), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p1-r1-6', (7, 6), (4, 7), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('p1-r1-7', (4, 7), (2, 11), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-8', (2, 11), (2, 13))
        self.add_arc('p1-r1-9', (2, 13), (4, 15), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p1-r1-10', (4, 15), (3, 27))
        self.add_line('p1-r1-11', (3, 27), (29, 27))
        self.add_line('p1-r1-12', (29, 27), (28, 15))
        self.add_bezier('p1-r1-13', (28, 15), ((29, 14), (29, 14), (29, 13)))
        self.add_bezier('p1-r1-14', (29, 13), ((30, 13), (30, 12), (30, 11)))
        self.add_arc('p1-r1-15', (30, 11), (28, 7), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('p1-r1-16', (28, 7), (22, 5), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('p1-r1-17', (22, 5), (20, 5))
        self.add_line('p1-r1-18', (20, 5), (16, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', closed=False)
