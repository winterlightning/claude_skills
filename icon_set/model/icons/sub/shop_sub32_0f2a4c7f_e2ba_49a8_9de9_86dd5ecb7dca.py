"""Independent 32px profile of shop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca', 'pictographic-primitives/shopping/shop_0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shop',)
SOLO_SOURCE_ICON_IDS = ('shop',)
REFERENCE_EXPORT_SHA256 = '0f32fc330b5c8b5a33166cb8d011feeba756f88f76d45438a1ce7929b2922ad7'

class Drawing(Sub32):
    icon_id = 'shop-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 13), (5, 5))
        self.add_line('p1-r1-2', (5, 5), (27, 5))
        self.add_line('p1-r1-3', (27, 5), (30, 13))
        self.add_bezier('p1-r1-4', (30, 13), ((30, 15), (29, 17), (27, 17)))
        self.add_bezier('p1-r1-5', (27, 17), ((24, 17), (22, 15), (21, 13)))
        self.add_bezier('p1-r1-6', (21, 13), ((20, 15), (18, 16), (16, 16)))
        self.add_bezier('p1-r1-7', (16, 16), ((14, 16), (12, 15), (11, 13)))
        self.add_bezier('p1-r1-8', (11, 13), ((10, 15), (8, 17), (5, 17)))
        self.add_bezier('p1-r1-9', (5, 17), ((3, 17), (2, 15), (2, 13)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (5, 17), (5, 27))
        self.add_line('p2-r1-2', (5, 27), (27, 27))
        self.add_line('p2-r1-3', (27, 27), (27, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-3')
        self.relate("connect", 'p1-r1-5', 'p2-r1-3')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
