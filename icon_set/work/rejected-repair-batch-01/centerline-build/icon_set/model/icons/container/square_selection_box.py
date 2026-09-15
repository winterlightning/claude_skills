"""A selection frame with four rounded square resize handles.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide square: matching tangent corners.
Four handles mirrored around both central axes; no details dropped.
Hosting (compose.py): plus passes, heart passes, check passes.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SquareSelectionBox(Container64):
    icon_id = 'square-selection-box'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'selection', 'box')

    def build(self) -> None:
        self.add_line('nw-0', (5, 2), (11, 2))
        self.add_arc('nw-1', (11, 2), (14, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_line('nw-2', (14, 5), (14, 11))
        self.add_arc('nw-3', (14, 11), (11, 14), radius_x=3, radius_y=3, sweep=True)
        self.add_line('nw-4', (11, 14), (5, 14))
        self.add_arc('nw-5', (5, 14), (2, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_line('nw-6', (2, 11), (2, 5))
        self.add_arc('nw-7', (2, 5), (5, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('nw', 'nw-0', 'nw-1', 'nw-2', 'nw-3', 'nw-4', 'nw-5', 'nw-6', 'nw-7', closed=True)
        self.add_line('ne-0', (53, 2), (59, 2))
        self.add_arc('ne-1', (59, 2), (62, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_line('ne-2', (62, 5), (62, 11))
        self.add_arc('ne-3', (62, 11), (59, 14), radius_x=3, radius_y=3, sweep=True)
        self.add_line('ne-4', (59, 14), (53, 14))
        self.add_arc('ne-5', (53, 14), (50, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_line('ne-6', (50, 11), (50, 5))
        self.add_arc('ne-7', (50, 5), (53, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('ne', 'ne-0', 'ne-1', 'ne-2', 'ne-3', 'ne-4', 'ne-5', 'ne-6', 'ne-7', closed=True)
        self.add_line('se-0', (53, 50), (59, 50))
        self.add_arc('se-1', (59, 50), (62, 53), radius_x=3, radius_y=3, sweep=True)
        self.add_line('se-2', (62, 53), (62, 59))
        self.add_arc('se-3', (62, 59), (59, 62), radius_x=3, radius_y=3, sweep=True)
        self.add_line('se-4', (59, 62), (53, 62))
        self.add_arc('se-5', (53, 62), (50, 59), radius_x=3, radius_y=3, sweep=True)
        self.add_line('se-6', (50, 59), (50, 53))
        self.add_arc('se-7', (50, 53), (53, 50), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('se', 'se-0', 'se-1', 'se-2', 'se-3', 'se-4', 'se-5', 'se-6', 'se-7', closed=True)
        self.add_line('sw-0', (5, 50), (11, 50))
        self.add_arc('sw-1', (11, 50), (14, 53), radius_x=3, radius_y=3, sweep=True)
        self.add_line('sw-2', (14, 53), (14, 59))
        self.add_arc('sw-3', (14, 59), (11, 62), radius_x=3, radius_y=3, sweep=True)
        self.add_line('sw-4', (11, 62), (5, 62))
        self.add_arc('sw-5', (5, 62), (2, 59), radius_x=3, radius_y=3, sweep=True)
        self.add_line('sw-6', (2, 59), (2, 53))
        self.add_arc('sw-7', (2, 53), (5, 50), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('sw', 'sw-0', 'sw-1', 'sw-2', 'sw-3', 'sw-4', 'sw-5', 'sw-6', 'sw-7', closed=True)
        self.add_line('top', (14, 8), (50, 8))
        self.relate("connect", 'top', 'nw')
        self.relate("connect", 'top', 'ne')
        self.add_line('right', (56, 14), (56, 50))
        self.relate("connect", 'right', 'ne')
        self.relate("connect", 'right', 'se')
        self.add_line('bottom', (50, 56), (14, 56))
        self.relate("connect", 'bottom', 'se')
        self.relate("connect", 'bottom', 'sw')
        self.add_line('left', (8, 50), (8, 14))
        self.relate("connect", 'left', 'sw')
        self.relate("connect", 'left', 'nw')
