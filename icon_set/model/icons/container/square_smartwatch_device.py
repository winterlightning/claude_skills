"""A square smartwatch face sits in front of an open curved wristband.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide watch: strap attachment; square: tangent screen corners.
The side-view band is deliberately asymmetric; its right-hand opening and inner attachment seams are retained.
Hosting (compose.py): plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-smartwatch-device SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SquareSmartwatchDevice(Container64):
    icon_id = 'square-smartwatch-device'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'smartwatch', 'device')

    def build(self) -> None:
        self.add_line('screen-0', (12, 14), (36, 14))
        self.add_arc('screen-1', (36, 14), (42, 20), radius_x=6)
        self.add_line('screen-2', (42, 20), (42, 44))
        self.add_arc('screen-3', (42, 44), (36, 50), radius_x=6)
        self.add_line('screen-4', (36, 50), (12, 50))
        self.add_arc('screen-5', (12, 50), (6, 44), radius_x=6)
        self.add_line('screen-6', (6, 44), (6, 20))
        self.add_arc('screen-7', (6, 20), (12, 14), radius_x=6)
        self.add_arc('band-top-0', (14, 14), (24, 6), radius_x=13)
        self.add_line('band-top-1', (24, 6), (44, 6))
        self.add_arc('band-top-2', (44, 6), (58, 26), radius_x=14, radius_y=20)
        self.add_arc('band-bottom-0', (58, 38), (44, 58), radius_x=14, radius_y=20)
        self.add_line('band-bottom-1', (44, 58), (24, 58))
        self.add_arc('band-bottom-2', (24, 58), (14, 50), radius_x=13)
        self.add_arc('inner-top', (34, 14), (44, 6), radius_x=12)
        self.add_arc('inner-bottom', (44, 58), (34, 50), radius_x=12)
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.add_contour('band-top', 'band-top-0', 'band-top-1', 'band-top-2')
        self.add_contour('band-bottom', 'band-bottom-0', 'band-bottom-1', 'band-bottom-2')
        self.relate('connect', 'band-top', 'screen')
        self.relate('connect', 'band-bottom', 'screen')
        self.relate('connect', 'inner-top', 'screen')
        self.relate('connect', 'inner-bottom', 'screen')
        self.relate('connect', 'inner-top', 'band-top')
        self.relate('connect', 'inner-bottom', 'band-bottom')
