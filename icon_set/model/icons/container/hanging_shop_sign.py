"""A blank rounded sign suspended by a triangular cord.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide smartphone rounded panel construction and signpost attached support inform the enclosure..
No identity features omitted.
Hosting measured with compose.py: plus: does not clear; heart: does not clear; check: does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (hanging-shop-sign SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class HangingShopSign(Container64):
    icon_id = 'hanging-shop-sign'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('hanging', 'shop', 'sign')

    def build(self) -> None:
        self.add_line('panel-0', (12, 20), (52, 20))
        self.add_arc('panel-1', (52, 20), (58, 26), radius_x=6)
        self.add_line('panel-2', (58, 26), (58, 52))
        self.add_arc('panel-3', (58, 52), (52, 58), radius_x=6)
        self.add_line('panel-4', (52, 58), (12, 58))
        self.add_arc('panel-5', (12, 58), (6, 52), radius_x=6)
        self.add_line('panel-6', (6, 52), (6, 26))
        self.add_arc('panel-7', (6, 26), (12, 20), radius_x=6)
        self.add_line('cord-1', (20, 20), (32, 6))
        self.add_line('cord-2', (32, 6), (44, 20))
        self.add_contour('panel', 'panel-0', 'panel-1', 'panel-2', 'panel-3', 'panel-4', 'panel-5', 'panel-6', 'panel-7', closed=True)
        self.add_contour('cord', 'cord-1', 'cord-2')
        self.relate('connect', 'panel', 'cord')
