"""Raise the awning and broaden the storefront opening.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (awning-storefront-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'b4fbca27-9be1-465c-821d-8b7db21f4d87'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_b4fbca27-9be1-465c-821d-8b7db21f4d87.svg'
AUTHOR = 'claude-opus-5-5'


class AwningStorefrontContainer(Container64):
    icon_id = 'awning-storefront-container'
    keyshape = Keyshape.SQUARE
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('awning-0', (6, 14), (12, 6))
        self.add_line('awning-1', (12, 6), (52, 6))
        self.add_line('awning-2', (52, 6), (58, 14))
        self.add_arc('awning-3', (58, 14), (40, 14), radius_x=9, radius_y=6)
        self.add_arc('awning-4', (40, 14), (24, 14), radius_x=8, radius_y=6)
        self.add_arc('awning-5', (24, 14), (6, 14), radius_x=9, radius_y=6)
        self.add_line('shop-1', (16, 20), (14, 20))
        self.add_line('shop-2', (14, 20), (14, 58))
        self.add_line('shop-3', (14, 58), (50, 58))
        self.add_line('shop-4', (50, 58), (50, 20))
        self.add_line('shop-5', (50, 20), (48, 20))
        self.add_contour('awning', 'awning-0', 'awning-1', 'awning-2', 'awning-3', 'awning-4', 'awning-5', closed=True)
        self.add_contour('shop', 'shop-1', 'shop-2', 'shop-3', 'shop-4', 'shop-5')
        self.relate('connect', 'shop', 'awning')
