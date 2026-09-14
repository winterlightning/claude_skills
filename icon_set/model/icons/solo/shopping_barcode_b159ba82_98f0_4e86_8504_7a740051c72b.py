"""Shopping barcode (products), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b159ba82-98f0-4e86-8504-7a740051c72b'
SOURCE_PATH = 'icons-json/products/shopping barcode_b159ba82-98f0-4e86-8504-7a740051c72b.json'
AUTHOR = 'json_to_solo'

class ShoppingBarcode(Solo48):
    icon_id = 'shopping-barcode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('shopping', 'barcode', 'products')

    def build(self):
        self.add_line('sym-e0', (4, 24), (44, 24))
        self.add_line('sym-e1', (7, 18), (7, 8))
        self.add_line('sym-e2', (19, 18), (19, 8))
        self.add_line('sym-e3', (31, 18), (31, 8))
        self.add_line('sym-e4', (41, 8), (41, 18))
        self.add_line('sym-e5', (7, 30), (7, 40))
        self.add_line('sym-e6', (19, 30), (19, 40))
        self.add_line('sym-e7', (31, 30), (31, 40))
        self.add_line('sym-e8', (41, 40), (41, 30))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2')
        self.add_contour('sym-c3', 'sym-e3')
        self.add_contour('sym-c4', 'sym-e4')
        self.add_contour('sym-c5', 'sym-e5')
        self.add_contour('sym-c6', 'sym-e6')
        self.add_contour('sym-c7', 'sym-e7')
        self.add_contour('sym-c8', 'sym-e8')
