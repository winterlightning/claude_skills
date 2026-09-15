"""Shopping Cart. Lucide shopping-cart: left handle, rounded front corner and equal wheels. Retained lower connecting rail; simplified support curl."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fbb64f8c-9db3-4eaa-a262-f09476e41a8d'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart 1_fbb64f8c-9db3-4eaa-a262-f09476e41a8d.svg'
AUTHOR = 'gpt-6'

class ShoppingCartLeftHandleLowerRail(Solo48):
    icon_id = 'shopping-cart-left-handle-lower-rail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')

    def build(self) -> None:
        # HRECT_L centerline extremes (4,8)-(44,40).
        self.add_polyline('handle',(4,8),(10,8),(12,16))
        self.add_line('rim',(12,16),(44,16))
        self.add_line('front',(44,16),(42,21))
        self.add_arc('corner',(42,21),(36,25),radius_x=6,radius_y=4)
        self.add_line('floor',(36,25),(14,25))
        self.add_line('back',(14,25),(12,16))
        self.add_contour('basket','rim','front','corner','floor','back',closed=True)
        self.relate('connect','handle','basket')

        for index,x in enumerate((14,34)):
            self.add_arc(f'wheel-{index}-a',(x,34),(x,40),radius_x=3)
            self.add_arc(f'wheel-{index}-b',(x,40),(x,34),radius_x=3)
            self.add_contour(f'wheel-{index}',f'wheel-{index}-a',f'wheel-{index}-b',closed=True)
        self.add_line('rail',(14,34),(34,34))
        for index in range(2):self.relate('connect','rail',f'wheel-{index}')
