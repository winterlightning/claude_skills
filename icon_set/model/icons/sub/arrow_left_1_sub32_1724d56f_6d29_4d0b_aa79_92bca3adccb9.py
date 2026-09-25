"""Independent 32px profile of arrow-left-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1724d56f-6d29-4d0b-aa79-92bca3adccb9'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow left 1_1724d56f-6d29-4d0b-aa79-92bca3adccb9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1724d56f-6d29-4d0b-aa79-92bca3adccb9', 'pictographic-primitives/arrows/arrow left 1_1724d56f-6d29-4d0b-aa79-92bca3adccb9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-left-1',)
SOLO_SOURCE_ICON_IDS = ('arrow-left-1',)
REFERENCE_EXPORT_SHA256 = '2d9791b2f4250c4a8c683b06931eb1bcaacc72e1bb80248cb9ef129680305fc2'

class Drawing(Sub32):
    icon_id = 'arrow-left-1-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 2), (5, 16))
        self.add_line('p1-r1-2', (5, 16), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
