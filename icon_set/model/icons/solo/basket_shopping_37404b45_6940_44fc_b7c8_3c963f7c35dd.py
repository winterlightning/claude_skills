"""Replace the tapered handle with one smooth half-ellipse. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '37404b45-6940-44fc-b7c8-3c963f7c35dd'
SOURCE_PATH = 'pictographic-primitives/symbol/basket_37404b45-6940-44fc-b7c8-3c963f7c35dd.svg'
AUTHOR = 'gpt-6'

class BasketShopping(Solo48):
    icon_id = 'basket-shopping'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('basket', 'shopping', 'cart', 'store', 'buy', 'ecommerce', 'groceries', 'market')

    def build(self) -> None:
        """Symbol plan: Replace the tapered handle with one smooth half-ellipse. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_polyline('rim', (6, 22), (16, 22), (32, 22), (42, 22))
        self.add_line('left-wall', (6, 22), (10, 38))
        self.add_arc('left-corner', (10, 38), (14, 42), radius_x=4, radius_y=4, sweep=False)
        self.add_line('bottom', (14, 42), (34, 42))
        self.add_arc('right-corner', (34, 42), (38, 38), radius_x=4, radius_y=4, sweep=False)
        self.add_line('right-wall', (38, 38), (42, 22))
        self.add_contour('basket', 'left-wall', 'left-corner', 'bottom', 'right-corner', 'right-wall')
        self.relate('connect', 'rim', 'basket')
        self.add_arc('handle', (16, 22), (32, 22), radius_x=8, radius_y=16)
        self.relate('connect', 'rim', 'handle')
