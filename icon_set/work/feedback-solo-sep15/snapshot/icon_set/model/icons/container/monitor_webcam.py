"""A desktop monitor with a centered camera in its interrupted top bezel and a flared stand.

Keyshape HRECT_XL; visible bounds (0, 4, 64, 60); centerline extremes (2, 6)-(62, 58).
Construction reference: Lucide monitor and monitor-dot: rounded bezel and isolated camera mark, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class MonitorWebcam(Container64):
    icon_id = 'monitor-webcam'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('computer-monitor-with-webcam',)
    keywords = ('monitor', 'webcam')

    def build(self) -> None:
        self.add_line('top-right', (42, 6), (58, 6))
        self.add_arc('ne', (58, 6), (62, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('right', (62, 10), (62, 42))
        self.add_arc('se', (62, 42), (58, 46), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bottom', (58, 46), (6, 46))
        self.add_arc('sw', (6, 46), (2, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left', (2, 42), (2, 10))
        self.add_arc('nw', (2, 10), (6, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('top-left', (6, 6), (22, 6))
        self.add_contour('screen', 'top-right', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', 'top-left', closed=False)
        self.add_dot("webcam", (32,6))
        self.add_line('stand-left', (26, 46), (22, 58))
        self.add_line('stand-right', (38, 46), (42, 58))
        self.add_line('foot', (18, 58), (46, 58))
        self.relate("connect", 'stand-left', 'screen')
        self.relate("connect", 'stand-right', 'screen')
        self.relate("connect", 'stand-left', 'foot')
        self.relate("connect", 'stand-right', 'foot')
