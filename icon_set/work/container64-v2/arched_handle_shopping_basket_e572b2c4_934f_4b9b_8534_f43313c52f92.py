"""Deepen the basket body while retaining the arched handle and rim.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (arched-handle-shopping-basket SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'e572b2c4-934f-4b9b-8534-f43313c52f92'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping basket_e572b2c4-934f-4b9b-8534-f43313c52f92.svg'
AUTHOR = 'claude-opus-5-5'


class ArchedHandleShoppingBasket(Container64):
    icon_id = 'arched-handle-shopping-basket'
    keyshape = Keyshape.SQUARE
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('basket-1', (10, 20), (16, 58))
        self.add_line('basket-2', (16, 58), (48, 58))
        self.add_line('basket-3', (48, 58), (54, 20))
        self.add_line('rim', (6, 20), (58, 20))
        self.add_line('handle-0', (10, 20), (20, 10))
        self.add_arc('handle-1', (20, 10), (28, 6), radius_x=10)
        self.add_line('handle-2', (28, 6), (36, 6))
        self.add_arc('handle-3', (36, 6), (44, 10), radius_x=10)
        self.add_line('handle-4', (44, 10), (54, 20))
        self.add_contour('basket', 'basket-1', 'basket-2', 'basket-3')
        self.add_contour('handle', 'handle-0', 'handle-1', 'handle-2', 'handle-3', 'handle-4')
        self.relate('connect', 'rim', 'basket')
        self.relate('connect', 'handle', 'basket')
        self.relate('connect', 'handle', 'rim')
