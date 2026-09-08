"""A blank rounded sign suspended by a triangular cord.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide smartphone rounded panel construction and signpost attached support inform the enclosure..
No identity features omitted.
Hosting measured with compose.py: plus: does not clear; heart: does not clear; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class HangingShopSign(Container64):
    icon_id = "hanging-shop-sign"
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('hanging', 'shop', 'sign')

    def build(self) -> None:
        self.add_line('panel-0', (8, 16), (56, 16))
        self.add_arc('panel-1', (56, 16), (62, 22), radius_x=6, sweep=True)
        self.add_line('panel-2', (62, 22), (62, 56))
        self.add_arc('panel-3', (62, 56), (56, 62), radius_x=6, sweep=True)
        self.add_line('panel-4', (56, 62), (8, 62))
        self.add_arc('panel-5', (8, 62), (2, 56), radius_x=6, sweep=True)
        self.add_line('panel-6', (2, 56), (2, 22))
        self.add_arc('panel-7', (2, 22), (8, 16), radius_x=6, sweep=True)
        self.add_contour('panel', 'panel-0', 'panel-1', 'panel-2', 'panel-3', 'panel-4', 'panel-5', 'panel-6', 'panel-7', closed=True)
        self.add_polyline('cord', (16, 16), (32, 2), (48, 16), closed=False)
        self.relate("connect", 'panel', 'cord')
