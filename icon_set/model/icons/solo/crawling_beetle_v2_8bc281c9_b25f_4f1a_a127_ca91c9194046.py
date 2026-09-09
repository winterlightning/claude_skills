# Variant of crawling-beetle; parent file remains unchanged.
'Crawling beetle with the middle lower leg removed. HRECT_L (2,8)-(46,40) preserves the low side silhouette and antenna. Lucide bug informed sparse leg construction.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8bc281c9-b25f-4f1a-a127-ca91c9194046'
SOURCE_PATH = 'pictographic-primitives/animals/insect_8bc281c9-b25f-4f1a-a127-ca91c9194046.svg'
AUTHOR = 'gpt-6'

class CrawlingBeetleVariant2(Solo48):
    icon_id = 'crawling-beetle-v2'
    variant_of = 'crawling-beetle'
    variant_label = 'Remove middle leg'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('beetle', 'bug', 'insect', 'crawl', 'side', 'profile', 'antenna', 'legs')

    def build(self) -> None:
        self.add_arc('dome-l', (8, 29), (27, 13), radius_x=19, radius_y=16, sweep=True)
        self.add_arc('dome-r', (27, 13), (46, 29), radius_x=19, radius_y=16, sweep=True)
        self.add_line('belly-1', (46, 29), (36, 29))
        self.add_line('belly-2', (36, 29), (25, 29))
        self.add_line('belly-3', (25, 29), (18, 29))
        self.add_line('chin', (18, 29), (8, 29))
        self.add_contour('body', 'dome-l', 'dome-r', 'belly-1', 'belly-2', 'belly-3', 'chin', closed=True)
        self.add_line('head-seam', (18, 29), (27, 13))
        self.relate('connect', 'body', 'head-seam')
        self.add_arc('antenna-r', (27, 13), (14, 8), radius_x=13, radius_y=5, sweep=False)
        self.add_arc('antenna-l', (14, 8), (2, 12), radius_x=12, radius_y=4, sweep=False)
        self.add_contour('antenna', 'antenna-r', 'antenna-l', closed=False)
        self.relate('connect', 'body', 'antenna')
        self.relate('connect', 'head-seam', 'antenna')
        self.add_line('leg-0', (18, 29), (10, 40))
        self.relate('connect', 'body', 'leg-0')
        self.add_line('leg-2', (36, 29), (28, 40))
        self.relate('connect', 'body', 'leg-2')
