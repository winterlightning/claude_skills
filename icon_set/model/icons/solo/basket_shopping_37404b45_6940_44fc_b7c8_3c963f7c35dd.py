"""Shopping Basket. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide shopping-basket: broad rim and tapered bowl; supplied source determines the single rounded triangular handle.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37404b45-6940-44fc-b7c8-3c963f7c35dd'
SOURCE_PATH = 'pictographic-primitives/symbol/basket_37404b45-6940-44fc-b7c8-3c963f7c35dd.svg'
AUTHOR = 'gpt-6'


class BasketShopping(Solo48):
    icon_id = 'basket-shopping'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('basket', 'shopping', 'cart', 'store', 'buy', 'ecommerce', 'groceries', 'market')

    def build(self) -> None:
        self.add_polyline('rim', (6, 22), (16, 22), (32, 22), (42, 22))
        self.add_line('left-wall', (6, 22), (10, 38))
        self.add_arc('left-corner', (10, 38), (14, 42), radius_x=4, radius_y=4, sweep=False)
        self.add_line('bottom', (14, 42), (34, 42))
        self.add_arc('right-corner', (34, 42), (38, 38), radius_x=4, radius_y=4, sweep=False)
        self.add_line('right-wall', (38, 38), (42, 22))
        self.add_contour('basket', 'left-wall', 'left-corner', 'bottom', 'right-corner', 'right-wall')
        self.relate("connect", 'rim', 'basket')
        self.add_line('handle-left', (16, 22), (20, 10))
        self.add_arc('handle-cap', (20, 10), (28, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-right', (28, 10), (32, 22))
        self.add_contour('handle', 'handle-left', 'handle-cap', 'handle-right')
        self.relate("connect", 'rim', 'handle')
