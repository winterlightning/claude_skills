"""A tapered shopping bag with an arched carry handle.

VRECT_XL: (4, 0, 60, 64); chosen for the source silhouette.
Lucide shopping-bag: simple body and a single curved handle; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
The shortened handle terminates at the rim, leaving the bag face clear.
Hosting is measured separately in the accompanying repair report.
"""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = '12a6aa6e-010c-419c-b6a1-fd8f3a38bd08'
SOURCE_PATH = 'icon_set/model/icons/container/shopping_bag.py'

class ShoppingBag(Container64):
    icon_id = 'shopping-bag'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('shopping', 'bag')

    def build(self) -> None:
        # The rim owns both handle attachment nodes. Neither strap enters the bag.
        self.add_line('bag-0', (12, 20), (20, 20))
        self.add_line('bag-rim-middle', (20, 20), (44, 20))
        self.add_line('bag-rim-right', (44, 20), (52, 20))
        self.add_line('bag-1', (52, 20), (58, 62))
        self.add_line('bag-2', (58, 62), (6, 62))
        self.add_line('bag-3', (6, 62), (12, 20))
        self.add_contour('bag', 'bag-0', 'bag-rim-middle', 'bag-rim-right', 'bag-1', 'bag-2', 'bag-3', closed=True)
        self.add_line('handle-0', (20, 20), (20, 14))
        self.add_arc('handle-1', (20, 14), (44, 14), radius_x=12, radius_y=12, sweep=True)
        self.add_line('handle-2', (44, 14), (44, 20))
        self.add_contour('handle', 'handle-0', 'handle-1', 'handle-2', closed=False)
        self.relate('connect', 'bag', 'handle')
