"""Shopping Basket. Lucide shopping-basket body and shopping-bag arch principle. Mirrored dome and blank front retained; double rim simplified."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c9188502-a980-4b81-82ef-8a7c9418de92'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping basket handle_c9188502-a980-4b81-82ef-8a7c9418de92.svg'
AUTHOR = 'gpt-6'

class ShoppingBasketDomedHandle(Solo48):
    icon_id = 'shopping-basket-domed-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    aliases = ()
    keywords = ('basket', 'shopping', 'handle', 'retail', 'groceries', 'carry', 'container')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42), broad rim with an intentionally tapered body.
        self.add_line('rim-1',(6, 20),(14, 20))
        self.add_line('rim-2',(14, 20),(34, 20))
        self.add_line('rim-3',(34, 20),(42, 20))
        self.add_line('right',(42,20),(38,38))
        self.add_arc('br',(38,38),(34,42),radius_x=4)
        self.add_line('base',(34,42),(14,42))
        self.add_arc('bl',(14,42),(10,38),radius_x=4)
        self.add_line('left',(10,38),(6,20))
        self.add_contour('body','rim-1','rim-2','rim-3','right','br','base','bl','left',closed=True)

        self.add_arc('handle',(14,20),(34,20),radius_x=10,radius_y=14)
        self.relate('connect','handle','body')
