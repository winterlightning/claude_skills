"""Steady down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '075e8ccf-ced2-4eff-9422-1c9dfb62b9dc'
SOURCE_PATH = 'icons-json/arrows/steady down_075e8ccf-ced2-4eff-9422-1c9dfb62b9dc.json'
AUTHOR = 'json_to_solo'

class SteadyDown075e8ccf(Solo48):
    icon_id = 'steady-down-075e8ccf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (8, 24), (22, 24))
        self.add_line('e1', (17, 39), (22, 44))
        self.add_line('e2', (27, 39), (22, 44))
        self.add_line('e3', (22, 24), (32, 24))
        self.add_line('e4', (22, 12), (22, 24))
        self.add_line('e5', (22, 44), (22, 24))
        self.add_bezier('e6', (32, 24), ((32.446, 24), (32.615, 23.764), (33.061, 23.627)), ((36.8, 22.473), (39.992, 18.709), (39.992, 14.345)), ((39.992, 14.247), (40, 14.157), (40, 14.059)), ((40, 14.058), (40, 14.056), (40, 14.055)), ((40, 13.791), (39.992, 13.527), (39.992, 13.264)), ((39.992, 8.345), (35.832, 4.009), (31.318, 4.009)), ((31.26, 4.009), (31.202, 4), (31.144, 4)), ((31.143, 4), (31.142, 4), (31.141, 4)), ((30.956, 4), (30.771, 4.009), (30.585, 4.009)), ((26.922, 4.009), (23.343, 7.2), (22.552, 11.018)), ((22.484, 11.345), (22, 11.682), (22, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e6', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
