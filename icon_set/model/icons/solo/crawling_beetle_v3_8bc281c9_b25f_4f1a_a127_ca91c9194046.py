"""Left-facing beetle with a smooth elliptical dome, head seam, antenna and three equally spaced swept legs. HRECT_L centerline bounds (4,8)-(44,40). Lucide bug informed repeated open legs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8bc281c9-b25f-4f1a-a127-ca91c9194046'
SOURCE_PATH = 'pictographic-primitives/animals/insect_8bc281c9-b25f-4f1a-a127-ca91c9194046.svg'
AUTHOR = 'gpt-6'

class CrawlingBeetleVariant3(Solo48):
    icon_id = 'crawling-beetle-v3'
    variant_of = 'crawling-beetle'
    variant_label = 'Roomier spacing — review 03'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('beetle', 'bug', 'insect', 'crawl', 'side', 'profile', 'antenna', 'legs')

    def build(self):
        self.add_arc('dome-left', (4, 29), (24, 13), radius_x=20, radius_y=16)
        self.add_arc('dome-right', (24, 13), (44, 29), radius_x=20, radius_y=16)
        self.add_line('belly-1', (44, 29), (38, 29))
        self.add_line('belly-2', (38, 29), (26, 29))
        self.add_line('belly-3', (26, 29), (14, 29))
        self.add_line('belly-4', (14, 29), (4, 29))
        self.add_contour('body', 'dome-left', 'dome-right', 'belly-1', 'belly-2', 'belly-3', 'belly-4', closed=True)
        self.add_line('head-seam', (14, 29), (24, 13))
        self.relate('connect', 'body', 'head-seam')
        self.add_polyline('antenna', (24, 13), (8, 8), (4, 8))
        self.relate('connect', 'body', 'antenna')
        self.relate('connect', 'head-seam', 'antenna')
        for i, x in enumerate((14, 26, 38)):
            self.add_line('leg-' + str(i), (x, 29), (x - 8, 40))
            self.relate('connect', 'body', 'leg-' + str(i))
