"""Happiness emotions (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20934b59-3187-55bc-ae3d-4a19287367e6'
SOURCE_PATH = 'icons-json/health/happiness emotions_20934b59-3187-55bc-ae3d-4a19287367e6.json'
AUTHOR = 'json_to_solo'

class HappinessEmotions(Solo48):
    icon_id = 'happiness-emotions'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('happiness', 'emotions', 'health')

    def build(self):
        self.add_line('e0', (13, 44), (13, 35))
        self.add_line('e1', (37, 15), (40, 25))
        self.add_line('e2', (37, 29), (36, 36))
        self.add_line('e3', (28, 40), (28, 44))
        self.add_arc('e4', (30, 31), (36, 35), radius_x=6, sweep=False)
        self.add_line('e5-1', (13, 35), (9, 26))
        self.add_line('e5-2', (9, 26), (8, 20))
        self.add_line('e5-3', (8, 20), (9, 14))
        self.add_arc('e5-4', (9, 14), (22, 4), radius_x=14)
        self.add_arc('e5-5', (22, 4), (37, 15), radius_x=16)
        self.add_arc('e6-1', (40, 25), (40, 27), radius_x=45, sweep=False)
        self.add_line('e6-2', (40, 27), (37, 29))
        self.add_arc('e7', (36, 36), (28, 40), radius_x=6)
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e1', 'e6-1', 'e6-2', 'e2', 'e7', 'e3')
        self.relate('connect', 'c0', 'c1')
