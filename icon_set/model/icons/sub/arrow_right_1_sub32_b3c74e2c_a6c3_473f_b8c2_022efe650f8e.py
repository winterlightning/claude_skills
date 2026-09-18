"""Independent 32px profile of arrow-right-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b3c74e2c-a6c3-473f-b8c2-022efe650f8e'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow right 1_b3c74e2c-a6c3-473f-b8c2-022efe650f8e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b3c74e2c-a6c3-473f-b8c2-022efe650f8e', 'pictographic-primitives/arrows/arrow right 1_b3c74e2c-a6c3-473f-b8c2-022efe650f8e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-right-1',)
SOLO_SOURCE_ICON_IDS = ('arrow-right-1',)
REFERENCE_EXPORT_SHA256 = '6569cf8c9e3e1be6c571c2ff04b5e98d20cec1c7a6fed1e1515fafd989d31a0f'

class Drawing(Sub32):
    icon_id = 'arrow-right-1-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (27, 16))
        self.add_line('p1-r1-2', (27, 16), (5, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
