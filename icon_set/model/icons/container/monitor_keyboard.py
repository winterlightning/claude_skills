"""A rounded monitor above a separate trapezoidal keyboard.

Keyshape SQUARE; visible bounds (0, 0, 64, 64); centerline extremes (2, 2)-(62, 62).
Construction reference: Lucide monitor: matching quarter-circle frame corners, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class MonitorKeyboard(Container64):
    icon_id = 'monitor-keyboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('computer-monitor-and-keyboard',)
    keywords = ('monitor', 'keyboard')

    def build(self) -> None:
        self.add_line('screen0', (6, 2), (58, 2))
        self.add_arc('screen1', (58, 2), (62, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('screen2', (62, 6), (62, 36))
        self.add_arc('screen3', (62, 36), (58, 40), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('screen4', (58, 40), (6, 40))
        self.add_arc('screen5', (6, 40), (2, 36), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('screen6', (2, 36), (2, 6))
        self.add_arc('screen7', (2, 6), (6, 2), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('screen', 'screen0', 'screen1', 'screen2', 'screen3', 'screen4', 'screen5', 'screen6', 'screen7', closed=True)
        self.add_polyline("keyboard", (10,50), (54,50), (60,62), (4,62), closed=True)
