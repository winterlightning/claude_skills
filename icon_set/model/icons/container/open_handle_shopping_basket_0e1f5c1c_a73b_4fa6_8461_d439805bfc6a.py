"""Minimal Shopping Basket: independently authored container.

Construction plan: One trapezoid with two mirrored open handle strokes; omit basket lattice absent from source.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/shopping/cart_0e1f5c1c-a73b-4fa6-8461-d439805bfc6a.svg. Lucide shopping-basket original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '0e1f5c1c-a73b-4fa6-8461-d439805bfc6a'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_0e1f5c1c-a73b-4fa6-8461-d439805bfc6a.svg'
AUTHOR = 'gpt-6'


class OpenHandleShoppingBasket(Container64):
    icon_id = 'open-handle-shopping-basket'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('open', 'handle', 'shopping', 'basket')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('basket',(2,28),(62,28),(52,58),(12,58),closed=True)
        for x,tip in ((14,25),(50,39)):
         line(f'handle-{x}',(x,28),(tip,6));join('basket',f'handle-{x}')
