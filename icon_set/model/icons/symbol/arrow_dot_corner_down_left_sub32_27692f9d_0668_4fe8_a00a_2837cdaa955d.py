"""Independent 32px profile of arrow-dot-corner-down-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '27692f9d-0668-4fe8-a00a-2837cdaa955d'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot corner down left_27692f9d-0668-4fe8-a00a-2837cdaa955d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('27692f9d-0668-4fe8-a00a-2837cdaa955d', 'pictographic-primitives/arrows/arrow dot corner down left_27692f9d-0668-4fe8-a00a-2837cdaa955d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-dot-corner-down-left',)
SOLO_SOURCE_ICON_IDS = ('arrow-dot-corner-down-left',)
REFERENCE_EXPORT_SHA256 = 'eb34e037f6b1d21cd45071f456bd7d35e18b9c31944b17a24b9c66b40dd833b7'

class Drawing(Sub32):
    icon_id = 'arrow-dot-corner-down-left-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 21), (4, 28))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (4, 28), (14, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (4, 28), (2, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (17, 15), (21, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (26, 6), (30, 2))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
