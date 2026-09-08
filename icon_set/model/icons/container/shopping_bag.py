"""A tapered shopping bag with an arched carry handle.

VRECT_XL: (4, 0, 60, 64); chosen for the source silhouette.
Lucide shopping-bag: simple body and a single curved handle; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus passes, heart blocked, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class ShoppingBag(Container64):
    icon_id = 'shopping-bag'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('shopping', 'bag')

    def build(self) -> None:
        self.add_line('bag-0', (12, 20), (52, 20))
        self.add_line('bag-1', (52, 20), (58, 62))
        self.add_line('bag-2', (58, 62), (6, 62))
        self.add_line('bag-3', (6, 62), (12, 20))
        self.add_contour('bag', 'bag-0', 'bag-1', 'bag-2', 'bag-3', closed=True)
        self.add_line('handle-0', (20, 30), (20, 14))
        self.add_arc('handle-1', (20, 14), (44, 14), radius_x=12, radius_y=12, sweep=True)
        self.add_line('handle-2', (44, 14), (44, 30))
        self.add_contour('handle', 'handle-0', 'handle-1', 'handle-2', closed=False)
        self.relate("connect", "bag", "handle")
