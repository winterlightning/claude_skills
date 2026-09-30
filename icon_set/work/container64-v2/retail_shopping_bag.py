"""A tapered shopping bag with a tall arched carrying handle.

Keyshape VRECT_XL: (4, 0, 60, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide shopping-bag informs the simple joined bag outline.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (retail-shopping-bag VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class RetailShoppingBag(Container64):
    icon_id = 'retail-shopping-bag'
    keyshape = Keyshape.VRECT_L
    aliases = ('retail-bag',)
    keywords = ('retail', 'shopping', 'bag')

    def build(self) -> None:
        self.add_line('bag-1', (16, 17), (48, 17))
        self.add_line('bag-2', (48, 17), (54, 60))
        self.add_line('bag-3', (54, 60), (10, 60))
        self.add_line('bag-4', (10, 60), (16, 17))
        self.add_line('handle-left', (24, 22), (23, 13))
        self.add_arc('handle-arch', (23, 13), (41, 13), radius_x=9)
        self.add_line('handle-right', (41, 13), (40, 22))
        self.add_contour('bag', 'bag-1', 'bag-2', 'bag-3', 'bag-4', closed=True)
        self.add_contour('handle', 'handle-left', 'handle-arch', 'handle-right')
        self.relate('connect', 'bag', 'handle')
