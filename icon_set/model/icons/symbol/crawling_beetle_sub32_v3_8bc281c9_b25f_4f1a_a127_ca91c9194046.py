"""Independent 32px profile of crawling-beetle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8bc281c9-b25f-4f1a-a127-ca91c9194046'
SOURCE_PATH = 'pictographic-primitives/animals/insect_8bc281c9-b25f-4f1a-a127-ca91c9194046.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8bc281c9-b25f-4f1a-a127-ca91c9194046', 'pictographic-primitives/animals/insect_8bc281c9-b25f-4f1a-a127-ca91c9194046.svg'),)
PROFILE_SOURCE_KEYS = ('solo/crawling-beetle',)
SOLO_SOURCE_ICON_IDS = ('crawling-beetle',)
REFERENCE_EXPORT_SHA256 = '75ebcd08227dd2d8addd8abdcfc1159ba87271f2ae488d60893da633f57d0a59'

class DrawingVariant3(Sub32):
    icon_id = 'crawling-beetle-sub32-v3'
    related_origin_icon_id = 'crawling-beetle-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('dome', (8, 22), (30, 22), radius_x=11, radius_y=12, sweep=True)
        self.add_line('belly', (30, 22), (8, 22))
        self.add_contour('body', 'dome', 'belly', closed=True)
        self.add_line('seam', (19, 10), (15, 22))
        self.relate('connect', 'seam', 'body')
        self.add_bezier('antenna-root', (19, 10), ((17, 6), (12, 4), (8, 4)))
        self.add_bezier('antenna-tip', (8, 4), ((4, 4), (2, 6), (2, 8)))
        self.add_contour('antenna', 'antenna-root', 'antenna-tip')
        self.relate('connect', 'antenna', 'body')
        self.relate('connect', 'antenna', 'seam')
        self.add_line('front-leg', (15, 22), (10, 28))
        self.add_line('back-leg', (24, 22), (27, 28))
        self.relate('connect', 'front-leg', 'body')
        self.relate('connect', 'back-leg', 'body')
        self.relate('connect', 'front-leg', 'seam')
