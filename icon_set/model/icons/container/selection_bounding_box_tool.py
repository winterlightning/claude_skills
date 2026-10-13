"""A square selection frame has four rounded square corner handles.

SQUARE: visible bounds (0, 0, 64, 64), chosen for the subject proportions.
Lucide scaling: rounded square geometry and clear frame rails; original and atomic-debug inspected.
Four matching corner handles and connecting rails retained. Symmetric about both axes.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (selection-bounding-box-tool SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
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
        self.add_line('nw0', (9, 6), (17, 6))
        self.add_arc('nw1', (17, 6), (20, 9), radius_x=3)
        self.add_line('nw2', (20, 9), (20, 17))
        self.add_arc('nw3', (20, 17), (17, 20), radius_x=3)
        self.add_line('nw4', (17, 20), (9, 20))
        self.add_arc('nw5', (9, 20), (6, 17), radius_x=3)
        self.add_line('nw6', (6, 17), (6, 9))
        self.add_arc('nw7', (6, 9), (9, 6), radius_x=3)
        self.add_line('ne0', (47, 6), (55, 6))
        self.add_arc('ne1', (55, 6), (58, 9), radius_x=3)
        self.add_line('ne2', (58, 9), (58, 17))
        self.add_arc('ne3', (58, 17), (55, 20), radius_x=3)
        self.add_line('ne4', (55, 20), (47, 20))
        self.add_arc('ne5', (47, 20), (44, 17), radius_x=3)
        self.add_line('ne6', (44, 17), (44, 9))
        self.add_arc('ne7', (44, 9), (47, 6), radius_x=3)
        self.add_line('se0', (47, 44), (55, 44))
        self.add_arc('se1', (55, 44), (58, 47), radius_x=3)
        self.add_line('se2', (58, 47), (58, 55))
        self.add_arc('se3', (58, 55), (55, 58), radius_x=3)
        self.add_line('se4', (55, 58), (47, 58))
        self.add_arc('se5', (47, 58), (44, 55), radius_x=3)
        self.add_line('se6', (44, 55), (44, 47))
        self.add_arc('se7', (44, 47), (47, 44), radius_x=3)
        self.add_line('sw0', (9, 44), (17, 44))
        self.add_arc('sw1', (17, 44), (20, 47), radius_x=3)
        self.add_line('sw2', (20, 47), (20, 55))
        self.add_arc('sw3', (20, 55), (17, 58), radius_x=3)
        self.add_line('sw4', (17, 58), (9, 58))
        self.add_arc('sw5', (9, 58), (6, 55), radius_x=3)
        self.add_line('sw6', (6, 55), (6, 47))
        self.add_arc('sw7', (6, 47), (9, 44), radius_x=3)
        self.add_line('top', (20, 13), (44, 13))
        self.add_line('right', (51, 20), (51, 44))
        self.add_line('bottom', (44, 51), (20, 51))
        self.add_line('left', (13, 44), (13, 20))
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
