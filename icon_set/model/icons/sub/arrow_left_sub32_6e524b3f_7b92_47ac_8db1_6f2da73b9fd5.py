"""Independent 32px profile of arrow-left-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6e524b3f-7b92-47ac-8db1-6f2da73b9fd5'
SOURCE_PATH = 'pictographic-primitives/symbol/return arrow with line_6e524b3f-7b92-47ac-8db1-6f2da73b9fd5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6e524b3f-7b92-47ac-8db1-6f2da73b9fd5', 'pictographic-primitives/symbol/return arrow with line_6e524b3f-7b92-47ac-8db1-6f2da73b9fd5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-left-solo',)
SOLO_SOURCE_ICON_IDS = ('arrow-left-solo',)
REFERENCE_EXPORT_SHA256 = '2a08b171b8fb0224f7506b7a81dd3f0d3b29093d2da7a2468b276335e75d0cb9'

class Drawing(Sub32):
    icon_id = 'arrow-left-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 5), (2, 16))
        self.add_line('p1-r1-2', (2, 16), (13, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
