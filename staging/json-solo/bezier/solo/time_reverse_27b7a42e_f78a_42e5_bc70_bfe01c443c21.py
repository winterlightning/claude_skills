"""Time reverse (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27b7a42e-f78a-42e5-bc70-bfe01c443c21'
SOURCE_PATH = 'icons-json/interface-essential/time reverse_27b7a42e-f78a-42e5-bc70-bfe01c443c21.json'
AUTHOR = 'json_to_solo'

class TimeReverseInterfaceEssential(Solo48):
    icon_id = 'time-reverse-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'reverse', 'interface-essential')

    def build(self):
        self.add_line('e0', (28, 4), (31, 8))
        self.add_line('e1', (31, 8), (32, 10))
        self.add_line('e2', (28, 14), (32, 10))
        self.add_line('e3', (22, 18), (22, 27))
        self.add_line('e4', (22, 27), (26, 31))
        self.add_bezier('e5', (40, 24), ((40, 24.491), (39.992, 24.982), (39.992, 25.473)), ((39.983, 25.536), (39.983, 25.609), (39.983, 25.673)), ((39.983, 25.882), (39.983, 26.082), (39.983, 26.282)), ((39.983, 26.518), (40, 26.755), (40, 26.991)), ((40, 27.091), (39.992, 27.2), (39.992, 27.309)), ((39.992, 35.873), (32.421, 43.991), (24.522, 43.991)), ((24.406, 43.991), (24.282, 44), (24.166, 44)), ((24.164, 44), (24.162, 44), (24.16, 44)), ((23.916, 44), (23.68, 43.991), (23.436, 43.991)), ((15.377, 43.991), (8.017, 35.809), (8.017, 27.155)), ((8.017, 26.993), (8, 26.841), (8, 26.68)), ((8, 26.678), (8, 26.675), (8, 26.673)), ((8, 26.264), (8.017, 25.855), (8.017, 25.445)), ((8.017, 16.645), (15.141, 8.255), (23.377, 7.973)), ((26.804, 7.855), (28.876, 8.6), (32, 10)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
