"""Sleeveless dress with paired eight-unit straps, round scoop, wider upper bodice and flared curved hem. VRECT_L centerline bounds (8,4)-(40,44). Lucide shirt informed the coherent scoop and garment outline."""
SOURCE_ICON_ID = None
SOURCE_PATH = None
from ...keyshapes import Keyshape
from ._base import Solo48
AUTHOR = 'gpt-6'

class DressVariant2(Solo48):
    icon_id = 'dress-v2'
    variant_of = 'dress'
    variant_label = 'Roomier spacing — review 03'
    keyshape = Keyshape.VRECT_L
    category = 'objects/clothing'
    aliases = ('sleeveless-dress', 'a-line-dress', 'sleeveless-woman-dress')
    keywords = ('dress', 'clothing', 'fashion', 'garment', 'apparel', 'womenswear', 'skirt', 'sleeveless')

    def build(self):
        self.add_line('left-strap-1', (10, 19), (10, 4))
        self.add_line('left-strap-2', (10, 4), (18, 4))
        self.add_line('left-strap-3', (18, 4), (18, 10))
        self.add_arc('neckline', (18, 10), (30, 10), radius_x=6, sweep=False)
        self.add_line('right-strap-1', (30, 10), (30, 4))
        self.add_line('right-strap-2', (30, 4), (38, 4))
        self.add_line('right-strap-3', (38, 4), (38, 19))
        self.add_line('right-body-1', (38, 19), (30, 25))
        self.add_line('right-body-2', (30, 25), (40, 42))
        self.add_arc('hem', (40, 42), (8, 42), radius_x=16, radius_y=2)
        self.add_line('left-body-1', (8, 42), (18, 25))
        self.add_line('left-body-2', (18, 25), (10, 19))
        self.add_contour('outline', 'left-strap-1', 'left-strap-2', 'left-strap-3', 'neckline', 'right-strap-1', 'right-strap-2', 'right-strap-3', 'right-body-1', 'right-body-2', 'hem', 'left-body-1', 'left-body-2', closed=True)
        self.add_line('waist', (18, 25), (30, 25))
        self.relate('connect', 'outline', 'waist')
