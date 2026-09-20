"""Independent 32px profile of woman-long-hair.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a4e06e7b-9f6c-4283-b751-e75fde558688'
SOURCE_PATH = 'pictographic-primitives/symbol/women_a4e06e7b-9f6c-4283-b751-e75fde558688.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a4e06e7b-9f6c-4283-b751-e75fde558688', 'pictographic-primitives/symbol/women_a4e06e7b-9f6c-4283-b751-e75fde558688.svg'),)
PROFILE_SOURCE_KEYS = ('solo/woman-long-hair',)
SOLO_SOURCE_ICON_IDS = ('woman-long-hair',)
REFERENCE_EXPORT_SHA256 = '92ee79de825c60ea285deee86b9153640dc44383c79c618d13cc57f8af68486a'

class Drawing(Sub32):
    icon_id = 'woman-long-hair-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (2, 16))
        self.add_arc('p1-r1-2', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 16), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (10, 21), (10, 14))
        self.add_line('p2-r1-2', (10, 14), (16, 10))
        self.add_line('p2-r1-3', (16, 10), (22, 14))
        self.add_line('p2-r1-4', (22, 14), (22, 21))
        self.add_arc('p2-r1-5', (22, 21), (10, 21), radius_x=6, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
