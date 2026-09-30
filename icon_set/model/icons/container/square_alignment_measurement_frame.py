"""A rounded square measurement frame with two inward ticks per edge. Unifies the shorter and longer tick references.

Keyshape: SQUARE; centerline extremes recorded in build.
Construction reference: Lucide scan: repeated quarter-circle frame corners.. Mirrored about x=32.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-alignment-measurement-frame SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SquareAlignmentMeasurementFrame(Container64):
    icon_id = 'square-alignment-measurement-frame'
    keyshape = Keyshape.SQUARE
    aliases = ('square-grid-layout',)
    keywords = ('square', 'alignment', 'measurement', 'frame')

    def build(self) -> None:
        self.add_line('frame-top', (14, 6), (50, 6))
        self.add_arc('frame-ne', (50, 6), (58, 14), radius_x=8)
        self.add_line('frame-right', (58, 14), (58, 50))
        self.add_arc('frame-se', (58, 50), (50, 58), radius_x=8)
        self.add_line('frame-bottom', (50, 58), (14, 58))
        self.add_arc('frame-sw', (14, 58), (6, 50), radius_x=8)
        self.add_line('frame-left', (6, 50), (6, 14))
        self.add_arc('frame-nw', (6, 14), (14, 6), radius_x=8)
        self.add_line('tick-top-0', (24, 6), (24, 14))
        self.add_line('tick-bottom-0', (24, 50), (24, 58))
        self.add_line('tick-left-0', (6, 24), (14, 24))
        self.add_line('tick-right-0', (50, 24), (58, 24))
        self.add_line('tick-top-1', (40, 6), (40, 14))
        self.add_line('tick-bottom-1', (40, 50), (40, 58))
        self.add_line('tick-left-1', (6, 40), (14, 40))
        self.add_line('tick-right-1', (50, 40), (58, 40))
        self.add_contour('frame', 'frame-top', 'frame-ne', 'frame-right', 'frame-se', 'frame-bottom', 'frame-sw', 'frame-left', 'frame-nw', closed=True)
        self.relate('connect', 'tick-top-0', 'frame')
        self.relate('connect', 'tick-bottom-0', 'frame')
        self.relate('connect', 'tick-left-0', 'frame')
        self.relate('connect', 'tick-right-0', 'frame')
        self.relate('connect', 'tick-top-1', 'frame')
        self.relate('connect', 'tick-bottom-1', 'frame')
        self.relate('connect', 'tick-left-1', 'frame')
        self.relate('connect', 'tick-right-1', 'frame')
