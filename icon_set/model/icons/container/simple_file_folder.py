"""A tabbed folder has a low overlapping front pocket.

SQUARE: visible bounds (0, 0, 64, 64), chosen for the subject proportions.
Lucide folder-open: tab transitions and overlapping pocket construction; original and atomic-debug inspected.
Unequal front and back heights and left tabs preserve the source asymmetry. No features dropped.
Hosting measured with compose.py: plus blocked, heart blocked, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-file-folder SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SimpleFileFolder(Container64):
    icon_id = 'simple-file-folder'
    keyshape = Keyshape.SQUARE
    aliases = ('file-folder',)
    keywords = ('simple', 'file', 'folder')

    def build(self) -> None:
        self.add_line('rear-left', (9, 40), (9, 10))
        self.add_arc('rear-nw', (9, 10), (12, 6), radius_x=3, radius_y=4)
        self.add_line('rear-tab', (12, 6), (21, 6))
        self.add_arc('rear-tab-down', (21, 6), (27, 8), radius_x=10)
        self.add_arc('rear-tab-level', (27, 8), (32, 10), radius_x=7, sweep=False)
        self.add_line('rear-top', (32, 10), (52, 10))
        self.add_arc('rear-ne', (52, 10), (55, 14), radius_x=3, radius_y=4)
        self.add_line('rear-right', (55, 14), (55, 46))
        self.add_line('front-tab', (9, 40), (16, 40))
        self.add_line('front-slope', (16, 40), (25, 46))
        self.add_line('front-top', (25, 46), (55, 46))
        self.add_arc('front-ne', (55, 46), (58, 50), radius_x=3, radius_y=4)
        self.add_line('front-right', (58, 50), (58, 54))
        self.add_arc('front-se', (58, 54), (55, 58), radius_x=3, radius_y=4)
        self.add_line('front-bottom', (55, 58), (9, 58))
        self.add_arc('front-sw', (9, 58), (6, 54), radius_x=3, radius_y=4)
        self.add_line('front-left', (6, 54), (6, 44))
        self.add_arc('front-nw', (6, 44), (9, 40), radius_x=3, radius_y=4)
        self.add_contour('rear', 'rear-left', 'rear-nw', 'rear-tab', 'rear-tab-down', 'rear-tab-level', 'rear-top', 'rear-ne', 'rear-right')
        self.add_contour('front', 'front-tab', 'front-slope', 'front-top', 'front-ne', 'front-right', 'front-se', 'front-bottom', 'front-sw', 'front-left', 'front-nw', closed=True)
        self.relate('connect', 'front', 'rear')
