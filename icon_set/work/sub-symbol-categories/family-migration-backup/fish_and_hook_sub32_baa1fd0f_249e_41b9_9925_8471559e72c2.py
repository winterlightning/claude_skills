"""Independent 32px profile of fish-and-hook.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'baa1fd0f-249e-41b9-9925-8471559e72c2'
SOURCE_PATH = 'pictographic-primitives/symbol/fish with a line_baa1fd0f-249e-41b9-9925-8471559e72c2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('baa1fd0f-249e-41b9-9925-8471559e72c2', 'pictographic-primitives/symbol/fish with a line_baa1fd0f-249e-41b9-9925-8471559e72c2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fish-and-hook',)
SOLO_SOURCE_ICON_IDS = ('fish-and-hook',)
REFERENCE_EXPORT_SHA256 = '79299493186c01e8a675ae795297aeb05f325a4716b486747035bfae89e251fc'

class Drawing(Sub32):
    icon_id = 'fish-and-hook-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (2, 24))
        self.add_arc('p1-r1-2', (2, 24), (8, 24), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (13, 19), (30, 19), radius_x=10, radius_y=18, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 19), (13, 19), radius_x=10, radius_y=18, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (30, 12), (30, 19))
        self.add_line('p3-r1-2', (30, 19), (30, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (22, 19), (22, 19))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
