"""Steady and fall (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3ce2565-5b74-4cc9-91e5-8808ecc070e9'
SOURCE_PATH = 'icons-json/arrows/steady and fall_e3ce2565-5b74-4cc9-91e5-8808ecc070e9.json'
AUTHOR = 'json_to_solo'

class SteadyAndFall(Solo48):
    icon_id = 'steady-and-fall'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'and', 'fall', 'arrows')

    def build(self):
        self.add_line('e0', (4, 8), (4, 21))
        self.add_line('e1', (9, 26), (23, 26))
        self.add_line('e2', (19, 36), (23, 40))
        self.add_line('e3', (28, 37), (23, 40))
        self.add_line('e4', (40, 29), (44, 26))
        self.add_line('e5', (40, 22), (44, 26))
        self.add_line('e6', (23, 26), (23, 40))
        self.add_line('e7', (23, 26), (44, 26))
        self.add_arc('e8', (4, 21), (9, 26), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e8', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
