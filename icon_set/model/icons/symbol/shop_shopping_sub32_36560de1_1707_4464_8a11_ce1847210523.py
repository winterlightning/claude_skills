"""Independent 32px profile of shop-shopping.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '36560de1-1707-4464-8a11-ce1847210523'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_36560de1-1707-4464-8a11-ce1847210523.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('36560de1-1707-4464-8a11-ce1847210523', 'pictographic-primitives/shopping/shop_36560de1-1707-4464-8a11-ce1847210523.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shop-shopping',)
SOLO_SOURCE_ICON_IDS = ('shop-shopping',)
REFERENCE_EXPORT_SHA256 = '5ec300bc93b378ab45109cf83ee39bad95024fa6f7933e608d71cc89df845b11'

class Drawing(Sub32):
    icon_id = 'shop-shopping-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Storefront: awning band with two dividers, body below with a centred door.
        self.add_line('p1-r1-1', (2, 4), (12, 4))
        self.add_line('p1-r1-2', (12, 4), (20, 4))
        self.add_line('p1-r1-3', (20, 4), (30, 4))
        self.add_line('p1-r1-4', (30, 4), (30, 12))
        self.add_line('p1-r1-5', (30, 12), (28, 12))
        self.add_line('p1-r1-6', (28, 12), (20, 12))
        self.add_line('p1-r1-7', (20, 12), (12, 12))
        self.add_line('p1-r1-8', (12, 12), (4, 12))
        self.add_line('p1-r1-9', (4, 12), (2, 12))
        self.add_line('p1-r1-10', (2, 12), (2, 4))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=True)
        self.add_line('p2-r1-1', (12, 4), (12, 12))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 4), (20, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (4, 12), (4, 28))
        self.add_line('p4-r1-2', (4, 28), (12, 28))
        self.add_line('p4-r1-3', (12, 28), (20, 28))
        self.add_line('p4-r1-4', (20, 28), (28, 28))
        self.add_line('p4-r1-5', (28, 28), (28, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (12, 28), (12, 20))
        self.add_line('p5-r1-2', (12, 20), (20, 20))
        self.add_line('p5-r1-3', (20, 20), (20, 28))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        for a, b in (('p1-r1-1', 'p2-r1-1'), ('p1-r1-2', 'p2-r1-1'), ('p1-r1-7', 'p2-r1-1'), ('p1-r1-8', 'p2-r1-1'),
                     ('p1-r1-2', 'p3-r1-1'), ('p1-r1-3', 'p3-r1-1'), ('p1-r1-6', 'p3-r1-1'), ('p1-r1-7', 'p3-r1-1'),
                     ('p1-r1-8', 'p4-r1-1'), ('p1-r1-9', 'p4-r1-1'), ('p1-r1-5', 'p4-r1-5'), ('p1-r1-6', 'p4-r1-5'),
                     ('p4-r1-2', 'p5-r1-1'), ('p4-r1-3', 'p5-r1-1'), ('p4-r1-3', 'p5-r1-3'), ('p4-r1-4', 'p5-r1-3')):
            self.relate('connect', a, b)
