"""Independent 32px profile of arrow-bottom-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow bottom_0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432', 'pictographic-primitives/symbol/arrow bottom_0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432.svg'), ('cccc0ae2-455e-5543-acd2-86328a04cbec', 'pictographic-primitives/arrows/arrow button bottom 1_cccc0ae2-455e-5543-acd2-86328a04cbec.svg'))
PROFILE_SOURCE_KEYS = ('solo/arrow-bottom-symbol', 'solo/arrow-button-bottom-1')
SOLO_SOURCE_ICON_IDS = ('arrow-bottom-symbol', 'arrow-button-bottom-1')
REFERENCE_EXPORT_SHA256 = '9ec597e0f406140f8860ffa9d27a4143e7f8e33e585523ce83d74a6ec7f423d2'

class Drawing(Sub32):
    icon_id = 'arrow-bottom-symbol-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 27), (15, 26))
        self.add_line('p1-r1-2', (15, 26), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 27), (17, 26))
        self.add_line('p2-r1-2', (17, 26), (30, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
