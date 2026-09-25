"""Lucide shopping-cart: trapezoidal basket and paired circular wheels; right handle preserves source direction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0941fae4-611d-41dd-8f02-a68399a41448'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_0941fae4-611d-41dd-8f02-a68399a41448.svg'
AUTHOR = 'gpt-6'

class ShoppingCartOpenWheels(Solo48):
    icon_id = 'shopping-cart-open-wheels'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')

    def build(self) -> None:
        # HRECT_L centerline extremes (4,8)-(44,40).
        self.add_polyline('basket', (40,16), (4,16), (10,25), (35,25), (40,16), closed=True)
        self.add_line('handle', (40,16), (44,8))
        self.relate('connect','basket','handle')

        for index, x in enumerate((14, 32)):
            y, radius = 37, 3
            self.add_arc(f'wheel-{index}-a', (x-radius,y), (x+radius,y), radius_x=radius)
            self.add_arc(f'wheel-{index}-b', (x+radius,y), (x-radius,y), radius_x=radius)
            self.add_contour(f'wheel-{index}', f'wheel-{index}-a', f'wheel-{index}-b', closed=True)
