"""Robot (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '233b4b91-c66d-47bb-8540-9a5b8f63230e'
SOURCE_PATH = 'icons-json/artificial-intelligence/robot_233b4b91-c66d-47bb-8540-9a5b8f63230e.json'
AUTHOR = 'json_to_solo'

class Robot233b4b91(Solo48):
    icon_id = 'robot-233b4b91'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('robot', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (16, 4), (16, 16))
        self.add_line('e1', (32, 4), (32, 16))
        self.add_line('e2', (8, 22), (8, 34))
        self.add_line('e3', (16, 44), (32, 44))
        self.add_line('e4', (40, 35), (40, 21))
        self.add_line('e5', (16, 16), (32, 16))
        self.add_line('e6', (18, 28), (18, 32))
        self.add_line('e7', (30, 28), (30, 32))
        self.add_bezier('e8', (16, 16), ((12.918, 16), (10.585, 15.773), (8.834, 19.027)), ((8.472, 19.7), (8, 20.764), (8, 21.573)), ((8, 21.773), (8, 21.8), (8, 22)))
        self.add_bezier('e9', (8, 34), ((8, 34.209), (8, 34.409), (8, 34.618)), ((8, 35.209), (8.202, 35.909), (8.345, 36.473)), ((9.204, 39.791), (11.68, 42.736), (14.771, 43.718)), ((14.88, 43.755), (15.756, 44), (15.874, 44)), ((16.059, 44), (15.815, 44), (16, 44)))
        self.add_bezier('e10', (32, 44), ((32.185, 44), (32.783, 44), (32.968, 44)), ((33.095, 44), (33.945, 43.745), (34.063, 43.709)), ((36.935, 42.773), (38.914, 39.882), (39.697, 36.864)), ((39.806, 36.427), (40, 36), (40, 35.545)), ((40, 35.336), (40, 35.209), (40, 35)))
        self.add_bezier('e11', (40, 21), ((40, 20.782), (40, 20.845), (40, 20.627)), ((40, 20.064), (39.528, 19.136), (39.267, 18.664)), ((37.465, 15.391), (35.006, 16), (32, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', 'e11')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
