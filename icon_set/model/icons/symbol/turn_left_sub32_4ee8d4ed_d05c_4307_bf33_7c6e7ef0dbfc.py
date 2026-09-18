"""Independent 32px profile of turn-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc'
SOURCE_PATH = 'pictographic-primitives/transportation/turn left_4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc', 'pictographic-primitives/transportation/turn left_4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/turn-left',)
SOLO_SOURCE_ICON_IDS = ('turn-left',)
REFERENCE_EXPORT_SHA256 = 'e5064bfc8e8bf30d807682f6de39a6a086a82682413478ab166d335a1375a82f'

class Drawing(Sub32):
    icon_id = 'turn-left-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 8), (19, 8))
        self.add_arc('p1-r1-2', (19, 8), (27, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 16), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (10, 2), (5, 8))
        self.add_line('p2-r1-2', (5, 8), (10, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
