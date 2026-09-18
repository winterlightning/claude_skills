"""Independent 32px profile of star-b255daf0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b255daf0-3adf-4238-9c62-9622160eca5c'
SOURCE_PATH = 'pictographic-primitives/holidays/star_b255daf0-3adf-4238-9c62-9622160eca5c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b255daf0-3adf-4238-9c62-9622160eca5c', 'pictographic-primitives/holidays/star_b255daf0-3adf-4238-9c62-9622160eca5c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/star-b255daf0',)
SOLO_SOURCE_ICON_IDS = ('star-b255daf0',)
REFERENCE_EXPORT_SHA256 = '0a22b5410635ca0f47991ea40dd4af06922258510c8882b58b8a4f93df602a55'

class Drawing(Sub32):
    icon_id = 'star-b255daf0-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'holidays'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (20, 11))
        self.add_line('p1-r1-2', (20, 11), (30, 13))
        self.add_line('p1-r1-3', (30, 13), (22, 20))
        self.add_line('p1-r1-4', (22, 20), (25, 30))
        self.add_line('p1-r1-5', (25, 30), (16, 25))
        self.add_line('p1-r1-6', (16, 25), (7, 30))
        self.add_line('p1-r1-7', (7, 30), (10, 20))
        self.add_line('p1-r1-8', (10, 20), (2, 13))
        self.add_line('p1-r1-9', (2, 13), (12, 11))
        self.add_line('p1-r1-10', (12, 11), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
