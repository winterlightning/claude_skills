"""Independent 32px profile of plunger.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b15b5df3-6dde-4ab7-88f6-b70887ad1a96'
SOURCE_PATH = 'pictographic-primitives/symbol/plunger_b15b5df3-6dde-4ab7-88f6-b70887ad1a96.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b15b5df3-6dde-4ab7-88f6-b70887ad1a96', 'pictographic-primitives/symbol/plunger_b15b5df3-6dde-4ab7-88f6-b70887ad1a96.svg'),)
PROFILE_SOURCE_KEYS = ('solo/plunger',)
SOLO_SOURCE_ICON_IDS = ('plunger',)
REFERENCE_EXPORT_SHA256 = 'a0d6ce796d19d0f3c654c04601a7ffd2890af0ddc7bb24fa0eba4fdd99e40d61'

class Drawing(Sub32):
    icon_id = 'plunger-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (20, 6), (20, 12))
        self.add_arc('p1-r1-3', (20, 12), (16, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 16), (12, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (12, 12), (12, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 16), (16, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (16, 18), (28, 30), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (28, 30), (4, 30))
        self.add_arc('p3-r1-3', (4, 30), (16, 18), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
