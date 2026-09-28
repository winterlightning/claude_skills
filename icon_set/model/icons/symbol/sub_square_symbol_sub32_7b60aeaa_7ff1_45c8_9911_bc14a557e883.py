"""Independent 32px profile of sub-square-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7b60aeaa-7ff1-45c8-9911-bc14a557e883'
SOURCE_PATH = 'pictographic-primitives/symbol/sub square_7b60aeaa-7ff1-45c8-9911-bc14a557e883.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b60aeaa-7ff1-45c8-9911-bc14a557e883', 'pictographic-primitives/symbol/sub square_7b60aeaa-7ff1-45c8-9911-bc14a557e883.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sub-square-symbol',)
SOLO_SOURCE_ICON_IDS = ('sub-square-symbol',)
REFERENCE_EXPORT_SHA256 = '29d2258489a1814df6fc4adeabca6f3af718f521ffd435a81f1df3e50ea4e21e'

class Drawing(Sub32):
    icon_id = 'sub-square-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 2), (21, 2))
        self.add_arc('p1-r1-2', (21, 2), (30, 11), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 11), (30, 21))
        self.add_arc('p1-r1-4', (30, 21), (21, 30), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (21, 30), (11, 30))
        self.add_arc('p1-r1-6', (11, 30), (2, 21), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 21), (2, 11))
        self.add_arc('p1-r1-8', (2, 11), (11, 2), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
