"""Independent 32px profile of pine-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b0aed9fe-a6b3-4563-a48a-d62a019d2531'
SOURCE_PATH = 'pictographic-primitives/symbol/pine_b0aed9fe-a6b3-4563-a48a-d62a019d2531.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b0aed9fe-a6b3-4563-a48a-d62a019d2531', 'pictographic-primitives/symbol/pine_b0aed9fe-a6b3-4563-a48a-d62a019d2531.svg'), ('f98a2e8b-5ad3-4faa-93ec-ec561d2f996b', 'pictographic-primitives/symbol/pine_f98a2e8b-5ad3-4faa-93ec-ec561d2f996b.svg'))
PROFILE_SOURCE_KEYS = ('solo/pine-symbol', 'solo/pine-f98a2e8b')
SOLO_SOURCE_ICON_IDS = ('pine-symbol', 'pine-f98a2e8b')
REFERENCE_EXPORT_SHA256 = '746c6de1f8be97b9810f9d07fdd8faa4a5977bd8a13de4603e35417e73b71eaa'

class Drawing(Sub32):
    icon_id = 'pine-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (24, 12))
        self.add_line('p1-r1-2', (24, 12), (20, 12))
        self.add_bezier('p1-r1-3', (20, 12), ((20, 18), (24, 23), (27, 26)))
        self.add_line('p1-r1-4', (27, 26), (16, 26))
        self.add_line('p1-r1-5', (16, 26), (5, 26))
        self.add_bezier('p1-r1-6', (5, 26), ((8, 23), (13, 18), (13, 12)))
        self.add_line('p1-r1-7', (13, 12), (8, 12))
        self.add_line('p1-r1-8', (8, 12), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (16, 26), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
