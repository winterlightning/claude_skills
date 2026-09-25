"""Taller monitor display; retained top webcam and flared stand.
Independent CONTAINER64 revision, 4-unit strokes. Lucide monitor/presentation construction retained. Hosting results in container-fit-repair report."""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class MonitorWebcam(Container64):
    icon_id = 'monitor-webcam'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('computer-monitor-with-webcam',)
    keywords = ('monitor', 'webcam')

    def build(self) -> None:
        self.add_line('top-right', (42, 2), (58, 2))
        self.add_arc('ne', (58, 2), (62, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('right', (62, 6), (62, 42))
        self.add_arc('se', (62, 42), (58, 46), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bottom', (58, 46), (6, 46))
        self.add_arc('sw', (6, 46), (2, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left', (2, 42), (2, 6))
        self.add_arc('nw', (2, 6), (6, 2), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('top-left', (6, 2), (22, 2))
        self.add_contour('screen', 'top-right', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', 'top-left', closed=False)
        self.add_dot('webcam', (32, 2))
        self.add_line('stand-left', (26, 46), (22, 62))
        self.add_line('stand-right', (38, 46), (42, 62))
        self.add_line('foot', (18, 62), (46, 62))
        self.relate('connect', 'stand-left', 'screen')
        self.relate('connect', 'stand-right', 'screen')
        self.relate('connect', 'stand-left', 'foot')
        self.relate('connect', 'stand-right', 'foot')
SOURCE_ICON_ID = None
SOURCE_PATH = None
