"""Shopping Cart. Lucide shopping-cart: tapered basket, right-side grip and paired wheels. Retained wheel rail; omitted cramped vertical support."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '22ba9936-54d3-4de1-815f-e80d16f43ff1'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart_22ba9936-54d3-4de1-815f-e80d16f43ff1.svg'
AUTHOR = 'gpt-6'

class ShoppingCartRightGripLowerRail(Solo48):
    icon_id = 'shopping-cart-right-grip-lower-rail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')

    def build(self) -> None:
        # HRECT_L (4,8)-(44,40); right handle with a horizontal grip.
        self.add_polyline('basket',(4,16),(39,16),(36,25),(9,25),(4,16),closed=True)
        self.add_polyline('handle',(39,16),(40,8),(44,8))
        self.relate('connect','handle','basket')

        for index,x in enumerate((14,34)):
            self.add_arc(f'wheel-{index}-a',(x,34),(x,40),radius_x=3)
            self.add_arc(f'wheel-{index}-b',(x,40),(x,34),radius_x=3)
            self.add_contour(f'wheel-{index}',f'wheel-{index}-a',f'wheel-{index}-b',closed=True)
        self.add_line('rail',(14,34),(34,34))
        for index in range(2):self.relate('connect','rail',f'wheel-{index}')
