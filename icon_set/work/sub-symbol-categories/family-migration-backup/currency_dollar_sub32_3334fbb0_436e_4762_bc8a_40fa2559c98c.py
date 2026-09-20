"""Independent 32px profile of currency-dollar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3334fbb0-436e-4762-bc8a-40fa2559c98c'
SOURCE_PATH = 'pictographic-primitives/money/currency dollar_3334fbb0-436e-4762-bc8a-40fa2559c98c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3334fbb0-436e-4762-bc8a-40fa2559c98c', 'pictographic-primitives/money/currency dollar_3334fbb0-436e-4762-bc8a-40fa2559c98c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/currency-dollar',)
SOLO_SOURCE_ICON_IDS = ('currency-dollar',)
REFERENCE_EXPORT_SHA256 = '5e6ae904dbd4dbed023aad02e14cd60d9a7bfe52c2be8dcf5e26a98ea531ec6b'

class Drawing(Sub32):
    icon_id = 'currency-dollar-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 6))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 30), (16, 26))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (5, 24), ((8, 25), (11, 26), (14, 26)))
        self.add_bezier('p3-r1-2', (14, 26), ((15, 26), (15, 26), (16, 26)))
        self.add_bezier('p3-r1-3', (16, 26), ((21, 26), (27, 24), (27, 21)))
        self.add_bezier('p3-r1-4', (27, 21), ((27, 21), (27, 21), (27, 21)))
        self.add_bezier('p3-r1-5', (27, 21), ((27, 16), (16, 16), (11, 15)))
        self.add_bezier('p3-r1-6', (11, 15), ((8, 15), (5, 13), (5, 11)))
        self.add_bezier('p3-r1-7', (5, 11), ((5, 11), (5, 11), (5, 11)))
        self.add_bezier('p3-r1-8', (5, 11), ((5, 11), (5, 11), (5, 11)))
        self.add_bezier('p3-r1-9', (5, 11), ((5, 10), (5, 10), (5, 9)))
        self.add_bezier('p3-r1-10', (5, 9), ((7, 7), (12, 6), (16, 6)))
        self.add_bezier('p3-r1-11', (16, 6), ((19, 6), (22, 7), (25, 8)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-10')
        self.relate("connect", 'p1-r1-1', 'p3-r1-11')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-1', 'p3-r1-3')
