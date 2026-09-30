"""Closed Cardboard Shipping Box: independently authored container.

Construction plan: Front box with shallow trapezoid top and two tape seams; the reference is frontal, not isometric.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/shipping/package_77c6bcd1-df40-4a4c-8496-bcdb8d646c03.svg. Lucide package original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (shipping-box-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '77c6bcd1-df40-4a4c-8496-bcdb8d646c03'
SOURCE_PATH = 'pictographic-primitives/shipping/package_77c6bcd1-df40-4a4c-8496-bcdb8d646c03.svg'
AUTHOR = 'claude-opus-5-5'


class ShippingBoxContainer(Container64):
    icon_id = 'shipping-box-container'
    keyshape = Keyshape.SQUARE
    category = 'shipping'
    categories = ('shipping', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('shipping', 'box', 'container')

    def build(self) -> None:
        self.add_line('box-1', (6, 20), (15, 6))
        self.add_line('box-2', (15, 6), (49, 6))
        self.add_line('box-3', (49, 6), (58, 20))
        self.add_line('box-4', (58, 20), (58, 58))
        self.add_line('box-5', (58, 58), (6, 58))
        self.add_line('box-6', (6, 58), (6, 20))
        self.add_line('fold', (6, 20), (58, 20))
        self.add_line('tape-26', (27, 6), (27, 20))
        self.add_line('tape-38', (37, 6), (37, 20))
        self.add_contour('box', 'box-1', 'box-2', 'box-3', 'box-4', 'box-5', 'box-6', closed=True)
        self.relate('connect', 'fold', 'box')
        self.relate('connect', 'tape-26', 'box')
        self.relate('connect', 'tape-26', 'fold')
        self.relate('connect', 'tape-38', 'box')
        self.relate('connect', 'tape-38', 'fold')
