"""Independent 32px profile of crawling-beetle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8bc281c9-b25f-4f1a-a127-ca91c9194046'
SOURCE_PATH = 'pictographic-primitives/animals/insect_8bc281c9-b25f-4f1a-a127-ca91c9194046.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8bc281c9-b25f-4f1a-a127-ca91c9194046', 'pictographic-primitives/animals/insect_8bc281c9-b25f-4f1a-a127-ca91c9194046.svg'),)
PROFILE_SOURCE_KEYS = ('solo/crawling-beetle',)
SOLO_SOURCE_ICON_IDS = ('crawling-beetle',)
REFERENCE_EXPORT_SHA256 = '75ebcd08227dd2d8addd8abdcfc1159ba87271f2ae488d60893da633f57d0a59'

class Drawing(Sub32):
    icon_id = 'crawling-beetle-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'animals'
    categories = ('animals', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 20), ((2, 17), (3, 14), (6, 12)))
        self.add_bezier('p1-r1-2', (6, 12), ((9, 9), (12, 8), (16, 8)))
        self.add_bezier('p1-r1-3', (16, 8), ((20, 8), (23, 9), (26, 12)))
        self.add_bezier('p1-r1-4', (26, 12), ((29, 14), (30, 17), (30, 20)))
        self.add_line('p1-r1-5', (30, 20), (26, 20))
        self.add_line('p1-r1-6', (26, 20), (17, 20))
        self.add_line('p1-r1-7', (17, 20), (9, 20))
        self.add_line('p1-r1-8', (9, 20), (2, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (9, 20), (16, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 8), (5, 5))
        self.add_line('p3-r1-2', (5, 5), (2, 5))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (9, 20), (3, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (26, 20), (20, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p5-r1-1')
        self.relate("connect", 'p1-r1-6', 'p5-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p4-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-8', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
