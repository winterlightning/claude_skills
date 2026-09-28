"""Independent 32px profile of arrow-angle-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9edbcf4f-df9f-48e0-94e9-f06f136a161b'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow angle right_9edbcf4f-df9f-48e0-94e9-f06f136a161b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9edbcf4f-df9f-48e0-94e9-f06f136a161b', 'pictographic-primitives/symbol/arrow angle right_9edbcf4f-df9f-48e0-94e9-f06f136a161b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-angle-right',)
SOLO_SOURCE_ICON_IDS = ('arrow-angle-right',)
REFERENCE_EXPORT_SHA256 = '238aa737a94c471cab6a309ce9a6ad66b4b55a6a9276f9d9a921516c587b511a'

class Drawing(Sub32):
    icon_id = 'arrow-angle-right-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (30, 16))
        self.add_line('p1-r1-2', (30, 16), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
