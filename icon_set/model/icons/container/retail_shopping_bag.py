"""A tapered shopping bag with a tall arched carrying handle.

Keyshape VRECT_XL: (4, 0, 60, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide shopping-bag informs the simple joined bag outline.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus does not clear, heart does not clear, check does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class RetailShoppingBag(Container64):
    icon_id = 'retail-shopping-bag'
    keyshape = Keyshape.VRECT_XL
    aliases = ('retail-bag',)
    keywords = ('retail', 'shopping', 'bag')

    def build(self) -> None:
        self.add_polyline('bag', (12, 16), (52, 16), (58, 62), (6, 62), closed=True)
        self.add_line('handle-left', (21, 21), (21, 13))
        self.add_arc('handle-arch', (21, 13), (43, 13), radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_line('handle-right', (43, 13), (43, 21))
        self.add_contour('handle', 'handle-left', 'handle-arch', 'handle-right', closed=False)
        self.relate("connect", 'bag', 'handle')
