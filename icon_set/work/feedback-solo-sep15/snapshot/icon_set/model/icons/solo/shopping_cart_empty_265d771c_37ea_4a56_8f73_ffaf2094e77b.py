'Empty cart: lift the platform to clear two equal round wheels; preserve the raised handle.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '265d771c-37ea-4a56-8f73-ffaf2094e77b'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart empty_265d771c-37ea-4a56-8f73-ffaf2094e77b.svg'
AUTHOR = 'gpt-6'

class ShoppingCartEmpty(Solo48):
    icon_id = 'shopping-cart-empty'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'cart', 'empty')

    def build(self) -> None:
        self.add_polyline('cart',(4,25),(34,25),(38,8),(44,8))

        self.add_arc('wheel-left-top', (8,37), (14,37), radius_x=3, radius_y=3)
        self.add_arc('wheel-left-bottom', (14,37), (8,37), radius_x=3, radius_y=3)
        self.add_contour('wheel-left', 'wheel-left-top', 'wheel-left-bottom', closed=True)

        self.add_arc('wheel-right-top', (28,37), (34,37), radius_x=3, radius_y=3)
        self.add_arc('wheel-right-bottom', (34,37), (28,37), radius_x=3, radius_y=3)
        self.add_contour('wheel-right', 'wheel-right-top', 'wheel-right-bottom', closed=True)
