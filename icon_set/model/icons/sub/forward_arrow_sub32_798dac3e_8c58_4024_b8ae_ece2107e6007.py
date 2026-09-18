"""Independent 32px profile of forward-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '798dac3e-8c58-4024-b8ae-ece2107e6007'
SOURCE_PATH = 'pictographic-primitives/symbol/forward arrow_798dac3e-8c58-4024-b8ae-ece2107e6007.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('798dac3e-8c58-4024-b8ae-ece2107e6007', 'pictographic-primitives/symbol/forward arrow_798dac3e-8c58-4024-b8ae-ece2107e6007.svg'),)
PROFILE_SOURCE_KEYS = ('solo/forward-arrow',)
SOLO_SOURCE_ICON_IDS = ('forward-arrow',)
REFERENCE_EXPORT_SHA256 = '97c732dddcbcac10acff0d35a93a368f785b31edc1c20edf99a0f560951df346'

class Drawing(Sub32):
    icon_id = 'forward-arrow-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (20, 2), (27, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (5, 30), (5, 24))
        self.add_bezier('p2-r1-2', (5, 24), ((5, 24), (5, 23), (5, 23)))
        self.add_bezier('p2-r1-3', (5, 23), ((5, 23), (5, 22), (5, 21)))
        self.add_bezier('p2-r1-4', (5, 21), ((6, 17), (9, 13), (13, 11)))
        self.add_bezier('p2-r1-5', (13, 11), ((14, 10), (15, 10), (17, 10)))
        self.add_line('p2-r1-6', (17, 10), (27, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (20, 18), (27, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-6')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
