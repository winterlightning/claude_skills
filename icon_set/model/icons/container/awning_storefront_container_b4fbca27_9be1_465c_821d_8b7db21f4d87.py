"""Raise the awning and broaden the storefront opening.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (awning-storefront-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.


v3 (2026-10-07): redrawn as a horizontal storefront (HRECT_L) with a full scalloped awning so shop signs fit: 4 letters, 5 letters smaller.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'b4fbca27-9be1-465c-821d-8b7db21f4d87'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_b4fbca27-9be1-465c-821d-8b7db21f4d87.svg'
AUTHOR = 'claude-opus-5-5'


class AwningStorefrontContainer(Container64):
    icon_id = 'awning-storefront-container'
    keyshape = Keyshape.HRECT_L
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # HRECT_L (was SQUARE): a wide shopfront. The awning spans the frame (top 10, eaves at 17) with four full
        # scallops (rx 7, ry 5) down to 22, and the walls fall from its outer corners to the floor at 54. The front
        # is 44 wide, so a 4-letter sign fits and a 5-letter one comes out smaller; symbols take 20 (24 when their
        # ink keeps 2 px). Mirrored about x = 32.
        self.add_line('awning-0', (4, 17), (10, 10))
        self.add_line('awning-1', (10, 10), (54, 10))
        self.add_line('awning-2', (54, 10), (60, 17))
        self.add_arc('awning-3', (60, 17), (46, 17), radius_x=7, radius_y=5)
        self.add_arc('awning-4', (46, 17), (32, 17), radius_x=7, radius_y=5)
        self.add_arc('awning-5', (32, 17), (18, 17), radius_x=7, radius_y=5)
        self.add_arc('awning-6', (18, 17), (4, 17), radius_x=7, radius_y=5)
        self.add_line('shop-1', (4, 17), (4, 54))
        self.add_line('shop-2', (4, 54), (60, 54))
        self.add_line('shop-3', (60, 54), (60, 17))
        self.add_contour('awning', 'awning-0', 'awning-1', 'awning-2', 'awning-3', 'awning-4', 'awning-5', 'awning-6', closed=True)
        self.add_contour('shop', 'shop-1', 'shop-2', 'shop-3')
        self.relate('connect', 'shop', 'awning')
