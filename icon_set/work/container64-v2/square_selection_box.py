"""A selection frame with four rounded square resize handles.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide square: matching tangent corners.
Four handles mirrored around both central axes; no details dropped.
Hosting (compose.py): plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-selection-box SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class SquareSelectionBox(Container64):
    icon_id = 'square-selection-box'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'selection', 'box')

    def build(self) -> None:
        self.add_line('nw-0', (9, 6), (15, 6))
        self.add_arc('nw-1', (15, 6), (18, 9), radius_x=3)
        self.add_line('nw-2', (18, 9), (18, 15))
        self.add_arc('nw-3', (18, 15), (15, 18), radius_x=3)
        self.add_line('nw-4', (15, 18), (9, 18))
        self.add_arc('nw-5', (9, 18), (6, 15), radius_x=3)
        self.add_line('nw-6', (6, 15), (6, 9))
        self.add_arc('nw-7', (6, 9), (9, 6), radius_x=3)
        self.add_line('ne-0', (49, 6), (55, 6))
        self.add_arc('ne-1', (55, 6), (58, 9), radius_x=3)
        self.add_line('ne-2', (58, 9), (58, 15))
        self.add_arc('ne-3', (58, 15), (55, 18), radius_x=3)
        self.add_line('ne-4', (55, 18), (49, 18))
        self.add_arc('ne-5', (49, 18), (46, 15), radius_x=3)
        self.add_line('ne-6', (46, 15), (46, 9))
        self.add_arc('ne-7', (46, 9), (49, 6), radius_x=3)
        self.add_line('se-0', (49, 46), (55, 46))
        self.add_arc('se-1', (55, 46), (58, 49), radius_x=3)
        self.add_line('se-2', (58, 49), (58, 55))
        self.add_arc('se-3', (58, 55), (55, 58), radius_x=3)
        self.add_line('se-4', (55, 58), (49, 58))
        self.add_arc('se-5', (49, 58), (46, 55), radius_x=3)
        self.add_line('se-6', (46, 55), (46, 49))
        self.add_arc('se-7', (46, 49), (49, 46), radius_x=3)
        self.add_line('sw-0', (9, 46), (15, 46))
        self.add_arc('sw-1', (15, 46), (18, 49), radius_x=3)
        self.add_line('sw-2', (18, 49), (18, 55))
        self.add_arc('sw-3', (18, 55), (15, 58), radius_x=3)
        self.add_line('sw-4', (15, 58), (9, 58))
        self.add_arc('sw-5', (9, 58), (6, 55), radius_x=3)
        self.add_line('sw-6', (6, 55), (6, 49))
        self.add_arc('sw-7', (6, 49), (9, 46), radius_x=3)
        self.add_line('top', (18, 12), (46, 12))
        self.add_line('right', (52, 18), (52, 46))
        self.add_line('bottom', (46, 52), (18, 52))
        self.add_line('left', (12, 46), (12, 18))
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
