"""Independent 32px profile of user-bust-overlap.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '421aee38-8e76-46f2-b9c5-aeb683f83bc5'
SOURCE_PATH = 'pictographic-primitives/symbol/person 1_421aee38-8e76-46f2-b9c5-aeb683f83bc5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('421aee38-8e76-46f2-b9c5-aeb683f83bc5', 'pictographic-primitives/symbol/person 1_421aee38-8e76-46f2-b9c5-aeb683f83bc5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/user-bust-overlap',)
SOLO_SOURCE_ICON_IDS = ('user-bust-overlap',)
REFERENCE_EXPORT_SHA256 = '5939d1cc19c0e4cd9059162ec043a04b2e6690c84a9b05fafa4b5de67dffdd1d'

class Drawing(Sub32):
    icon_id = 'user-bust-overlap-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 19), (16, 2), radius_x=8.5, radius_y=8.5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (16, 19), radius_x=8.5, radius_y=8.5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (5, 30), (16, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (16, 19), (27, 30), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
