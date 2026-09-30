"""An empty landscape frame has four matching rounded corners.

Keyshape HRECT_L: visible bounds (0, 8, 64, 56).
Lucide rectangle-horizontal informs straight runs meeting quarter-circle corners.
The source is visibly wider than tall despite its square label.
Centerline extremes (2,10)-(62,54); radius 6. No features removed.
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (empty-rounded-rectangle HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class EmptyRoundedRectangle(Container64):
    icon_id = 'empty-rounded-rectangle'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('empty-rounded-square-shape', 'rounded-rectangle-container')
    keywords = ('frame', 'rectangle', 'rounded', 'border')

    def build(self) -> None:
        self.add_line('frame-top', (10, 12), (54, 12))
        self.add_arc('frame-ne', (54, 12), (60, 18), radius_x=6)
        self.add_line('frame-right', (60, 18), (60, 46))
        self.add_arc('frame-se', (60, 46), (54, 52), radius_x=6)
        self.add_line('frame-bottom', (54, 52), (10, 52))
        self.add_arc('frame-sw', (10, 52), (4, 46), radius_x=6)
        self.add_line('frame-left', (4, 46), (4, 18))
        self.add_arc('frame-nw', (4, 18), (10, 12), radius_x=6)
        self.add_contour('frame', 'frame-top', 'frame-ne', 'frame-right', 'frame-se', 'frame-bottom', 'frame-sw', 'frame-left', 'frame-nw', closed=True)
