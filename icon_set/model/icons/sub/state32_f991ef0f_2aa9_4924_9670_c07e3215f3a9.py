"""Independent 32px profile of state32-f991ef0f-2aa9-4924-9670-c07e3215f3a9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f991ef0f-2aa9-4924-9670-c07e3215f3a9'
SOURCE_PATH = 'icon_set/assets/combination-state32/f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f991ef0f-2aa9-4924-9670-c07e3215f3a9', 'icon_set/assets/combination-state32/f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'e6e5c915dd37893e38de09ff5861fe6f4b913458a0f70d1ebe3b187773d99df8'

class Drawing(Sub32):
    icon_id = 'state32-f991ef0f-2aa9-4924-9670-c07e3215f3a9'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (3, 14), (3, 18))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (9, 8), (9, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 8), (23, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (29, 14), (29, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
