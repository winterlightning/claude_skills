'Barcode scanning: preserve the four bar pairs with an exact four-unit ink gap above and below the scan line.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b159ba82-98f0-4e86-8504-7a740051c72b'
SOURCE_PATH = 'pictographic-primitives/products/shopping barcode_b159ba82-98f0-4e86-8504-7a740051c72b.svg'
AUTHOR = 'gpt-6'

class ShoppingBarcode(Solo48):
    icon_id = 'shopping-barcode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('shopping', 'barcode', 'products')

    def build(self) -> None:
        self.add_line('scan',(4,24),(44,24))
        for i,x in enumerate((7,19,31,41)):
            self.add_line(f'upper-{i}',(x,8),(x,16))
            self.add_line(f'lower-{i}',(x,32),(x,40))
