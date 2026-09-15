"""An empty landscape frame has four matching rounded corners.

Keyshape HRECT_L: visible bounds (0, 8, 64, 56).
Lucide rectangle-horizontal informs straight runs meeting quarter-circle corners.
The source is visibly wider than tall despite its square label.
Centerline extremes (2,10)-(62,54); radius 6. No features removed.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class EmptyRoundedRectangle(Container64):
    icon_id = 'empty-rounded-rectangle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('empty-rounded-square-shape', 'rounded-rectangle-container')
    keywords = ('frame', 'rectangle', 'rounded', 'border')

    def build(self) -> None:
        self.add_line('frame-top', (8, 10), (56, 10))
        self.add_arc('frame-ne', (56, 10), (62, 16), radius_x=6, radius_y=6, sweep=True)
        self.add_line('frame-right', (62, 16), (62, 48))
        self.add_arc('frame-se', (62, 48), (56, 54), radius_x=6, radius_y=6, sweep=True)
        self.add_line('frame-bottom', (56, 54), (8, 54))
        self.add_arc('frame-sw', (8, 54), (2, 48), radius_x=6, radius_y=6, sweep=True)
        self.add_line('frame-left', (2, 48), (2, 16))
        self.add_arc('frame-nw', (2, 16), (8, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('frame', 'frame-top', 'frame-ne', 'frame-right', 'frame-se', 'frame-bottom', 'frame-sw', 'frame-left', 'frame-nw', closed=True)
