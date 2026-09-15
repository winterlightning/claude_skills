"""Shopping Cart. Lucide shopping-cart contour principles. Broad rounded basket, short angled grip and relatively larger detached wheel rings; no rail in source."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '76482251-1a3c-4ca3-b8db-13d73354b42d'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart_76482251-1a3c-4ca3-b8db-13d73354b42d.svg'
AUTHOR = 'gpt-6'

class ShoppingCartLargeOpenWheels(Solo48):
    icon_id = 'shopping-cart-large-open-wheels'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')

    def build(self) -> None:
        # HRECT_L (4,8)-(44,40); larger wheel circles share y=36 and radius 4.
        self.add_line('rim-1',(4, 15),(36, 15))
        self.add_line('rim-2',(36, 15),(44, 15))
        self.add_line('right',(44,15),(41,21))
        self.add_arc('br',(41,21),(35,23),radius_x=6,radius_y=2)
        self.add_line('base',(35,23),(13,23))
        self.add_arc('bl',(13,23),(7,21),radius_x=6,radius_y=2)
        self.add_line('left',(7,21),(4,15))
        self.add_contour('basket','rim-1','rim-2','right','br','base','bl','left',closed=True)
        self.add_line('grip',(36,15),(42,8))
        self.relate('connect','grip','basket')
        for index,x in enumerate((14,34)):
            self.add_arc(f'wheel-{index}-a',(x-4,36),(x+4,36),radius_x=4)
            self.add_arc(f'wheel-{index}-b',(x+4,36),(x-4,36),radius_x=4)
            self.add_contour(f'wheel-{index}',f'wheel-{index}-a',f'wheel-{index}-b',closed=True)
