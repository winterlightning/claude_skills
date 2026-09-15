"""A square selection frame has four rounded square corner handles.

SQUARE: visible bounds (0, 0, 64, 64), chosen for the subject proportions.
Lucide scaling: rounded square geometry and clear frame rails; original and atomic-debug inspected.
Four matching corner handles and connecting rails retained. Symmetric about both axes.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SelectionBoundingBoxTool(Container64):
    icon_id = 'selection-bounding-box-tool'
    keyshape = Keyshape.SQUARE
    aliases = ('selection-frame',)
    keywords = ('selection', 'bounding', 'box', 'tool')

    def build(self) -> None:
        self.add_line('nw0', (5, 2), (13, 2))
        self.add_arc('nw1', (13, 2), (16, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_line('nw2', (16, 5), (16, 13))
        self.add_arc('nw3', (16, 13), (13, 16), radius_x=3, radius_y=3, sweep=True)
        self.add_line('nw4', (13, 16), (5, 16))
        self.add_arc('nw5', (5, 16), (2, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_line('nw6', (2, 13), (2, 5))
        self.add_arc('nw7', (2, 5), (5, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('nw', 'nw0', 'nw1', 'nw2', 'nw3', 'nw4', 'nw5', 'nw6', 'nw7', closed=True)
        self.add_line('ne0', (51, 2), (59, 2))
        self.add_arc('ne1', (59, 2), (62, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_line('ne2', (62, 5), (62, 13))
        self.add_arc('ne3', (62, 13), (59, 16), radius_x=3, radius_y=3, sweep=True)
        self.add_line('ne4', (59, 16), (51, 16))
        self.add_arc('ne5', (51, 16), (48, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_line('ne6', (48, 13), (48, 5))
        self.add_arc('ne7', (48, 5), (51, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('ne', 'ne0', 'ne1', 'ne2', 'ne3', 'ne4', 'ne5', 'ne6', 'ne7', closed=True)
        self.add_line('se0', (51, 48), (59, 48))
        self.add_arc('se1', (59, 48), (62, 51), radius_x=3, radius_y=3, sweep=True)
        self.add_line('se2', (62, 51), (62, 59))
        self.add_arc('se3', (62, 59), (59, 62), radius_x=3, radius_y=3, sweep=True)
        self.add_line('se4', (59, 62), (51, 62))
        self.add_arc('se5', (51, 62), (48, 59), radius_x=3, radius_y=3, sweep=True)
        self.add_line('se6', (48, 59), (48, 51))
        self.add_arc('se7', (48, 51), (51, 48), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('se', 'se0', 'se1', 'se2', 'se3', 'se4', 'se5', 'se6', 'se7', closed=True)
        self.add_line('sw0', (5, 48), (13, 48))
        self.add_arc('sw1', (13, 48), (16, 51), radius_x=3, radius_y=3, sweep=True)
        self.add_line('sw2', (16, 51), (16, 59))
        self.add_arc('sw3', (16, 59), (13, 62), radius_x=3, radius_y=3, sweep=True)
        self.add_line('sw4', (13, 62), (5, 62))
        self.add_arc('sw5', (5, 62), (2, 59), radius_x=3, radius_y=3, sweep=True)
        self.add_line('sw6', (2, 59), (2, 51))
        self.add_arc('sw7', (2, 51), (5, 48), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('sw', 'sw0', 'sw1', 'sw2', 'sw3', 'sw4', 'sw5', 'sw6', 'sw7', closed=True)
        self.add_line('top', (16, 9), (48, 9))
        self.relate("connect", 'top', 'nw')
        self.relate("connect", 'top', 'ne')
        self.add_line('right', (55, 16), (55, 48))
        self.relate("connect", 'right', 'ne')
        self.relate("connect", 'right', 'se')
        self.add_line('bottom', (48, 55), (16, 55))
        self.relate("connect", 'bottom', 'se')
        self.relate("connect", 'bottom', 'sw')
        self.add_line('left', (9, 48), (9, 16))
        self.relate("connect", 'left', 'sw')
        self.relate("connect", 'left', 'nw')
