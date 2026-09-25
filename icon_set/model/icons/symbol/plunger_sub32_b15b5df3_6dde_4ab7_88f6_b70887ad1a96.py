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
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (13, 5), (19, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (19, 5), (19, 12))
        self.add_arc('p1-r1-3', (19, 12), (16, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 15), (13, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (13, 12), (13, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 15), (16, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (16, 19), (27, 30), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (27, 30), (5, 30))
        self.add_arc('p3-r1-3', (5, 30), (16, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
