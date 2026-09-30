"""Taller monitor display; retained top webcam and flared stand.
Independent CONTAINER64 revision, 4-unit strokes. Lucide monitor/presentation construction retained. Hosting results in container-fit-repair report.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (monitor-webcam SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


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
        self.add_line('top-right', (42, 6), (54, 6))
        self.add_arc('ne', (54, 6), (58, 10), radius_x=4)
        self.add_line('right', (58, 10), (58, 40))
        self.add_arc('se', (58, 40), (54, 44), radius_x=4)
        self.add_line('bottom', (54, 44), (10, 44))
        self.add_arc('sw', (10, 44), (6, 40), radius_x=4)
        self.add_line('left', (6, 40), (6, 10))
        self.add_arc('nw', (6, 10), (10, 6), radius_x=4)
        self.add_line('top-left', (10, 6), (22, 6))
        self.add_dot('webcam', (32, 6))
        self.add_line('stand-left', (26, 44), (22, 58))
        self.add_line('stand-right', (38, 44), (42, 58))
        self.add_line('foot', (18, 58), (46, 58))
        self.add_contour('screen', 'top-right', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', 'top-left')
        self.relate('connect', 'stand-left', 'screen')
        self.relate('connect', 'stand-right', 'screen')
        self.relate('connect', 'stand-left', 'foot')
        self.relate('connect', 'stand-right', 'foot')
