"""Lucide shopping-cart: coherent basket contour and equal wheels. Dropped the cramped lower support curl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f97114c-a7e4-4f5d-935d-2b5d4711fb3f'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_4f97114c-a7e4-4f5d-935d-2b5d4711fb3f.svg'
AUTHOR = 'gpt-6'

class ShoppingCartRoundedBasket(Solo48):
    icon_id = 'shopping-cart-rounded-basket'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')

    def build(self) -> None:
        # HRECT_L centerline extremes (4,8)-(44,40).
        self.add_line('rim',(40,16),(4,16))
        self.add_line('left',(4,16),(7,22))
        self.add_arc('corner',(7,22),(13,25),radius_x=6,radius_y=4,sweep=False)
        self.add_line('floor',(13,25),(35,25))
        self.add_line('right',(35,25),(40,16))
        self.add_contour('basket','rim','left','corner','floor','right',closed=True)
        self.add_line('handle',(40,16),(44,8))
        self.relate('connect','basket','handle')

        for index, x in enumerate((14, 32)):
            y, radius = 37, 3
            self.add_arc(f'wheel-{index}-a', (x-radius,y), (x+radius,y), radius_x=radius)
            self.add_arc(f'wheel-{index}-b', (x+radius,y), (x-radius,y), radius_x=radius)
            self.add_contour(f'wheel-{index}', f'wheel-{index}-a', f'wheel-{index}-b', closed=True)
