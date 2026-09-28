"""Independent 32px profile of square-brackets.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'acfbd10d-de12-4626-bd35-5e7b02ef616f'
SOURCE_PATH = 'pictographic-primitives/symbol/square brackets_acfbd10d-de12-4626-bd35-5e7b02ef616f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('acfbd10d-de12-4626-bd35-5e7b02ef616f', 'pictographic-primitives/symbol/square brackets_acfbd10d-de12-4626-bd35-5e7b02ef616f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/square-brackets',)
SOLO_SOURCE_ICON_IDS = ('square-brackets',)
REFERENCE_EXPORT_SHA256 = 'a52cca56f9d73a59135df1c7d7bc5f828c5e50830b5a2d7111bd513f8eaa908a'

class Drawing(Sub32):
    icon_id = 'square-brackets-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 16), (30, 28))
        self.add_line('p1-r1-2', (30, 28), (29, 30))
        self.add_line('p1-r1-3', (29, 30), (25, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 16), (2, 28))
        self.add_line('p2-r1-2', (2, 28), (4, 30))
        self.add_line('p2-r1-3', (4, 30), (6, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (30, 16), (30, 4))
        self.add_line('p3-r1-2', (30, 4), (29, 2))
        self.add_line('p3-r1-3', (29, 2), (25, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 16), (2, 4))
        self.add_line('p4-r1-2', (2, 4), (4, 2))
        self.add_line('p4-r1-3', (4, 2), (6, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
