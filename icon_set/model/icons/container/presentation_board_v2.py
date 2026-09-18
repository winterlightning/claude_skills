"""Taller presentation board with deep tray and two short legs.
The secondary cross brace is omitted to preserve clear spacing below the larger panel.
SQUARE CONTAINER64; matching tangent corners follow the inspected Lucide presentation construction."""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class PresentationBoardVariant2(Container64):
    icon_id = 'presentation-board-v2'
    variant_of = 'presentation-board'
    variant_label = 'Native SUB32 clearance'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'containers'
    aliases = ('classroom-presentation-board',)
    keywords = ('presentation', 'board')

    def build(self) -> None:
        self.add_line('panel-left', (6, 44), (6, 6))
        self.add_arc('panel-nw', (6, 6), (10, 2), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('panel-top', (10, 2), (54, 2))
        self.add_arc('panel-ne', (54, 2), (58, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('panel-right', (58, 6), (58, 44))
        self.add_contour('panel', 'panel-left', 'panel-nw', 'panel-top', 'panel-ne', 'panel-right', closed=False)
        self.add_line('tray-top', (2, 44), (62, 44))
        self.add_line('tray-right', (62, 44), (62, 48))
        self.add_arc('tray-se', (62, 48), (58, 52), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('tray-bottom', (58, 52), (6, 52))
        self.add_arc('tray-sw', (6, 52), (2, 48), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('tray-left', (2, 48), (2, 44))
        self.add_contour('tray', 'tray-top', 'tray-right', 'tray-se', 'tray-bottom', 'tray-sw', 'tray-left', closed=True)
        self.relate('connect', 'panel', 'tray')
        self.add_line('leg10', (10, 52), (10, 62))
        self.relate('connect', 'leg10', 'tray')
        self.add_line('leg54', (54, 52), (54, 62))
        self.relate('connect', 'leg54', 'tray')
SOURCE_ICON_ID = None
SOURCE_PATH = None
