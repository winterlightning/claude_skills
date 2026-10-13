"""A square selection frame has four rounded square corner handles.

SQUARE: visible bounds (0, 0, 64, 64), chosen for the subject proportions.
Lucide scaling: rounded square geometry and clear frame rails; original and atomic-debug inspected.
Four matching corner handles and connecting rails retained. Symmetric about both axes.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (selection-bounding-box-tool SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SelectionBoundingBoxTool(Container64):
    icon_id = 'selection-bounding-box-tool'
    keyshape = Keyshape.SQUARE
    aliases = ('selection-frame',)
    keywords = ('selection', 'bounding', 'box', 'tool')

    def build(self) -> None:
        # Corner handles 10 x 10 (6..16 and 48..58) with the frame edges on their centre lines (11 and 53), so the
        # frame holds a symbol of 25 with a 4 px gap (was 17).
        self.add_line('nw0', (9, 6), (13, 6))
        self.add_arc('nw1', (13, 6), (16, 9), radius_x=3)
        self.add_line('nw2', (16, 9), (16, 13))
        self.add_arc('nw3', (16, 13), (13, 16), radius_x=3)
        self.add_line('nw4', (13, 16), (9, 16))
        self.add_arc('nw5', (9, 16), (6, 13), radius_x=3)
        self.add_line('nw6', (6, 13), (6, 9))
        self.add_arc('nw7', (6, 9), (9, 6), radius_x=3)
        self.add_line('ne0', (51, 6), (55, 6))
        self.add_arc('ne1', (55, 6), (58, 9), radius_x=3)
        self.add_line('ne2', (58, 9), (58, 13))
        self.add_arc('ne3', (58, 13), (55, 16), radius_x=3)
        self.add_line('ne4', (55, 16), (51, 16))
        self.add_arc('ne5', (51, 16), (48, 13), radius_x=3)
        self.add_line('ne6', (48, 13), (48, 9))
        self.add_arc('ne7', (48, 9), (51, 6), radius_x=3)
        self.add_line('se0', (51, 48), (55, 48))
        self.add_arc('se1', (55, 48), (58, 51), radius_x=3)
        self.add_line('se2', (58, 51), (58, 55))
        self.add_arc('se3', (58, 55), (55, 58), radius_x=3)
        self.add_line('se4', (55, 58), (51, 58))
        self.add_arc('se5', (51, 58), (48, 55), radius_x=3)
        self.add_line('se6', (48, 55), (48, 51))
        self.add_arc('se7', (48, 51), (51, 48), radius_x=3)
        self.add_line('sw0', (9, 48), (13, 48))
        self.add_arc('sw1', (13, 48), (16, 51), radius_x=3)
        self.add_line('sw2', (16, 51), (16, 55))
        self.add_arc('sw3', (16, 55), (13, 58), radius_x=3)
        self.add_line('sw4', (13, 58), (9, 58))
        self.add_arc('sw5', (9, 58), (6, 55), radius_x=3)
        self.add_line('sw6', (6, 55), (6, 51))
        self.add_arc('sw7', (6, 51), (9, 48), radius_x=3)
        self.add_line('top', (16, 11), (48, 11))
        self.add_line('right', (53, 16), (53, 48))
        self.add_line('bottom', (48, 53), (16, 53))
        self.add_line('left', (11, 48), (11, 16))
        self.add_contour('nw', 'nw0', 'nw1', 'nw2', 'nw3', 'nw4', 'nw5', 'nw6', 'nw7', closed=True)
        self.add_contour('ne', 'ne0', 'ne1', 'ne2', 'ne3', 'ne4', 'ne5', 'ne6', 'ne7', closed=True)
        self.add_contour('se', 'se0', 'se1', 'se2', 'se3', 'se4', 'se5', 'se6', 'se7', closed=True)
        self.add_contour('sw', 'sw0', 'sw1', 'sw2', 'sw3', 'sw4', 'sw5', 'sw6', 'sw7', closed=True)
        self.relate('connect', 'top', 'nw')
        self.relate('connect', 'top', 'ne')
        self.relate('connect', 'right', 'ne')
        self.relate('connect', 'right', 'se')
        self.relate('connect', 'bottom', 'se')
        self.relate('connect', 'bottom', 'sw')
        self.relate('connect', 'left', 'sw')
        self.relate('connect', 'left', 'nw')
