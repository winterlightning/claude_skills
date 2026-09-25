"""Lucide shopping-cart contour flow; deliberate left handle. Omitted tight underside curl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddf04c55-ea1f-4ecd-932d-d90c57f04ad7'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_ddf04c55-ea1f-4ecd-932d-d90c57f04ad7.svg'
AUTHOR = 'gpt-6'

class ShoppingCartLeftHandle(Solo48):
    icon_id = 'shopping-cart-left-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')

    def build(self) -> None:
        # HRECT_L centerline extremes (4,8)-(44,40).
        self.add_polyline('handle',(4,8),(10,8),(12,16))
        self.add_line('top',(12,16),(44,16))
        self.add_line('front',(44,16),(42,24))
        self.add_arc('corner',(42,24),(36,29),radius_x=6,radius_y=5)
        self.add_line('floor',(36,29),(15,29))
        self.add_line('upright',(15,29),(12,16))
        self.add_contour('basket','top','front','corner','floor','upright',closed=True)
        self.relate('connect','handle','basket')
        self.add_dot('wheel-left',(17,40))
        self.add_dot('wheel-right',(35,40))
