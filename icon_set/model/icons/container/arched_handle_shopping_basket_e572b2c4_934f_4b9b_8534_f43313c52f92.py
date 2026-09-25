"""Deepen the basket body while retaining the arched handle and rim.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'e572b2c4-934f-4b9b-8534-f43313c52f92'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping basket_e572b2c4-934f-4b9b-8534-f43313c52f92.svg'
AUTHOR = 'gpt-6'

class ArchedHandleShoppingBasket(Container64):
    icon_id = 'arched-handle-shopping-basket'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        poly('basket',(6,18),(12,62),(52,62),(58,18))
        line('rim',(2,18),(62,18));join('rim','basket')
        path(self,'handle',(6,18),[('L',(16,6)),('A',(24,2),10,10,True),('L',(40,2)),('A',(48,6),10,10,True),('L',(58,18))]);join('handle','basket');join('handle','rim')
