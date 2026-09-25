"""Closed Cardboard Shipping Box: independently authored container.

Construction plan: Front box with shallow trapezoid top and two tape seams; the reference is frontal, not isometric.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/shipping/package_77c6bcd1-df40-4a4c-8496-bcdb8d646c03.svg. Lucide package original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '77c6bcd1-df40-4a4c-8496-bcdb8d646c03'
SOURCE_PATH = 'pictographic-primitives/shipping/package_77c6bcd1-df40-4a4c-8496-bcdb8d646c03.svg'
AUTHOR = 'gpt-6'


class ShippingBoxContainer(Container64):
    icon_id = 'shipping-box-container'
    category = 'shipping'
    categories = ('shipping', 'other', 'primitives-generate')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('shipping', 'box', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('box',(2,18),(12,2),(52,2),(62,18),(62,62),(2,62),closed=True)
        line('fold',(2,18),(62,18));join('fold','box')
        for x in (26,38):line(f'tape-{x}',(x,2),(x,18));join(f'tape-{x}','box');join(f'tape-{x}','fold')
