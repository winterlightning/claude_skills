"""Deepen the basket and shorten the open handles, retaining taper.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (open-handle-shopping-basket SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '0e1f5c1c-a73b-4fa6-8461-d439805bfc6a'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_0e1f5c1c-a73b-4fa6-8461-d439805bfc6a.svg'
AUTHOR = 'claude-opus-5-5'


class OpenHandleShoppingBasket(Container64):
    icon_id = 'open-handle-shopping-basket'
    keyshape = Keyshape.SQUARE
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('basket-1', (6, 20), (58, 20))
        self.add_line('basket-2', (58, 20), (50, 58))
        self.add_line('basket-3', (50, 58), (14, 58))
        self.add_line('basket-4', (14, 58), (6, 20))
        self.add_line('handle-14', (18, 20), (26, 6))
        self.add_line('handle-50', (46, 20), (38, 6))
        self.add_contour('basket', 'basket-1', 'basket-2', 'basket-3', 'basket-4', closed=True)
        self.relate('connect', 'basket', 'handle-14')
        self.relate('connect', 'basket', 'handle-50')
