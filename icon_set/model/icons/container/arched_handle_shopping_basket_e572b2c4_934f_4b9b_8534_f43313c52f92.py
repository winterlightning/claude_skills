"""Simple Shopping Basket: independently authored container.

Construction plan: A tapered basket and one continuous arched handle over an extended rim; no lattice absent from source.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/shopping/shopping basket_e572b2c4-934f-4b9b-8534-f43313c52f92.svg. Lucide shopping-basket original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'e572b2c4-934f-4b9b-8534-f43313c52f92'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping basket_e572b2c4-934f-4b9b-8534-f43313c52f92.svg'
AUTHOR = 'gpt-6'


class ArchedHandleShoppingBasket(Container64):
    icon_id = 'arched-handle-shopping-basket'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('arched', 'handle', 'shopping', 'basket')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('basket',(8,24),(14,58),(50,58),(56,24))
        line('rim',(2,24),(62,24));join('rim','basket')
        path(self,'handle',(8,24),[('L',(16,10)),('A',(22,6),8,8,True),('L',(42,6)),('A',(48,10),8,8,True),('L',(56,24))]);join('handle','basket');join('handle','rim')
