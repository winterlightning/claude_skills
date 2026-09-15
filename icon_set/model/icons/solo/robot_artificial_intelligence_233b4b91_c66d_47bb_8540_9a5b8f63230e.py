"""Robot (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '233b4b91-c66d-47bb-8540-9a5b8f63230e'
SOURCE_PATH = 'icons-json/artificial-intelligence/robot_233b4b91-c66d-47bb-8540-9a5b8f63230e.json'
AUTHOR = 'gpt-6'

class RobotArtificialIntelligence(Solo48):
    icon_id = 'robot-artificial-intelligence'
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
        self.add_line('e3', (16, 44), (33, 44))
        self.add_line('e4', (40, 35), (40, 21))
        self.add_line('e5', (16, 16), (32, 16))
        self.add_line('e6', (18, 28), (18, 32))
        self.add_line('e7', (30, 28), (30, 32))
        self.add_arc('e8', (16, 16), (8, 22), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e9', (8, 34), (16, 44), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('e10-2', (33, 44), (40, 35), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('e11', (40, 21), (32, 16), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e8', 'e2', 'e9', 'e3', 'e10-2', 'e4', 'e11', closed=False)
        self.add_contour('c3', 'e5', closed=False)
        self.add_contour('c4', 'e6', closed=False)
        self.add_contour('c5', 'e7', closed=False)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
