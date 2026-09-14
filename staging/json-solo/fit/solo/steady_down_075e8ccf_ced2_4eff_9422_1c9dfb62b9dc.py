"""Steady down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e6-1', (32, 24), (40, 14), radius_x=11, sweep=False)
        self.add_line('e6-2', (40, 14), (39, 9))
        self.add_arc('e6-3', (39, 9), (31, 4), radius_x=9, sweep=False)
        self.add_line('e6-4', (31, 4), (27, 5))
        self.add_arc('e6-5', (27, 5), (22, 12), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
