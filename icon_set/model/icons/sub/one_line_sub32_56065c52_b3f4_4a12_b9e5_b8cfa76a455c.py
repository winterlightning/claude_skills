"""Independent 32px profile of one-line.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '56065c52-b3f4-4a12-b9e5-b8cfa76a455c'
SOURCE_PATH = 'pictographic-primitives/symbol/one line_56065c52-b3f4-4a12-b9e5-b8cfa76a455c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('56065c52-b3f4-4a12-b9e5-b8cfa76a455c', 'pictographic-primitives/symbol/one line_56065c52-b3f4-4a12-b9e5-b8cfa76a455c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/one-line',)
SOLO_SOURCE_ICON_IDS = ('one-line',)
REFERENCE_EXPORT_SHA256 = '9ef55c7446516f32a9602192fe6c5b8e5a3b13bf32957915daaf5415d58fff06'

class Drawing(Sub32):
    icon_id = 'one-line-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 2), (5, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
