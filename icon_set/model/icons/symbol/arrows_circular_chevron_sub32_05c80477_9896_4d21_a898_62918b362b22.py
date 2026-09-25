"""Independent 32px profile of arrows-circular-chevron.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '05c80477-9896-4d21-a898-62918b362b22'
SOURCE_PATH = 'pictographic-primitives/symbol/circular arrows_05c80477-9896-4d21-a898-62918b362b22.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('05c80477-9896-4d21-a898-62918b362b22', 'pictographic-primitives/symbol/circular arrows_05c80477-9896-4d21-a898-62918b362b22.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrows-circular-chevron',)
SOLO_SOURCE_ICON_IDS = ('arrows-circular-chevron',)
REFERENCE_EXPORT_SHA256 = '30f10464c9a92871013348a680985a97f896650d8fd5be46921bb7d230c97231'

class Drawing(Sub32):
    icon_id = 'arrows-circular-chevron-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 19), (14, 7), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (14, 7), (21, 7))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 2), (21, 7))
        self.add_line('p2-r1-2', (21, 7), (16, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (30, 13), (18, 25), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (18, 25), (11, 25))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 21), (11, 25))
        self.add_line('p4-r1-2', (11, 25), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
