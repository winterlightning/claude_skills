"""Independent 32px profile of storefront-with-centre-seam.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '64bc751c-6428-4912-8109-7f61de02332f'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_64bc751c-6428-4912-8109-7f61de02332f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('64bc751c-6428-4912-8109-7f61de02332f', 'pictographic-primitives/shopping/shop_64bc751c-6428-4912-8109-7f61de02332f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/storefront-with-centre-seam',)
SOLO_SOURCE_ICON_IDS = ('storefront-with-centre-seam',)
REFERENCE_EXPORT_SHA256 = 'b85f72a7c225b9a3c3212315a6b94d5786ab3a3ae714034a5493388620c1c4ab'

class Drawing(Sub32):
    icon_id = 'storefront-with-centre-seam-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'shopping'
    categories = ('shopping', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 10), (5, 2))
        self.add_line('p1-r1-2', (5, 2), (27, 2))
        self.add_line('p1-r1-3', (27, 2), (30, 10))
        self.add_arc('p1-r1-4', (30, 10), (21, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (21, 10), (11, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (11, 10), (2, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (2, 10), (2, 30))
        self.add_line('p2-r1-2', (2, 30), (16, 30))
        self.add_line('p2-r1-3', (16, 30), (30, 30))
        self.add_line('p2-r1-4', (30, 30), (30, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, 30), (16, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-4')
        self.relate("connect", 'p1-r1-4', 'p2-r1-4')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
