"""Deepen the basket and shorten the open handles, retaining taper.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '0e1f5c1c-a73b-4fa6-8461-d439805bfc6a'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_0e1f5c1c-a73b-4fa6-8461-d439805bfc6a.svg'
AUTHOR = 'gpt-6'

class OpenHandleShoppingBasket(Container64):
    icon_id = 'open-handle-shopping-basket'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        poly('basket',(2,18),(62,18),(54,62),(10,62),closed=True)
        for x,tip in ((14,22),(50,42)):
         line(f'handle-{x}',(x,18),(tip,2));join('basket',f'handle-{x}')
