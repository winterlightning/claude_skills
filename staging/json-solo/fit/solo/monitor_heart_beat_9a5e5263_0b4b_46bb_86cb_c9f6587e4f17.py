"""Monitor heart beat (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a5e5263-0b4b-46bb-86cb-c9f6587e4f17'
SOURCE_PATH = 'icons-json/health/monitor heart beat_9a5e5263-0b4b-46bb-86cb-c9f6587e4f17.json'
AUTHOR = 'json_to_solo'

class MonitorHeartBeatHealth(Solo48):
    icon_id = 'monitor-heart-beat-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('monitor', 'heart', 'beat', 'health')

    def build(self):
        self.add_line('e0', (6, 27), (10, 27))
        self.add_line('e1', (42, 27), (39, 27))
        self.add_line('e2', (8, 22), (10, 27))
        self.add_line('e3', (39, 27), (31, 27))
        self.add_line('e4', (31, 27), (30, 24))
        self.add_line('e5', (30, 24), (26, 33))
        self.add_line('e6', (26, 33), (20, 18))
        self.add_line('e7', (20, 18), (17, 27))
        self.add_line('e8', (17, 27), (10, 27))
        self.add_line('e9', (39, 27), (35, 32))
        self.add_line('e10', (13, 31), (10, 27))
        self.add_arc('e11-1', (39, 27), (42, 16), radius_x=24, sweep=False)
        self.add_arc('e11-2', (42, 16), (40, 10), radius_x=10, sweep=False)
        self.add_arc('e11-3', (40, 10), (33, 6), radius_x=9, sweep=False)
        self.add_line('e11-4', (33, 6), (28, 7))
        self.add_line('e11-5', (28, 7), (24, 11))
        self.add_arc('e11-6', (24, 11), (16, 6), radius_x=9, sweep=False)
        self.add_arc('e11-7', (16, 6), (6, 16), radius_x=10, sweep=False)
        self.add_arc('e11-8', (6, 16), (8, 22), radius_x=23, sweep=False)
        self.add_arc('e12-1', (35, 32), (24, 42), radius_x=63)
        self.add_arc('e12-2', (24, 42), (13, 31), radius_x=51)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e11-1', 'e11-2', 'e11-3', 'e11-4', 'e11-5', 'e11-6', 'e11-7', 'e11-8', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8')
        self.add_contour('c4', 'e9', 'e12-1', 'e12-2', 'e10')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
