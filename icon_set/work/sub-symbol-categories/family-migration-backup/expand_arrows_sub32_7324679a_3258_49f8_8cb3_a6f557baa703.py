"""Independent 32px profile of expand-arrows.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7324679a-3258-49f8-8cb3-a6f557baa703'
SOURCE_PATH = 'pictographic-primitives/symbol/expand arrows_7324679a-3258-49f8-8cb3-a6f557baa703.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7324679a-3258-49f8-8cb3-a6f557baa703', 'pictographic-primitives/symbol/expand arrows_7324679a-3258-49f8-8cb3-a6f557baa703.svg'),)
PROFILE_SOURCE_KEYS = ('solo/expand-arrows',)
SOLO_SOURCE_ICON_IDS = ('expand-arrows',)
REFERENCE_EXPORT_SHA256 = '30a7a5f4885c61e43f213cd7a7776378e7254a08e95d84dfbe0b8229589ea006'

class Drawing(Sub32):
    icon_id = 'expand-arrows-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (2, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (11, 11), (2, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 2), (30, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 2), (21, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (30, 2), (30, 8))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (11, 21), (2, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (2, 23), (2, 30))
        self.add_line('p7-r1-2', (2, 30), (8, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.add_line('p8-r1-1', (21, 21), (30, 30))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (24, 30), (30, 30))
        self.add_line('p9-r1-2', (30, 30), (30, 23))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p6-r1-1', 'p7-r1-1')
        self.relate("connect", 'p6-r1-1', 'p7-r1-2')
        self.relate("connect", 'p8-r1-1', 'p9-r1-1')
        self.relate("connect", 'p8-r1-1', 'p9-r1-2')
