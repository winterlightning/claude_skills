"""A hand grips a smartphone with an open screen and a bottom bezel.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide smartphone quarter-circle enclosure informs the phone; no useful exact hand match was found..
The grip intentionally interrupts the right phone edge; hand and wrist retain their directional asymmetry.
Hosting measured with compose.py: plus: pass; heart: does not clear; check: pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (hand-holding-smartphone SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class HandHoldingSmartphone(Container64):
    icon_id = 'hand-holding-smartphone'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('hand', 'holding', 'smartphone')

    def build(self) -> None:
        self.add_line('phone-top', (11, 6), (32, 6))
        self.add_arc('phone-ne', (32, 6), (38, 11), radius_x=6, radius_y=5)
        self.add_line('phone-right', (38, 11), (38, 29))
        self.add_line('thumb-top', (43, 29), (32, 28))
        self.add_arc('thumb-end', (32, 28), (32, 36), radius_x=4, sweep=False)
        self.add_line('thumb-bottom', (32, 36), (38, 35))
        self.add_arc('palm', (38, 35), (48, 47), radius_x=10, radius_y=12, sweep=False)
        self.add_line('wrist-bottom', (48, 47), (58, 47))
        self.add_line('phone-lower', (38, 47), (38, 53))
        self.add_arc('phone-se', (38, 53), (32, 58), radius_x=6, radius_y=5)
        self.add_line('phone-bottom', (32, 58), (11, 58))
        self.add_arc('phone-sw', (11, 58), (6, 53), radius_x=5)
        self.add_line('phone-left', (6, 53), (6, 11))
        self.add_arc('phone-nw', (6, 11), (11, 6), radius_x=5)
        self.add_line('hand-top-1', (38, 15), (43, 15))
        self.add_line('hand-top-2', (43, 15), (53, 23))
        self.add_line('hand-top-3', (53, 23), (58, 23))
        self.add_line('bezel', (6, 49), (38, 49))
        self.add_contour('grip', 'thumb-top', 'thumb-end', 'thumb-bottom', 'palm', 'wrist-bottom')
        self.add_contour('phone', 'phone-lower', 'phone-se', 'phone-bottom', 'phone-sw', 'phone-left', 'phone-nw', 'phone-top', 'phone-ne', 'phone-right')
        self.add_contour('hand-top', 'hand-top-1', 'hand-top-2', 'hand-top-3')
        self.relate('connect', 'phone', 'grip')
        self.relate('connect', 'hand-top', 'phone')
        self.relate('connect', 'bezel', 'phone')
