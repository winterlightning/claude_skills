"""Lucide shopping-cart silhouette; source filled wheels retained and wire detail omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa216d16-932a-4199-a750-e243701b34d3'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_aa216d16-932a-4199-a750-e243701b34d3.svg'
AUTHOR = 'gpt-6'

class ShoppingCartExtendedHandle(Solo48):
    icon_id = 'shopping-cart-extended-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')

    def build(self) -> None:
        # HRECT_L centerline extremes (4,8)-(44,40).
        self.add_polyline('basket',(40,16),(4,16),(11,28),(36,28),(40,16),closed=True)
        self.add_line('handle',(40,16),(44,8))
        self.relate('connect','handle','basket')
        self.add_dot('wheel-left',(15,40))
        self.add_dot('wheel-right',(32,40))
        self.add_line('handle-tail',(36,28),(35,31))
        self.relate('connect','handle-tail','basket')
