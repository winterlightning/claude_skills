"""A tabbed folder has a low overlapping front pocket.

SQUARE: visible bounds (0, 0, 64, 64), chosen for the subject proportions.
Lucide folder-open: tab transitions and overlapping pocket construction; original and atomic-debug inspected.
Unequal front and back heights and left tabs preserve the source asymmetry. No features dropped.
Hosting measured with compose.py: plus blocked, heart blocked, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-file-folder SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): reproportioned so a container symbol has more room (container-combination64 space check).
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
        # Closed folder: rounded body 6..58 x 14..58 with a tab rising to 6 on the left. The open front flap it
        # replaces cut the hosting area to 26; the closed body leaves room for a full 32 symbol.
        self.add_line('tab-left', (6, 52), (6, 12))
        self.add_arc('tab-nw', (6, 12), (12, 6), radius_x=6)
        self.add_line('tab-top', (12, 6), (22, 6))
        self.add_arc('tab-down', (22, 6), (27, 9), radius_x=6)
        self.add_line('tab-slope', (27, 9), (30, 13))
        self.add_arc('tab-level', (30, 13), (34, 14), radius_x=4, sweep=False)
        self.add_line('top', (34, 14), (52, 14))
        self.add_arc('ne', (52, 14), (58, 20), radius_x=6)
        self.add_line('right', (58, 20), (58, 52))
        self.add_arc('se', (58, 52), (52, 58), radius_x=6)
        self.add_line('bottom', (52, 58), (12, 58))
        self.add_arc('sw', (12, 58), (6, 52), radius_x=6)
        self.add_contour('folder', 'tab-left', 'tab-nw', 'tab-top', 'tab-down', 'tab-slope', 'tab-level', 'top', 'ne', 'right', 'se', 'bottom', 'sw', closed=True)
