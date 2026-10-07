"""A selection frame with four rounded square resize handles.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide square: matching tangent corners.
Four handles mirrored around both central axes; no details dropped.
Hosting (compose.py): plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-selection-box SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SquareSelectionBox(Container64):
    icon_id = 'square-selection-box'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'selection', 'box')

    def build(self) -> None:
        # Corner handles 10 x 10 (6..16 and 48..58) with the frame edges on their centre lines (11 and 53), so the
        # frame holds a symbol of 25 with a 4 px gap (was 21).
        self.add_line('nw-0', (9, 6), (13, 6))
        self.add_arc('nw-1', (13, 6), (16, 9), radius_x=3)
        self.add_line('nw-2', (16, 9), (16, 13))
        self.add_arc('nw-3', (16, 13), (13, 16), radius_x=3)
        self.add_line('nw-4', (13, 16), (9, 16))
        self.add_arc('nw-5', (9, 16), (6, 13), radius_x=3)
        self.add_line('nw-6', (6, 13), (6, 9))
        self.add_arc('nw-7', (6, 9), (9, 6), radius_x=3)
        self.add_line('ne-0', (51, 6), (55, 6))
        self.add_arc('ne-1', (55, 6), (58, 9), radius_x=3)
        self.add_line('ne-2', (58, 9), (58, 13))
        self.add_arc('ne-3', (58, 13), (55, 16), radius_x=3)
        self.add_line('ne-4', (55, 16), (51, 16))
        self.add_arc('ne-5', (51, 16), (48, 13), radius_x=3)
        self.add_line('ne-6', (48, 13), (48, 9))
        self.add_arc('ne-7', (48, 9), (51, 6), radius_x=3)
        self.add_line('se-0', (51, 48), (55, 48))
        self.add_arc('se-1', (55, 48), (58, 51), radius_x=3)
        self.add_line('se-2', (58, 51), (58, 55))
        self.add_arc('se-3', (58, 55), (55, 58), radius_x=3)
        self.add_line('se-4', (55, 58), (51, 58))
        self.add_arc('se-5', (51, 58), (48, 55), radius_x=3)
        self.add_line('se-6', (48, 55), (48, 51))
        self.add_arc('se-7', (48, 51), (51, 48), radius_x=3)
        self.add_line('sw-0', (9, 48), (13, 48))
        self.add_arc('sw-1', (13, 48), (16, 51), radius_x=3)
        self.add_line('sw-2', (16, 51), (16, 55))
        self.add_arc('sw-3', (16, 55), (13, 58), radius_x=3)
        self.add_line('sw-4', (13, 58), (9, 58))
        self.add_arc('sw-5', (9, 58), (6, 55), radius_x=3)
        self.add_line('sw-6', (6, 55), (6, 51))
        self.add_arc('sw-7', (6, 51), (9, 48), radius_x=3)
        self.add_line('top', (16, 11), (48, 11))
        self.add_line('right', (53, 16), (53, 48))
        self.add_line('bottom', (48, 53), (16, 53))
        self.add_line('left', (11, 48), (11, 16))
        self.add_contour('nw', 'nw-0', 'nw-1', 'nw-2', 'nw-3', 'nw-4', 'nw-5', 'nw-6', 'nw-7', closed=True)
        self.add_contour('ne', 'ne-0', 'ne-1', 'ne-2', 'ne-3', 'ne-4', 'ne-5', 'ne-6', 'ne-7', closed=True)
        self.add_contour('se', 'se-0', 'se-1', 'se-2', 'se-3', 'se-4', 'se-5', 'se-6', 'se-7', closed=True)
        self.add_contour('sw', 'sw-0', 'sw-1', 'sw-2', 'sw-3', 'sw-4', 'sw-5', 'sw-6', 'sw-7', closed=True)
        self.relate('connect', 'top', 'nw')
        self.relate('connect', 'top', 'ne')
        self.relate('connect', 'right', 'ne')
        self.relate('connect', 'right', 'se')
        self.relate('connect', 'bottom', 'se')
        self.relate('connect', 'bottom', 'sw')
        self.relate('connect', 'left', 'sw')
        self.relate('connect', 'left', 'nw')
