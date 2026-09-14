"""Full Shopping Cart. Lucide shopping-cart construction. Deliberately asymmetric groceries: tall tilted package and peaked package. Lower rail and both wheels retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '630d9a1b-993a-4e00-8596-860eb78fdae3'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart full_630d9a1b-993a-4e00-8596-860eb78fdae3.svg'
AUTHOR = 'gpt-6'

class FullShoppingCart(Solo48):
    icon_id = 'full-shopping-cart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('cart', 'shopping', 'groceries', 'packages', 'trolley', 'full', 'retail')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42); groceries above the rim establish a full cart.
        self.add_polyline('basket',(6,18),(38,18),(34,27),(10,27),(6,18),closed=True)
        self.add_polyline('handle',(38,18),(40,10),(42,10))
        self.relate('connect','handle','basket')
        self.add_polyline('tall-package',(10,18),(8,6),(18,6),(20,18))
        self.add_polyline('roof-package',(24,18),(30,10),(38,18))
        self.relate('connect','tall-package','basket')
        self.relate('connect','roof-package','basket')
        for index,x in enumerate((14,32)):
            self.add_arc(f'wheel-{index}-a',(x,36),(x,42),radius_x=3)
            self.add_arc(f'wheel-{index}-b',(x,42),(x,36),radius_x=3)
            self.add_contour(f'wheel-{index}',f'wheel-{index}-a',f'wheel-{index}-b',closed=True)
        self.add_line('rail',(14,36),(32,36))
        for index in range(2):self.relate('connect','rail',f'wheel-{index}')
