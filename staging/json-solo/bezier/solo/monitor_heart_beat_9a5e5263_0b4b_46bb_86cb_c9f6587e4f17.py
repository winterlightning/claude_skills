"""Monitor heart beat (health), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e11', (39, 27), ((40.571, 25.11), (41.992, 19.271), (41.992, 16.669)), ((41.992, 16.538), (42, 16.399), (42, 16.268)), ((42, 15.998), (41.984, 15.728), (41.984, 15.458)), ((41.984, 10.762), (37.713, 6.008), (32.926, 6.008)), ((32.814, 6.008), (32.709, 6), (32.596, 6)), ((32.594, 6), (32.593, 6), (32.591, 6)), ((32.435, 6), (32.272, 6.008), (32.116, 6.008)), ((29.932, 6.008), (27.674, 7.08), (26.119, 8.577)), ((25.612, 9.06), (25.178, 9.608), (24.794, 10.189)), ((24.581, 10.508), (24.36, 10.835), (24.147, 11.155)), ((23.91, 10.827), (23.665, 10.508), (23.427, 10.181)), ((22.994, 9.592), (22.519, 9.035), (21.979, 8.545)), ((20.367, 7.072), (18.117, 6.008), (15.908, 6.008)), ((15.843, 6.008), (15.785, 6), (15.72, 6)), ((15.475, 6), (15.221, 6.008), (14.975, 6.008)), ((11.007, 6.008), (7.735, 9.297), (6.597, 12.865)), ((6.352, 13.634), (6.016, 14.46), (6.016, 15.286)), ((6.016, 15.409), (6, 15.54), (6, 15.671)), ((6, 15.777), (6.008, 15.875), (6.008, 15.982)), ((6.008, 17.266), (7.46, 20.92), (8, 22)))
        self.add_bezier('e12', (35, 32), ((32.709, 34.749), (29.703, 37.533), (26.945, 39.815)), ((26.615, 40.089), (24.446, 42), (24.144, 42)), ((24.139, 42), (24.135, 42), (24.131, 42)), ((24.025, 42), (21.488, 39.946), (21.218, 39.717)), ((18.256, 37.222), (15.414, 34.019), (13, 31)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e11', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8')
        self.add_contour('c4', 'e9', 'e12', 'e10')
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
