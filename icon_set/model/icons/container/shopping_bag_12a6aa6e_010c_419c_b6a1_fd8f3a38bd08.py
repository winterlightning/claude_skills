"""A tapered shopping bag with an arched carry handle.

VRECT_XL: (4, 0, 60, 64); chosen for the source silhouette.
Lucide shopping-bag: simple body and a single curved handle; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
The shortened handle terminates at the rim, leaving the bag face clear.
Hosting is measured separately in the accompanying repair report.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (shopping-bag VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '12a6aa6e-010c-419c-b6a1-fd8f3a38bd08'
SOURCE_PATH = 'icon_set/model/icons/container/shopping_bag.py'
AUTHOR = 'claude-opus-5-5'


class ShoppingBag(Container64):
    icon_id = 'shopping-bag'
    keyshape = Keyshape.VRECT_L
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('shopping', 'bag')

    def build(self) -> None:
        self.add_line('bag-0', (16, 21), (24, 21))
        self.add_line('bag-rim-middle', (24, 21), (40, 21))
        self.add_line('bag-rim-right', (40, 21), (48, 21))
        self.add_line('bag-1', (48, 21), (54, 60))
        self.add_line('bag-2', (54, 60), (10, 60))
        self.add_line('bag-3', (10, 60), (16, 21))
        self.add_line('handle-0', (24, 21), (24, 15))
        self.add_arc('handle-1', (24, 15), (40, 15), radius_x=8, radius_y=11)
        self.add_line('handle-2', (40, 15), (40, 21))
        self.add_contour('bag', 'bag-0', 'bag-rim-middle', 'bag-rim-right', 'bag-1', 'bag-2', 'bag-3', closed=True)
        self.add_contour('handle', 'handle-0', 'handle-1', 'handle-2')
        self.relate('connect', 'bag', 'handle')
