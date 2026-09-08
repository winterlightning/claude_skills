"""A classroom board with a deep tray, paired legs and cross brace.

Keyshape SQUARE; visible bounds (0, 0, 64, 64); centerline extremes (2, 2)-(62, 62).
Construction reference: Lucide presentation: rounded rectangular panel; reference stand retained, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class PresentationBoard(Container64):
    icon_id = 'presentation-board'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('classroom-presentation-board',)
    keywords = ('presentation', 'board')

    def build(self) -> None:
        self.add_line('panel-left', (6, 38), (6, 6))
        self.add_arc('panel-nw', (6, 6), (10, 2), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('panel-top', (10, 2), (54, 2))
        self.add_arc('panel-ne', (54, 2), (58, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('panel-right', (58, 6), (58, 38))
        self.add_contour('panel', 'panel-left', 'panel-nw', 'panel-top', 'panel-ne', 'panel-right', closed=False)
        self.add_line('tray-top', (2, 38), (62, 38))
        self.add_line('tray-right', (62, 38), (62, 42))
        self.add_arc('tray-se', (62, 42), (58, 46), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('tray-bottom', (58, 46), (6, 46))
        self.add_arc('tray-sw', (6, 46), (2, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('tray-left', (2, 42), (2, 38))
        self.add_contour('tray', 'tray-top', 'tray-right', 'tray-se', 'tray-bottom', 'tray-sw', 'tray-left', closed=True)
        self.relate("connect", 'panel', 'tray')
        self.add_line('leg10', (10, 46), (10, 62))
        self.relate("connect", 'leg10', 'tray')
        self.add_line('leg54', (54, 46), (54, 62))
        self.relate("connect", 'leg54', 'tray')
        self.add_line('brace', (10, 55), (54, 55))
        self.relate("connect", 'brace', 'leg10')
        self.relate("connect", 'brace', 'leg54')
