"""Taller presentation board with deep tray and two short legs.
The secondary cross brace is omitted to preserve clear spacing below the larger panel.
SQUARE CONTAINER64; matching tangent corners follow the inspected Lucide presentation construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (presentation-board SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class PresentationBoard(Container64):
    icon_id = 'presentation-board'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('classroom-presentation-board',)
    keywords = ('presentation', 'board')

    def build(self) -> None:
        self.add_line('panel-left', (10, 40), (10, 10))
        self.add_arc('panel-nw', (10, 10), (14, 6), radius_x=4)
        self.add_line('panel-top', (14, 6), (50, 6))
        self.add_arc('panel-ne', (50, 6), (54, 10), radius_x=4)
        self.add_line('panel-right', (54, 10), (54, 40))
        self.add_line('tray-top', (6, 40), (58, 40))
        self.add_line('tray-right', (58, 40), (58, 44))
        self.add_arc('tray-se', (58, 44), (54, 48), radius_x=4)
        self.add_line('tray-bottom', (54, 48), (10, 48))
        self.add_arc('tray-sw', (10, 48), (6, 44), radius_x=4)
        self.add_line('tray-left', (6, 44), (6, 40))
        self.add_line('leg10', (14, 48), (14, 58))
        self.add_line('leg54', (50, 48), (50, 58))
        self.add_contour('panel', 'panel-left', 'panel-nw', 'panel-top', 'panel-ne', 'panel-right')
        self.add_contour('tray', 'tray-top', 'tray-right', 'tray-se', 'tray-bottom', 'tray-sw', 'tray-left', closed=True)
        self.relate('connect', 'panel', 'tray')
        self.relate('connect', 'leg10', 'tray')
        self.relate('connect', 'leg54', 'tray')
