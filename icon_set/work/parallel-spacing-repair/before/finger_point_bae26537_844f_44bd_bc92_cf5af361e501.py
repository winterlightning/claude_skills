"""Finger point (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bae26537-844f-44bd-bc92-cf5af361e501'
SOURCE_PATH = 'icons-json/wayfinding/finger point_bae26537-844f-44bd-bc92-cf5af361e501.json'
AUTHOR = 'json_to_solo'

class FingerPoint(Solo48):
    icon_id = 'finger-point'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('finger', 'point', 'wayfinding')

    def build(self):
        self.add_line('e0', (21, 21), (21, 18))
        self.add_line('e1', (28, 21), (28, 19))
        self.add_line('e2', (15, 29), (15, 24))
        self.add_line('e3', (21, 18), (21, 7))
        self.add_line('e4', (15, 7), (15, 24))
        self.add_line('e5', (21, 18), (23, 17))
        self.add_line('e6', (40, 33), (40, 21))
        self.add_line('e7', (28, 19), (30, 18))
        self.add_arc('e8', (35, 21), (35, 20), radius_x=23)
        self.add_arc('e9-1', (21, 7), (18, 4), radius_x=3, sweep=False)
        self.add_arc('e9-2', (18, 4), (15, 7), radius_x=3, sweep=False)
        self.add_arc('e10', (23, 17), (28, 19), radius_x=3)
        self.add_arc('e11-1', (15, 24), (8, 29), radius_x=6, sweep=False)
        self.add_arc('e11-2', (8, 29), (11, 37), radius_x=16, sweep=False)
        self.add_arc('e11-3', (11, 37), (15, 41), radius_x=15, sweep=False)
        self.add_arc('e11-4', (15, 41), (19, 43), radius_x=16, sweep=False)
        self.add_line('e11-5', (19, 43), (26, 44))
        self.add_arc('e11-6', (26, 44), (39, 37), radius_x=16, sweep=False)
        self.add_line('e11-7', (39, 37), (40, 33))
        self.add_arc('e12', (40, 21), (35, 20), radius_x=3, sweep=False)
        self.add_arc('e13', (30, 18), (35, 20), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e8')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e9-1', 'e9-2', 'e4')
        self.add_contour('c5', 'e5', 'e10')
        self.add_contour('c6', 'e11-1', 'e11-2', 'e11-3', 'e11-4', 'e11-5', 'e11-6', 'e11-7', 'e6', 'e12')
        self.add_contour('c7', 'e7', 'e13')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
