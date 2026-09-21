"""Raise the awning and broaden the storefront opening.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'b4fbca27-9be1-465c-821d-8b7db21f4d87'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_b4fbca27-9be1-465c-821d-8b7db21f4d87.svg'
AUTHOR = 'gpt-6'

class AwningStorefrontContainer(Container64):
    icon_id = 'awning-storefront-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'awning',(2,10),[('L',(8,2)),('L',(56,2)),('L',(62,10)),('A',(42,10),10,6,True),('A',(22,10),10,6,True),('A',(2,10),10,6,True)],True)
        poly('shop',(12,16),(10,16),(10,62),(54,62),(54,16),(52,16));join('shop','awning')
