"""A tapered shopping bag with a tall arched carrying handle.

Keyshape VRECT_XL: (4, 0, 60, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide shopping-bag informs the simple joined bag outline.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (retail-shopping-bag VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RetailShoppingBag(Container64):
    icon_id = 'retail-shopping-bag'
    keyshape = Keyshape.VRECT_L
    aliases = ('retail-bag',)
    keywords = ('retail', 'shopping', 'bag')

    def build(self) -> None:
        # Sides closer to upright (13..51 at the rim) and the handle rising from the rim instead of from inside
        # the bag, so the bag holds a symbol of 27 with a 4 px gap (was 23.5). Mirrored about x = 32.
        self.add_line('bag-1', (13, 17), (51, 17))
        self.add_line('bag-2', (51, 17), (54, 60))
        self.add_line('bag-3', (54, 60), (10, 60))
        self.add_line('bag-4', (10, 60), (13, 17))
        self.add_line('handle-left', (23, 17), (23, 13))
        self.add_arc('handle-arch', (23, 13), (41, 13), radius_x=9)
        self.add_line('handle-right', (41, 13), (41, 17))
        self.add_contour('bag', 'bag-1', 'bag-2', 'bag-3', 'bag-4', closed=True)
        self.add_contour('handle', 'handle-left', 'handle-arch', 'handle-right')
        self.relate('connect', 'bag', 'handle')
