"""Lucide shopping-cart silhouette; source filled wheels retained and wire detail omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa3ca15f-b005-4f2a-a7fa-abd754bde34f'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_fa3ca15f-b005-4f2a-a7fa-abd754bde34f.svg'
AUTHOR = 'gpt-6'

class ShoppingCartShallowBasket(Solo48):
    icon_id = 'shopping-cart-shallow-basket'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')

    def build(self) -> None:
        # HRECT_L centerline extremes (4,8)-(44,40).
        self.add_polyline('basket',(40,16),(4,16),(11,25),(36,25),(40,16),closed=True)
        self.add_line('handle',(40,16),(44,8))
        self.relate('connect','handle','basket')
        self.add_dot('wheel-left',(15,40))
        self.add_dot('wheel-right',(32,40))
