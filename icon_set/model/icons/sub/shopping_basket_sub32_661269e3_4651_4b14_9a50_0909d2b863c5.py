"""Independent 32px profile of shopping-basket.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '661269e3-4651-4b14-9a50-0909d2b863c5'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping basket_661269e3-4651-4b14-9a50-0909d2b863c5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('661269e3-4651-4b14-9a50-0909d2b863c5', 'pictographic-primitives/shopping/shopping basket_661269e3-4651-4b14-9a50-0909d2b863c5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shopping-basket',)
SOLO_SOURCE_ICON_IDS = ('shopping-basket',)
REFERENCE_EXPORT_SHA256 = 'c83f38101b2d8df7cbe47d2c0e91da7b5dbc125e0ddfe9ce1eafc012de998c04'

class Drawing(Sub32):
    icon_id = 'shopping-basket-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 5), (6, 13))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 5), (26, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (6, 13), (2, 13))
        self.add_line('p3-r1-2', (2, 13), (8, 27))
        self.add_line('p3-r1-3', (8, 27), (23, 27))
        self.add_line('p3-r1-4', (23, 27), (30, 13))
        self.add_line('p3-r1-5', (30, 13), (27, 13))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (6, 13), (27, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (19, 21), (19, 19))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (13, 19), (13, 21))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-5', 'p4-r1-1')
