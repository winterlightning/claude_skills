"""A hand grips a smartphone with an open screen and a bottom bezel.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide smartphone quarter-circle enclosure informs the phone; no useful exact hand match was found..
The grip intentionally interrupts the right phone edge; hand and wrist retain their directional asymmetry.
Hosting measured with compose.py: plus: pass; heart: does not clear; check: pass.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class HandHoldingSmartphone(Container64):
    icon_id = "hand-holding-smartphone"
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('hand', 'holding', 'smartphone')

    def build(self) -> None:
        self.add_line('phone-top', (8, 2), (32, 2))
        self.add_arc('phone-ne', (32, 2), (38, 8), radius_x=6, sweep=True)
        self.add_line('phone-right', (38, 8), (38, 26))
        self.add_line('thumb-top', (44, 26), (32, 26))
        self.add_arc('thumb-end', (32, 26), (32, 38), radius_x=6, sweep=False)
        self.add_line('thumb-bottom', (32, 38), (38, 38))
        self.add_arc('palm', (38, 38), (50, 50), radius_x=12, sweep=False)
        self.add_line('wrist-bottom', (50, 50), (62, 50))
        self.add_contour('grip', 'thumb-top', 'thumb-end', 'thumb-bottom', 'palm', 'wrist-bottom', closed=False)
        self.add_line('phone-lower', (38, 50), (38, 56))
        self.add_arc('phone-se', (38, 56), (32, 62), radius_x=6, sweep=True)
        self.add_line('phone-bottom', (32, 62), (8, 62))
        self.add_arc('phone-sw', (8, 62), (2, 56), radius_x=6, sweep=True)
        self.add_line('phone-left', (2, 56), (2, 8))
        self.add_arc('phone-nw', (2, 8), (8, 2), radius_x=6, sweep=True)
        self.add_contour('phone', 'phone-lower', 'phone-se', 'phone-bottom', 'phone-sw', 'phone-left', 'phone-nw', 'phone-top', 'phone-ne', 'phone-right', closed=False)
        self.relate("connect", 'phone', 'grip')
        self.add_polyline('hand-top', (38, 12), (44, 12), (56, 20), (62, 20), closed=False)
        self.relate("connect", 'hand-top', 'phone')
        self.add_line('bezel', (2, 52), (38, 52))
        self.relate("connect", 'bezel', 'phone')
