"""A square smartwatch face sits in front of an open curved wristband.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide watch: strap attachment; square: tangent screen corners.
The side-view band is deliberately asymmetric; its right-hand opening and inner attachment seams are retained.
Hosting (compose.py): plus passes, heart passes, check passes.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SquareSmartwatchDevice(Container64):
    icon_id = 'square-smartwatch-device'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'smartwatch', 'device')

    def build(self) -> None:
        self.add_line('screen-0', (8, 12), (36, 12))
        self.add_arc('screen-1', (36, 12), (42, 18), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-2', (42, 18), (42, 46))
        self.add_arc('screen-3', (42, 46), (36, 52), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-4', (36, 52), (8, 52))
        self.add_arc('screen-5', (8, 52), (2, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-6', (2, 46), (2, 18))
        self.add_arc('screen-7', (2, 18), (8, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.add_arc('band-top-0', (10, 12), (24, 2), radius_x=16, radius_y=16, sweep=True)
        self.add_line('band-top-1', (24, 2), (44, 2))
        self.add_arc('band-top-2', (44, 2), (62, 24), radius_x=18, radius_y=22, sweep=True)
        self.add_contour('band-top', 'band-top-0', 'band-top-1', 'band-top-2', closed=False)
        self.add_arc('band-bottom-0', (62, 40), (44, 62), radius_x=18, radius_y=22, sweep=True)
        self.add_line('band-bottom-1', (44, 62), (24, 62))
        self.add_arc('band-bottom-2', (24, 62), (10, 52), radius_x=16, radius_y=16, sweep=True)
        self.add_contour('band-bottom', 'band-bottom-0', 'band-bottom-1', 'band-bottom-2', closed=False)
        self.add_arc('inner-top', (34, 12), (44, 2), radius_x=14, radius_y=14, sweep=True)
        self.add_arc('inner-bottom', (44, 62), (34, 52), radius_x=14, radius_y=14, sweep=True)
        self.relate("connect", 'band-top', 'screen')
        self.relate("connect", 'band-bottom', 'screen')
        self.relate("connect", 'inner-top', 'screen')
        self.relate("connect", 'inner-bottom', 'screen')
        self.relate("connect", 'inner-top', 'band-top')
        self.relate("connect", 'inner-bottom', 'band-bottom')
