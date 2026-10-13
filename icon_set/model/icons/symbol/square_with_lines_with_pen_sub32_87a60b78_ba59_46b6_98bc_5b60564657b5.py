"""Independent 32px profile of square-with-lines-with-pen.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '87a60b78-ba59-46b6-98bc-5b60564657b5'
SOURCE_PATH = 'pictographic-primitives/symbol/square with lines with pen_87a60b78-ba59-46b6-98bc-5b60564657b5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('87a60b78-ba59-46b6-98bc-5b60564657b5', 'pictographic-primitives/symbol/square with lines with pen_87a60b78-ba59-46b6-98bc-5b60564657b5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/square-with-lines-with-pen',)
SOLO_SOURCE_ICON_IDS = ('square-with-lines-with-pen',)
REFERENCE_EXPORT_SHA256 = '3d8f4e8be2c4c0c69df896f4a3d2a260548fbf633e9a19ba4ef49535b1e9a2e6'

class Drawing(Sub32):
    icon_id = 'square-with-lines-with-pen-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Pencil on the diagonal writing a line.
        self.add_polyline('body', (9, 17), (24, 2), (30, 8), (15, 23), closed=True)
        self.add_line('tip-a', (9, 17), (2, 30))
        self.add_line('tip-b', (15, 23), (2, 30))
        self.add_line('line', (20, 30), (30, 30))
        self.relate('connect', 'body', 'tip-a')
        self.relate('connect', 'body', 'tip-b')
        self.relate('connect', 'tip-a', 'tip-b')
