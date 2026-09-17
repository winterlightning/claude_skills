"""Storefront building with awning: independently authored container.

Construction plan: Tapered canopy with three equal scallops above a rectangular shop opening.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/shopping/shop_b4fbca27-9be1-465c-821d-8b7db21f4d87.svg. Lucide store original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
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
    keywords = ('awning', 'storefront', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'awning',(2,18),[('L',(8,2)),('L',(56,2)),('L',(62,18)),('A',(42,18),10,8,True),('A',(22,18),10,8,True),('A',(2,18),10,8,True)],True)
        poly('shop',(12,26),(12,62),(52,62),(52,26))
        join('shop','awning')
